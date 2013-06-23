#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MasterX2'

from lastfmApi import lfmAPI

lfm = lfmAPI("f3d8fbacbda2a35bfa855ef52052ca25")

artists = lfm.artist_search(u'Сплин')
print 'Artist   - %s' % artists[0]

albums = lfm.getTopAlbums(artists[0])
print 'Albums   - %s' % albums[0]

covers = lfm.getAlbumCovers(artists[0], albums[0])
print 'Covers   - %s' % covers

tracks, release_date = lfm.getAlbumInfo(artists[0], albums[0])
for track in tracks:
    print 'Track #%s - %s | %s' % (track[0], track[1], track[2])
print 'Year     - %s' % release_date.strip()

tags = lfm.getTopTags(artists[0])
print 'Tag #1   - %s' % tags[0]



