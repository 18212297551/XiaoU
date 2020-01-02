# -*- coding: utf-8 -*-

# Form implementation generated from reading UI file '小U2.UI'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# import ctypes
import base64
import pickle
import random
import traceback
import eyed3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QCursor, QPixmap, QPainter, QImage, QPen, QPainterPath
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl, QThread, pyqtSignal, QPoint
from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel, QSpinBox, QSlider, QColorDialog
import requests
import socket
import json
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
from urllib.parse import quote_plus

from pydub.utils import mediainfo
from pydub import AudioSegment
from baidu_aip import AipSpeech
from lxml import etree
import os
import time
import re
import shutil
import multiprocessing
import pyautogui
import cv2 as cv
import numpy as np



# 自定义模块



## 全局变量区域#########################################

friend_int = 0  # tab3图片播放序号
sum_songs = {}  # 搜索过的所有音乐信息
API = 'baidu'  # 定义机器人接口和默认值
PER = 4  # 定义机器人语音人物
PIT = 6  # 定义机器人语音音调
video_items = {}  # 搜索过的所有视频信息
syn_items = {}
asr_items = {}
info = {
    "apiKey": "9ad4e7ad478b4353a27aad1eab121d79",
    "userId": "15261800956"
}

# 音乐下载池
Queue_song = multiprocessing.Queue()
# 语音合成线程池
Queue_speech = multiprocessing.Queue()
# 语音识别线程池
Queue_ASR = multiprocessing.Queue()

socket.setdefaulttimeout(120)
here_dic = os.getcwd()  # 当前路径，读取依赖文件
# os.system('setx PATH=%PATH%;{}\\'.format(here_dic))
screen_height = pyautogui.size().height
screen_width = pyautogui.size().width
# app_width = screen_width/3 + 65
# app_height = screen_height/3 + 130

app_width = screen_width / 3 + 65
app_height = screen_height / 3 + 130



## 全局变量区域##########################
try:
    if os.path.exists(r'D:\XiaoU\Deal\Voice\Reco'):
        shutil.rmtree(r'D:\XiaoU\Deal\Voice\Reco')
except:pass

def catch_except(func,**kwargs):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except:
            with open('./log.txt', 'a+') as _f:
                _error = traceback.format_exc()
                _t = '>'*10 + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '<'*10
                content = "\n{}\n{}\n".format(_t,_error)
                _f.write(content)
                print(_error)
    return wrapper

