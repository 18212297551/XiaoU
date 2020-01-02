from base import *






class Chat(UiForm):
    def __init__(self):
        super(Chat, self).__init__()
        self.__init_tab1_ui__()
        self.API = 'baidu'  # 定义机器人接口和默认值
        self.PER = 4  # 定义机器人语音人物
        self.PIT = 6  # 定义机器人语音音调
        self.friend_int = 0  # tab3图片播放序号
        self.info = {
            "apiKey": "9ad4e7ad478b4353a27aad1eab121d79",
            "userId": "15261800956"
        }

    def __init_tab1_ui__(self):
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

    def listWidget_1_additem(self, Text1):
        self.label_2_image.close()
        self.listWidget_1_1.show()
        self.listWidget_1_1.addItem(Text1)
        self.listWidget_1_1.scrollToBottom()
        # 歌曲获取

    

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
