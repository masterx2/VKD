#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cmd
import ConfigParser
import pickle

from mbrainzApi import mbzAPI
from lastfmApi import lfmAPI
from unidecode import unidecode
from vkdtools import tomin, initVk, get_links, getWorkdir, DownloadPrepare, ProcessFile

config = ConfigParser.ConfigParser()

mbz_api = mbzAPI()
lfm = lfmAPI("f3d8fbacbda2a35bfa855ef52052ca25")


intro = "\nWelcome to VKD ver 3.0 with Command Interface\ntype 'help' for view command list\n"

#noinspection PyBroadException
class command_interface(cmd.Cmd):
    status = {'vk': 'off',
              'artist': 'notset',
              'album': 'notset',
              'score': 98.0,
              'listsize': 5,
              'timerange': 0,
              'manual': False
    }
    prompt = '(VK:%s|Artist:%s) > ' % (status['vk'], status['artist'])
    runDir = os.getcwdu()


    def do_status(self, line):
        for key in self.status.keys():
            print '[%s] -> [%s]' % (key, self.status[key]) # # OK

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
        index = 1
        self.artist_list = lfm.artist_search(line)
        for artist in self.artist_list:
            print index, artist
            index += 1

    def do_set(self, line):
        self.status['artist'] = self.artist_list[int(line)-1]
        self.prompt = '(VK:%s|Artist:%s) > ' % (self.status['vk'], self.status['artist'])
        self.album_list = lfm.getTopAlbums(self.status['artist'])

        if self.album_list:
            index = 1
            for album in self.album_list:
                print index, album
                index += 1
        else:
            print 'No Albums'

    def do_score(self, line):
        if line:
            self.status['score'] = float(line)
        else:
            print '[Score] Current Score Limit = %s' % (self.status['score'])

        def do_timerange(self, line):
            if line:
                self.status['timerange'] = int(line)
            else:
                print '[TimeRange] Current Time Range = %s' % (self.status['timerange'])

    def do_timerange(self, line):
        if line:
            self.status['timerange'] = int(line)
        else:
            print '[TimeRange] Current Time Range = %s' % (self.status['timerange'])

    def do_listsize(self, line):
        if line:
            self.status['listsize'] = int(line)
        else:
            print '[ListSize] Current List Limit = %s' % (self.status['listsize'])

    def do_manual(self, line):
        if line:
            if line == 'on':
                self.status['manual'] = True
            elif line == 'off':
                self.status['manual'] = False
        else:
            print '[Acoustic ID] Score Mode', self.status['manual']

    def do_tracks(self, line):
        self.status['album'] = self.album_list[int(line)-1]
        self.tracks, self.release_date = lfm.getAlbumInfo(self.status['artist'], self.status['album'])

        if self.release_date: self.status['year'] = self.release_date.year
        else: self.status['year'] = ''

        for track in self.tracks:
            print '[%s] %s (%s)' % (track[0], track[1], tomin(track[2]))

    def do_get(self, line):
        if self.status['vk'] == 'OK':
            artist = self.status['artist']
            album = self.status['album'] = self.album_list[int(line)-1]

            tracks, release_date, covers = lfm.getAlbumInfo(artist, album)

            tags = lfm.getTopTags(artist)
            self.status['tag'] = tags[0]

            if release_date: year = self.status['year'] = str(release_date.year)
            else: year = self.status['year'] = ''

            # Session Save
            data_save = [artist, album, covers, year, tracks, self.status]
            with open('session.data' , 'w') as dump_file:
                pickle.dump(data_save, dump_file)
            del data_save
            print 'Session saved in session.data'

            DownloadPrepare(artist, album, covers, year)

            for track in tracks:
                ProcessFile(track, self.status, self.br)

            os.chdir('../..')
            os.remove('session.data')

        else:
            print 'Login VK First!'

    def do_resume(self, line):
        if self.status['vk'] == 'OK':
            if os.path.exists('session.data'):
                with open('session.data' , 'r') as dump_file:
                    data_load = pickle.load(dump_file)
                    artist = data_load[0]
                    album = data_load[1]
                    covers = data_load[2]
                    year = data_load[3]
                    tracks = data_load[4]
                    self.status = data_load[5]
                del data_load
                print 'Session Resume....'
                DownloadPrepare(artist, album, covers, year)

                for track in tracks:
                    ProcessFile(track, self.status, self.br)

                os.chdir('../..')
                os.remove('session.data')

            else: print 'Session file not found!'
        else: print 'Login VK First'

def main():
    terminal = command_interface()
    terminal.cmdloop(intro)

if __name__ == '__main__':
    main()