class Ui_Form(QWidget):  # QMainWindow

    def __init__(self):
        super(Ui_Form, self).__init__()  # ,QtCore.Qt.FramelessWindowHint
        global friend_int, sum_songs, API, PER, PIT, video_items, info
        self.friend_int = friend_int
        self.sum_songs = sum_songs
        self.API = API
        self.PER = PER
        self.PIT = PIT
        self.video_items = video_items
        self.info = info
        self.initDrag()
        self.player_2_list_Mode = 1
        self.player_5_list_Mode = 1
        self.listwidget_5_list_state = 1


        # 窗口初始化
        self.init_mainwindow()

        self.init_tab1()
        self.init_tab2()
        self.init_tab5()
        # self.init_tab3()
        self.init_tab4()



        self.init_public()





    def init_mainwindow(self):
        self.setObjectName("Main")
        self.resize(app_width, app_height)
        # 窗体透明度设置
        self.setMouseTracking(True)
        # self.setWindowOpacity(0.8)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("{}/ico/b1.ico".format(here_dic)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.tabWidget = QtWidgets.QTabWidget()
        # self.gridLayout.setSpacing(0)
        # 主窗口 》》》》》》》》》》》
        font = QtGui.QFont()
        font.setFamily("楷体")
        #font.setPointSize(10)
        self.tabWidget.setFont(font)
        #self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setObjectName("tabWidget")


        #self.tabWidget.setMouseTracking(True)

        # 自定义窗口关闭最大化最小化按钮
        self.btn_0_max = QtWidgets.QToolButton()
        self.btn_0_max.setObjectName('btn_0_max')
        self.gridLayout.addWidget(self.btn_0_max, 0, 10, 1, 1)
        self.btn_0_min = QtWidgets.QToolButton()
        self.btn_0_min.setObjectName('btn_0_min')
        self.gridLayout.addWidget(self.btn_0_min, 0, 9, 1, 1)
        self.btn_0_close = QtWidgets.QToolButton()
        self.btn_0_close.setObjectName('btn_0_close')
        self.gridLayout.addWidget(self.btn_0_close, 0, 11, 1, 1)
        self.btn_0_min.setFixedSize(QtCore.QSize(25, 25))
        self.btn_0_max.setFixedSize(QtCore.QSize(25, 25))
        self.btn_0_close.setFixedSize(QtCore.QSize(25, 25))
        ico_max = QIcon()
        ico_max.addPixmap(QPixmap('{}\ico\show_max1.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_0_max.setIcon(ico_max)
        ico_min = QIcon()
        ico_min.addPixmap(QPixmap('{}\ico\show_min.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_0_min.setIcon(ico_min)
        ico_close = QIcon()
        ico_close.addPixmap(QPixmap('{}\ico\show_close.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_0_close.setIcon(ico_close)

        # 标题图标
        self.label_0_title = QLabel()
        self.label_0_title.setObjectName('label_0_title')
        self.gridLayout.addWidget(self.label_0_title, 0, 0, 1, 1)
        self.label_0_title.setFixedSize(QtCore.QSize(25, 25))
        self.label_0_title.show()
        label_0_titie_img = QPixmap(r'{}\ico\a1.jpg'.format(here_dic)).scaled(self.label_0_title.width(),
                                                                              self.label_0_title.height())
        self.label_0_title.setPixmap(label_0_titie_img)
        self.label_0_title.show()

        # 链接
        self.btn_0_min.clicked.connect(self.showMinimized)
        self.btn_0_max.clicked.connect(self.showMaximized)
        self.btn_0_close.clicked.connect(self.closeEvent)



    def init_tab1(self):
        # tab1 开始
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.listWidget_1_1 = QtWidgets.QListWidget(self.tab_1)

        self.listWidget_1_1.setObjectName("listWidget_1_1")
        # self.listWidget_1_1.addItem('''  输入想说的话，快来和我快乐滴玩耍呀, \n【警告】请不要直接搞事，先做做其他的，否则可能带来严重后果\n  >>>2019-06-01  -- Bingbing<<<''')
        self.gridLayout_1.addWidget(self.listWidget_1_1, 0, 0, 1, 5)
        self.ckBox_1_voice = QtWidgets.QCheckBox(self.tab_1)
        self.ckBox_1_voice.setToolTip('勾选开启对话语音')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ckBox_1_voice.sizePolicy().hasHeightForWidth())
        self.ckBox_1_voice.setSizePolicy(sizePolicy)
        self.ckBox_1_voice.setMinimumSize(QtCore.QSize(15, 15))
        self.ckBox_1_voice.setMaximumSize(QtCore.QSize(15, 15))
        self.ckBox_1_voice.setSizeIncrement(QtCore.QSize(51, 15))
        self.ckBox_1_voice.setBaseSize(QtCore.QSize(15, 15))
        self.ckBox_1_voice.setFixedSize(QtCore.QSize(15, 15))
        self.ckBox_1_voice.setText("")
        self.ckBox_1_voice.setObjectName("ckBox_1_voice")
        self.gridLayout_1.addWidget(self.ckBox_1_voice, 1, 0, 1, 1)
        self.lnedit_1_input = QtWidgets.QLineEdit(self.tab_1)
        self.lnedit_1_input.setMinimumSize(QtCore.QSize(25, 25))
        self.lnedit_1_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lnedit_1_input.setSizeIncrement(QtCore.QSize(25, 25))
        self.lnedit_1_input.setBaseSize(QtCore.QSize(25, 25))
        self.lnedit_1_input.setObjectName("lnedit_1_input")
        # self.lnedit_1_input.textChanged.connect(self.check_input)
        self.lnedit_1_input.returnPressed.connect(self.input_send_1_clicked)

        self.gridLayout_1.addWidget(self.lnedit_1_input, 1, 3, 1, 1)
        self.btn_1_input_send = QtWidgets.QPushButton(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1_input_send.sizePolicy().hasHeightForWidth())
        self.btn_1_input_send.setSizePolicy(sizePolicy)
        self.btn_1_input_send.setMinimumSize(QtCore.QSize(60, 25))
        self.btn_1_input_send.setMaximumSize(QtCore.QSize(60, 25))
        self.btn_1_input_send.setSizeIncrement(QtCore.QSize(60, 25))
        self.btn_1_input_send.setBaseSize(QtCore.QSize(60, 25))
        self.btn_1_input_send.setObjectName("btn_1_input_send")
        # input_send1
        self.btn_1_input_send.clicked.connect(self.input_send_1_clicked)
        self.gridLayout_1.addWidget(self.btn_1_input_send, 1, 4, 1, 1)

        self.cmBox_1_per = QtWidgets.QComboBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmBox_1_per.sizePolicy().hasHeightForWidth())
        # combox_per
        self.cmBox_1_per.setSizePolicy(sizePolicy)
        self.cmBox_1_per.setFixedSize(QtCore.QSize(60, 25))
        self.cmBox_1_per.setObjectName("cmBox_1_per")
        per = ['小优', '小酷'] #, '小云', '小辰'
        self.cmBox_1_per.addItems(per)
        self.gridLayout_1.addWidget(self.cmBox_1_per, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_1, "唠嗑")


    def init_tab2(self):
        """
        音乐播放器
        :return:
        """
        # tab2 开始 》》》》》》》》
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # tab2 播放器
        self.player_2_media = QMediaPlayer(self.tab_2)
        self.player_2_list = QMediaPlaylist(self.tab_2)
        self.player_2_media.setPlaylist(self.player_2_list)
        self.player_2_media.setVolume(30)
        self.slider_2_vol = QSlider(self)
        self.slider_2_vol.setRange(0, 100)
        self.slider_2_vol.setValue(30)
        self.slider_2_vol.setOrientation(QtCore.Qt.Horizontal)
        self.slider_2_vol.setFixedHeight(10)

        self.slider_2_vol.valueChanged.connect(self.slider_2_vol_valueChanged)

        self.slider_2_progress = QSlider(self)
        self.slider_2_progress.setObjectName('slider_2_progress')
        self.slider_2_progress.setOrientation(QtCore.Qt.Horizontal)
        self.slider_2_progress.setEnabled(False)
        self.slider_2_progress.setFixedHeight(10)
        self.btn_2_vol = QtWidgets.QPushButton()
        self.btn_2_vol.setObjectName('btn_2_vol')
        self.btn_2_vol.setFixedSize(QtCore.QSize(25, 25))
        self.btn_2_vol.clicked.connect(self.btn_2_vol_clicked)
        ico_vol = QtGui.QIcon()
        ico_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_on.png".format(here_dic)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_2_vol.setIcon(ico_vol)
        self.label_2_time = QLabel()
        self.label_2_time.setObjectName('label_2_time')
        self.label_2_time.setText('   --/--')
        self.label_2_time.setEnabled(False)
        self.label_2_time.setFixedSize(QtCore.QSize(80, 25))
        # self.label_2_time.setAutoFillBackground(True)
        self.btn_2_listmode = QtWidgets.QToolButton()
        self.btn_2_listmode.setObjectName('btn_2_listmode')
        self.btn_2_listmode.setFixedSize(QtCore.QSize(25, 25))
        self.gridLayout_2.addWidget(self.btn_2_listmode, 2, 7, 1, 1)
        ico_2_mode = QtGui.QIcon()
        ico_2_mode.addPixmap(QPixmap('{}\ico\item_loop.png'.format(here_dic)))
        self.btn_2_listmode.setIcon(ico_2_mode)

        self.gridLayout_2.addWidget(self.label_2_time, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.btn_2_vol, 2, 6, 1, 1)
        self.gridLayout_2.addWidget(self.slider_2_progress, 2, 0, 1, 3)
        self.gridLayout_2.addWidget(self.slider_2_vol, 2, 4, 1, 2)
        self.player_2_media.positionChanged.connect(self.player_2_positionChanged)
        self.slider_2_progress.sliderMoved.connect(self.slider_2_progress_moved)
        self.player_2_media.durationChanged.connect(self.player_2_media_durationChanged)
        self.player_2_media.stateChanged.connect(self.player_2_media_stateChanged)
        self.player_2_list.currentIndexChanged.connect(self.listwidget_2_update)
        self.btn_2_listmode.clicked.connect(self.player_2_list_setPlaybackMode)

        self.tlBtn_2_play = QtWidgets.QToolButton(self.tab_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("{}/ico/play.ico".format(here_dic)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tlBtn_2_play.setIcon(icon1)
        self.tlBtn_2_play.setIconSize(QtCore.QSize(25, 25))
        self.tlBtn_2_play.setFixedSize(QtCore.QSize(25, 25))
        self.tlBtn_2_play.setObjectName("tlBtn_2_play")
        # self.tlBtn_2_play.setToolTip('停止')
        self.tlBtn_2_play.clicked.connect(self.btn_2_play_clicked)
        self.gridLayout_2.addWidget(self.tlBtn_2_play, 1, 5, 1, 1)
        self.tlBtn_2_next = QtWidgets.QToolButton(self.tab_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("{}/ico/b3.png".format(here_dic)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tlBtn_2_next.setIcon(icon2)
        self.tlBtn_2_next.setIconSize(QtCore.QSize(25, 25))
        self.tlBtn_2_next.setFixedSize(QtCore.QSize(25, 25))
        self.tlBtn_2_next.setObjectName("tlBtn_2_next")
        self.tlBtn_2_next.clicked.connect(self.btn_2_next_clicked)
        # self.tlBtn_2_next.setToolTip('下一曲')
        self.gridLayout_2.addWidget(self.tlBtn_2_next, 1, 6, 1, 1)
        self.tlBtn_2_previous = QtWidgets.QToolButton(self.tab_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("{}/ico/b4.png".format(here_dic)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tlBtn_2_previous.setIcon(icon3)
        self.tlBtn_2_previous.setIconSize(QtCore.QSize(25, 25))
        self.tlBtn_2_previous.setFixedSize(QtCore.QSize(25, 25))
        self.tlBtn_2_previous.setObjectName("tlBtn_2_previous")
        self.tlBtn_2_previous.clicked.connect(self.btn_2_previous_clicked)
        # self.tlBtn_2_previous.setToolTip('上一曲')
        self.gridLayout_2.addWidget(self.tlBtn_2_previous, 1, 4, 1, 1)
        self.cmBox_2_mcsource = QtWidgets.QComboBox(self.tab_2)

        self.cmBox_2_mcsource.setFixedSize(QtCore.QSize(80, 25))
        self.cmBox_2_mcsource.setObjectName("cmBox_2_mcsource")
        # mc_source = ['网易云', 'QQ音乐', '酷狗', '酷我', '百度', '一听', '蜻蜓', '喜马拉雅', '5Sing原创', '5Sing翻唱']
        mc_source = ['网易云', 'QQ音乐', '酷狗', '酷我', '一听', '喜马拉雅', ]  # '蜻蜓' '百度'
        self.cmBox_2_mcsource.addItems(mc_source)
        self.gridLayout_2.addWidget(self.cmBox_2_mcsource, 3, 1, 1, 1)
        self.btn_2_input_send = QtWidgets.QPushButton(self.tab_2)

        self.btn_2_input_send.setMaximumSize(QtCore.QSize(52, 25))
        self.btn_2_input_send.setObjectName("btn_2_input_send")
        # btn_2_input_send

        self.btn_2_input_send.clicked.connect(self.input_send_2_clicked)
        self.gridLayout_2.addWidget(self.btn_2_input_send, 3, 6, 1, 2)
        self.label_2_mc_source = QtWidgets.QLabel(self.tab_2)
        self.label_2_mc_source.setFixedSize(QtCore.QSize(45, 25))
        self.label_2_mc_source.setObjectName("label_2_mc_source")
        # self.label_2_mc_source.setToolTip('音乐来源')

        self.gridLayout_2.addWidget(self.label_2_mc_source, 3, 0, 1, 1)
        self.lnedit_2_input = QtWidgets.QLineEdit(self.tab_2)

        self.lnedit_2_input.setMinimumSize(QtCore.QSize(25, 25))
        self.lnedit_2_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lnedit_2_input.setSizeIncrement(QtCore.QSize(25, 25))
        self.lnedit_2_input.setObjectName("lnedit_2_input")
        # self.lnedit_2_input.textChanged.connect(self.check_input)
        self.gridLayout_2.addWidget(self.lnedit_2_input, 3, 2, 1, 4)
        self.lnedit_2_input.returnPressed.connect(self.input_send_2_clicked)

        # 下载按钮
        self.tlBtn_2_download = QtWidgets.QToolButton(self.tab_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("{}/ico/b5.png".format(here_dic)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tlBtn_2_download.setIcon(icon4)
        self.tlBtn_2_download.setIconSize(QtCore.QSize(25, 25))
        self.tlBtn_2_download.setFixedSize(QtCore.QSize(25, 25))
        self.tlBtn_2_download.setObjectName("tlBtn_2_download")
        self.tlBtn_2_download.clicked.connect(self.tlBtn_2_download_clicked)
        # self.tlBtn_2_download.setToolTip('先在上方选中歌曲再点击下载，保存在D:\XiaoU\Download')
        self.gridLayout_2.addWidget(self.tlBtn_2_download, 1, 7, 1, 1)
        self.listWidget_2_mc_info = QtWidgets.QListWidget(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.listWidget_2_mc_info.setFont(font)
        self.listWidget_2_mc_info.setObjectName("listWidget_2_mc_info")
        self.gridLayout_2.addWidget(self.listWidget_2_mc_info, 0, 4, 1, 4)
        self.listWidget_2_mc_info.itemDoubleClicked.connect(self.listWidget_2_doubleclicked)

        self.listwidget_2_play_view = QtWidgets.QListWidget(self.tab_2)
        self.listwidget_2_play_view.setObjectName('listwidget_2_play_view')
        self.gridLayout_2.addWidget(self.listwidget_2_play_view, 0, 0, 2, 4)
        font_lrc = QtGui.QFont()
        font_lrc.setFamily("楷体")
        font_lrc.setPointSize(12)

        self.listwidget_2_play_view.setFont(font_lrc)
        # self.listwidget_2_play_view.setEnabled(False)
        # self.listwidget_2_play_view.setAutoFillBackground(True)

        # tab2 label
        self.label_2_image = QLabel(self.tab_1)
        # self.label_2_image.setMinimumSize(QtCore.QSize(300, 200))
        # self.label_2_image.setSizeIncrement(QtCore.QSize(20, 400))
        # self.label_2_image.setBaseSize(QtCore.QSize(758, 404))
        self.label_2_image.setObjectName("label_2_image")
        self.gridLayout_1.addWidget(self.label_2_image, 0, 0, 1, 5)
        # 将tab2加入tabwidgte
        self.tabWidget.addTab(self.tab_2, "听曲")




    def init_tab3(self):
        """
        浏览器
        :return:
        """
        # tab3开始 》》》》》》》》》》》》》》
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.btn_3_ok = QtWidgets.QPushButton(self.tab_3)
        self.btn_3_ok.setObjectName('btn_tool_ok')
        # self.btn_3_ok.setFixedSize(QtCore.QSize(60, 25))
        self.gridLayout_3.addWidget(self.btn_3_ok, 1, 2, 1, 1)

        self.browser_3 = QWebEngineView()
        self.browser_3.setObjectName('browser_3')
        self.browser_3.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.browser_3.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.browser_3.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.gridLayout_3.addWidget(self.browser_3, 3, 0, 1, 5)
        self.cmBox_3_mv_soure = QtWidgets.QComboBox(self.tab_3)
        self.cmBox_3_mv_soure.setObjectName('cmBox_3_mv_soure')
        self.cmBox_3_mv_soure.setFixedSize(QtCore.QSize(85, 25))
        cmBox_3_tool_item = ['视频接口-1', '视频接口-2', '视频接口-3', '视频接口-4', '视频接口-5', '浏览器','本地文件'] #  '表情包', '有趣网址',
        self.cmBox_3_mv_soure.addItems(cmBox_3_tool_item)
        self.gridLayout_3.addWidget(self.cmBox_3_mv_soure, 0, 0, 1, 1)
        self.lnedit_3_Input = QtWidgets.QLineEdit(self.tab_3)
        # self.lnedit_3_Input.setMinimumSize(QtCore.QSize(400,25))
        self.setObjectName('lnedit_3_Input')
        self.gridLayout_3.addWidget(self.lnedit_3_Input, 0, 1, 1, 4)
        self.lnedit_3_Input.setMinimumSize(QtCore.QSize(25, 25))
        self.lnedit_3_Input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lnedit_3_Input.setSizeIncrement(QtCore.QSize(25, 25))
        # self.lnedit_3_Input.setBaseSize(QtCore.QSize(25, 25))
        self.btn_3_mv_clear = QtWidgets.QPushButton(self.tab_3)
        self.btn_3_mv_clear.setObjectName('btn_3_mv_clear')

        self.btn_3_mv_clear.setFixedSize(QtCore.QSize(80, 25))
        self.gridLayout_3.addWidget(self.btn_3_mv_clear, 1, 4, 1, 1)
        self.btn_3_mv_clear.setFixedSize(QtCore.QSize(80, 25))

        self.btn_3_reload = QtWidgets.QPushButton(self.tab_3)
        self.btn_3_reload.setObjectName('btn_5_update')
        self.btn_3_reload.setFixedSize(QtCore.QSize(80, 25))
        self.gridLayout_3.addWidget(self.btn_3_reload, 1, 3, 1, 1)
        self.btn_3_forward = QtWidgets.QPushButton(self.tab_3)
        self.btn_3_forward.setObjectName('btn_5_goto')
        self.btn_3_forward.setFixedSize(QtCore.QSize(80, 25))
        self.gridLayout_3.addWidget(self.btn_3_forward, 1, 1, 1, 1)
        self.btn_3_back = QtWidgets.QPushButton(self.tab_3)
        self.btn_3_back.setObjectName('btn_3_back')
        self.btn_3_back.setFixedSize(QtCore.QSize(80, 25))
        self.gridLayout_3.addWidget(self.btn_3_back, 1, 0, 1, 1)
        self.label_3_space = QLabel()
        self.label_3_space.setObjectName('label_3_space')
        self.gridLayout_3.addWidget(self.label_3_space, 3, 0, 1, 5)

        # tab3 事件

        self.btn_3_mv_clear.clicked.connect(self.brower_3_quit)
        self.lnedit_3_Input.returnPressed.connect(self.btn_3_ok_clicked)
        self.btn_3_back.clicked.connect(self.browser_3.back)
        self.btn_3_forward.clicked.connect(self.browser_3.forward)
        self.btn_3_reload.clicked.connect(self.browser_3.reload)
        self.browser_3.urlChanged.connect(self.browser_3_renew_input)
        self.btn_3_ok.clicked.connect(self.btn_3_ok_clicked)
        self.browser_3.loadStarted.connect(self.label_3_space_close)

        self.tabWidget.addTab(self.tab_3, "搞事")

    def init_tab4(self):
        """
        语音合成、识别
        :return:
        """
        # TAB4
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName('tab_4')
        self.tabWidget.addTab(self.tab_4, "语音")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName('gridLayout_4')
        self.txedit_4_input_text = QtWidgets.QTextEdit(self.tab_4)
        self.txedit_4_input_text.setObjectName('listwidget_6_1')
        font_4 = QtGui.QFont()
        font_4.setFamily("楷体")
        font_4.setPointSize(10)
        self.txedit_4_input_text.setFont(font_4)
        # self.txedit_4_input_text.setText('【语音合成】即文字转语音，在上方输入框输入保存文件名(不输入则随机生成），在此处输入需要转换为语音的文字。输出路径：D:\XiaoU\Download\SpeechSynthesis\n【语音识别】即语音转文字，在上方输入框输入音频文件完整路径及文件名，识别结果显示在此处\n【提示】完成需要一定时间，请不要重复提交，输入转换文本前，请先删掉提示内容')
        self.txedit_4_input_file = QtWidgets.QLineEdit(self.tab_4)
        self.txedit_4_input_file.setObjectName('txedit_4_input_file')
        self.txedit_4_input_file.setFixedHeight(25)
        self.txedit_4_input_file.setMouseTracking(True)
        self.gridLayout_4.addWidget(self.txedit_4_input_file, 0, 1, 1, 9)
        self.gridLayout_4.addWidget(self.txedit_4_input_text, 2, 0, 1, 10)
        self.btn_4_clear = QtWidgets.QPushButton()
        self.btn_4_clear.setObjectName('btn_4_clear')
        self.btn_4_clear.setFixedSize(QtCore.QSize(52, 25))
        self.gridLayout_4.addWidget(self.btn_4_clear, 0, 11, 1, 2)
        self.listWidget_4_used_info = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_4_used_info.setObjectName('listWidget_4_used_info')
        self.gridLayout_4.addWidget(self.listWidget_4_used_info, 2, 10, 1, 3)
        self.btn_4_ok = QtWidgets.QPushButton(self.tab_4)
        self.btn_4_ok.setObjectName('btn_4_ok')
        self.btn_4_ok.setFixedSize(QtCore.QSize(52, 25))
        self.gridLayout_4.addWidget(self.btn_4_ok, 0, 10, 1, 1)


        self.cmbox_4_tool = QtWidgets.QComboBox(self.tab_4)
        self.cmbox_4_tool.setObjectName('cmbox_4_tool')
        self.cmbox_4_tool.setFixedSize(QtCore.QSize(85, 25))
        #self.cmbox_4_tool.setMinimumSize(QtCore.QSize(60, 25))
        self.gridLayout_4.addWidget(self.cmbox_4_tool, 0, 0, 1, 2)
        tool = ['语音合成', '语音识别']
        self.cmbox_4_tool.addItems(tool)

        # 语音合成参数
        # 发音人
        cm_6_per = ['普通女声', '普通男生', '成熟女性', '成熟男声', '度逍遥', '度丫丫']
        self.cmbox_4_per = QtWidgets.QComboBox(self.tab_4)
        self.cmbox_4_per.setObjectName('cmbox_4_per')
        self.cmbox_4_per.setFixedSize(QtCore.QSize(85, 25))
        #self.cmbox_4_per.setMinimumSize(QtCore.QSize(60, 25))
        self.cmbox_4_per.addItems(cm_6_per)
        self.gridLayout_4.addWidget(self.cmbox_4_per, 1, 0, 1, 1)
        # 格式
        self.cmbox_4_aue = QtWidgets.QComboBox(self.tab_4)
        self.cmbox_4_aue.setObjectName('cmbox_4_aue')
        self.cmbox_4_aue.setMaximumSize(QtCore.QSize(70, 25))
        self.cmbox_4_aue.setMinimumSize(QtCore.QSize(45, 25))
        cm_6_aue = ["wav", "mp3", "pcm-16k"] #  "pcm-8k",
        # 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
        self.cmbox_4_aue.addItems(cm_6_aue)
        self.gridLayout_4.addWidget(self.cmbox_4_aue, 1, 8, 1, 1)
        # label

        self.label_4_spd = QLabel()
        self.label_4_spd.setObjectName('label_4_spd')
        self.label_4_spd.setMaximumSize(QtCore.QSize(45, 25))
        self.label_4_spd.setMinimumSize(QtCore.QSize(1, 1))
        self.gridLayout_4.addWidget(self.label_4_spd, 1, 1, 1, 1)
        self.label_4_pit = QLabel()
        self.label_4_pit.setObjectName('label_4_pit')
        self.label_4_pit.setMaximumSize(QtCore.QSize(45, 25))
        self.label_4_pit.setMinimumSize(QtCore.QSize(1, 1))
        self.gridLayout_4.addWidget(self.label_4_pit, 1, 3, 1, 1)
        self.label_4_vol = QLabel()
        self.label_4_vol.setObjectName('label_4_vol')
        self.label_4_vol.setMaximumSize(QtCore.QSize(45, 25))
        self.label_4_vol.setMinimumSize(QtCore.QSize(1, 1))
        self.gridLayout_4.addWidget(self.label_4_vol, 1, 5, 1, 1)
        self.label_4_aue = QLabel()
        self.label_4_aue.setObjectName('label_4_aue')
        self.label_4_aue.setMaximumSize(QtCore.QSize(45, 25))
        self.label_4_aue.setMinimumSize(QtCore.QSize(1, 1))
        self.gridLayout_4.addWidget(self.label_4_aue, 1, 7, 1, 1)
        # 补空
        self.label_4_start = QLabel()
        self.label_4_start.setObjectName('label_4_start')
        self.gridLayout_4.addWidget(self.label_4_start, 1, 9, 1, 1)

        self.slider_4_vol = QSlider()
        self.slider_4_vol.setOrientation(QtCore.Qt.Horizontal)
        self.slider_4_vol.setObjectName('slider_4_vol')
        self.slider_4_vol.setFixedSize(QtCore.QSize(52, 10))
        self.slider_4_vol.setRange(0, 100)
        self.slider_4_vol.setValue(30)
        self.gridLayout_4.addWidget(self.slider_4_vol, 1, 10, 1, 1)
        self.slider_4_vol.valueChanged.connect(self.play_common_vol_control)

        self.btn_4_quit_vol = QtWidgets.QToolButton(self.tab_4)
        self.btn_4_quit_vol.setObjectName('btn_4_quit_vol')
        self.btn_4_quit_vol.setFixedSize(QtCore.QSize(25, 25))
        ico_4_vol_quit = QtGui.QIcon()
        ico_4_vol_quit.addPixmap(QtGui.QPixmap(r'{}\ico\play.ico'.format(here_dic)), QtGui.QIcon.Normal,
                                 QtGui.QIcon.Off)
        self.btn_4_quit_vol.setIcon(ico_4_vol_quit)
        self.btn_4_quit_vol.setIconSize(QtCore.QSize(25, 25))
        self.gridLayout_4.addWidget(self.btn_4_quit_vol, 1, 11, 1, 1)
        self.btn_4_quit_vol.clicked.connect(self.play_common_stop)
        self.btn_4_folder = QtWidgets.QToolButton(self.tab_4)
        self.btn_4_folder.setObjectName('btn_4_folder')
        self.btn_4_folder.setFixedSize(QtCore.QSize(25, 25))
        self.btn_4_folder.setIconSize(QtCore.QSize(15, 15))
        ico_4_folder = QtGui.QIcon()
        ico_4_folder.addPixmap(QtGui.QPixmap(r"{}/ico/show.png".format(here_dic)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_4_folder.setIcon(ico_4_folder)
        self.gridLayout_4.addWidget(self.btn_4_folder, 1, 12, 1, 1)

        # Qspinbox
        # 语速
        self.spb_4_spd = QSpinBox(self.tab_4)
        self.spb_4_spd.setObjectName('spb_4_spd')
        self.spb_4_spd.setMaximumSize(QtCore.QSize(60, 25))
        self.spb_4_spd.setMinimumSize(QtCore.QSize(45, 25))
        self.gridLayout_4.addWidget(self.spb_4_spd, 1, 2, 1, 1)
        self.spb_4_spd.setMinimum(0)
        self.spb_4_spd.setValue(5)
        self.spb_4_spd.setMaximum(15)
        # 音调
        self.spb_4_pit = QSpinBox(self.tab_4)
        self.spb_4_pit.setObjectName('spb_4_pit')
        self.spb_4_pit.setMaximumSize(QtCore.QSize(60, 25))
        self.spb_4_pit.setMinimumSize(QtCore.QSize(45, 25))
        self.gridLayout_4.addWidget(self.spb_4_pit, 1, 4, 1, 1)
        self.spb_4_pit.setMinimum(0)
        self.spb_4_pit.setValue(5)
        self.spb_4_pit.setMaximum(15)
        # 音量
        self.spb_4_vol = QSpinBox(self.tab_4)
        self.spb_4_vol.setObjectName('spb_4_vol')
        self.spb_4_vol.setMaximumSize(QtCore.QSize(60, 25))
        self.spb_4_vol.setMinimumSize(QtCore.QSize(45, 25))
        self.gridLayout_4.addWidget(self.spb_4_vol, 1, 6, 1, 1)
        self.spb_4_vol.setMinimum(0)
        self.spb_4_vol.setValue(5)
        self.spb_4_vol.setMaximum(9)

        # tab4 事件
        self.btn_4_ok.clicked.connect(self.btn_4_ok_clicked)
        self.btn_4_clear.clicked.connect(self.btn_4_clear_clicked)
        self.btn_4_clear.clicked.connect(self.play_common_stop)
        self.listWidget_4_used_info.clicked.connect(self.listWidget_4_used_info_clicked)
        self.listWidget_4_used_info.doubleClicked.connect(self.listWidget_4_used_info_doubleclicked)
        self.cmbox_4_tool.currentTextChanged.connect(self.cmbox_4_tool_currentTextChanged)
        self.btn_4_folder.clicked.connect(self.open_folder)

        # tab4 结束》》》》》》》》》》》》》》
    def init_tab5(self):
        # 视频播放器
        # tabvideo

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName('tab_5')
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_5.setSpacing(5)
        self.player_5_video = QMediaPlayer(self)
        self.player_5_list = QMediaPlaylist(self)
        self.player_5_video.setPlaylist(self.player_5_list)
        self.player_5_list.setPlaybackMode(QMediaPlaylist.Sequential)
        self.videowidget_5_video = QVideoWidget(self.tab_5)
        self.videowidget_5_video.setObjectName('videowidget_5_video')
        self.player_5_video.setVolume(30)
        self.gridLayout_5.addWidget(self.videowidget_5_video, 1, 1, 1, 9)
        # self.gridLayout.addWidget(self.videowidget_5_video, 1, 0, 10, 20)
        self.player_5_video.setVideoOutput(self.videowidget_5_video)

        self.label_5_space = QLabel()
        self.label_5_space.setObjectName('label_5_space')
        self.gridLayout_5.addWidget(self.label_5_space, 1, 1, 1, 9)

        self.btn_5_ok = QtWidgets.QPushButton()
        self.btn_5_ok.setObjectName('btn_5_ok')
        self.btn_5_ok.setFixedSize(QtCore.QSize(50, 25))
        self.btn_5_ok.setText('确定')
        self.gridLayout_5.addWidget(self.btn_5_ok, 0, 10, 1, 1)
        self.btn_5_ok.setFixedHeight(25)
        self.lnedit_5_input = QtWidgets.QTextEdit()
        self.lnedit_5_input.setObjectName('lnedit_5_input')
        self.lnedit_5_input.setFixedHeight(25)
        self.gridLayout_5.addWidget(self.lnedit_5_input, 0, 4, 1, 6)
        self.btn_5_stop = QtWidgets.QToolButton()
        self.btn_5_stop.setObjectName('btn_5_stop')
        ico_5_stop = QtGui.QIcon()
        ico_5_stop.addPixmap(QtGui.QPixmap("{}/ico/play.ico".format(here_dic)), QtGui.QIcon.Normal,
                             QtGui.QIcon.Off)
        self.btn_5_stop.setIcon(ico_5_stop)
        self.btn_5_stop.setIconSize(QtCore.QSize(25, 25))
        self.gridLayout_5.addWidget(self.btn_5_stop, 0, 11, 1, 1)

        self.btn_5_listshow = QtWidgets.QToolButton()
        self.setObjectName('btn_5_listshow')
        ico_5_folder = QtGui.QIcon()
        ico_5_folder.addPixmap(QtGui.QPixmap("{}/ico/show.png".format(here_dic)), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
        self.btn_5_listshow.setIcon(ico_5_folder)
        self.gridLayout_5.addWidget(self.btn_5_listshow, 0, 13, 1, 1)
        self.slider_5_vol = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_5_vol.setObjectName('slider_5_vol')
        self.slider_5_vol.setFixedSize(QtCore.QSize(60, 10))
        self.slider_5_vol.setRange(0, 100)
        self.slider_5_vol.setValue(30)
        self.gridLayout_5.addWidget(self.slider_5_vol, 0, 2, 1, 1)
        self.slider_5_progress = QSlider(QtCore.Qt.Vertical)
        self.slider_5_progress.setObjectName('slider_5_progress')
        self.gridLayout_5.addWidget(self.slider_5_progress, 1, 0, 1, 1)
        self.slider_5_progress.setFixedWidth(10)

        self.btn_5_vol = QtWidgets.QToolButton()
        self.btn_5_vol.setObjectName('btn_5_vol')
        ico_5_vol = QtGui.QIcon()
        ico_5_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_on.png".format(here_dic)), QtGui.QIcon.Normal,
                            QtGui.QIcon.Off)
        self.btn_5_vol.setIcon(ico_5_vol)
        self.gridLayout_5.addWidget(self.btn_5_vol, 0, 3, 1, 1)
        self.label_5_start = QLabel()
        self.label_5_start.setObjectName('label_5_start')
        self.gridLayout_5.addWidget(self.label_5_start, 0, 0, 1, 1)
        self.label_5_start.setFixedSize(QtCore.QSize(10, 25))
        self.label_5_start.setEnabled(False)
        self.label_5_time = QLabel()
        self.label_5_time.setObjectName('label_5_time')
        self.label_5_time.setText('  --/--')
        # self.label_5_time.setEnabled(False)
        self.label_5_time.setFixedSize(QtCore.QSize(70, 25))
        self.label_5_time.setAutoFillBackground(True)
        self.gridLayout_5.addWidget(self.label_5_time, 0, 1, 1, 1)
        self.btn_5_listshow.setFixedSize(QtCore.QSize(25, 25))
        self.btn_5_vol.setFixedSize(QtCore.QSize(25, 25))
        self.btn_5_stop.setFixedSize(QtCore.QSize(25, 25))
        self.btn_5_listclear = QtWidgets.QToolButton()
        self.btn_5_listclear.setObjectName('btn_5_listclear')
        self.gridLayout_5.addWidget(self.btn_5_listclear, 0, 12, 1, 1)
        ico_5_listclear = QtGui.QIcon()
        ico_5_listclear.addPixmap(QtGui.QPixmap("{}/ico/clear.png".format(here_dic)), QtGui.QIcon.Normal,
                                  QtGui.QIcon.Off)
        self.btn_5_listclear.setIcon(ico_5_listclear)
        # 播放列表
        self.listWidget_5_playlist = QtWidgets.QListWidget()
        self.listWidget_5_playlist.setObjectName('listwidget_5_playlist')
        self.gridLayout_5.addWidget(self.listWidget_5_playlist, 1, 10, 1, 4)
        self.listWidget_5_playlist.doubleClicked.connect(self.listWidget_5_playlist_doubleClicked)
        self.player_5_list.currentIndexChanged.connect(self.player_5_list_currentIndexChanged)
        self.player_5_video.stateChanged.connect(self.player_5_video_stateChanged)

        self.btn_5_ok.clicked.connect(self.btn_5_ok_clicked)
        self.btn_5_stop.clicked.connect(self.btn_5_stop_clicked)
        self.btn_5_vol.clicked.connect(self.btn_5_vol_clicked)
        self.slider_5_vol.valueChanged.connect(self.slider_5_vol_valueChanged)
        self.slider_5_progress.sliderMoved.connect(self.slider_5_progress_moved)
        self.btn_5_listshow.clicked.connect(self.listwidget_5_list_show)
        self.player_5_video.positionChanged.connect(self.player_5_positionChanged)
        self.player_5_video.durationChanged.connect(self.player_5_video_durationChanged)
        self.btn_5_listclear.clicked.connect(self.btn_5_listclear_clicked)
        self.tabWidget.currentChanged.connect(self.label_5_space_show)

        self.tabWidget.addTab(self.tab_5, '视频')

    def init_public(self):
        # 时间日期显示label   第一行 >>>>>>>
        self.time_show = QtCore.QTimer()
        self.time_show.start(100)
        self.time_show.timeout.connect(self.time_show_out)
        self.label_0_time = QLabel()
        self.setObjectName('label_0_time')
        self.label_0_time.setStyleSheet("QLabel{color: white ; background-color: 1}")
        self.label_0_time.setEnabled(False)
        font_time = QtGui.QFont()
        font_time.setFamily("楷体")
        font_time.setPointSize(10)
        self.label_0_time.setFont(font_time)
        self.label_0_time.setFixedSize(QtCore.QSize(180, 15))
        # self.gridLayout.addWidget(self.label_0_time, 0,2,1,1)
        #self.label_0_time.setEnabled(False)
        self.gridLayout.addWidget(self.label_0_time, 0, 5, 1, 1)

        # 公共音频接口
        self.play_common_list = QMediaPlaylist()
        self.play_common_player = QMediaPlayer()
        self.play_common_player.setPlaylist(self.play_common_list)
        self.play_common_player.stateChanged.connect(self.play_common_player_stateChanged)

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 线程管理
        self._down_song = Download_Song(self)
        self.speech_syn = Speech_synthesis(self)
        self.voice_ars = Voice_recognition(self)
        self.listwidget_2_additems_lrc_thread = listwidget_2_additems_lrc()

        # 信号处理
        self._down_song.down_song_log.connect(self.msg)
        self.speech_syn.speech_synthesis_log.connect(self.speech_syn_log_deal)
        self.voice_ars.asr_result.connect(self.voice_asr_result_deal)
        # self.listwidget_2_additems_lrc_thread.lrc_view.connect(self.listwidget_2_additems_lrc)


        ## 主布局
        self.retranslateUi()
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 12)
        self.setLayout(self.gridLayout)
        self.tabWidget.setCurrentIndex(0)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.btn_1_input_send.setText(_translate("Form", "发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Form", "唠嗑"))
        self.tlBtn_2_play.setText(_translate("Form", "..."))
        self.tlBtn_2_next.setText(_translate("Form", "..."))
        self.tlBtn_2_previous.setText(_translate("Form", "..."))
        self.btn_2_input_send.setText(_translate("Form", "发送"))
        self.label_2_mc_source.setText(_translate("Form", " 音乐源"))
        self.tlBtn_2_download.setText(_translate("Form", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "听曲"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "浏览器"))
        # # TAB3
        # self.btn_3_ok.setText(_translate('From', '确定'))
        # self.btn_3_mv_clear.setText(_translate('Form', '清除'))
        # self.btn_3_forward.setText(_translate('Form', '前进'))
        # self.btn_3_reload.setText(_translate('Form', '刷新'))
        # self.btn_3_back.setText(_translate('From', '后退'))
        # tab4
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("From", "语音"))
        self.btn_4_clear.setText(_translate('From', "清除"))
        self.btn_4_ok.setText(_translate('From', "确定"))
        self.label_4_spd.setText(_translate('Form', ' 语速'))
        self.label_4_pit.setText(_translate('Form', ' 音调'))
        self.label_4_vol.setText(_translate('Form', ' 音量'))
        self.label_4_aue.setText(_translate('Form', ' 格式'))




    def label_5_space_show(self):
        if self.tabWidget.currentWidget().objectName() == 'tab_5':
            if self.player_5_video.state() != 1:
                self.label_5_space.show()

    def listwidget_5_list_show(self):
        if self.listwidget_5_list_state == 1:
            self.listWidget_5_playlist.setVisible(False)
            self.gridLayout_5.addWidget(self.videowidget_5_video, 1, 1, 1, 13)
            self.gridLayout_5.addWidget(self.label_5_space, 1, 1, 1, 13)
            ico_listshow = QIcon()
            ico_listshow.addPixmap(QPixmap('{}\ico\hide.png'.format(here_dic)))
            self.btn_5_listshow.setIcon(ico_listshow)
            self.listwidget_5_list_state = 2
        else:
            self.gridLayout_5.addWidget(self.videowidget_5_video, 1, 1, 1, 9)
            self.gridLayout_5.addWidget(self.label_5_space, 1, 1, 1, 9)
            self.listWidget_5_playlist.setVisible(True)
            ico_listshow = QIcon()
            ico_listshow.addPixmap(QPixmap('{}\ico\show.png'.format(here_dic)))
            self.btn_5_listshow.setIcon(ico_listshow)
            self.listwidget_5_list_state = 1

    def listwidget_5_additem(self, text):
        self.listWidget_5_playlist.addItem(text)

    def listWidget_5_playlist_doubleClicked(self):
        self.player_5_list.setCurrentIndex(self.listWidget_5_playlist.currentRow())
        self.player_5_video.play()

    def player_5_list_currentIndexChanged(self):
        self.listWidget_5_playlist.setCurrentRow(self.player_5_list.currentIndex())

    def btn_5_listclear_clicked(self):
        warn_clear = QMessageBox.warning(self, '警告', '继续操作将会清空播放列表，是否确认继续？', QMessageBox.Yes | QMessageBox.Cancel,
                                         QMessageBox.Cancel)
        if warn_clear == 16384:  # cancel = 4194304
            self.player_5_video.stop()
            self.player_5_list.clear()
            self.label_5_space.show()
            self.lnedit_5_input.clear()
            self.listWidget_5_playlist.clear()
            self.label_5_time.setText('  --/--')

    def slider_5_vol_valueChanged(self):
        self.player_5_video.setVolume(self.slider_5_vol.value())
        if self.slider_5_vol.value() == 0:
            ico_vol = QtGui.QIcon()
            ico_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_off.png".format(here_dic)), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
            self.btn_5_vol.setIcon(ico_vol)
        else:
            ico_vol = QtGui.QIcon()
            ico_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_on.png".format(here_dic)), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
            self.btn_5_vol.setIcon(ico_vol)

    def btn_5_vol_clicked(self):
        if self.player_5_video.volume() != 0:
            self.player_5_video.setVolume(0)
            self.slider_5_vol.setEnabled(False)
            ico_5_vol = QtGui.QIcon()
            ico_5_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_off.png".format(here_dic)))
            self.btn_5_vol.setIcon(ico_5_vol)
        else:
            self.slider_5_vol.setEnabled(True)
            self.player_5_video.setVolume(self.slider_5_vol.value())
            ico_5_vol = QtGui.QIcon()
            ico_5_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_on.png".format(here_dic)))
            self.btn_5_vol.setIcon(ico_5_vol)

    def player_5_positionChanged(self, curr_time):
        self.slider_5_progress.setValue(curr_time)
        self.video_curtime_get(curr_time)

    def video_curtime_get(self, curr_time):
        maxtime = self.slider_5_progress.maximum()
        secm = maxtime // 1000
        minm = secm // 60
        secm -= minm * 60
        if minm == 0 and secm == 0:
            self.label_5_time.setText('  --/--')
        else:
            sec = curr_time // 1000
            min_ = sec // 60
            sec -= min_ * 60
            if min == 0 and sec == 0:
                self.label_5_time.setText('  --/{}:{}'.format(minm, secm))
            else:
                self.label_5_time.setText('{}:{}/{}:{}'.format(min_, sec, minm, secm))
                self.videowidget_5_video.show()

    def slider_5_progress_moved(self):
        self.player_5_video.setPosition(self.slider_5_progress.value())

    # 时长改变
    def player_5_video_durationChanged(self):

        video_time_long = self.player_5_video.duration()
        self.slider_5_progress.setRange(0, video_time_long)
        self.slider_5_progress.setEnabled(True)

    def btn_5_ok_clicked(self):
        text = self.lnedit_5_input.toPlainText()
        if not text == '':
            try:
                if 'file:///' in text:
                    text = text.replace('file:///', '')

                re_url = re.compile('^http|www1.|.h1tm')
                text_url = re.findall(re_url, text)
                if text_url:
                    self.player_5_list.addMedia(QMediaContent(QUrl(text)))

                else:
                    self.player_5_list.addMedia(QMediaContent(QUrl.fromLocalFile(text)))

                self.listwidget_5_additem(text)
                self.lnedit_5_input.clear()
                if self.player_5_video.state() != 1:
                    self.player_5_video.play()
                self.label_5_space.close()
                self.videowidget_5_video.show()

            except:
                pass

        else:
            self.msg('请先选择你要播放的文件')

    def player_5_video_stateChanged(self):
        if self.player_5_video.state() == 1:
            self.videowidget_5_video.show()
            ico_5_quit = QIcon()
            ico_5_quit.addPixmap(QtGui.QPixmap('{}\ico\pause.ico'.format(here_dic)), QtGui.QIcon.Normal,
                                 QtGui.QIcon.Off)
            self.btn_5_stop.setIcon(ico_5_quit)
            self.label_5_space.close()
            self.videowidget_5_video.show()
        else:
            self.label_5_space.close()
            ico_5_quit = QIcon()
            ico_5_quit.addPixmap(QtGui.QPixmap('{}\ico\play.ico'.format(here_dic)), QtGui.QIcon.Normal,
                                 QtGui.QIcon.Off)
            self.btn_5_stop.setIcon(ico_5_quit)
            self.videowidget_5_video.close()
            self.label_5_space.show()

    def btn_5_stop_clicked(self):
        if self.player_5_video.state() != 1 and not self.player_5_list.isEmpty():
            if self.listWidget_5_playlist.currentItem():
                self.player_5_list.setCurrentIndex(self.listWidget_5_playlist.currentRow())
            self.player_5_video.play()

        else:
            self.player_5_video.stop()
            self.label_5_time.setText('  --/--')
            self.label_5_space.show()

    def player_5_list_setPlaybackMode(self):
        if self.player_5_list_Mode == 1:
            self.player_5_list.setPlaybackMode(QMediaPlaylist.Sequential)  # 顺序播放
            ico_5 = QtGui.QIcon()
            ico_5.addPixmap(QPixmap('{}\ico\itm_loop.png'.format(here_dic)))

        elif self.player_5_list_Mode == 2:
            self.player_5_list.setPlaybackMode(QMediaPlaylist.Random)  # 随机播放
        elif self.player_5_list_Mode == 3:
            self.player_5_list.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)  # 单曲循环
        elif self.player_5_list_Mode == 4:
            self.player_5_list.setPlaybackMode(QMediaPlaylist.Loop)  # 列表循环
        elif self.player_5_list_Mode == 5:
            self.player_5_list.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)  # 当前内容播放一次


    def closeEvent(self, QCloseEvent):
        warn_close = QMessageBox.warning(self, '退出提示', '您确定要退出吗？', QMessageBox.Yes | QMessageBox.Cancel,QMessageBox.Cancel)
        if warn_close == 4194304:  # yes = 16384
            pass
        else:
            sys.exit()



    def showMaximized(self):
        if self.isFullScreen():
            self.setGeometry((screen_width-app_width) / 2, (screen_height- app_height) / 2 , app_width, app_height)
            ico_max = QIcon()
            ico_max.addPixmap(QPixmap('{}\ico\show_max1.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_0_max.setIcon(ico_max)
            self.tabWidget.setVisible(True)
            self.gridLayout_5.addWidget(self.videowidget_5_video, 1, 1, 1, 13)

        else:
            self.showFullScreen()
            self.setGeometry(0, 0, 1920, 1080)
            ico_max = QIcon()
            ico_max.addPixmap(QPixmap('{}\ico\show_max2.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_0_max.setIcon(ico_max)
            if self.player_5_video.state() == 1:
                self.gridLayout.addWidget(self.videowidget_5_video, 1, 0, 10, 12)
                self.tabWidget.setVisible(False)
                self.videowidget_5_video.show()

    def showMaximized2(self):
        if self.isFullScreen():
            self.resize(800, 543)
            self.move(560, 270)
            ico_max = QIcon()
            ico_max.addPixmap(QPixmap('{}\ico\show_max1.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_0_max.setIcon(ico_max)
            self.tabWidget.setVisible(True)
            self.gridLayout_5.addWidget(self.videowidget_5_video, 1, 1, 1, 13)

        else:
            self.showFullScreen()
            self.setGeometry(0, 0, 1920, 1080)
            ico_max = QIcon()
            ico_max.addPixmap(QPixmap('{}\ico\show_max2.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_0_max.setIcon(ico_max)
            if self.player_5_video.state() == 1:
                self.gridLayout.addWidget(self.videowidget_5_video, 1, 0, 10, 12)
                self.tabWidget.setVisible(False)




    def initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self.m_flag = False
        self._padding = 5
        self._top_drag = False
        self._left_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        self._leftcorner_drag = False

    def resizeEvent_base(self, QResizeEvent):
        if not self.isFullScreen():
            ico_max = QIcon()
            ico_max.addPixmap(QPixmap('{}\ico\show_max1.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_0_max.setIcon(ico_max)
            self.tabWidget.setVisible(True)
            self.gridLayout_5.addWidget(self.videowidget_5_video, 1, 1, 1, 13)
        self.right_rect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 2)
                           for y in range(10, self.height() - self._padding -5)]
        self.bottom_rect = [QPoint(x, y) for x in range(10, self.width() - self._padding - 5)
                            for y in range(self.height() - self._padding, self.height() + 2)]
        self.left_rect = [QPoint(x, y) for x in range(-2, self._padding)
                          for y in range(10, self.height() - self._padding -5)]
        self.top_rect = [QPoint(x, y) for x in range(10, self.width() - self._padding -5)
                         for y in range(-2, self._padding)]
        self.corner_rect = [QPoint(x, y) for x in range(self.width() - self._padding -5, self.width() + 2)
                            for y in range(self.height() - self._padding -5, self.height() + 2)]
        self.leftcprner_rect = [QPoint(x, y) for x in range(-2, self._padding +5)
                                for y in range(-2, self._padding +5)]
        self.move_rect = [QPoint(x,y) for x in range(0,self.width()) for y in range(0, 60)]

        # self.drawing_rect = [QPoint(x,y) for x in range(20, 20 + self.label_6_drawing.width())
        #                       for y in range(105, self.height())]
        # self.drawing_rect = [QPoint(x, y) for x in range(25, self.width())
        #                      for y in range(105, self.height())]


        if self.listwidget_2_additems_lrc_thread.isRunning():
            self.lrc_2_view()

    def mousePressEvent_base(self, event):
        if (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self.corner_rect):
            # 鼠标左键点击右下角边界区域
            self._corner_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self.right_rect):
            # 鼠标左键点击右侧边界区域
            self._right_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self.bottom_rect):
            # 鼠标左键点击下侧边界区域
            self._bottom_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self.left_rect):
            # 鼠标左键点击右侧边界区域
            self._left_drag = True
            event.accept()

        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self.top_rect):
            # 鼠标左键点击下侧边界区域
            self._top_drag = True
            event.accept()
        elif (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self.leftcprner_rect):
            self._leftcorner_drag = True
            event.accept()

        # 移动
        elif (event.button() == QtCore.Qt.LeftButton or event.button() == QtCore.Qt.MidButton) and (event.pos() in self.move_rect):
            # if  self._top_drag == False and self._left_drag == False and self._corner_drag == False and self._bottom_drag == False and self._right_drag == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标





    def mouseMoveEvent_base(self, QMouseEvent):
        if QMouseEvent.pos() in self.corner_rect:
            self.setCursor(QtCore.Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self.bottom_rect:
            self.setCursor(QtCore.Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self.right_rect:
            self.setCursor(QtCore.Qt.SizeHorCursor)
        elif QMouseEvent.pos() in self.top_rect:
            self.setCursor(QtCore.Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self.left_rect:
            self.setCursor(QtCore.Qt.SizeHorCursor)
        elif QMouseEvent.pos() in self.leftcprner_rect:
            self.setCursor(QtCore.Qt.SizeFDiagCursor)
        elif self.m_flag:
            self.setCursor(QtCore.Qt.OpenHandCursor)


        else:
            self.setCursor(QtCore.Qt.ArrowCursor)

        if QtCore.Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._corner_drag:
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._top_drag:
            # 上侧侧调整窗口高度
            self.setGeometry(self.pos().x(), QMouseEvent.globalPos().y(), self.width(), (self.pos().y() + self.height() - QMouseEvent.globalPos().y()))
            # self.resize(self.width(), self.pos().y() + self.height() - QMouseEvent.globalPos().y())
            # self.move(self.pos().x(), QMouseEvent.globalPos().y())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._left_drag:
            # 左侧同时调整高度和宽度
            self.setGeometry(QMouseEvent.globalPos().x(), self.pos().y(), (self.pos().x() + self.width() - QMouseEvent.globalPos().x()), self.height())
            # self.resize(self.pos().x() + self.width() - QMouseEvent.globalPos().x(), self.height())
            # self.move(QMouseEvent.globalPos().x(), self.pos().y())
            QMouseEvent.accept()
        elif QtCore.Qt.LeftButton and self._leftcorner_drag:
            self.setGeometry(QMouseEvent.globalPos().x(), QMouseEvent.globalPos().y(),
                             (self.width() + self.pos().x() - QMouseEvent.globalPos().x()), (self.height() + self.pos().y() - QMouseEvent.globalPos().y()))
            QMouseEvent.accept()

        elif QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()


    def wheelEvent_base(self, QWheelEvent):
        pass


    def mouseReleaseEvent_base(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        # 鼠标释放后，各扳机复位
        self._top_drag = False
        self._left_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        self._leftcorner_drag = False






    # 公共音频播放接口
    def play_common_play(self, file, f_type_int=1):
        '''
        f_type是文件类型， url = 1   file_audio = 2  file_video = 3
        '''
        self.play_common_player.stop()
        self.play_common_list.clear()
        if f_type_int == 1:
            self.play_common_list.addMedia(QMediaContent(QUrl(file)))
        elif f_type_int == 2:
            self.play_common_list.addMedia(QMediaContent(QUrl.fromLocalFile(file)))
        elif f_type_int == 3:
            self.play_common_list.addMedia(QMediaContent(QUrl.fromLocalFile(file)))
        self.play_common_player.play()

    def play_common_stop(self):
        if self.play_common_player.state() == 1:

            self.play_common_player.stop()
            self.play_common_list.clear()
        else:
            if self.listWidget_4_used_info.currentItem():
                self.listWidget_4_used_info_doubleclicked()

    def play_common_vol_control(self):
        self.play_common_player.setVolume(self.slider_4_vol.value())

    # 播放状态链接图标
    def play_common_player_stateChanged(self):
        if self.play_common_player.state() == 1:
            ico_4_vol_quit = QIcon()
            ico_4_vol_quit.addPixmap(QtGui.QPixmap('{}\ico\pause.ico'.format(here_dic)), QtGui.QIcon.Normal,
                                     QtGui.QIcon.Off)
            self.btn_4_quit_vol.setIcon(ico_4_vol_quit)
        else:
            ico_4_vol_quit = QIcon()
            ico_4_vol_quit.addPixmap(QtGui.QPixmap('{}\ico\play.ico'.format(here_dic)), QtGui.QIcon.Normal,
                                     QtGui.QIcon.Off)
            self.btn_4_quit_vol.setIcon(ico_4_vol_quit)
            self.play_common_player.stop()
            self.play_common_list.clear()

    def open_folder(self):
        os.system('start explorer D:\XiaoU\Download')

    def time_show_out(self):
        self.time_now = time.strftime('%Y-%m-%d %a %H:%M:%S', time.localtime())
        self.label_0_time.setText(self.time_now)
        # self.btn_0_openfolder.setText(self.time_now)

    def cmbox_4_tool_currentTextChanged(self):
        curText = self.cmbox_4_tool.currentText()
        if curText == '语音合成':
            self.spb_4_spd.setEnabled(True)
            self.spb_4_vol.setEnabled(True)
            self.spb_4_pit.setEnabled(True)
            self.label_4_aue.setEnabled(True)
            self.label_4_pit.setEnabled(True)
            self.label_4_spd.setEnabled(True)
            self.label_4_start.setEnabled(True)
            self.label_4_vol.setEnabled(True)
            self.cmbox_4_per.setEnabled(True)
            self.cmbox_4_aue.setEnabled(True)

        elif curText == '语音识别':

            self.spb_4_spd.setEnabled(False)
            self.spb_4_vol.setEnabled(False)
            self.spb_4_pit.setEnabled(False)
            self.label_4_aue.setEnabled(False)
            self.label_4_pit.setEnabled(False)
            self.label_4_spd.setEnabled(False)
            self.label_4_start.setEnabled(False)
            self.label_4_vol.setEnabled(False)
            self.cmbox_4_per.setEnabled(False)
            self.cmbox_4_aue.setEnabled(False)

    def speech_syn_log_deal(self, syn_item):
        if syn_item[0] == '语音合成完成':
            self.listWidget_4_used_info.addItem('【合成】 - {}'.format(syn_item[1]))
        QtWidgets.QMessageBox.about(self, '语音合成提示', '{} - {}'.format(syn_item[0], syn_item[1]))

    def voice_asr_result_deal(self, asr_item):
        if asr_item[0] == '语音识别错误':
            QtWidgets.QMessageBox.about(self, '语音识别提示', '{} - {}'.format(asr_item[0], asr_item[1]))
        else:
            self.listWidget_4_used_info.addItem('【识别】 - {}'.format(asr_item[1]))
            self.listWidget_4_used_info.scrollToBottom()
            self.txedit_4_input_text.setText(asr_item[2])
            QtWidgets.QMessageBox.about(self, '语音识别提示', '{} - {}'.format(asr_item[0], asr_item[1]))

    def listWidget_4_used_info_doubleclicked(self):
        global asr_items, syn_items
        try:
            listwidget_6_1_item = self.listWidget_4_used_info.currentItem().text()

            if '【合成】' in listwidget_6_1_item:
                syn_item = listwidget_6_1_item.replace('【合成】 - ', '')
                self.txedit_4_input_text.setText(
                    '【保存路径】 - {}\n【合成文本】 - {}'.format(syn_items[syn_item][0], syn_items[syn_item][1]))
                self.play_common_play(syn_items[syn_item][0], 2)
                # playsound(syn_items[syn_item][0], False)

            elif '【识别】 -' in listwidget_6_1_item:
                asr_item = listwidget_6_1_item.replace('【识别】 - ', '')
                self.txedit_4_input_text.setText(
                    '【识别文件】 - {}\n【识别结果】 - {}'.format(asr_items[asr_item][0], asr_items[asr_item][1]))
                self.play_common_play(asr_items[asr_item][0], 2)
        except Exception as e:
            self.msg('发生错误 - {}'.format(e))

        self.txedit_4_input_text.show()

    def listWidget_4_used_info_clicked(self):
        global asr_items, syn_items
        listwidget_6_1_item = self.listWidget_4_used_info.currentItem().text()
        if '【合成】 - ' in listwidget_6_1_item:
            syn_item = listwidget_6_1_item.replace('【合成】 - ', '')
            self.txedit_4_input_text.setText(
                '【保存路径】 - {}\n【合成文本】 - {}'.format(syn_items[syn_item][0], syn_items[syn_item][1]))

        elif '【识别】 - ' in listwidget_6_1_item:
            asr_item = listwidget_6_1_item.replace('【识别】 - ', '')
            self.txedit_4_input_text.setText(
                '【识别文件】 - {}\n【识别结果】 - {}'.format(asr_items[asr_item][0], asr_items[asr_item][1]))

        self.txedit_4_input_text.show()

    def btn_4_ok_clicked(self):
        global Queue_speech, Queue_ASR
        text = self.txedit_4_input_file.text()
        if self.cmbox_4_tool.currentText() == '语音合成':
            speech_name = text
            voice_text = self.txedit_4_input_text.toPlainText()
            per = self.cmbox_4_per.currentText()
            spd = self.spb_4_spd.value()
            pit = self.spb_4_pit.value()
            vol = self.spb_4_vol.value()
            aue = self.cmbox_4_aue.currentText()
            item = [speech_name, voice_text, per, spd, pit, vol, aue]
            Queue_speech.put(item)
            if not self.speech_syn.isRunning():
                self.speech_syn.start()

        elif self.cmbox_4_tool.currentText() == '语音识别':
            if not text == '':
                item = []
                # 默认值
                asr_rate = 16000
                # 自定义值
                asr_speech = r'{}'.format(text)
                asr_format = re.findall(r'.*\.(.*)', asr_speech)[0]

                item.append(asr_speech)
                item.append(asr_format)
                item.append(asr_rate)
                Queue_ASR.put(item)
                if not self.voice_ars.isRunning():
                    self.voice_ars.start()
            else:
                self.msg('请正确输入文件路径！')

    def btn_4_clear_clicked(self):
        global asr_items, syn_items
        sure = QtWidgets.QMessageBox.warning(self, '警告', '该操作会清除该模块所有输入内容和之前\n所有操作记录（不会删除保存文件），\n是否确认继续？',
                                             QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if sure == 16384:  # cancal = 4194304

            self.txedit_4_input_file.clear()
            self.txedit_4_input_text.clear()
            self.listWidget_4_used_info.clear()
            asr_items = {}
            syn_items = {}

        # 获取全民解析接口

    def get_port(self, port):
        try:
            start_url = 'http://www.qmaile.com/'
            start_res = requests.get(start_url)
            start_html = etree.HTML(start_res.text)
            start_port = start_html.xpath('//select[@class="form-control input-lg"]//option/@value')
            return start_port[int(port) - 1]
        except Exception as e:
            all_port = ['http://jx.du2.cc/?url=', 'http://jx.drgxj.com/?url=', 'http://jx.618ge.com/?url=',
                        'http://vip.jlsprh.com/?url=', 'http://jx.598110.com/?url=']
            return all_port[int(port) - 1]

    def browser_3_renew_input(self, q):
        self.lnedit_3_Input.setText(q.toString())
        self.lnedit_3_Input.setCursorPosition(0)

    def browser_3_open(self, url):
        self.browser_3.load(QUrl(url))
        self.browser_3.show()

    def brower_3_quit(self):
        self.browser_3.history().clear()
        self.browser_3.setUrl(QUrl('file:///{}/ico/b7.jpg'.format(here_dic.replace('\\', '/'))))
        self.browser_3.show()
        self.lnedit_3_Input.clear()


    def label_3_space_close(self):
        self.label_3_space.close()

    def btn_3_ok_clicked(self):

        input_text = self.lnedit_3_Input.text()
        all_port = ['http://jx.du2.cc/?url=', 'http://jx.drgxj.com/?url=', 'http://jx.618ge.com/?url=',
                    'http://vip.jlsprh.com/?url=', 'http://jx.598110.com/?url=']
        if self.cmBox_3_mv_soure.currentText() == '视频接口-1' and input_text != '':
            if 'http' in input_text or 'htm' in input_text or 'www' in input_text or 'com' in input_text:
                try:
                    need_port = all_port[0]
                    if not need_port in input_text:
                        input_text = need_port + input_text
                    self.browser_3_open(input_text)

                except Exception as port_e:
                    warn = QMessageBox.warning(self, '载入失败', '是否尝试再次载入', QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.Yes)
                    if warn == 16384:
                        need_port = self.get_port(1)
                        if not need_port in input_text:
                            input_text = need_port + input_text
                        self.browser_3_open(input_text)

            else:
                self.msg('请输入视频链接！')

        elif self.cmBox_3_mv_soure.currentText() == '视频接口-2' and input_text != '':
            if 'http' in input_text or 'htm' in input_text or 'www' in input_text or 'com' in input_text:
                try:
                    need_port = all_port[1]
                    if not need_port in input_text:
                        input_text = need_port + input_text
                    self.browser_3_open(input_text)

                except Exception as port_e:
                    warn = QMessageBox.warning(self, '载入失败', '是否尝试再次载入', QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.Yes)
                    if warn == 16384:
                        need_port = self.get_port(2)
                        if not need_port in input_text:
                            input_text = need_port + input_text
                        self.browser_3_open(input_text)

            else:
                self.msg('请输入视频链接！')

        elif self.cmBox_3_mv_soure.currentText() == '视频接口-3' and input_text != '':
            if 'http' in input_text or 'htm' in input_text or 'www' in input_text or 'com' in input_text:
                try:
                    need_port = all_port[2]
                    if not need_port in input_text:
                        input_text = need_port + input_text
                    self.browser_3_open(input_text)

                except Exception as port_e:
                    warn = QMessageBox.warning(self, '载入失败', '是否尝试再次载入', QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.Yes)
                    if warn == 16384:
                        need_port = self.get_port(3)
                        if not need_port in input_text:
                            input_text = need_port + input_text
                        self.browser_3_open(input_text)
            else:
                self.msg('请输入视频链接！')

        elif self.cmBox_3_mv_soure.currentText() == '视频接口-4' and input_text != '':
            if 'http' in input_text or 'htm' in input_text or 'www' in input_text or 'com' in input_text:
                try:
                    need_port = all_port[3]
                    if not need_port in input_text:
                        input_text = need_port + input_text
                    self.browser_3_open(input_text)
                except Exception as port_e:
                    warn = QMessageBox.warning(self, '载入失败', '是否尝试再次载入', QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.Yes)
                    if warn == 16384:
                        need_port = self.get_port(4)
                        if not need_port in input_text:
                            input_text = need_port + input_text
                        self.browser_3_open(input_text)
            else:
                self.msg('请输入视频链接！')

        elif self.cmBox_3_mv_soure.currentText() == '视频接口-5' and input_text != '':
            if 'http' in input_text or 'htm' in input_text or 'www' in input_text or 'com' in input_text:
                try:
                    need_port = all_port[4]
                    if not need_port in input_text:
                        input_text = need_port + input_text
                    self.browser_3_open(input_text)

                except Exception as port_e:
                    warn = QMessageBox.warning(self, '载入失败', '是否尝试再次载入', QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.Yes)
                    if warn == 16384:
                        need_port = self.get_port(5)
                        if not need_port in input_text:
                            input_text = need_port + input_text
                        self.browser_3_open(input_text)
            else:
                self.msg('请输入视频链接！')

        elif self.cmBox_3_mv_soure.currentText() == '浏览器' and input_text != '':
            if not input_text.startswith('http'):
                input_text = 'https://www.baidu.com/s?tn=50000021_hao_pg&ie=utf-8&sc=UWd1pgw-pA7EnHc1FMfqnHRvnj03nWDYnjDznBuW5y99U1Dznzu9m1YkP1b1PHb1n1m4&ssl_sample=normal&srcqid=3187887507166429981&H123Tmp=nunew7&word=' + input_text
            self.browser_3_open(input_text)

        elif self.cmBox_3_mv_soure.currentText() == '本地文件':
            if not 'file:///' in input_text:
                input_text = r'file:///{}'.format(input_text.replace('\\', '/'))
            self.browser_3_open(input_text)

        elif self.cmBox_3_mv_soure.currentText() == '表情包':
            self.browser_3_open('http://www.doutula.com/')

        elif self.cmBox_3_mv_soure.currentText() == '有趣网址':
            self.browser_3_open('https://youquhome.com/?tdsourcetag=s_pctim_aiomsg')

        elif self.cmBox_3_mv_soure.currentText() == 'test':
            self.player_5_list.clear()
            inp = self.lnedit_3_Input.text()
            self.player_5_list.addMedia(QMediaContent(QUrl(inp)))
            # self.player_5_list.addMedia(QMediaContent(QUrl('https://www.iqiyi.com/v_19rsfsh484.html?vfm=m_419_hao1#curid=2296217800_df95384944fe44fd93c91f1266e37da4')))
            # self.player_5_list.addMedia(QMediaContent(QUrl('http://m10.music.126.net/20190604193300/61046138638efc243b5c57fab1a1048d/ymusic/228b/d38e/a5a8/3429bfcceb5026cfd3357b8c63ccab58.mp3')))
            # self.player_5_list.addMedia(QMediaContent(QUrl.fromLocalFile(r'C:\Users\me\全程高能,那些值得回味多次的爆笑名场景{(6,可怜人与万恶之源与麻衣大神.flv')))
            self.player_5_video.play()
            self.videowidget_5_video.show()
            p = self.player_5_video.duration()
            print(p)

    def input_send_2_clicked(self):
        send2 = self.lnedit_2_input.text()
        if not send2 == '':
            for i in range(1, 6):
                self.get_song(send2, i)
            self.lnedit_2_input.clear()
        else:
            self.msg('请输入需要查找的歌曲名')

    def listWidget_1_additem(self, Text1):
        self.label_2_image.close()
        self.listWidget_1_1.show()
        self.listWidget_1_1.addItem(Text1)
        self.listWidget_1_1.scrollToBottom()

    def listWidget_2_additem(self, Text22):
        self.listWidget_2_mc_info.addItem(Text22)
        self.listWidget_2_mc_info.scrollToBottom()

    def listWidget_2_doubleclicked(self):
        self.player_2_media_play()

    def slider_2_vol_valueChanged(self):
        self.player_2_media.setVolume(self.slider_2_vol.value())
        if self.slider_2_vol.value() == 0:
            ico_vol = QtGui.QIcon()
            ico_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_off.png".format(here_dic)), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
            self.btn_2_vol.setIcon(ico_vol)
        else:
            ico_vol = QtGui.QIcon()
            ico_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_on.png".format(here_dic)), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
            self.btn_2_vol.setIcon(ico_vol)

    def btn_2_vol_clicked(self):
        if self.player_2_media.volume() != 0:
            self.player_2_media.setVolume(0)
            self.slider_2_vol.setEnabled(False)
            ico_2_vol = QtGui.QIcon()
            ico_2_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_off.png".format(here_dic)))
            self.btn_2_vol.setIcon(ico_2_vol)
        else:
            self.slider_2_vol.setEnabled(True)
            self.player_2_media.setVolume(self.slider_2_vol.value())
            ico_2_vol = QtGui.QIcon()
            ico_2_vol.addPixmap(QtGui.QPixmap("{}/ico/sound_on.png".format(here_dic)))
            self.btn_2_vol.setIcon(ico_2_vol)

    def player_2_positionChanged(self, curr_time):
        self.slider_2_progress.setValue(curr_time)
        self.song_curtime_get(curr_time)

    def song_curtime_get(self, curr_time):

        maxtime = self.slider_2_progress.maximum()
        secm = maxtime // 1000
        minm = secm // 60
        secm -= minm * 60
        if minm == 0 and secm == 0:
            self.label_2_time.setText('  --/--')
        else:
            sec = curr_time // 1000
            min_ = sec // 60
            sec -= min_ * 60
            if min == 0 and sec == 0:
                self.label_2_time.setText(' --/{}:{}'.format(minm, secm))
            else:
                self.label_2_time.setText('{}:{}/{}:{}'.format(min_, sec, minm, secm))

    def player_2_list_setPlaybackMode(self):
        if self.player_2_list_Mode < 5:
            self.player_2_list_Mode += 1
        else:
            self.player_2_list_Mode = 1
        if self.player_2_list_Mode == 1:
            self.player_2_list.setPlaybackMode(QMediaPlaylist.Sequential)  # 顺序播放
            ico_2_mode = QtGui.QIcon()
            ico_2_mode.addPixmap(QPixmap(r'{}\ico\item_loop.png'.format(here_dic)))
            self.btn_2_listmode.setIcon(ico_2_mode)
        elif self.player_2_list_Mode == 2:
            self.player_2_list.setPlaybackMode(QMediaPlaylist.Random)  # 随机播放
            ico_2_mode = QtGui.QIcon()
            ico_2_mode.addPixmap(QPixmap(r'{}\ico\random.png'.format(here_dic)))
            self.btn_2_listmode.setIcon(ico_2_mode)
        elif self.player_2_list_Mode == 3:
            self.player_2_list.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)  # 单曲循环
            ico_2_mode = QtGui.QIcon()
            ico_2_mode.addPixmap(QPixmap(r'{}\ico\one_loop.png'.format(here_dic)))
            self.btn_2_listmode.setIcon(ico_2_mode)
        elif self.player_2_list_Mode == 4:
            self.player_2_list.setPlaybackMode(QMediaPlaylist.Loop)  # 列表循环
            ico_2_mode = QtGui.QIcon()
            ico_2_mode.addPixmap(QPixmap(r'{}\ico\list_loop.png'.format(here_dic)))
            self.btn_2_listmode.setIcon(ico_2_mode)
        elif self.player_2_list_Mode == 5:
            self.player_2_list.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)  # 当前内容播放一次
            ico_2_mode = QtGui.QIcon()
            ico_2_mode.addPixmap(QPixmap(r'{}\ico\onlyone.png'.format(here_dic)))
            self.btn_2_listmode.setIcon(ico_2_mode)

    def slider_2_progress_moved(self):
        self.player_2_media.setPosition(self.slider_2_progress.value())

    # 时长改变
    def player_2_media_durationChanged(self):
        song_time_long = self.player_2_media.duration()
        self.slider_2_progress.setRange(0, song_time_long)
        self.slider_2_progress.setEnabled(True)

    def listwidget_2_update(self, p):
        if p >= 0:
            self.listWidget_2_mc_info.setCurrentRow(p)
            self.lrc_2_view()
        else:
            self.player_2_media.stop()

    def player_2_media_stateChanged(self, s):
        if s == 1:
            icon_2_play = QtGui.QIcon()
            icon_2_play.addPixmap(QtGui.QPixmap("{}/ico/pause.ico".format(here_dic)), QtGui.QIcon.Normal,QtGui.QIcon.Off)
            self.tlBtn_2_play.setIcon(icon_2_play)
        else:
            icon_2_pause = QtGui.QIcon()
            icon_2_pause.addPixmap(QtGui.QPixmap("{}/ico/play.ico".format(here_dic)), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
            self.tlBtn_2_play.setIcon(icon_2_pause)

            print(s)


    def player_2_media_play(self):

        try:
            if self.player_2_media.state() == 2:
                song_pos = self.player_2_media.position()
                self.player_2_list.setCurrentIndex(self.listWidget_2_mc_info.currentRow())
                self.player_2_media.play()
                self.player_2_media.setPosition(song_pos)
                self.lrc_2_view()
            elif self.listWidget_2_mc_info.currentItem():
                if self.player_2_media.state() != 1:
                    self.player_2_list.setCurrentIndex(self.listWidget_2_mc_info.currentRow())
                    self.player_2_media.play()
                self.player_2_list.setCurrentIndex(self.listWidget_2_mc_info.currentRow())
                self.player_2_media.play()
                self.lrc_2_view()

            elif self.player_2_media.state() == 1:
                self.player_2_list.setCurrentIndex(self.listWidget_2_mc_info.currentRow())
                self.player_2_media.play()
                self.lrc_2_view()


            else:
                self.listwidget_2_additems_lrc_thread.lrc_run = False
                self.msg('请先选择你要播放的歌曲')
        except Exception as e:
            self.msg('播放出错了 {}'.format(e))

    def lrc_2_view(self):
        self.listwidget_2_additems_lrc_thread.lrc_run = False
        self.listwidget_2_play_view.clear()
        self.listwidget_2_additems_lrc_thread = listwidget_2_additems_lrc()
        self.listwidget_2_additems_lrc_thread.lrc_song_name = self.listWidget_2_mc_info.currentItem().text()
        self.listwidget_2_additems_lrc_thread.listview = self.listwidget_2_play_view
        self.listwidget_2_additems_lrc_thread.lrc_media = self.player_2_media
        self.listwidget_2_additems_lrc_thread.lrc_window_width = self.listwidget_2_play_view.width()
        self.listwidget_2_additems_lrc_thread.start()

    def btn_2_play_clicked(self):
        if self.listWidget_2_mc_info.currentItem():
            if self.player_2_media.state() == 1:
                self.player_2_media.pause()
                self.listwidget_2_additems_lrc_thread.lrc_run = False

            else:
                self.player_2_media_play()

        else:
            self.msg('请先选择你要播放的歌曲')

    def btn_2_next_clicked(self):
        if self.listWidget_2_mc_info.currentItem():
            indef = self.listWidget_2_mc_info.currentRow()
            if indef < self.listWidget_2_mc_info.count() - 1:
                self.listWidget_2_mc_info.setCurrentRow(indef + 1)
                self.player_2_media_play()
        elif self.player_2_media.state() == 1:
            indef = self.player_2_list.currentIndex()
            if indef < self.listWidget_2_mc_info.count() - 1:
                self.listWidget_2_mc_info.setCurrentRow(indef + 1)
                self.player_2_media_play()
        else:
            self.msg('请选择要播放的音乐')

    def btn_2_previous_clicked(self):
        if self.listWidget_2_mc_info.currentItem():
            indef = self.listWidget_2_mc_info.currentRow()
            if indef > 0:
                self.listWidget_2_mc_info.setCurrentRow(indef - 1)
                self.player_2_media_play()
        elif self.player_2_media.state() == 1:
            indef = self.player_2_list.currentIndex()
            if indef < self.listWidget_2_mc_info.count() - 1:
                self.listWidget_2_mc_info.setCurrentRow(indef + 1)
                self.player_2_media_play()
        else:
            self.msg('请选择要播放的音乐')

    def tlBtn_2_download_clicked(self):
        global Queue_song
        # 音乐下载
        if self.listWidget_2_mc_info.currentItem():
            if not os.path.exists(r'D:\XiaoU\Download\Audio'):
                os.makedirs(r'D:\XiaoU\Download\Audio')
            item = self.listWidget_2_mc_info.currentItem().text()
            Queue_song.put(item)
            if not self._down_song.isRunning():
                self._down_song.start()

    def msg(self, mymsg):
        QMessageBox.about(self, '提示', mymsg)

    # TAB1 label图片
    def label_1_images_show(self, pg=1):
        self.label_2_image.show()
        fri_image = QtGui.QPixmap(r'{}\ico\a{}.jpg'.format(here_dic, pg)).scaled(self.label_2_image.width(),
                                                                                 self.label_2_image.height())
        self.label_2_image.setPixmap(fri_image)
        self.label_2_image.show()

    # 指定输入完成标识
    def check_input(self):
        input1 = str(self.lnedit_1_input.text())
        input2 = str(self.lnedit_2_input.text())
        if '  ' in input1 or '。' in input1 or '.' in input1 or '?' in input1 or '？' in input1 or '!' in input1 or '！' in input1:
            self.input_send_1_clicked()
        if '  ' in input2 or '。' in input2 or '.' in input2 or '?' in input2 or '？' in input2 or '!' in input2 or '！' in input2:
            self.input_send_2_clicked()

    def input_send_1_clicked(self):
        send1 = self.lnedit_1_input.text()
        if send1 == '朋友' or (self.friend_int != 0 and send1 == '') or send1 == '友情' or send1 == '友谊':
            self.main_voice(send1)
            self.lnedit_1_input.clear()

        else:
            user_tip = '本人啦：\n  ' + send1
            self.listWidget_1_additem(user_tip)
            self.main_voice(send1)
            self.lnedit_1_input.clear()

        # 歌曲获取

    def get_song(self, inputg, page=1):
        try:
            if not os.path.exists(r'D:\XiaoU\Download'):
                os.makedirs(r'D:\XiaoU\Download')
            F_song = open(r'D:\XiaoU\Download\XiaoUsong_info.docx', 'a', encoding='utf-8')
            F_song.write('\n******{}******\n'.format(time.strftime('%Y%m%d %H:%M:%S', time.localtime())))
            mc_source = {
                '网易云': 'netease',
                'QQ音乐': 'qq',
                '酷狗': 'kugou',
                '酷我': 'kuwo',
                '虾米': 'xiami',
                '百度': 'baidu',
                '一听': '1ting',
                '咪咕': 'migu',
                '荔枝': 'lizhi',
                '蜻蜓': 'qingting',
                '喜马拉雅': 'ximalaya',
                '全名K歌': 'kg',
                '5Sing原创': '5singyc',
                '5Sing翻唱': '5singfc'
            }
            url = 'http://hd215.api.yesapi.cn/?s=App.Music.Search' #http://hn216.api.yesapi.cn/  http://hd215.api.yesapi.cn/
            _filter = 'name'
            mc_key = self.cmBox_2_mcsource.currentText()
            _website = mc_source[mc_key]
            # print(_website)

            data = {
                'app_key': '5E8512AAB713A041C41E076C754E3305',# C4486C64E77292F94BC56307B64C92AE  5E8512AAB713A041C41E076C754E3305
                'input': inputg,
                'filter': _filter,
                'website': _website,
                'page': page,
            }

            res = requests.get(url, data)

            req = res.text.encode('utf-8')
            reqq = json.loads(req)
            # print(reqq)

            data = reqq['data']
            musics = data['music']
            for song in musics:
                song_title = song['title']
                song_author = song['author']
                song_id = song['songid']
                song_link = song['link']
                song_url = song['url']
                song_pic = song['pic']
                song_lrc = song['lrc']
                # print(song_type, song_title, song_author, song_id, song_link, song_url, song_pic, song_lrc)
                song_ta = str(song_title) + '-' + str(song_author)
                F_info = '\n》》》 ' + '来源：' + str(mc_key) + '\n' + '歌名：' + str(song_title) + '\n' + '歌手：' + str(
                    song_author) + '\n' + '歌曲ID：' + str(song_id) + '\n' + '歌曲链接：' + str(song_link) + '\n' + '下载链接：' + str(song_url) + '\n' + '封面图片：' + str(song_pic) + '\n'
                if song_ta in sum_songs.keys():
                    continue
                F_song.write(F_info)
                self.sum_songs[song_ta] = [mc_key, song_title, song_author, song_id, song_link, song_url, song_pic,
                                           song_lrc]
                self.listWidget_2_additem(song_ta)
                # 添加歌曲链接到播放链表
                self.player_2_list.addMedia(QMediaContent(QUrl(song_url)))
                # print(mc_key, song_title, song_author, song_id, song_link, song_url, song_pic)
                # print(song_link)
            F_song.flush()
            F_song.close()
            # print(sum_songs)
        except Exception as e:
            self.msg('发生错误 {}'.format(e))

    # 播放语音
    def get_voice(self, voice_text):
        TTS_URL = 'http://tsn.baidu.com/text2audio'
        API_KEY = 'fWF3HKtPBAOejtCtfGqIGwIr'
        SECRET_KEY = 'omiaIm5GGe1rWEO4vQPmCvXeclQmvqc7'

        class DemoError(Exception):
            pass

        TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
        SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选

        def fetch_token():
            try:
                param = {'grant_type': 'client_credentials',
                         'client_id': API_KEY,
                         'client_secret': SECRET_KEY}
                post_data = urlencode(param)
                post_data = post_data.encode('utf-8')
                reqf = Request(TOKEN_URL, post_data)

                ff = urlopen(reqf, timeout=5)
                result_strf = ff.read()
                result_strf = result_strf.decode()
                result = json.loads(result_strf)
                if 'access_token' in result.keys() and 'scope' in result.keys():
                    if not SCOPE in result['scope'].split(' '):
                        raise DemoError('scope is not correct')
                    return result['access_token']
                else:
                    raise DemoError(
                        'MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')
            except Exception as errf:
                self.msg('发生错误 {}'.format(errf))

        # 播放
        try:
            token = fetch_token()
            tex = quote_plus(voice_text)  # 此处TEXT需要两次urlencode
            params = {'tok': token, 'tex': tex, 'per': self.PER, 'spd': '5', 'pit': self.PIT, 'vol': '5', 'aue': '3',
                      'cuid': "123456PYTHON",
                      'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数
            data = urlencode(params)
            req = Request(TTS_URL, data.encode('utf-8'))
            f = urlopen(req)
            if not os.path.exists(r'D:\XiaoU\Deal\Voice'):
                os.makedirs(r'D:\XiaoU\Deal\Voice')
            f2 = open(r'D:\XiaoU\Deal\Voice.mp3', 'wb')
            f2.write(f.read())
            f2.flush()
            f2.close()
            self.play_common_play(r'D:\XiaoU\Deal\Voice.mp3', 2)
        except Exception as err:
            self.msg('发生错误 {}'.format(err))

    # 获取对话应答
    def get_result(self, selfInfo, inputs):
        try:
            if inputs:
                output = ''
                if self.API == 'baidu':
                    data = {
                        "reqType": '0',
                        "perception": {
                            "inputText": {
                                "text": inputs
                            },
                        },
                        "selfInfo": selfInfo,
                        "userInfo": self.info
                    }

                    data = json.dumps(data).encode('utf-8')
                    res = requests.post(url='http://openapi.tuling123.com/openapi/api/v2', data=data, json=None)
                    result = res.json()
                    # 读取应答信息
                    results = result['results']
                    values = results[0]['values']
                    text = values['text']
                    if self.PER == 4:
                        output = '小优：\n  ' + text
                    elif self.PER == 2:
                        output = '小酷：\n  ' + text
                    elif self.PER == 3:
                        output = '小辰：\n  ' + text
                    self.listWidget_1_additem(Text1=output)
                    if self.ckBox_1_voice.isChecked():
                        self.get_voice(text)

                elif self.API == 'qingyun':
                    res = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(inputs))
                    req = res.text
                    rec = re.compile('"content":"(.*)"')
                    req = rec.search(req).group(1)
                    req = req.replace('{br}', '')
                    output = '小酷：\n  ' + req
                    self.listWidget_1_additem(Text1=output)
                    if self.ckBox_1_voice.isChecked():
                        self.get_voice(req)
            else:
                per = self.cmBox_1_per.currentText()
                req = '读心术很厉害，可是我还不会啊！'
                output = '{}：\n  '.format(per) + req
                self.listWidget_1_additem(Text1=output)
                if self.ckBox_1_voice.isChecked():
                    self.get_voice(req)
        except Exception as e:
            self.msg('发生错误 {}'.format(e))

    # 语音API切换
    def user_info(self):
        # baidu self.API
        if self.cmBox_1_per.currentText() == '小优':
            self.API = 'baidu'
            self.info = {
                "apiKey": "2ea5ef3f4c35489c97deebd32df6332f",
                "userId": "14520"
            }

            self.PER = 4
            self.PIT = 6

        elif self.cmBox_1_per.currentText() == '小云':
            self.API = 'baidu'
            self.info = {

                  "apiKey": "9ad4e7ad478b4353a27aad1eab121d79",
                    "userId": "13520"
            }
            self.PER = 5
            self.PIT = 12


        elif self.cmBox_1_per.currentText() == '小辰':
            self.API = 'baidu'
            self.info = {
                "apiKey": "c1cc29c831604b61bfc993110533af0a",
                "userId": "9420"
            }
            self.PER = 3
            self.PIT = 12

        # qingyun self.API
        elif self.cmBox_1_per.currentText() == '小酷':
            self.API = 'qingyun'
            self.PER = 2
            self.PIT = 12

    def main_voice(self, text_Voice):
        self.user_info()
        info = {
            "location": {
                "province": '江苏',
                "city": '南京',
                "street": '盘城街道'
            }
        }
        if text_Voice == '朋友' or (
                self.friend_int >= 1 and text_Voice == '') or text_Voice == '友情' or text_Voice == '友谊':
            self.friend_int += 1
            if self.friend_int >= 11:
                self.friend_int = 1
            self.label_1_images_show(self.friend_int)
        else:
            self.friend_int = 0
            self.get_result(info, text_Voice)




class listwidget_2_additems_lrc(QThread):
    lrc_view = pyqtSignal(object)

    def __init__(self, parent=None):
        super(listwidget_2_additems_lrc, self).__init__(parent)
        self.lrc_run = True
        self.listview = object
        self.lrc_song_name = object
        self.lrc_media = object
        self.lrc_window_width = object


    def run(self):
        lrc_add = 0
        lrc_info = {}
        lrc_pos_last = ''
        lrc_times = []
        while self.lrc_run:
            if lrc_add == 0:
                try:
                    song_lrc = sum_songs[self.lrc_song_name][7]
                    if not song_lrc:
                        break
                    if not os.path.exists(r'D:\XiaoU\Deal'):
                        os.makedirs(r'D:\XiaoU\Deal')
                    with open('D:\XiaoU\Deal\Lrc.txt', 'w', encoding='utf-8') as f:
                        f.write(song_lrc)
                        f.flush()
                        f.close()

                    with open('D:\XiaoU\Deal\Lrc.txt', 'r', encoding='utf-8') as f2:
                        f2.seek(0)
                        num = 0
                        self.listview.clear()
                        for lrc in f2:

                            try:
                                re_lrc = re.compile('^\[.*?\](.*)')
                                lrc2 = re.search(re_lrc, lrc)[1]
                                if lrc2 == '':
                                    continue
                                if len(lrc2) < (int(self.lrc_window_width)/10):
                                    lrc_len = int((int(self.lrc_window_width)/10 - len(lrc2))/2)
                                    lrc_item = ' '*lrc_len + lrc2
                                self.listview.addItem(lrc_item)
                                self.listview.update()
                                re_lrc_time = re.compile('^\[(.*)\]')
                                re_lrc_time_min = re.compile('^(\d*):')
                                re_lrc_time_sec = re.compile('[.|:](\d*)[.|:]')
                                re_lrc_time_ms = re.compile('[.|:](\d*)$')
                                lrc_time = re.search(re_lrc_time, lrc)[1]
                                lrc_time_ms = re.search(re_lrc_time_ms, lrc_time)[1]
                                if len(lrc_time_ms) < 2:
                                    lrc_time_ms = '{}0'.format(lrc_time_ms)
                                # lrc_time_ms = '0.{}'.format(lrc_time_ms)
                                # lrc_time_ms = round(float(lrc_time_ms), 2)
                                lrc_time_s = int(re.search(re_lrc_time_min, lrc_time)[1]) * 60 + int(re.search(re_lrc_time_sec, lrc_time)[1])
                                lrc_time_s = float('{}.{}'.format(lrc_time_s, lrc_time_ms[:2]))
                                lrc_info[str(lrc_time_s)] = str(num) + '::' + lrc2
                                num += 1
                            except:
                                pass
                        f2.close()
                        self.listview.update()
                        for i in range(10):
                            self.listview.addItem(' ')
                            self.listview.update()
                finally:
                    lrc_add = 1
                    lrc_times = list(lrc_info.keys())

            else:
                pos = self.lrc_media.position()
                pos = float(pos)/1000
                pos =str(round(pos, 2))
                if (pos in lrc_times) and (pos != lrc_pos_last):
                    lrc_pos_last = pos
                    lrc = lrc_info[pos]
                    re_index = re.compile('^(\d.*)::')
                    index = re.findall(re_index, lrc)[0]
                    self.listview.setCurrentRow(int(index) + 10)
                    self.listview.setCurrentRow(int(index))
                    self.listview.update()
        if self.lrc_media.state() == 0:
            self.listview.clear()






class Download_Song(QThread):
    down_song_log = pyqtSignal(object)

    def run(self):
        global Queue_song, sum_songs
        while not Queue_song.empty():
            song = Queue_song.get()
            try:
                songd = sum_songs[song]
                sour = songd[0]
                if sour == '5Sing原创' or sour == '百度' or sour == '蜻蜓' or sour == '5Sing翻唱':
                    self.down_song_log.emit('下载失败,{} 不支持下载'.format(sour))
                else:
                    songd_url = songd[5]
                    resd = requests.get(songd_url)
                    F_songd = open(r'D:\XiaoU\Download\Audio\{}.mp3'.format(song), 'wb')
                    F_songd.write(resd.content)
                    F_songd.close()
                    self.down_song_log.emit('下载完成 - {}'.format(song))

            except Exception as e:
                self.down_song_log.emit('{} - 下载错误 - {}'.format(song, str(e)))
            if Queue_song.empty():
                time.sleep(10)
class BaiDuApi(object):
    def __init__(self, app_id=None, api_key=None, secretkey=None):
        """
        人脸检测程序，调用设备摄像头，提取图像中的人脸，并与百度人脸库中的人脸数据进行比对
        :param app_id:
        :param api_key:
        :param secretkey:
        """

        # 初始化用户信息
        self.UserInfo = {}
        if os.path.exists('./PConfig/config.pkl'):
            with open('./PConfig/config.pkl', 'rb') as f: self.UserInfo = pickle.load(f)
        self.UserInfo['APPID'] = self.UserInfo['APPID'] if 'APPID' in self.UserInfo.keys() else '17376947'
        self.UserInfo['APIKEY'] = self.UserInfo[
            'APIKEY'] if 'APIKEY' in self.UserInfo.keys() else 'K7G0KLcoQnTLH4QjmCZMigyM'
        self.UserInfo['SECRETKEY'] = self.UserInfo[
            'SECRETKEY'] if 'SECRETKEY' in self.UserInfo.keys() else 'xqdTGx6mMB6pu3WtD9c0r8yX9Sxy0OiL'
        self.UserInfo['AccessToken'] = self.UserInfo[
            'AccessToken'] if 'AccessToken' in self.UserInfo.keys() else "24.db9b8bb237b3dc364e22bd5526871bb6.2592000.1572765301.282335-17376947"  # 语音合成添加参数时，避免布尔判断为空，丢掉参数

        self.APPID = app_id if app_id else self.UserInfo['APPID']
        self.APIKEY = api_key if api_key else self.UserInfo['APIKEY']
        self.SECRETKEY = secretkey if secretkey else self.UserInfo['SECRETKEY']
        self.AccessToken = self.UserInfo['AccessToken']

    def _Request_post(self, _url, _data):
        """
        自定义网络请求，自动处理token失效问题
        :param _url:
        :param _data:
        :return:
        """
        _res = requests.post(_url, _data)
        _rec = None
        try:
            _ret = json.loads(_res.text)
            if "error_code" in _ret.keys():
                _rec = int(_ret['error_code'])
            elif 'err_subcode' in _ret.keys():
                _rec = int(_ret['err_subcode'])
        except Exception as e:
            print(e)
        if _rec == 100 or _rec == 110 or _rec == 111 or _rec == 16:
            print('ACCECC_TOKEN失效')
            # 重新获取access_token
            self.get_token()
            # 更新数据中的access_token
            if '?access_token=' in _url:
                re_tok = re.compile('\?access_token=(.*)')
                tok = re.findall(re_tok, _url)[0]
                _url = _url.replace(tok, self.AccessToken)
            elif 'access_token' in _data.keys():
                _data['tok'] = self.AccessToken
            elif 'tok' in _data.keys():
                print('in')
                _data['tok'] = self.AccessToken
            # 重新执行一次访问请求
            return self._Request_post(_url, _data)
        return _res

    def _get_requrl(self, _url):
        """
        传入url，整合acesstoken后返回
        :param _url:
        :return:
        """
        return '{}?access_token={}'.format(_url, self.AccessToken)

    def get_token(self):
        """
        获取ACESSTOKEN
        :return:
        """
        print('正在获取ACCESS_TOKEN')
        _url = 'https://aip.baidubce.com/oauth/2.0/token'
        _data = self._make_req_params(_key=True)
        _res = self._Request_post(_url, _data)
        _answer = json.loads(_res.text)
        self.AccessToken = _answer['access_token']
        self.UserInfo['AccessToken'] = self.AccessToken
        TokenAlTime = int(_answer['expires_in']) + int(time.time())
        with open('./PConfig/Pconfig.pkl', 'wb') as f: pickle.dump(self.UserInfo, f)
        print(self.AccessToken)
        print('获取ACCECC_TOKEN成功')

    def media_to_bs64(self, media):
        with open(media, 'rb') as f: return base64.b64encode(f.read()).decode()

    def _make_req_params(self, _key=False,**kwargs):
        """
        百度API请求参数处理
        :param kwargs:
        :return:
        """

        _data = {'grant_type': 'client_credentials', 'client_id': self.APIKEY, 'client_secret': self.SECRETKEY,'cuid':2019100311}
        for arg in kwargs:
            if arg == 'tok': _data[arg] = kwargs[arg] if kwargs[arg] else self.AccessToken
            elif arg == 'image': _data[arg] = self.media_to_bs64(kwargs[arg])
            elif arg == 'token': _data[arg] = kwargs[arg] if kwargs[arg] else self.AccessToken
            elif arg == 'tex': _data[arg] = quote_plus(kwargs[arg])
            elif arg == 'speech':
                with open(kwargs[arg], 'rb') as f:
                    speech = f.read()
                    _data[arg] =  base64.b64encode(speech).decode()
                    _data['len'] = len(speech)
            else:
                if kwargs[arg]:
                    _data[arg] = kwargs[arg]
        return _data



class Speech_synthesis(QThread):
    speech_synthesis_log = pyqtSignal(object)
    @catch_except
    def run(self):
        """
        语音合成
        """
        global Queue_speech, syn_items
        while not Queue_speech.empty():

            self.syn_result = []
            try:
                item = Queue_speech.get()
                self.speech_name = item[0]
                self.voice_text = item[1]
                self.per = item[2]
                self.spd = item[3]
                self.pit = item[4]
                self.vol = item[5]
                self.aue = item[6]
                self.people = {'普通女声': 0, '普通男生': 1, '成熟女性': 5, '成熟男声': 2, '度逍遥': 3, '度丫丫': 4}
                self.per = self.people[self.per]
                speech_aue = {"mp3": 3, "pcm-16k": 4, "pcm-8k": 5, "wav": 6}
                if 'pcm' in self.aue:
                    self.out_aue = 'pcm'
                else:
                    self.out_aue = self.aue
                self.aue_h = speech_aue[self.aue]
                # 发音人选择, 0为普通女声，1为普通男生，2成熟男声，3为情感合成-度逍遥，4为情感合成-度丫丫，5成熟女性，默认为普通女声
                if self.speech_name == '':
                    self.speech_name = time.strftime('%Y%m%d-%H%M%S', time.localtime())
                TTS_URL = 'http://tsn.baidu.com/text2audio'
                API_KEY = 'fWF3HKtPBAOejtCtfGqIGwIr'
                SECRET_KEY = 'omiaIm5GGe1rWEO4vQPmCvXeclQmvqc7'

                class DemoError(Exception):
                    pass

                TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
                SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选

                param = {'grant_type': 'client_credentials',
                         'client_id': API_KEY,
                         'client_secret': SECRET_KEY}
                post_data = urlencode(param)
                post_data = post_data.encode('utf-8')
                reqf = Request(TOKEN_URL, post_data)
                ff = urlopen(reqf, timeout=30)
                result_strf = ff.read()
                result_strf = result_strf.decode()
                result = json.loads(result_strf)
                if 'access_token' in result.keys() and 'scope' in result.keys():
                    if not SCOPE in result['scope'].split(' '):
                        raise DemoError('scope is not correct')
                    token = result['access_token']
                    if not os.path.exists(r'D:\XiaoU\Download\SpeechSynthesis'):
                        os.makedirs(r'D:\XiaoU\Download\SpeechSynthesis')
                    syn_save_dic = r'D:\XiaoU\Download\SpeechSynthesis\{}.{}'.format(self.speech_name, self.out_aue)
                    f2 = open(syn_save_dic, 'wb')
                    voice_texts = []
                    print(self.voice_text)
                    if len(self.voice_text) <= 2000:
                        voice_texts.append(self.voice_text)
                    else:
                        all_num = len(self.voice_text)
                        num = 0
                        while all_num > num*2000:
                            voice_texts.append(self.voice_text[num*2000:(num+1)*2000 if all_num >= (num+1)*2000 else all_num])
                            num += 1
                    for index, voice_text in enumerate(voice_texts):
                        # print(index,len(voice_texts)-1)
                        tex = quote_plus(voice_text)  # 此处TEXT需要两次urlencode
                        params = {'tok': token, 'tex': tex, 'per': self.per, 'spd': self.spd, 'pit': self.pit,
                                  'vol': self.vol, 'aue': self.aue_h,
                                  'cuid': "123456PYTHON",
                                  'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数
                        data = urlencode(params)
                        req = Request(TTS_URL, data.encode('utf-8'))
                        f = urlopen(req)
                        f2.write(f.read())
                        f2.flush()

                    f2.close()
                    res_log = '语音合成完成'
                    self.syn_name_out = '{}.{}'.format(self.speech_name, self.out_aue)
                    self.syn_result.append(res_log)
                    self.syn_result.append(self.syn_name_out)
                    self.syn_result.append(syn_save_dic)
                    # 将名字，路径，文本保存在字典
                    syn_items[self.syn_name_out] = [syn_save_dic, self.voice_text]
                    self.speech_synthesis_log.emit(self.syn_result)
            except Exception as err:
                res_log = '语音合成错误'
                self.syn_result.append(res_log)
                self.syn_result.append(str(err))
                self.speech_synthesis_log.emit(self.syn_result)


class Voice_recognition(QThread):

    asr_result = pyqtSignal(object)
    __asrUrl = 'http://vop.baidu.com/server_api'
    # __asrUrl = 'http://vop.baidu.com/server_api'
    @catch_except
    def run(self):
        """
        语音识别
        """

        global Queue_ASR, asr_items
        while not Queue_ASR.empty():
            result = []
            # '17376947', 'K7G0KLcoQnTLH4QjmCZMigyM', 'xqdTGx6mMB6pu3WtD9c0r8yX9Sxy0OiL'
            APP_ID = '17376947'
            APP_KEY = 'K7G0KLcoQnTLH4QjmCZMigyM'
            SECRET_KEY = 'xqdTGx6mMB6pu3WtD9c0r8yX9Sxy0OiL'
            item = Queue_ASR.get()
            speech_dic = item[0]
            asr_format = item[1]


            speech_dic = speech_dic.replace('/',os.sep)
            speech_file = re.findall(r'.*\\(.*\.(.*))', speech_dic)
            speech_name = speech_file[0][0]
            # 获取音频时长
            sec = mediainfo(speech_dic)
            if sec:sec = eval(sec['duration'])
            else:sec = 0

            file_list = []
            num = 0
            # 如果文件时长太长，则将文件分割
            if sec > 55:
                ASFF = AudioSegment.from_file(speech_dic,format=speech_file[0][1])
                if not os.path.exists(r'D:\XiaoU\Deal\Voice\Reco'):
                    os.makedirs(r'D:\XiaoU\Deal\Voice\Reco')# shutil.rmtree(_file)
                while True:
                    end_t = (num + 1)*50*1000 if (num + 1)*50*1000 < sec*1000 else sec*1000
                    while True:
                        # 单次请求重复文件名
                        _file = r'D:\XiaoU\Deal\Voice\Reco\P{}.{}'.format(random.randint(100,300),speech_file[0][1])
                        if _file not in file_list:
                            break
                    ASFF[num*50*1000:end_t].export(_file,format=speech_file[0][1])
                    file_list.append(_file)
                    if end_t >= sec*1000:
                        break
                    num += 1
            else:
                file_list.append(speech_dic)
            text_sub = ''
            err_file = ''
            # 遍历文件
            for file in file_list:
                with open(file,'rb') as _f:
                    # , options = {"dev_pid": 1536, }
                    text = AipSpeech(APP_ID,APP_KEY,SECRET_KEY).asr(_f.read(),format=asr_format)
                    print(text)
                    err_no = text['err_no'] if 'err_no' in text.keys() else text['error_code']
                    err_msg = text['err_msg'] if 'err_msg' in text.keys() else text['error_msg']
                    if str(err_no) == "0":
                        text_sub += text['result'][0]
                    else:
                        err_file += '文件名：' + file + '\n失败原因：' + err_msg + '\n'
            if text_sub:
                res_log = '语音识别完成'
                if err_file:
                    res_log += '\n未识别内容：\n' + err_file
                result.append(res_log)
                result.append(speech_name)
                result.append(speech_dic)
                result.append(text_sub)
                asr_items[speech_name] = [speech_dic, text_sub]
                self.asr_result.emit(result)
            else:
                res_log = '语音识别错误'
                result.append(res_log)
                result.append(err_file)
                self.asr_result.emit(result)








class Opencv(Ui_Form):
    def __init__(self):
        super(Opencv, self).__init__()


        self.init_7_variable()
        self.init_7_tab()
        self.init_7_event()


    def init_7_variable(self):

        self.lbtn = 0
        self.opencv_7_drawor = 0
        self.img = np.zeros((600, 800), np.uint8)
        self.var_7_take_photo = 0
        self.var_7_photography = 0
        # 相机
        self.var_7_camera = None
        # 录像保存
        self.var_7_videowriter = None
        self.var_7_videowriter_state = 0

    def init_7_tab(self):
        self.tab_7 = QtWidgets.QTableWidget()
        self.tab_7.setObjectName('tab_7')
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_7.setObjectName('gridLayout_7')
        self.tabWidget.addTab(self.tab_7, '相机')
        self.gridLayout_7.setSpacing(2)

        self.timer_show = QtCore.QTimer()
        self.timer_show.start(25)
        self.label_7_imshow = QLabel()
        self.label_7_imshow.setObjectName('label_7_imshow')
        self.gridLayout_7.addWidget(self.label_7_imshow, 1, 0, 1, 4)
        self.label_7_imshow.setPixmap(QPixmap(r'{}/ico/carmera.png'.format(here_dic)))
        self.btn_7_ok = QtWidgets.QToolButton()
        self.btn_7_ok.setObjectName('btn_7_ok')
        ico_7_ok = QIcon()
        ico_7_ok.addPixmap(QPixmap(r'{}/ico/carmera.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_7_ok.setIcon(ico_7_ok)
        self.btn_7_ok.setFixedSize(QtCore.QSize(25,25))
        self.btn_7_ok.setIconSize(QtCore.QSize(20,20))
        self.gridLayout_7.addWidget(self.btn_7_ok, 0,1,1,1)
        self.cm_7_func = QtWidgets.QComboBox()
        self.cm_7_func.setObjectName('cm_7_func')
        self.cm_7_func.setFixedSize(QtCore.QSize(70, 25))
        self.gridLayout_7.addWidget(self.cm_7_func, 0,0,1,1)
        cm_7_func = ['拍照', '录像']
        self.cm_7_func.addItems(cm_7_func)


        self.btn_7_save = QtWidgets.QToolButton()
        self.btn_7_save.setObjectName('btn_7_save')
        self.gridLayout_7.addWidget(self.btn_7_save,0,2,1,1 )
        ico_7_save = QIcon()
        ico_7_save.addPixmap(QPixmap(r'{}/ico/save.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_7_save.setIcon(ico_7_save)
        self.btn_7_save.setFixedSize(QtCore.QSize(25,25))
        self.btn_7_save.setIconSize(QtCore.QSize(20,20))
        self.label_7_space = QLabel()
        self.label_7_space.setObjectName('label_7_space')
        self.gridLayout_7.addWidget(self.label_7_space, 0,3,1,1)





    def timer_show_timeout(self):
        func = self.cm_7_func.currentText()
        if self.opencv_7_drawor == 1:
            pass
            #cv.setMouseCallback('drawing', self.drawing2)
        elif func == '拍照' and (self.var_7_take_photo == 1 or self.var_7_take_photo == 2):
            self.take_photo()
        elif func == '录像' and (self.var_7_photography == 1 or self.var_7_photography == 2):
            self.photography()

    def init_7_event(self):
        self.timer_show.timeout.connect(self.timer_show_timeout)
        self.btn_7_ok.clicked.connect(self.btn_7_ok_clicked)
        self.btn_7_save.clicked.connect(self.btn_7_save_clicked)
        self.cm_7_func.currentTextChanged.connect(self.cm_7_func_currentTextChanged)



    def btn_7_save_clicked(self):
        func = self.cm_7_func.currentText()
        if func == '拍照' and self.var_7_take_photo == 2:
            save_pix = self.label_7_imshow.pixmap()
            filename = time.strftime('%m%d%H%M%S')
            if not os.path.exists(r'D:\XiaoU\Download\Carmera\Photo'):
                os.makedirs(r'D:\XiaoU\Download\Carmera\Photo')

            save_state = save_pix.save(r'D:\XiaoU\Download\Carmera\Photo\img{}.jpg'.format(filename))
            if save_state:
                QMessageBox.information(self, '保存提示', '照片保存成功\nImage{}.jpg'.format(filename), QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, '保存提示', '照片保存失败', QMessageBox.Ok,QMessageBox.Ok)
        elif func == '录像':
            if self.var_7_photography == 2:
                if self.var_7_videowriter_state == 0:
                    self.var_7_videowriter_state = 1
                    ico_7_pause = QIcon()
                    ico_7_pause.addPixmap(QPixmap('{}/ico/pause.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
                    self.btn_7_save.setIcon(ico_7_pause)
                else:
                    self.var_7_videowriter_state = 0
                    self.var_7_videowriter.release()
                    ico_7_begin = QIcon()
                    ico_7_begin.addPixmap(QPixmap('{}/ico/play.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
                    self.btn_7_save.setIcon(ico_7_begin)





    def btn_7_ok_clicked(self):
        func = self.cm_7_func.currentText()
        if func == '拍照':
            if self.var_7_take_photo == 0:
                self.var_7_take_photo = 1
                ico_7_ok = QIcon()
                ico_7_ok.addPixmap(QPixmap('{}/ico/close.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
                self.btn_7_ok.setIcon(ico_7_ok)
            else:
                self.var_7_take_photo = 0
                self.var_7_camera.release()
                cv.destroyAllWindows()
                ico_7_ok = QIcon()
                ico_7_ok.addPixmap(QPixmap('{}/ico/carmera.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
                self.btn_7_ok.setIcon(ico_7_ok)
                self.label_7_imshow.setPixmap(QPixmap('{}/ico/carmera.png'.format(here_dic)))

        elif func == '录像':
            if self.var_7_photography == 0:
                self.var_7_photography = 1
                ico_7_ok = QIcon()
                ico_7_ok.addPixmap(QPixmap('{}/ico/close.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
                self.btn_7_ok.setIcon(ico_7_ok)
            else:
                if self.var_7_videowriter_state == 2:
                    self.var_7_videowriter_state = 0
                    self.var_7_videowriter.release()
                    ico_7_begin = QIcon()
                    ico_7_begin.addPixmap(QPixmap('{}/ico/play.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
                    self.btn_7_save.setIcon(ico_7_begin)
                self.var_7_photography = 0
                self.var_7_camera.release()
                ico_7_ok = QIcon()
                ico_7_ok.addPixmap(QPixmap('{}/ico/video.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
                self.btn_7_ok.setIcon(ico_7_ok)
                self.label_7_imshow.setPixmap(QPixmap('{}/ico/video.png'.format(here_dic)))
        elif func == '测试':
            if self.var_7_take_photo == 0:
                self.var_7_take_photo = 1
            else:
                self.var_7_take_photo = 0
                self.var_7_camera.release()
                cv.destroyAllWindows()
                cv.destroyAllWindows()
                print(self.label_7_imshow.pixmap().save('img.jpg'))


    def cm_7_func_currentTextChanged(self):
        func = self.cm_7_func.currentText()
        if func == '拍照':
            ico_7_save = QIcon()
            ico_7_save.addPixmap(QPixmap('{}/ico/save.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_7_save.setIcon(ico_7_save)
            ico_7_ok = QIcon()
            ico_7_ok.addPixmap(QPixmap('{}/ico/carmera.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_7_ok.setIcon(ico_7_ok)
            self.label_7_imshow.setPixmap(QPixmap(r'{}/ico/carmera.png'.format(here_dic)))
        elif func == '录像':
            self.var_7_photography = 0
            ico_7_begin = QIcon()
            ico_7_begin.addPixmap(QPixmap('{}/ico/play.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_7_save.setIcon(ico_7_begin)
            ico_7_ok = QIcon()
            ico_7_ok.addPixmap(QPixmap('{}/ico/video.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
            self.btn_7_ok.setIcon(ico_7_ok)
            self.label_7_imshow.setPixmap(QPixmap(r'{}/ico/video.png'.format(here_dic)))

    # 图片显示
    def im_deal(self):
        img = cv.imread(r'E:\Python\Testfile\A1.jpg', 1)
        while True:
            cv.imshow('A1', img)
            k_1 = cv.waitKey(100)
            if k_1 == ord('s'):
                cv.imwrite('test.png', img)
            elif k_1 == ord('q'):
                break
        cv.destroyWindow('A1')

    def take_photo(self):
        if self.var_7_take_photo == 1:
            self.var_7_camera = cv.VideoCapture(0)
            #self.var_7_camera.set(3,1280)
            #self.var_7_camera.set(4,720)
            self.var_7_take_photo = 2
        elif self.var_7_take_photo == 2:
            # 播放视频
            # cap = cv.VideoCapture('a2.flv')
            if self.var_7_camera.isOpened():
                ret, frame = self.var_7_camera.read()
                if ret:
                    frame = cv.flip(frame,1)
                    img_size = (int(self.label_7_imshow.width()), int(self.label_7_imshow.height()))
                    frame = cv.resize(frame,img_size )
                    #gray = cv.cvtColor(frame, cv.COLOR_RGB2RGBA)
                    gray = cv.cvtColor(frame, cv.COLOR_RGB2RGBA)

                    img = QImage(gray.data, gray.shape[1], gray.shape[0],gray.shape[1]*4, QImage.Format_ARGB32)
                    self.label_7_imshow.setPixmap(QPixmap.fromImage(img))
                    #cv.imshow('frame', gray)




    # 摄像
    def photography(self):
        if self.var_7_photography == 1:
            self.var_7_camera = cv.VideoCapture(0)
            self.var_7_photography = 2
        if self.var_7_camera.isOpened():
            if self.var_7_videowriter_state == 1:
                filename = time.strftime('%m%d%H%M%S')
                fourcc = cv.VideoWriter_fourcc(*'MJPG')
                if not os.path.exists(r'D:\XiaoU\Download\Carmera\Video'):
                    os.makedirs(r'D:\XiaoU\Download\Carmera\Video')
                self.var_7_videowriter = cv.VideoWriter(r'D:\XiaoU\Download\Carmera\Video\Video{}.mp4'.format(filename), fourcc, 20.0, (640,480))
                self.var_7_videowriter_state = 2

            if self.var_7_photography == 2:
                if self.var_7_camera.isOpened():
                    ret, frame = self.var_7_camera.read()
                    if not ret:
                        QMessageBox.information(self,'ERROR', 'Canera open failed', QMessageBox.Ok, QMessageBox.Ok)
                    frame1 = cv.flip(frame, 1)
                    frame_size = (int(self.label_7_imshow.width()), int(self.label_7_imshow.height()))
                    frame = cv.resize(frame1,frame_size )
                    frame = cv.cvtColor(frame, cv.COLOR_RGB2RGBA)
                    #frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                    #cv.imshow('frame', frame)
                    img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1]*4, QImage.Format_ARGB32)
                    self.label_7_imshow.setPixmap(QPixmap.fromImage(img))
                    if self.var_7_videowriter_state == 2:
                        self.var_7_videowriter.write(frame1)

class Drawing(Ui_Form):
    def __init__(self):
        super(Drawing, self).__init__()
        self.init_variate()
        self.init_tab6()
        self.init_pen_6()
        self.init_pix_6()

        self.init_event()

    def init_tab6(self):
        # tab6
        self.tab_6 = QtWidgets.QTableWidget()
        self.tab_6.setObjectName('tab_6')
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_6.setObjectName('gridLayout_6')
        self.tabWidget.addTab(self.tab_6, '画板')
        self.cm_6_shape = QtWidgets.QComboBox()
        self.cm_6_shape.setObjectName('cm_6_shape')

        shape_6_type = ['轨迹', '点', '线', '矩形', '圆', '椭圆', '多边形', '扇形', '弧形',  '文字']
        self.cm_6_shape.addItems(shape_6_type)
        self.cm_6_shape.setFixedSize(QtCore.QSize(70,25))
        self.cm_6_linetype = QtWidgets.QComboBox()
        self.cm_6_linetype.setObjectName('cm_6_linetype')
        cm_6_linetype = ['实线', '虚线', '划线', '点划线', '点点划线']
        self.cm_6_linetype.addItems(cm_6_linetype)
        self.cm_6_linetype.setFixedSize(QtCore.QSize(70,25))

        self.cm_6_color_item = QtWidgets.QComboBox()
        self.cm_6_color_item.setObjectName('cm_6_color_item')
        self.cm_6_color_item.setFixedSize(QtCore.QSize(70, 25))
        cm_6_color_item = ['画笔', '画布']
        self.cm_6_color_item.addItems(cm_6_color_item)

        self.spb_6_linewidth = QtWidgets.QSpinBox()
        self.spb_6_linewidth.setObjectName('spb_6_linewidth')
        self.spb_6_linewidth.setRange(1, 500)
        self.spb_6_linewidth.setFixedSize(QtCore.QSize(45,25))


        self.btn_6_colorselect = QtWidgets.QToolButton()
        self.btn_6_colorselect.setObjectName('btn_6_colorselect')
        self.btn_6_save = QtWidgets.QToolButton()
        self.btn_6_save.setObjectName('btn_6_save')
        ico_6_save = QIcon()
        ico_6_save.addPixmap(QPixmap(r'{}/ico/save.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_6_save.setIcon(ico_6_save)
        self.btn_6_save.setText('保存')
        self.btn_6_save.setIconSize(QtCore.QSize(20,20))
        self.btn_6_clear = QtWidgets.QToolButton()
        self.btn_6_clear.setObjectName('btn_6_clear')
        self.btn_6_clear.setText('清空')
        ico_6_clear = QIcon()
        ico_6_clear.addPixmap(QPixmap(r'{}/ico/clear.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_6_clear.setIcon(ico_6_clear)
        self.btn_6_clear.setIconSize(QtCore.QSize(20,20))
        self.btn_zoomout = QtWidgets.QToolButton()
        self.btn_zoomout.setObjectName('btn_zoomout')
        self.btn_zoomin = QtWidgets.QToolButton()
        self.btn_zoomin.setObjectName('btn_zoomin')


        # label
        self.label_6_shape = QLabel()
        self.label_6_shape.setObjectName('label_6_shape')
        self.label_6_shape.setText('形状')
        self.label_6_color = QLabel()
        self.label_6_color.setObjectName('label_6_color')
        self.label_6_color.setText('颜色')
        self.label_6_linewidth = QLabel()
        self.label_6_linewidth.setObjectName('label_6_linewidth')
        self.label_6_linewidth.setText('线宽')
        self.label_6_linetype = QLabel()
        self.label_6_linetype.setObjectName('label_6_linetype')
        self.label_6_linetype.setText('线型')
        self.btn_zoomin.setText('缩小')
        ico_6_zommin = QIcon()
        ico_6_zommin.addPixmap(QPixmap(r'{}/ico/zoomin.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_zoomin.setIcon(ico_6_zommin)
        self.btn_zoomin.setIconSize(QtCore.QSize(25,25))
        # ico_4_folder.addPixmap(QtGui.QPixmap(r"{}/ico/show.png".format(here_dic)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoomout.setText('放大')
        ico_6_zommout = QIcon()
        ico_6_zommout.addPixmap(QPixmap(r'{}/ico/zoomout.png'.format(here_dic)), QIcon.Normal, QIcon.Off)
        self.btn_zoomout.setIcon(ico_6_zommout)
        self.btn_zoomout.setIconSize(QtCore.QSize(25,25))
        self.label_6_bottom = QLabel()
        self.label_6_bottom.setObjectName('label_6_bottom')
        self.gridLayout_6.addWidget(self.label_6_bottom, 2,0,1,14)
        self.lnedit_6_input = QtWidgets.QLineEdit()
        self.lnedit_6_input.setObjectName('lnedit_6_input')

        self.label_6_space = QLabel()
        self.label_6_space.setObjectName('label_6_space')

        #self.label_6_shape.setGeometry(20,67,25,25)
        self.label_6_shape.setMaximumSize(QtCore.QSize(25,25))
        self.label_6_shape.setMinimumSize(QtCore.QSize(1, 1))
        self.label_6_color.setMaximumSize(QtCore.QSize(25, 25))
        self.label_6_color.setMinimumSize(QtCore.QSize(1, 1))
        self.label_6_linewidth.setMaximumSize(QtCore.QSize(25, 25))
        self.label_6_linewidth.setMinimumSize(QtCore.QSize(1, 1))
        self.label_6_linetype.setMaximumSize(QtCore.QSize(25, 25))
        self.label_6_linetype.setMinimumSize(QtCore.QSize(1, 1))
        self.btn_6_save.setFixedSize(QtCore.QSize(25,25))
        self.btn_6_clear.setFixedSize(QtCore.QSize(25,25))
        self.btn_zoomout.setFixedSize(QtCore.QSize(25,25))
        self.btn_zoomin.setFixedSize(QtCore.QSize(25,25))
        self.lnedit_6_input.setFixedHeight(25)
        self.label_6_space.setFixedHeight(25)

        self.gridLayout_6.addWidget(self.label_6_shape, 0,0,1,1)
        self.gridLayout_6.addWidget(self.cm_6_shape, 0,1,1,1)
        self.gridLayout_6.addWidget(self.label_6_linetype, 0,2,1,1)
        self.gridLayout_6.addWidget(self.cm_6_linetype, 0, 3, 1, 1)
        self.gridLayout_6.addWidget(self.label_6_linewidth, 0,4,1,1)
        self.gridLayout_6.addWidget(self.spb_6_linewidth, 0, 5, 1, 1)
        self.gridLayout_6.addWidget(self.label_6_color, 0,6,1,1)
        self.gridLayout_6.addWidget(self.cm_6_color_item, 0, 7, 1, 1)
        self.gridLayout_6.addWidget(self.btn_6_colorselect, 0, 8, 1, 1)
        self.gridLayout_6.addWidget(self.btn_zoomout, 0,9,1,1)
        self.gridLayout_6.addWidget(self.btn_zoomin, 0,10,1,1)
        self.gridLayout_6.addWidget(self.btn_6_clear, 0, 11, 1, 1)
        self.gridLayout_6.addWidget(self.btn_6_save, 0,12,1,1)
        #self.gridLayout_6.addWidget(self.label_6_space, 0,13,1,1)
        self.gridLayout_6.addWidget(self.lnedit_6_input, 0,13,1,1 )

    # def test(self):
    #     print('test')
    #     color = QColorDialog()
    #     colo = color.getColor()
    #     print(colo)
    #     self.btn_6_colorselect.setStyleSheet('#btn_6_colorselect{background-color:%s}' %colo.name())
    #     #self.pix_6.fill(colo)
    #     self.pen_6.setColor(colo)
    #     self.painter_6_pix.setPen(self.pen_6)

    def init_variate(self):
        # 绘图状态管理
        self.var_6_drawing_state = 0
        # 多边形
        self.var_6_polygon = 0
        self.var_6_polygon_start = QtCore.QPoint(22, 95)
        self.var_6_polygon_next = self.var_6_polygon_start



    def init_event(self):
        # 事件
        self.btn_6_colorselect.setStyleSheet('#btn_6_colorselect{background-color:%s}' % self.pen_6_color.name())
        self.btn_6_colorselect.clicked.connect(self.color_select)
        self.cm_6_color_item.currentTextChanged.connect(self.cm_6_color_item_change)
        self.spb_6_linewidth.valueChanged.connect(self.spb_6_linewidth_change)
        self.btn_6_save.clicked.connect(self.btn_6_save_clicked)
        self.btn_6_clear.clicked.connect(self.btn_6_clear_clicked)
        self.btn_zoomin.clicked.connect(self.btn_zoomin_clicked)
        self.btn_zoomout.clicked.connect(self.btn_zoomout_clicked)
        self.cm_6_linetype.currentTextChanged.connect(self.cm_6_linetype_currentTextChanged)




    def init_pen_6(self):
        self.pen_6_color = QtGui.QColor(QtCore.Qt.black)
        self.pen_6_with = 1
        self.pen_6_linetype = QtCore.Qt.SolidLine
        self.pen_6 = QPen(self.pen_6_color, self.pen_6_with, self.pen_6_linetype )
        self.pen_6.setCapStyle(QtCore.Qt.RoundCap)

    def init_pix_6(self):
        self.point_6_end = QPoint()
        self.point_6_start = QPoint()
        self.pix_6_size_w = 666
        self.pix_6_size_h = 375
        self.pix_6_offset = QtCore.QPoint(22, 95)
        self.pix_6_move = 0

        self.label_6_drawing = QLabel()
        self.label_6_drawing.setObjectName('label_6_drawing')
        self.label_6_drawing.setStyleSheet('QLabel{background-color:blue}')
        self.label_6_drawing.setFixedSize(QtCore.QSize(self.pix_6_size_w, self.pix_6_size_h))
        self.gridLayout_6.addWidget(self.label_6_drawing, 1, 0, 1, 14)
        self.pix_6 = QPixmap(self.label_6_drawing.width(), self.label_6_drawing.height())
        self.pix_6_color = QtGui.QColor(QtCore.Qt.white)
        self.pix_6.fill(self.pix_6_color)
        self.label_6_drawing.setPixmap(self.pix_6)
        self.painter_6_pix = QPainter(self.pix_6)
        self.painter_6_pix.setPen(self.pen_6)
        # 形状DRAG
        self.var_6_line = 0
        self.var_6_circle = 0
        self.var_6_point = 0
        self.var_6_rect = 0
        self.var_6_ellipse = 0
        self.var_6_text = 0
        self.var_6_polygon = 0
        # 扇形
        self.var_6_pie = 0
        # 弧形
        self.var_6_arc = 0
        # 路径
        self.var_6_path = 0



    def btn_zoomout_clicked(self):
        del self.painter_6_pix
        self.pix_6_size_h += 5
        self.pix_6_size_w = self.pix_6_size_h*(16/9)
        self.pix_6_offset = QtCore.QPoint(22, 95)
        img_temp = self.pix_6.copy()
        pix_temp = QPixmap(self.pix_6_size_w, self.pix_6_size_h)
        pp_temp = QPainter(pix_temp)
        pp_temp.drawPixmap(0, 0, self.pix_6_size_w, self.pix_6_size_h, img_temp)
        self.label_6_drawing.setFixedSize(QtCore.QSize(self.pix_6_size_w,self.pix_6_size_h))
        self.label_6_drawing.show()
        self.pix_6 = pix_temp.copy()
        self.painter_6_pix = QPainter(self.pix_6)
        self.label_6_drawing.setPixmap(self.pix_6)
        del pp_temp




    def btn_zoomin_clicked(self):
        del self.painter_6_pix
        self.pix_6_size_h -= 5
        self.pix_6_size_w = self.pix_6_size_h*(16/9)
        self.pix_6_offset = QtCore.QPoint(22, 95)
        img_temp = self.pix_6.copy()
        pix_temp = QPixmap(self.pix_6_size_w, self.pix_6_size_h)
        pp_temp = QPainter(pix_temp)
        pp_temp.drawPixmap(0, 0, self.pix_6_size_w, self.pix_6_size_h, img_temp)
        self.label_6_drawing.setFixedSize(QtCore.QSize(self.pix_6_size_w,self.pix_6_size_h))
        self.label_6_drawing.show()
        self.pix_6 = pix_temp.copy()
        self.painter_6_pix = QPainter(self.pix_6)
        self.label_6_drawing.setPixmap(self.pix_6)
        del pp_temp


    def btn_6_clear_clicked(self):
        warn = QMessageBox.warning(self,'提示', '此操作会清空画板内容\n是否继续？', QMessageBox.Yes|QMessageBox.Cancel, QMessageBox.Cancel)
        if warn == 16384:
            self.pix_6.fill(self.pix_6_color)
            self.label_6_drawing.setPixmap(self.pix_6)

    def btn_6_save_clicked(self):
        save_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        if not os.path.exists('D:\XiaoU\Download\Image'):
            os.makedirs('D:\XiaoU\Download\Image')
        save_state = self.pix_6.save(r'D:\XiaoU\Download\Image\image{}.jpg'.format(save_time))
        if save_state:
            QMessageBox.information(self, '保存提示', '保存成功\nimage{}'.format(save_time), QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self, '保存提示', '保存失败', QMessageBox.Ok, QMessageBox.Ok)

    def spb_6_linewidth_change(self):
        self.pen_6_with = self.spb_6_linewidth.value()
        self.pen_6.setWidth(self.pen_6_with)
        self.painter_6_pix.setPen(self.pen_6)

    def cm_6_linetype_currentTextChanged(self):
        current_text = self.cm_6_linetype.currentText()
        if current_text == '实线':
            self.pen_6.setStyle(QtCore.Qt.SolidLine)
        elif current_text == '虚线':
            self.pen_6.setStyle(QtCore.Qt.DotLine)
        elif current_text == '划线':
            self.pen_6.setStyle(QtCore.Qt.DashLine)
        elif current_text == '点划线':
            self.pen_6.setStyle(QtCore.Qt.DashDotLine)
        elif current_text == '点点划线':
            self.pen_6.setStyle(QtCore.Qt.DashDotDotLine)
        self.painter_6_pix.setPen(self.pen_6)


    def color_select(self):
        self.color_6_select = QColorDialog.getColor()
        item = self.cm_6_color_item.currentText()
        if item == '画笔':
            self.pen_6.setColor(self.color_6_select)
            self.painter_6_pix.setPen(self.pen_6)

        elif item == '画布':
            self.pix_6_color = self.color_6_select
            self.pix_6.fill(color=self.pix_6_color)
            self.label_6_drawing.setPixmap(self.pix_6)


        self.btn_6_colorselect.setStyleSheet('#btn_6_colorselect{background-color:%s}' % self.color_6_select.name())



    def cm_6_color_item_change(self):
        item = self.cm_6_color_item.currentText()
        color = self.pen_6.color()
        if item == '画笔':
            color = self.pen_6.color()

        elif item == '画布':
            color = self.pix_6_color

        elif item == '文字':
            pass
        self.btn_6_colorselect.setStyleSheet('#btn_6_colorselect{background-color:%s}' % color.name())

    def paintEvent(self, QPaintEvent):

        shape = self.cm_6_shape.currentText()
        if self.var_6_drawing_state == 1 or self.var_6_drawing_state == 2:
            pix_temp = self.pix_6.copy()
            pp_temp = QPainter(pix_temp)
            pp_temp.setPen(self.pen_6)

            if shape == '点':

                if self.var_6_drawing_state == 1:
                    pp_temp.drawPoint(self.point_6_end)
                    self.label_6_drawing.setPixmap(pix_temp)
                elif self.var_6_drawing_state == 2:
                    self.painter_6_pix.setPen(self.pen_6)
                    self.painter_6_pix.drawPoint(self.point_6_end)
                    self.var_6_drawing_state = 0

            elif shape == '线':
                if self.var_6_drawing_state == 1:
                    pp_temp.drawLine(self.point_6_start, self.point_6_end)
                    self.label_6_drawing.setPixmap(pix_temp)
                elif self.var_6_drawing_state == 2:
                    self.painter_6_pix.setPen(self.pen_6)
                    self.painter_6_pix.drawLine(self.point_6_start, self.point_6_end)
                    self.label_6_drawing.setPixmap(self.pix_6)
                    self.var_6_drawing_state = 0

            elif shape == '矩形':
                redis = self.point_6_end - self.point_6_start
                if self.var_6_drawing_state == 1:
                    pp_temp.drawRect(self.point_6_start.x(), self.point_6_start.y(), redis.x(), redis.y())
                    self.label_6_drawing.setPixmap(pix_temp)
                    self.label_6_drawing.update()
                elif self.var_6_drawing_state == 2:
                    self.painter_6_pix.drawRect(self.point_6_start.x(), self.point_6_start.y(), redis.x(), redis.y())
                    self.var_6_drawing_state = 0

            elif shape == '圆':
                dis = (self.point_6_end - self.point_6_start)
                radius = math.sqrt((dis.x() ** 2 + dis.y() ** 2))
                if self.var_6_drawing_state == 1:
                    pp_temp.drawEllipse(self.point_6_start, radius, radius)
                    self.label_6_drawing.setPixmap(pix_temp)
                elif self.var_6_drawing_state == 2:
                    self.painter_6_pix.drawEllipse(self.point_6_start, radius, radius)
                    self.label_6_drawing.setPixmap(self.pix_6)
                    self.var_6_drawing_state = 0

            elif shape == '椭圆':
                long = re.findall('(\d+)(:|：)', self.lnedit_6_input.text())
                short = re.findall('(:|：)(\d+)', self.lnedit_6_input.text())
                if long and short:
                    long = int(long[0][0])
                    short = int(short[0][1])
                    if self.var_6_drawing_state == 1:
                        pp_temp.drawEllipse(self.point_6_end, long, short)
                        self.label_6_drawing.setPixmap(pix_temp)
                    elif self.var_6_drawing_state ==2:
                        self.painter_6_pix.drawEllipse(self.point_6_end, long, short)
                        self.var_6_drawing_state = 0
                else:
                    if self.var_6_drawing_state == 1:
                        self.var_6_drawing_state = 0
                        tip_info = '''请在右上方输入框中输入数据：\n椭圆：需输入长半轴和短半轴，以冒号隔开， 如  100:120\n扇形：需输入两条母线长度以及起止角度，以冒号隔开 如 100:100:0:90\n弧形：与扇形输入一致\n文字：需输入需要添加的文字'''
                        QMessageBox.information(self, '输入提示', tip_info, QMessageBox.Ok, QMessageBox.Ok)


            elif shape == '多边形':
                if self.var_6_drawing_state == 1 and self.var_6_polygon == 0:
                    self.var_6_polygon = 1
                    self.var_6_polygon_start = self.point_6_start
                    self.var_6_polygon_next = self.var_6_polygon_start

                if  self.var_6_polygon == 1:
                    if self.var_6_drawing_state == 1:
                        pp_temp.drawLine(self.var_6_polygon_next, self.point_6_end)
                        self.label_6_drawing.setPixmap(pix_temp)
                    elif self.var_6_drawing_state == 2:
                        self.painter_6_pix.setPen(self.pen_6)
                        self.painter_6_pix.drawLine(self.var_6_polygon_next, self.point_6_end)
                        self.label_6_drawing.setPixmap(self.pix_6)
                        self.var_6_drawing_state = 0
                        self.var_6_polygon_next = self.point_6_end

            elif shape == '扇形':
                data = re.findall('(\d+)(:|：)(\d+)(:|：)(\d+)(:|：)(\d+)', self.lnedit_6_input.text())
                if data:
                    data = data[0]
                    if self.var_6_drawing_state == 1:
                        pp_temp.drawPie(self.point_6_end.x(), self.point_6_end.y(),int(data[0]), int(data[2]),int(data[4])*16,int(data[6])*16)
                        self.label_6_drawing.setPixmap(pix_temp)
                    elif self.var_6_drawing_state == 2:
                        self.painter_6_pix.drawPie(self.point_6_end.x(), self.point_6_end.y(),int(data[0]), int(data[2]),int(data[4])*16,int(data[6])*16)
                        self.label_6_drawing.setPixmap(self.pix_6)
                        self.var_6_drawing_state =0
                else:
                    if self.var_6_drawing_state == 1:
                        self.var_6_drawing_state = 0
                        tip_info = '''请在右上方输入框中输入数据：\n椭圆：需输入长半轴和短半轴，以冒号隔开， 如  100:120\n扇形：需输入两条母线长度以及起止角度，以冒号隔开 如 100:100:0:90\n弧形：与扇形输入一致\n文字：需输入需要添加的文字'''
                        QMessageBox.information(self, '输入提示', tip_info, QMessageBox.Ok, QMessageBox.Ok)


            elif shape == '弧形':
                data = re.findall('(\d+)(:|：)(\d+)(:|：)(\d+)(:|：)(\d+)', self.lnedit_6_input.text())
                if data:
                    data = data[0]
                    if self.var_6_drawing_state == 1:
                        pp_temp.drawArc(self.point_6_end.x(), self.point_6_end.y(), int(data[0]), int(data[2]),
                                        int(data[4]) * 16, int(data[6]) * 16)
                        self.label_6_drawing.setPixmap(pix_temp)
                    elif self.var_6_drawing_state == 2:
                        self.painter_6_pix.drawArc(self.point_6_end.x(), self.point_6_end.y(), int(data[0]),
                                                   int(data[2]), int(data[4]) * 16, int(data[6]) * 16)
                        self.label_6_drawing.setPixmap(self.pix_6)
                        self.var_6_drawing_state = 0
                else:
                    if self.var_6_drawing_state == 1:
                        self.var_6_drawing_state = 0
                        tip_info = '''请在右上方输入框中输入数据：\n椭圆：需输入长半轴和短半轴，以冒号隔开， 如  100:120\n扇形：需输入两条母线长度以及起止角度，以冒号隔开 如 100:100:0:90\n弧形：与扇形输入一致\n文字：需输入需要添加的文字'''
                        QMessageBox.information(self, '输入提示', tip_info, QMessageBox.Ok, QMessageBox.Ok)



            elif shape == '轨迹':
                if self.var_6_drawing_state == 1:
                    self.painter_6_pix.setPen(self.pen_6)
                    self.painter_6_pix.drawLine(self.point_6_start, self.point_6_end)
                    self.label_6_drawing.setPixmap(self.pix_6)
                    self.point_6_start = self.point_6_end
                elif self.var_6_drawing_state == 2:
                    self.var_6_drawing_state = 0

            elif shape == '文字':
                if self.var_6_drawing_state == 1:
                    pp_temp.drawText(self.point_6_end, self.lnedit_6_input.text())
                    self.label_6_drawing.setPixmap(pix_temp)
                if self.var_6_drawing_state == 2:
                    self.painter_6_pix.drawText(self.point_6_end, self.lnedit_6_input.text())
                    self.var_6_drawing_state = 0


            elif shape == '测试':
                path = QPainterPath()
                path.addRect(50, 50, 300, 300)
                path.addRect(100, 100, 200, 200)
                path.addEllipse(150, 150, 60, 80)
                pp_temp.setBrush(QtCore.Qt.blue)
                path.setFillRule(QtCore.Qt.OddEvenFill)
                if self.var_6_drawing_state == 1:
                    pp_temp.drawPath(path)
                    self.label_6_drawing.setPixmap(pix_temp)
                elif self.var_6_drawing_state == 2:
                    self.painter_6_pix.setBrush(QtCore.Qt.blue)
                    self.painter_6_pix.drawPath(path)
                    self.var_6_drawing_state = 0


            if self.var_6_drawing_state == 0:
                self.label_6_drawing.setPixmap(self.pix_6)
            # 删除临时绘图
            del pp_temp
        ## 背景图片
        pp_background = QPainter(self)
        pix_background = QPixmap(r'E:\Python\代码\XiaoU\b_packages\ico\b7.jpg')
        pp_background.drawPixmap(self.rect(), pix_background)


    def resizeEvent_drawing(self, QResizeEvent):

        # self.drawing_rect = [QPoint(x,y) for x in range(20, 20 + self.label_6_drawing.width())
        #                       for y in range(105, self.height())]
        self.drawing_rect = [QPoint(x, y) for x in range(22, self.width())
                             for y in range(95, self.height())]


    def wheelEvent_drawing(self, QWheelEvent):
        if (QWheelEvent.pos() in self.drawing_rect) and self.tabWidget.currentIndex() == 4:
            delta = QWheelEvent.angleDelta()
            if int(delta.y()) > 0:
                self.btn_zoomout_clicked()
            elif int(delta.y()) < 0:
                self.btn_zoomin_clicked()


    def mousePressEvent_drawing(self, event):
        # 画图
        if (event.button() == QtCore.Qt.LeftButton) and (event.pos() in self.drawing_rect) and self.tabWidget.currentIndex() == 4: # 当前界面为当前窗口生效
            self.var_6_drawing_state = 1
            self.point_6_start = event.pos() - self.pix_6_offset
            self.point_6_end = self.point_6_start
            self.tab_6.setMouseTracking(True)
        # 画板移动
        elif (event.button() == QtCore.Qt.MidButton) and (event.pos() in self.drawing_rect) and self.tabWidget.currentIndex() == 4:
            self.pix_6_move = 1
            self.label_6_drawing_pos = event.globalPos() - self.label_6_drawing.pos()  # 获取鼠标相对窗口的位置
            self.mouse_6_pos = event.globalPos()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseDoubleClickEvent_drawing(self, QMouseEvent):
        if (QMouseEvent.button() == QtCore.Qt.MidButton) and (QMouseEvent.pos() in self.drawing_rect) and self.tabWidget.currentIndex() == 4:
            del self.painter_6_pix
            self.pix_6_size_w = 666
            self.pix_6_size_h = 375
            self.pix_6_offset = QPoint(22,95)
            img_temp = self.pix_6.copy()
            pix_temp = QPixmap(self.pix_6_size_w, self.pix_6_size_h)
            pp_temp = QPainter(pix_temp)
            pp_temp.drawPixmap(0, 0, self.pix_6_size_w, self.pix_6_size_h, img_temp)
            self.label_6_drawing.setFixedSize(QtCore.QSize(self.pix_6_size_w,self.pix_6_size_h))
            self.label_6_drawing.show()
            self.pix_6 = pix_temp.copy()
            self.painter_6_pix = QPainter(self.pix_6)
            self.label_6_drawing.setPixmap(self.pix_6)
            del pp_temp
        elif (QMouseEvent.button() == QtCore.Qt.LeftButton) and (QMouseEvent.pos() in self.drawing_rect) and self.tabWidget.currentIndex() == 4:
            # 让多边形闭合
            if self.var_6_polygon == 1:
                self.painter_6_pix.setPen(self.pen_6)
                self.painter_6_pix.drawLine(self.var_6_polygon_next, self.var_6_polygon_start)
                self.label_6_drawing.setPixmap(self.pix_6)
                self.var_6_drawing_state = 0
                self.var_6_polygon = 0

    def mouseMoveEvent_drawing(self, QMouseEvent):
        # print('aa')
        # 画图
        if self.var_6_drawing_state == 1:
            self.point_6_end = QMouseEvent.pos() - self.pix_6_offset
            self.update()
        # 画板移动
        elif (QMouseEvent.pos() in self.drawing_rect) and self.tabWidget.currentIndex() == 4 and  self.pix_6_move == 1:
            self.label_6_drawing.move(QMouseEvent.globalPos() - self.label_6_drawing_pos)
            QMouseEvent.accept()

    def mouseReleaseEvent_drawing(self, QMouseEvent):

        # 画图
        if QMouseEvent.button() == QtCore.Qt.LeftButton and self.var_6_drawing_state == 1:
            self.point_6_end = QMouseEvent.globalPos() - self.pos() - self.pix_6_offset
            self.update()
            self.var_6_drawing_state = 2
        # 画板移动
        elif (QMouseEvent.button() == QtCore.Qt.MidButton) and (QMouseEvent.pos() in self.drawing_rect) and self.tabWidget.currentIndex() == 4 and self.pix_6_move == 1:
            self.pix_6_offset += (QMouseEvent.globalPos() - self.mouse_6_pos)
            self.pix_6_move = 0

class Clock(Ui_Form):
    def __init__(self):
        super(Clock, self).__init__()
        self.init_8_tab()
        self.init_8_layout()
        self.init_8_event()


    def init_8_tab(self):
        self.tab_8 = QtWidgets.QTabWidget()
        self.tab_8.setObjectName('tab_8')
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_8.setObjectName('gridLayout_8')
        self.tabWidget.addTab(self.tab_8, '时钟')

        self.cm_8_clock = QtWidgets.QComboBox()
        self.cm_8_clock.setObjectName('cm_8_clock')
        self.cm_8_clock.setFixedSize(QtCore.QSize(60,25))
        cm_8_clock = ['闹钟']
        self.cm_8_clock.addItems(cm_8_clock)
        self.label_8_view = QLabel()
        self.label_8_view.setObjectName('label_8_view')
        self.lnedit_8_input = QtWidgets.QLineEdit()
        self.lnedit_8_input.setObjectName('lnedit_8_input')
        self.lnedit_8_input.setText('请输入6位时间（如：131420）！')
        self.btn_8_ok = QtWidgets.QPushButton()
        self.btn_8_ok.setObjectName('btn_8_ok')
        self.btn_8_ok.setText('确认')

        self.timer_8_clock = QtCore.QTimer()


    def init_8_layout(self):
        self.gridLayout_8.addWidget(self.cm_8_clock, 0,0,1,1)
        self.gridLayout_8.addWidget(self.lnedit_8_input, 0,1,1,1)
        self.gridLayout_8.addWidget(self.btn_8_ok, 0,2,1,1)
        self.gridLayout_8.addWidget(self.label_8_view, 1,0,1,3)

    def init_8_var(self):
        self.var_8_clock = 0
        self.var_8_clock_time = 0

    def init_8_event(self):
        self.btn_8_ok.clicked.connect(self.btn_8_ok_clicked)

    def btn_8_ok_clicked(self):

        func = self.cm_8_clock.currentText()
        if func == '闹钟':

            self.var_8_clock_time = self.lnedit_8_input.text()
            self.var_8_clock = 1
            self.timer_8_clock.timeout.connect(self.clock)
        self.timer_8_clock.start(100)


    def clock(self):
        if self.var_8_clock == 1:
            conf = self.var_8_clock_time
            if len(conf) == 6 and int(conf[:2]) < 24 and int(conf[2:4]) < 60 and int(conf[4:6]) < 60:
                self.label_8_view.setText('正在等待时间到达...')
                if time.strftime('%H%M%S', time.localtime()) < conf:
                    conf_ = int(conf[:2]) * 3600 + int(conf[2:4]) * 60 + int(conf[4:6])
                    now = time.strftime('%H%M%S', time.localtime())
                    now = int(now[:2]) * 3600 + int(now[2:4]) * 60 + int(now[4:6])
                    last = int(conf_) - int(now)
                    self.label_8_view.setText('距离预订时间-{}-还剩-{} 秒'.format(conf,last))
                else:
                    self.label_8_view.setText('{}-时间到了'.format(conf))
                    self.play_common_list.addMedia(QMediaContent(QUrl.fromLocalFile(r'./PConfig/PClock.wav')))
                    self.play_common_player.play()
                if self.play_common_player.position() == self.play_common_player.duration() and self.play_common_player.position() != 0:
                    self.var_8_clock = 0
                    self.timer_8_clock.stop()
                    self.play_common_player.stop()
                    self.play_common_list.clear()
                    self.label_8_view.setText('Success')
            else:
                self.label_8_view.setText('请输入6位时间（如：131420）！')
                self.var_8_clock = 0


class Main(Clock, Opencv, Drawing):
    def __init__(self):
        super(Main, self).__init__()
        self.init_Style_sheet()


    def init_Style_sheet(self):
        # 主窗口布局风格
        # 窗口透明度
        #self.setWindowOpacity(0.99)
        #self.tabWidget.setWindowOpacity(0.5)

        self.gridLayout.setSpacing(2)
        self.gridLayout_1.setSpacing(2)
        self.gridLayout_2.setSpacing(2)
        # self.gridLayout_3.setSpacing(2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_6.setSpacing(2)



        qss_main = open('{}/xiaou.qss'.format(here_dic), 'r').read()

        self.setStyleSheet(qss_main)

        # *********====================+++++++++++++++++++++++++++++++++********
        # ********************************************************************


    def resizeEvent(self, QResizeEvent):
        self.resizeEvent_base(QResizeEvent)
        self.resizeEvent_drawing(QResizeEvent)

    def mousePressEvent(self, event):
        self.mousePressEvent_base(event)
        self.mousePressEvent_drawing(event)


    def mouseMoveEvent(self, QMouseEvent):
        self.mouseMoveEvent_base(QMouseEvent)
        self.mouseMoveEvent_drawing(QMouseEvent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouseReleaseEvent_base(QMouseEvent)
        self.mouseReleaseEvent_drawing(QMouseEvent)

    def wheelEvent(self, QWheelEvent):
        self.wheelEvent_drawing(QWheelEvent)

    def mouseDoubleClickEvent(self, QMouseEvent):
        self.mouseDoubleClickEvent_drawing(QMouseEvent)




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()

    ui.show()
    sys.exit(app.exec_())
