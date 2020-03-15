from XiaoU.base import *

video_items = {}  # 搜索过的所有视频信息


class Video(UiForm):
    def __init__(self):
        super(Video, self).__init__()
        self.player_5_list_Mode = 1
        self.listwidget_5_list_state = 1
        self.__init_tab5_ui__()
    def __init_tab5_ui__(self):
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

