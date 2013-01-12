#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import glob
import time
import urllib2
import lastfmApi
import acoustid
import mechanize
import HTMLParser
import threading

only_digit = re.compile(r'^[0-9]+$')
sysname = re.compile(r'[!/\\:;*?«<>|]+')
time_find = re.compile('data-dur="(.*)" onclick')
artist_find = re.compile('<span class="artist">(.*)</span>')
tracks_find = re.compile('<span class="title">(.*)</span>')
mp3s_find = re.compile('<input type="hidden" value="(.*)">')
year_find = re.compile('(\d[4])')

default_workdirs = ['c:\music', 'd:\music', 'e:\music', 'f:\music',
                    'g:\music', 'h:\music', 'i:\music', '/mnt/sdcard/Music']

intro_workdir = """
Input work directory path, choose defaults from list
or leave blank for current directory
"""

lfm_api = lastfmApi.lfmAPI("f3d8fbacbda2a35bfa855ef52052ca25")
acoustid_apikey = 'FDaQARn2'

def initVk(email, password):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Linux; U; Android 3.0; \
    ru-RU; Xoom Build/HRI39) AppleWebKit/534.13 KHTML, like Gecko Version/4.0 \
    Safari/534.13')]
    br.open('http://m.vk.com')
    br.select_form(nr = 0)
    br.form['email'] = email
    br.form['pass'] = password
    br.submit()
    return br


def parseVk(search, br):
    parser = HTMLParser.HTMLParser()
    un = parser.unescape
    url = 'http://m.vk.com/audio?act=search&q=' + urllib2.quote(search.encode('utf-8'))
    response = br.open(url)
    html = un(response.read().decode('utf-8')).replace('<em>', '').replace('</em>', '')

    times = time_find.findall(html)
    artists = artist_find.findall(html)
    tracks = tracks_find.findall(html)
    mp3s = mp3s_find.findall(html)

    if len(times) == len(artists) == len(tracks) == len(mp3s):
        vkinfo = zip(artists, tracks, times, mp3s)
        return vkinfo
    else:
        print 'Bad VK Parse'
        raise RuntimeError


def get_links(artist, track, time, br, listsize, timerange):
    out_list = []
    vksearch = '%s - %s' % (artist, track)
    vkout = parseVk(vksearch, br)
    for item in vkout:
        if item[2] != '':
            if int(item[2]) in range(time - timerange, time + timerange + 1):
                out_list.append((item[2], item[3]))
    if out_list:
        if len(out_list) > listsize: out_list = out_list[:listsize]
        final_list = addBitrate(out_list)
        return final_list
    else: return None


def DownloadPrepare(artist, album, covers, year=''):
    # Create Artist Directory and proceed
    if os.path.exists(sysname.sub('', artist)):
        os.chdir(sysname.sub('', artist))
    else:
        os.mkdir(sysname.sub('', artist))
        os.chdir(sysname.sub('', artist))

    # Create Album Directory and proceed:
    if year and year != '':
        folder_prefix = '[%d] ' % year
    else:
        folder_prefix = ''

    if os.path.exists(sysname.sub('', folder_prefix + album)):
        os.chdir(sysname.sub('', folder_prefix + album))
    else:
        os.mkdir(sysname.sub('', folder_prefix + album))
        os.chdir(sysname.sub('', folder_prefix + album))

    # Download Covers
    if covers['extralarge'] and covers['mega']:
        print 'Big Cover Downloading'
        downloadFile(covers['mega'], 'Big_Cover.' + covers['mega'][-3:])
        print 'Standart Cover Downloading'
        downloadFile(covers['extralarge'], 'Cover.' + covers['extralarge'][-3:])
    else:
        print 'No Cover Found!'
        print 'Default Image Download...'
        downloadFile('http://masterx2.com/tech_data/Cover.png', 'Cover.png')



def ProcessFile(filename, url, id3tags):
    downloadFile(url, filename)
    writeTag(filename, id3tags)

def getWorkdir():
    print ('Input work directory path, choose defaults from list\nor leave blank for current directory')
    print ('Current workdir is  >> %s\n' % (os.getcwd()))
    default_workdir_num = 1
    detected_workdirs = []
    for default_workdir in default_workdirs:
        if os.path.exists(default_workdir):
            print ('#%d | %s' % (default_workdir_num, default_workdir))
            detected_workdirs.append(default_workdir)
            default_workdir_num += 1
    print ('')
    while True:
        workdir = raw_input('WorkDir > ')
        if only_digit.match(workdir) and int(workdir) in range(1, default_workdir_num):
            print ('\nWorking Directory is %s\n' % (detected_workdirs[int(workdir) - 1]))
            return detected_workdirs[int(workdir) - 1]
        elif os.path.exists(workdir):
            print ('[system] Directory exist, using as work directory')
            return workdir
        elif workdir == '':
            print ('[system] Use current directory')
            return '.'
        else:
            answer = 'default'
            while answer != 'n':
                answer = raw_input('[system] Directory not found, create?(y/n): ')
                if answer == 'y':
                    os.mkdir(workdir)
                    print ('[system] Directory created\n')
                    return workdir


