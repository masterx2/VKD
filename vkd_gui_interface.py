# -*- coding: utf-8 -*-

from PyQt4.QtCore import QUrl, SIGNAL
from PyQt4.QtGui import *
import os
import sys
from lastfmApi import lfmAPI
import ConfigParser

from vkdtools import tomin, initVk

import vkd3ui

class MainWindow(QDialog, vkd3ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.lfm = lfmAPI("f3d8fbacbda2a35bfa855ef52052ca25") # Init Last.FM Api
        self.status = {'artist' : '',
                       'album' : '',
                        'tags' : ''}

        self.runDir = os.getcwdu()
        config = ConfigParser.ConfigParser()

        try:
            config.read(os.path.join(self.runDir, 'vkdconfig.ini'))
            self.login = config.get('vkuser', 'login')
            self.password = config.get('vkuser', 'pass')
            self.vkLoginLine.setText(self.login)
            self.vkPassLine.setText(self.password)
        except:
            print 'Fail'

        self.connect(self.searchButton, SIGNAL('clicked()'), self.fillArtists)
        self.connect(self.artistList, SIGNAL('itemDoubleClicked(QListWidgetItem *)'), self.ArtistListClick)
        self.connect(self.albumsList, SIGNAL('itemDoubleClicked(QListWidgetItem *)'), self.AlbumsListClick)
        self.connect(self.downloadChekedAlbums, SIGNAL('clicked()'), self.downloadCheckedAlbumsGo)
        self.connect(self.trackList, SIGNAL('itemDoubleClicked(QListWidgetItem *)'), self.TrackListClick)
        self.connect(self.vkLoginButton, SIGNAL('clicked()'), self.vkLogin)

    def vkLogin(self):
        login = self.vkLoginLine.text()
        password = self.vkPassLine.text()

        if login and password:
            self.br = initVk(login, password)
            self.label_4.setText(u"Учетная запись [Вконтакте] - <font color=green>Вход выполнен</font>")
        else:
            QMessageBox.warning(self, 'VKD3', 'VK Login Error')

    def fillArtists(self):
        if self.lineEdit.text():
            self.artistList.clear()
            self.artistList.addItems(self.lfm.artist_search(unicode(self.lineEdit.text())))
        else:
            QMessageBox.warning(self, 'VKD3', 'Search request is Empty')

    def ArtistListClick(self, item):
        selectedArtist = unicode(item.text())
        self.albumsList.clear()
        self.albumsList.addItems(self.lfm.getTopAlbums(selectedArtist))
        self.status['tags'] = self.lfm.getTopTags(selectedArtist)
        self.status['artist'] = selectedArtist
        self.artistLabel.setText(selectedArtist)

    def AlbumsListClick(self, item):
        self.downloadAlbumButton.setEnabled(True)
        self.downloadCheckedTracksButton.setEnabled(True)
        self.downloadAlbumartButton.setEnabled(True)
        self.playListGetAlbumButton.setEnabled(True)
        self.trackList.clear()
        selectedAlbum = unicode(item.text())
        covers = self.lfm.getAlbumCovers(self.status['artist'], selectedAlbum)
        tracks, release_date = self.lfm.getAlbumInfo(self.status['artist'], selectedAlbum)
        self.albumArtView.load(QUrl(covers['large']))
        self.AlbumLabel.setText(selectedAlbum)
        self.trackCountLabel.setText(str(len(tracks)))

        if release_date:
            release_Year = release_date.year
        else:
            release_Year = ''

        self.status['year'] = release_Year
        self.trackCountLabel_2.setText(str(release_Year))

        self.dict_tracks = {}
        for track in tracks:
            trackListItem = '[%s] %s [%s]' % (track[0], track[1], tomin(track[2]))
            self.trackList.addItem(trackListItem)
            self.dict_tracks[trackListItem] = track

    def downloadCheckedAlbumsGo(self):
        selectedAlbums = self.albumsList.selectedItems()

    def TrackListClick(self, item):
        selectedTrack = unicode(item.text())
        selectedTrackDetailed = self.dict_tracks[selectedTrack]


app = QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())