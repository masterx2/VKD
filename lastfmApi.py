#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import xml.etree.ElementTree as et
from datetime import datetime

__author__ = 'MasterX2'

class lfmAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def api_request(self, method, search_string):

        request = 'http://ws.audioscrobbler.com/2.0/?method=' + \
                  method + \
                  search_string + \
                  '&api_key=' + \
                  self.api_key
        print ('API Request >>> %s' % (request[41:request.find('&api')]))
        return urllib2.urlopen(request).read()

    def artist_search(self, artist):
        artist = artist.encode('utf-8')
        artists = []
        artist_tree = et.fromstring(self.api_request('artist.search', '&artist=' + urllib2.quote(artist)))
        for element in artist_tree.findall('./results/artistmatches/artist'):
            artists.append(element[0].text)
        return artists

    def getTopAlbums(self, artist):
        artist = artist.encode('utf-8')
        albums = []
        albums_tree = et.fromstring(
            self.api_request('artist.gettopalbums', '&artist=' + urllib2.quote(artist)))
        for element in albums_tree.findall('./topalbums/album'):
            albums.append(element[0].text)
        return albums

    def getAlbumInfo(self, artist, album):
        artist = artist.encode('utf-8')
        album = album.encode('utf-8')
        tracks = []
        covers = {}

        tracks_tree = et.fromstring(self.api_request('album.getinfo', '&artist=' + urllib2.quote(artist) + \
                                                                      '&album=' + urllib2.quote(album)))
        try:
            release_date = datetime.strptime(tracks_tree[0][5].text.strip(), '%d %b %Y, %H:%M')
        except ValueError:
            release_date = None

        for element in tracks_tree.findall('./album/tracks/track'):
            tracks.append([element.items()[0][1], element[0].text, element[1].text])

        for element in tracks_tree.findall('./album/image'):
                covers[element.items()[0][1]] = element.text

        return tracks, release_date, covers


    def getTopTags(self, artist):
        artist = artist.encode('utf-8')
        top_tags = []
        tag_tree = et.fromstring(self.api_request('artist.gettoptags', '&artist=' + urllib2.quote(artist)))
        for element in tag_tree.findall('./toptags/tag'):
            top_tags.append(element[0].text)
        return top_tags