def tosec(duration):
    colon = duration.find(':')
    return int(duration[:colon]) * 60 + int(duration[colon + 1:])


def tomin(duration):
    try:
        duration = int(duration)
        minutes = duration / 60
        sec = duration - minutes * 60
        if sec == 0: sec = '00'
        if sec <= 9: sec = '0' + str(sec)
        return str(minutes) + ':' + str(sec)
    except:
        return duration

def getBitrate(url, time):
    if int(time) <= 0:
        return 0
    else:
        urlfile = urllib2.urlopen(url)
        totalBytes = int(urlfile.info().getheader('Content-Length').strip())
        return ((totalBytes * 8) / int(time)) / 1000


def addBitrate(url_list):
    out = []
    for item in url_list:
        out.append([item[1], getBitrate(item[1], item[0])])
    return sorted(out, key = lambda x: x[1])[::-1]


def downloadFile(fileurl, filename):
    def mbytes(frombytes):
        return (float(frombytes) / 1024) / 1024

    def showProgress(bytesSoFar, totalBytes):
        progressLine = 'Downloading file {0:0.4f}/{1:0.4f} ({2:0.2f}%)\r'\
        .format(mbytes(bytesSoFar), mbytes(totalBytes), float(bytesSoFar) / totalBytes * 100)
        print progressLine

    urlfile = urllib2.urlopen(fileurl)
    totalBytes = int(urlfile.info().getheader('Content-Length').strip())
    bytesSoFar = 0

    if os.path.exists(filename):
        print '[File Exist] Skip Download...'
        return True
    else:
        try:
            with open(filename + '.part', 'w+b') as tmpfile:
                while True:
                    readBytes = urlfile.read(1024 * 100)
                    bytesSoFar += len(readBytes)
                    if not readBytes:
                        break
                    tmpfile.write(readBytes)
                    # showProgress(bytesSoFar, totalBytes)
            os.rename('%s.part' % filename, filename)
            return True
        except WindowsError as er:
            print '[File] Windows Report Error:', er


def deleteTag(filename):
    from mutagen import id3

    try:
        TrackID3 = id3.ID3(filename)
    except id3.ID3NoHeaderError:
        TrackID3 = id3.ID3()
        TrackID3.save(filename)

    TrackID3.delete(filename)
    TrackID3.save(filename)


def writeTag(filename, tags):
    from mutagen import id3
    from mutagen.mp3 import MP3

    try:
        TrackID3 = id3.ID3(filename)
    except id3.ID3NoHeaderError:
        TrackID3 = id3.ID3()
        TrackID3.save(filename)

    print '[ID3] Writing Tag'
    TrackID3.delete(filename)
    TrackID3.add(id3.TRCK(encoding = 3, text = tags[0])) # Track Number
    TrackID3.add(id3.TIT2(encoding = 3, text = tags[1])) # Song Name
    TrackID3.add(id3.TPE1(encoding = 3, text = tags[2])) # Artist
    TrackID3.add(id3.TALB(encoding = 3, text = tags[3])) # Album Name
    TrackID3.add(id3.TDRC(encoding = 3, text = tags[4])) # Year
    TrackID3.add(id3.TCON(encoding = 3, text = tags[5])) # Tag
    TrackID3.add(id3.COMM(encoding = 3, lang = "eng", desc = "", text = tags[6])) # Comment
    TrackID3.save(filename)

    print '[ID3] Insert CoverArt'
    TrackCover = MP3(filename)
    CoverFile = glob.glob('Cover.*')[0]
    CoverExt = CoverFile[-3:]
    fPicture = file(CoverFile, 'rb')
    sPic = fPicture.read()
    if CoverExt == 'png': sMimeType = 'image/png'
    elif CoverExt == 'jpg' or CoverExt == 'jpeg': sMimeType = 'image/jpg'
    else: sMimeType = 'image/jpg'
    muPic = id3.APIC(encoding = 3, mime = sMimeType, type = 3, desc = u'Album front cover', data = 0)
    TrackCover.tags[u'APIC:frontcover'] = muPic
    TrackCover.tags[u'APIC:frontcover'].data = sPic
    TrackCover.save(v1 = 2)
