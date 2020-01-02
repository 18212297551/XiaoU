from base import *

class Camera(UiForm):
    def __init__(self):
        super(Camera, self).__init__()


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
