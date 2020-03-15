from XiaoU.base import *


# 音乐下载池
Queue_song = multiprocessing.Queue()
sum_songs = {}  # 搜索过的所有音乐信息

class Music(UiForm):
    def __init__(self):
        super(Music, self).__init__()
        global sum_songs
        self.sum_songs = sum_songs
        self.__init_tab2_ui__()

        self._down_song = Download_Song(self)
        self.listwidget_2_additems_lrc_thread = listwidget_2_additems_lrc()
        self._down_song.down_song_log.connect(self.msg)


    def __init_tab2_ui__(self):
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
        self.label_2_image = QLabel()
        # self.label_2_image.setMinimumSize(QtCore.QSize(300, 200))
        # self.label_2_image.setSizeIncrement(QtCore.QSize(20, 400))
        # self.label_2_image.setBaseSize(QtCore.QSize(758, 404))
        self.label_2_image.setObjectName("label_2_image")
        self.gridLayout_2.addWidget(self.label_2_image, 0, 0, 1, 5)
        # 将tab2加入tabwidgte
        self.tabWidget.addTab(self.tab_2, "听曲")




    def input_send_2_clicked(self):
        send2 = self.lnedit_2_input.text()
        if not send2 == '':
            for i in range(1, 6):
                self.get_song(send2, i)
            self.lnedit_2_input.clear()
        else:
            self.msg('请输入需要查找的歌曲名')

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