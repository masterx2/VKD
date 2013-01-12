#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MasterX2'

import os
import re
import sys
import ConfigParser

from mbrainzApi import mbzAPI
from lastfmApi import lfmAPI
from unidecode import unidecode
from vkdtools import tomin, initVk, parseVk, getWorkdir, DownloadPrepare, ProcessFile

sysname = re.compile(r'[!/\\:;*?«<>|]+')

# Init

# Пользователь выбирает интересуещего его исполнителя
user_artist = u'Noize MC'

Start_Dir = os.getcwdu()
config = ConfigParser.ConfigParser()

config.read(os.path.join(Start_Dir, 'vkdconfig.ini'))
login = config.get('vkuser', 'login')
password = config.get('vkuser', 'pass')

lfm = lfmAPI("f3d8fbacbda2a35bfa855ef52052ca25") # Init Last.FM Api
mbAPI = mbzAPI() # Init MusicBrainz Api

# VK Login

br = initVk(login, password)

# Last.FM Build Artist Profile

artists = lfm.artist_search(user_artist) # Список найденых исполнителей
albums = lfm.getTopAlbums(artists[0]) # Список альбомов испослнителя
# Словарь { 'тип обложки' : 'ссылка' } типы [small|large|medium|mega|extralarge]
covers = lfm.getAlbumCovers(artists[0], albums[0])
# Список треков в формате [['номер трека', 'имя трека', 'длительность в секундах'], ....]
# Дата релиза в формате datetime объекта
tracks, release_date = lfm.getAlbumInfo(artists[0], albums[0])
tags = lfm.getTopTags(artists[0]) # Список тегов исполнителя

selected_Artist = artists[0]
selected_Album = albums[0]

if release_date:
    release_Year = release_date.year
else:
    release_Year = ''


# Подготовка к скачиванию, необходимо передать имя исполнителя, название альбома, обложки, год релиза
# Если будет передан год то к началу названия папки с альбомом добавится [XXXX]
DownloadPrepare(artists[0], albums[0], covers, release_Year)

# Цикл по списку треков

for selected_Track in tracks:
    # VK Parse, Парсеру необходимо передать экземпляр браузера и строку поиска
    # Ответ парсера список в формате [['исполнитель', 'имя трека', 'длительность в секундах', 'ссылка на файл'], ....]
    vk_request = '%s - %s' % (selected_Artist, selected_Track[1])
    vk_data = parseVk(vk_request, br)

    selected_Url = vk_data[0][3]
    # Трек найден и выбран нужный URL
    # Скачиваем трек
    # -- Готовим название файла
    track_filename = '[%s] %s - %s.mp3' % (selected_Track[0], selected_Artist, selected_Track[1])
    # ---- Удаляем неподдерживаемые симфолы из имени файла
    track_filename = sysname.sub('', track_filename)
    # -- Переменная ID3 тегов
    track_id3tags = (selected_Track[0], # Track Number
                     selected_Track[1], # Song Name
                     selected_Artist, # Artist
                     selected_Album, # Album Name
                     str(release_Year),  # Year
                     tags[0], # Artist Tag
                     'Comment to File' # Comment
                     )
    # -- Скачиваем файл, записываем теги и вставляем обложку
    ProcessFile(track_filename, selected_Url, track_id3tags)

# Выходим в рабочую директорию
os.chdir('../..')

# При необходимости повторить ;)