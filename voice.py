from base import *


syn_items = {}
asr_items = {}

# 语音合成线程池
Queue_speech = multiprocessing.Queue()
# 语音识别线程池
Queue_ASR = multiprocessing.Queue()


class Voice(UiForm):
    def __init__(self):
        super(Voice, self).__init__()
        """
        语音合成、识别
        """
        self.__init_tab4_ui__()
        self.__init_tab4_event__()
        self.voice_ars = Voice_recognition(self)
        self.speech_syn = Speech_synthesis(self)
        self.speech_syn.speech_synthesis_log.connect(self.speech_syn_log_deal)
        self.voice_ars.asr_result.connect(self.voice_asr_result_deal)
    def __init_tab4_ui__(self):
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
        # self.cmbox_4_tool.setMinimumSize(QtCore.QSize(60, 25))
        self.gridLayout_4.addWidget(self.cmbox_4_tool, 0, 0, 1, 2)
        tool = ['语音合成', '语音识别']
        self.cmbox_4_tool.addItems(tool)

        # 语音合成参数
        # 发音人
        cm_6_per = ['普通女声', '普通男生', '成熟女性', '成熟男声', '度逍遥', '度丫丫']
        self.cmbox_4_per = QtWidgets.QComboBox(self.tab_4)
        self.cmbox_4_per.setObjectName('cmbox_4_per')
        self.cmbox_4_per.setFixedSize(QtCore.QSize(85, 25))
        # self.cmbox_4_per.setMinimumSize(QtCore.QSize(60, 25))
        self.cmbox_4_per.addItems(cm_6_per)
        self.gridLayout_4.addWidget(self.cmbox_4_per, 1, 0, 1, 1)
        # 格式
        self.cmbox_4_aue = QtWidgets.QComboBox(self.tab_4)
        self.cmbox_4_aue.setObjectName('cmbox_4_aue')
        self.cmbox_4_aue.setMaximumSize(QtCore.QSize(70, 25))
        self.cmbox_4_aue.setMinimumSize(QtCore.QSize(45, 25))
        cm_6_aue = ["wav", "mp3", "pcm-16k"]  # "pcm-8k",
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
    def __init_tab4_event__(self):
        # tab4 事件
        self.btn_4_ok.clicked.connect(self.btn_4_ok_clicked)
        self.btn_4_clear.clicked.connect(self.btn_4_clear_clicked)
        self.btn_4_clear.clicked.connect(self.play_common_stop)
        self.listWidget_4_used_info.clicked.connect(self.listWidget_4_used_info_clicked)
        self.listWidget_4_used_info.doubleClicked.connect(self.listWidget_4_used_info_doubleclicked)
        self.cmbox_4_tool.currentTextChanged.connect(self.cmbox_4_tool_currentTextChanged)
        self.btn_4_folder.clicked.connect(self.open_folder)

        # tab4 结束》》》》》》》》》》》》》》

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

