from XiaoU.base import *


class Browser(UiForm):
    def __init__(self):
        super(Browser, self).__init__()
        self.__init_tab3_ui__()

    def __init_tab3_ui__(self):
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
