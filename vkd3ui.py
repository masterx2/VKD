# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\vkd3gui.ui'
#
# Created: Mon Jan 07 04:00:08 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import phonon
from PyQt4 import QtWebKit


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(1004, 578)
        Dialog.setMinimumSize(QtCore.QSize(1004, 578))
        Dialog.setMaximumSize(QtCore.QSize(1004, 578))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 261, 23))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.searchButton = QtGui.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(9, 40, 81, 23))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.artistList = QtGui.QListWidget(Dialog)
        self.artistList.setGeometry(QtCore.QRect(10, 70, 261, 386))
        self.artistList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.artistList.setObjectName(_fromUtf8("artistList"))
        item = QtGui.QListWidgetItem()
        self.artistList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.artistList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.artistList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.artistList.addItem(item)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(95, 40, 86, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.clearButton = QtGui.QPushButton(Dialog)
        self.clearButton.setGeometry(QtCore.QRect(185, 40, 86, 23))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 455, 986, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.albumsList = QtGui.QListWidget(Dialog)
        self.albumsList.setGeometry(QtCore.QRect(280, 70, 261, 356))
        self.albumsList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.albumsList.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.albumsList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.albumsList.setObjectName(_fromUtf8("albumsList"))
        item = QtGui.QListWidgetItem()
        self.albumsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.albumsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.albumsList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.albumsList.addItem(item)
        self.trackList = QtGui.QListWidget(Dialog)
        self.trackList.setGeometry(QtCore.QRect(550, 70, 261, 381))
        self.trackList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.trackList.setObjectName(_fromUtf8("trackList"))
        item = QtGui.QListWidgetItem()
        self.trackList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.trackList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.trackList.addItem(item)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 45, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(550, 45, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.downloadAlbumButton = QtGui.QPushButton(Dialog)
        self.downloadAlbumButton.setEnabled(False)
        self.downloadAlbumButton.setGeometry(QtCore.QRect(825, 355, 166, 23))
        self.downloadAlbumButton.setObjectName(_fromUtf8("downloadAlbumButton"))
        self.albumArtView = QtWebKit.QWebView(Dialog)
        self.albumArtView.setGeometry(QtCore.QRect(820, 70, 174, 174))
        self.albumArtView.setUrl(QtCore.QUrl(_fromUtf8("http://userserve-ak.last.fm/serve/174s/52092823.jpg")))
        self.albumArtView.setObjectName(_fromUtf8("albumArtView"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(820, 45, 174, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vkLoginLine = QtGui.QLineEdit(Dialog)
        self.vkLoginLine.setGeometry(QtCore.QRect(10, 495, 261, 20))
        self.vkLoginLine.setObjectName(_fromUtf8("vkLoginLine"))
        self.vkPassLine = QtGui.QLineEdit(Dialog)
        self.vkPassLine.setGeometry(QtCore.QRect(10, 520, 261, 20))
        self.vkPassLine.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.vkPassLine.setEchoMode(QtGui.QLineEdit.Password)
        self.vkPassLine.setObjectName(_fromUtf8("vkPassLine"))
        self.vkLoginButton = QtGui.QPushButton(Dialog)
        self.vkLoginButton.setGeometry(QtCore.QRect(10, 545, 136, 23))
        self.vkLoginButton.setObjectName(_fromUtf8("vkLoginButton"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 475, 251, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.vkSaveCheckBox = QtGui.QCheckBox(Dialog)
        self.vkSaveCheckBox.setGeometry(QtCore.QRect(155, 545, 116, 23))
        self.vkSaveCheckBox.setObjectName(_fromUtf8("vkSaveCheckBox"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(285, 475, 151, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.workFolderLine = QtGui.QLineEdit(Dialog)
        self.workFolderLine.setGeometry(QtCore.QRect(280, 495, 258, 20))
        self.workFolderLine.setText(_fromUtf8(""))
        self.workFolderLine.setObjectName(_fromUtf8("workFolderLine"))
        self.workFolderButton = QtGui.QPushButton(Dialog)
        self.workFolderButton.setGeometry(QtCore.QRect(280, 520, 111, 23))
        self.workFolderButton.setObjectName(_fromUtf8("workFolderButton"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(825, 247, 166, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.artistLabel = QtGui.QLabel(Dialog)
        self.artistLabel.setGeometry(QtCore.QRect(825, 262, 166, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.artistLabel.setFont(font)
        self.artistLabel.setObjectName(_fromUtf8("artistLabel"))
        self.AlbumLabel = QtGui.QLabel(Dialog)
        self.AlbumLabel.setGeometry(QtCore.QRect(825, 290, 166, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AlbumLabel.setFont(font)
        self.AlbumLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.AlbumLabel.setWordWrap(True)
        self.AlbumLabel.setObjectName(_fromUtf8("AlbumLabel"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(825, 277, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(825, 337, 65, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.trackCountLabel = QtGui.QLabel(Dialog)
        self.trackCountLabel.setGeometry(QtCore.QRect(890, 335, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.trackCountLabel.setFont(font)
        self.trackCountLabel.setObjectName(_fromUtf8("trackCountLabel"))
        self.downloadCheckedTracksButton = QtGui.QPushButton(Dialog)
        self.downloadCheckedTracksButton.setEnabled(False)
        self.downloadCheckedTracksButton.setGeometry(QtCore.QRect(825, 380, 166, 23))
        self.downloadCheckedTracksButton.setObjectName(_fromUtf8("downloadCheckedTracksButton"))
        self.downloadAlbumartButton = QtGui.QPushButton(Dialog)
        self.downloadAlbumartButton.setEnabled(False)
        self.downloadAlbumartButton.setGeometry(QtCore.QRect(825, 405, 166, 23))
        self.downloadAlbumartButton.setObjectName(_fromUtf8("downloadAlbumartButton"))
        self.playListGetAlbumButton = QtGui.QPushButton(Dialog)
        self.playListGetAlbumButton.setEnabled(False)
        self.playListGetAlbumButton.setGeometry(QtCore.QRect(825, 430, 166, 23))
        self.playListGetAlbumButton.setObjectName(_fromUtf8("playListGetAlbumButton"))
        self.downloadChekedAlbums = QtGui.QPushButton(Dialog)
        self.downloadChekedAlbums.setGeometry(QtCore.QRect(280, 430, 166, 23))
        self.downloadChekedAlbums.setObjectName(_fromUtf8("downloadChekedAlbums"))
        self.playlistAlbums = QtGui.QCheckBox(Dialog)
        self.playlistAlbums.setGeometry(QtCore.QRect(455, 430, 86, 23))
        self.playlistAlbums.setObjectName(_fromUtf8("playlistAlbums"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(285, 10, 706, 34))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.playButton = QtGui.QPushButton(self.frame)
        self.playButton.setGeometry(QtCore.QRect(10, 5, 36, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.playButton.setFont(font)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.stopButton = QtGui.QPushButton(self.frame)
        self.stopButton.setGeometry(QtCore.QRect(50, 5, 36, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.prevButton = QtGui.QPushButton(self.frame)
        self.prevButton.setGeometry(QtCore.QRect(89, 5, 36, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.prevButton.setFont(font)
        self.prevButton.setObjectName(_fromUtf8("prevButton"))
        self.nextButton = QtGui.QPushButton(self.frame)
        self.nextButton.setGeometry(QtCore.QRect(130, 5, 36, 23))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.nextButton.setFont(font)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.frame)
        self.seekSlider.setGeometry(QtCore.QRect(248, 9, 305, 19))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.frame)
        self.volumeSlider.setGeometry(QtCore.QRect(568, 6, 131, 22))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(174, 10, 64, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(555, 474, 151, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.acoustidCheck = QtGui.QCheckBox(Dialog)
        self.acoustidCheck.setGeometry(QtCore.QRect(810, 522, 160, 17))
        self.acoustidCheck.setObjectName(_fromUtf8("acoustidCheck"))
        self.acoustidMinRateSpin = QtGui.QSpinBox(Dialog)
        self.acoustidMinRateSpin.setGeometry(QtCore.QRect(756, 548, 46, 23))
        self.acoustidMinRateSpin.setSpecialValueText(_fromUtf8(""))
        self.acoustidMinRateSpin.setMinimum(50)
        self.acoustidMinRateSpin.setMaximum(100)
        self.acoustidMinRateSpin.setProperty("value", 95)
        self.acoustidMinRateSpin.setObjectName(_fromUtf8("acoustidMinRateSpin"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(811, 551, 181, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(610, 525, 134, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.processListSpin = QtGui.QSpinBox(Dialog)
        self.processListSpin.setGeometry(QtCore.QRect(553, 522, 46, 23))
        self.processListSpin.setSpecialValueText(_fromUtf8(""))
        self.processListSpin.setMinimum(1)
        self.processListSpin.setMaximum(20)
        self.processListSpin.setProperty("value", 3)
        self.processListSpin.setObjectName(_fromUtf8("processListSpin"))
        self.timeRangeSpin = QtGui.QSpinBox(Dialog)
        self.timeRangeSpin.setGeometry(QtCore.QRect(553, 548, 46, 23))
        self.timeRangeSpin.setSpecialValueText(_fromUtf8(""))
        self.timeRangeSpin.setMinimum(0)
        self.timeRangeSpin.setMaximum(20)
        self.timeRangeSpin.setProperty("value", 1)
        self.timeRangeSpin.setObjectName(_fromUtf8("timeRangeSpin"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(610, 550, 134, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.minBitrateSpin = QtGui.QSpinBox(Dialog)
        self.minBitrateSpin.setGeometry(QtCore.QRect(553, 497, 46, 23))
        self.minBitrateSpin.setSpecialValueText(_fromUtf8(""))
        self.minBitrateSpin.setMinimum(8)
        self.minBitrateSpin.setMaximum(500)
        self.minBitrateSpin.setProperty("value", 320)
        self.minBitrateSpin.setObjectName(_fromUtf8("minBitrateSpin"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(610, 500, 156, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(796, 473, 89, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.profilesBox = QtGui.QComboBox(Dialog)
        self.profilesBox.setGeometry(QtCore.QRect(796, 490, 191, 22))
        self.profilesBox.setObjectName(_fromUtf8("profilesBox"))
        self.profilesBox.addItem(_fromUtf8(""))
        self.profilesBox.addItem(_fromUtf8(""))
        self.profilesBox.addItem(_fromUtf8(""))
        self.profilesBox.addItem(_fromUtf8(""))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(825, 320, 86, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.trackCountLabel_2 = QtGui.QLabel(Dialog)
        self.trackCountLabel_2.setGeometry(QtCore.QRect(880, 318, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.trackCountLabel_2.setFont(font)
        self.trackCountLabel_2.setObjectName(_fromUtf8("trackCountLabel_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.searchButton, self.lineEdit)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Название группы или имя исполнителя...", None))
        self.searchButton.setText(_translate("Dialog", "Поиск", None))
        self.artistList.setToolTip(_translate("Dialog", "Список найденый исполнителей", None))
        __sortingEnabled = self.artistList.isSortingEnabled()
        self.artistList.setSortingEnabled(False)
        item = self.artistList.item(0)
        item.setText(_translate("Dialog", "РАз", None))
        item = self.artistList.item(1)
        item.setText(_translate("Dialog", "Два", None))
        item = self.artistList.item(2)
        item.setText(_translate("Dialog", "Три", None))
        item = self.artistList.item(3)
        item.setText(_translate("Dialog", "Четыре", None))
        self.artistList.setSortingEnabled(__sortingEnabled)
        self.cancelButton.setText(_translate("Dialog", "Отмена", None))
        self.clearButton.setText(_translate("Dialog", "Отчистить", None))
        self.albumsList.setToolTip(_translate("Dialog", "Список найденых альбомов", None))
        __sortingEnabled = self.albumsList.isSortingEnabled()
        self.albumsList.setSortingEnabled(False)
        item = self.albumsList.item(0)
        item.setText(_translate("Dialog", "Пять", None))
        item = self.albumsList.item(1)
        item.setText(_translate("Dialog", "Шерсть", None))
        item = self.albumsList.item(2)
        item.setText(_translate("Dialog", "Воусемь", None))
        item = self.albumsList.item(3)
        item.setText(_translate("Dialog", "Дейвять", None))
        self.albumsList.setSortingEnabled(__sortingEnabled)
        self.trackList.setToolTip(_translate("Dialog", "Список треков выбранного альбома", None))
        __sortingEnabled = self.trackList.isSortingEnabled()
        self.trackList.setSortingEnabled(False)
        item = self.trackList.item(0)
        item.setText(_translate("Dialog", "Васемнацадь", None))
        item = self.trackList.item(1)
        item.setText(_translate("Dialog", "ТриуатьДвадцать", None))
        item = self.trackList.item(2)
        item.setText(_translate("Dialog", "Пятьь", None))
        self.trackList.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "Албомы", None))
        self.label_2.setText(_translate("Dialog", "Трек лист", None))
        self.downloadAlbumButton.setText(_translate("Dialog", "Скачать альбом", None))
        self.label_3.setText(_translate("Dialog", "Обложка альбома", None))
        self.vkLoginLine.setPlaceholderText(_translate("Dialog", "Логин", None))
        self.vkPassLine.setPlaceholderText(_translate("Dialog", "Пароль", None))
        self.vkLoginButton.setText(_translate("Dialog", "Войти", None))
        self.label_4.setText(_translate("Dialog", "Учетная запись [Вконтакте]", None))
        self.vkSaveCheckBox.setText(_translate("Dialog", "Сохранить пароль", None))
        self.label_5.setText(_translate("Dialog", "Куда скачивать?", None))
        self.workFolderLine.setPlaceholderText(_translate("Dialog", "D:\\Music", None))
        self.workFolderButton.setText(_translate("Dialog", "Выбрать папку", None))
        self.label_6.setText(_translate("Dialog", "Исполнитель:", None))
        self.artistLabel.setText(_translate("Dialog", "Noize MC", None))
        self.AlbumLabel.setText(_translate("Dialog", "Последний Альбом", None))
        self.label_9.setText(_translate("Dialog", "Название альбома", None))
        self.label_10.setText(_translate("Dialog", "Всего треков:", None))
        self.trackCountLabel.setText(_translate("Dialog", "21", None))
        self.downloadCheckedTracksButton.setText(_translate("Dialog", "Скачать выбранные треки", None))
        self.downloadAlbumartButton.setText(_translate("Dialog", "Загрузить обложки", None))
        self.playListGetAlbumButton.setText(_translate("Dialog", "Сгенерировать плейлист", None))
        self.downloadChekedAlbums.setText(_translate("Dialog", "Скачать выбранные альбомы", None))
        self.playlistAlbums.setText(_translate("Dialog", "+ Плейлист", None))
        self.playButton.setText(_translate("Dialog", "Play", None))
        self.stopButton.setText(_translate("Dialog", "Stop", None))
        self.prevButton.setText(_translate("Dialog", "Prev", None))
        self.nextButton.setText(_translate("Dialog", "Next", None))
        self.label_8.setText(_translate("Dialog", "00:00/00:00", None))
        self.label_12.setText(_translate("Dialog", "Параметры выбора треков", None))
        self.acoustidCheck.setText(_translate("Dialog", "Использовать Acoustid.org", None))
        self.label_13.setText(_translate("Dialog", "Минимальный рейтингAcoustid.org", None))
        self.label_14.setText(_translate("Dialog", "Размер списка обработки", None))
        self.label_15.setText(_translate("Dialog", "Вилка времени", None))
        self.label_16.setText(_translate("Dialog", "Минимальный битрейт (kbit/s)", None))
        self.label_7.setText(_translate("Dialog", "Профили выбора", None))
        self.profilesBox.setItemText(0, _translate("Dialog", "Обычный", None))
        self.profilesBox.setItemText(1, _translate("Dialog", "Быстрый", None))
        self.profilesBox.setItemText(2, _translate("Dialog", "Медленный", None))
        self.profilesBox.setItemText(3, _translate("Dialog", "Очень медленный", None))
        self.label_11.setText(_translate("Dialog", "Год релиза", None))
        self.trackCountLabel_2.setText(_translate("Dialog", "2012", None))
