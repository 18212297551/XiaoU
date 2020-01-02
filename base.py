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
from PyQt5.QtWidgets import QMessageBox, QWidget, QLabel, QSpinBox, QSlider, QColorDialog, QApplication
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
                _t = '[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ']'
                content = "\n{}\n{}\n".format(_t,_error)
                _f.write(content)
                print(_error)
    return wrapper

class UiForm(QWidget):  # QMainWindow

    def __init__(self):
        super(UiForm, self).__init__()  # ,QtCore.Qt.FramelessWindowHint

        self.initDrag()
        self.player_2_list_Mode = 1



        # 窗口初始化
        self.init_mainwindow()

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


        ## 主布局
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 12)
        self.setLayout(self.gridLayout)
        self.tabWidget.setCurrentIndex(0)








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



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = UiForm()

    ui.show()
    sys.exit(app.exec_())
