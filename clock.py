from base import *

class Clock(UiForm):
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
