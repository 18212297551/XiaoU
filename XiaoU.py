import sys

from PyQt5.QtWidgets import QApplication
from base import *
from chat import Chat
from music import Music
from video import Video
from voice import Voice
from draw import Draw
from clock import Clock
from camera import Camera

class Main(Clock,Camera,Draw,Voice,Video,Music,Chat):
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

        self.retranslateUi()


        qss_main = open(r'XiaoU/xiaou.qss', 'r').read()

        self.setStyleSheet(qss_main)


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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())