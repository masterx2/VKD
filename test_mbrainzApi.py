#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MasterX2'

from mbrainzApi import mbzAPI

mbAPI = mbzAPI()

results = mbAPI.findArtists(u'Сплин')
artist = results[0].getArtist()

print 'name >', artist.name
print 'id >', artist.id[30:]

artist = mbAPI.getArtistById(artist.id)
releases = artist.releases
tag = artist.tags[0]
release = releases[0]

print 'title >', release.title
print 'tags >', tag
print 'id >', release.id[31:]

release = mbAPI.getReleaseById(release.id)
track = release.tracks[0]

print 'title >', track.title
print 'duration >', track.duration