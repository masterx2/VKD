#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cmd
import mbrainzApi
import ConfigParser
from unidecode import unidecode
from vkdtools import tomin, initVk, get_links, getWorkdir, DownloadPrepare, ProcessFile

config = ConfigParser.ConfigParser()

mbz_api = mbrainzApi.mbzAPI()

intro = "\nWelcome to VKD ver 3.0 with Command Interface\ntype 'help' for view command list\n"

#noinspection PyBroadException
class command_interface(cmd.Cmd):
    status = {'vk': 'off',
              'artist': 'notset',
              'album': 'notset',
              'score': 98.0,
              'listsize': 5,
              'timerange': 1,
              'manual': False
    }
    prompt = '(VK:%s|Artist:%s) > ' % (status['vk'], status['artist'])
    runDir = os.getcwdu()


    def do_status(self, line):
        for key in self.status.keys():
            print '[%s] -> [%s]' % (key, self.status[key])

    def do_cd(self, line):
        os.chdir(getWorkdir())

    def do_quit(self, line):
        print 'Exiting...'
        quit()

    def do_initvk(self, line):
        global login, login, password
        if line and len(line.split()) > 1:
            login = line.split()[0]
            password = line.split()[1]
        else:
            print 'Trying get from Config file...',
            try:
                config.read(os.path.join(self.runDir, 'vkdconfig.ini'))
                login = config.get('vkuser', 'login')
                password = config.get('vkuser', 'pass')
                print 'OK'
            except:
                print 'Fail'
        try:
            self.br = initVk(login, password)
            self.status['vk'] = 'OK'
            self.prompt = '(VK:%s|Artist:%s) > ' % (self.status['vk'], self.status['artist'])
        except: print 'VK Login Failed'

    def do_search(self, line):
        self.artist_list = mbz_api.findArtist(line.decode('utf-8'), 20)
        for index in self.artist_list.keys():
            try:
                print index, self.artist_list[index][0]
            except:
                print '[Output Error]'

    def do_set(self, line):
        self.status['artist'] = self.artist_list[int(line)][0]
        self.status['artistid'] = self.artist_list[int(line)][1]
        self.prompt = '(VK:%s|Artist:%s) > ' % (self.status['vk'], self.status['artist'])

    def do_score(self, line):
        if line:
            self.status['score'] = float(line)
        else:
            print '[Score] Current Score Limit = %s' % (self.status['score'])

    def do_listsize(self, line):
        if line:
            self.status['listsize'] = int(line)
        else:
            print '[ListSize] Current List Limit = %s' % (self.status['listsize'])

    def do_timerange(self, line):
        if line:
            self.status['timerange'] = int(line)
        else:
            print '[TimeRange] Current Time Range = %s' % (self.status['timerange'])

    def do_manual(self, line):
        if line:
            if line == 'on':
                self.status['manual'] = True
            elif line == 'off':
                self.status['manual'] = False
        else:
            print '[Acoustic ID] Score Mode', self.status['manual']

    def do_albums(self, line):
        self.album_list = mbz_api.getArtistById(self.status['artistid'])
        if self.album_list:
            for index in self.album_list.keys():
                try:
                    print index, self.album_list[index][0]
                except:
                    print '[Output Error]'

    def do_tracks(self, line):
        if len(line.split()) > 1:
            print '>>> Input Error, Need one Album number!'
        else:
            self.track_list, self.year = mbz_api.getAlbumById(self.album_list[int(line)][1])
            self.status['album'] = self.album_list[int(line)][0]
            self.status['year'] = self.year
            for index in self.track_list.keys():
                try:
                    print index, self.track_list[index][0], tomin(self.track_list[index][1])
                except:
                    print '[Output Error]'

    def do_tracksget(self, line):
        for index in line.split():
            index = int(index)
            filename = unidecode(u'[%d] %s - %s.mp3' % (index, self.status['artist'], self.track_list[index][0]))
            if not os.path.exists(filename):
                links = get_links(self.status['artist'],
                                  self.track_list[index][0],
                                  self.track_list[index][1],
                                  self.br, self.status['listsize'],
                                  self.status['timerange']
                )
                id3tags = (str(index), self.track_list[index][0], self.status['artist'],
                           self.status['album'], str(self.year))
                if links:
                    print '>>> Start Processing %s' % filename
                    ProcessFile(links, filename, id3tags, self.status['score'], self.status['manual'])
                else:
                    print '>>> No Files On Server'
            else:
                print 'File exist, skip downloading...'

    def do_get(self, line):
        if self.status['vk'] == 'OK':
            for album_index in line.split():
                self.track_list, self.year = mbz_api.getAlbumById(self.album_list[int(album_index)][1])
                DownloadPrepare(self.status['artist'], self.album_list[int(album_index)][0], self.year)
                for index in self.track_list.keys():
                    filename = unidecode(u'[%d] %s - %s.mp3' % (index, self.status['artist'], self.track_list[index][0]))
                    if not os.path.exists(filename):
                        links = get_links(self.status['artist'],
                                          self.track_list[index][0],
                                          self.track_list[index][1],
                                          self.br, self.status['listsize'],
                                          self.status['timerange'])
                        id3tags = (str(index), self.track_list[index][0], self.status['artist'],
                                   self.album_list[int(album_index)][0], str(self.year))
                        if links:
                            print '>>> Start Processing %s' % filename
                            ProcessFile(links, filename, id3tags, self.status['score'], self.status['manual'])
                        else:
                            print '>>> No Files On Server'
                    else:
                        print 'File exist, skip downloading...'
                os.chdir('..')
                os.chdir('..')
        else:
            print 'Login VK First!'

def main():
    terminal = command_interface()
    terminal.cmdloop(intro)

if __name__ == '__main__':
    main()