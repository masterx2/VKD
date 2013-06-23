#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MasterX2'

from musicbrainz2 import model, webservice
from musicbrainz2.webservice import Query, ArtistFilter, WebServiceError

class mbzAPI:
    def __init__(self):
        self.q = Query()

    def findArtists(self, artist, limit = 20):
        try:
            aFilter = ArtistFilter(artist, limit)
            return self.q.getArtists(aFilter)
        except WebServiceError, e:
            # Logging Need
            return None

    def getArtistById(self, artistid):
        try:
            inc = webservice.ArtistIncludes(releases = (model.Release.TYPE_ALBUM, model.Release.TYPE_OFFICIAL),
                                            tags = True)
            return self.q.getArtistById(artistid, inc)
        except webservice.WebServiceError, e:
            # Logging Need
            return None

    def getReleaseById(self, album):
        try:
            inc = webservice.ReleaseIncludes(tracks = True)

            return self.q.getReleaseById(album, inc)
        except webservice.WebServiceError, e:
            # Logging Need
            return None