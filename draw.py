from base import *

class Draw(UiForm):
    def __init__(self):
        super(Draw, self).__init__()
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

        self.pix_6_offset = QtCore.QPoint(22, 95)

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

        self.pix_6_offset = QtCore.QPoint(22, 95)
        self.pix_6_move = 0
        self.pix_6_size_h = 400
        self.pix_6_size_w = self.pix_6_size_h*(16/9)

        self.label_6_drawing = QLabel()
        self.label_6_drawing.setObjectName('label_6_drawing')
        self.label_6_drawing.setStyleSheet('QLabel{background-color:blue}')

        self.label_6_drawing.setFixedSize(QtCore.QSize(self.pix_6_size_w, self.pix_6_size_h))
        self.gridLayout_6.addWidget(self.label_6_drawing, 1, 0, 1, 14)
        self.pix_6 = QPixmap(self.label_6_drawing.width(), self.label_6_drawing.height())
        self.draw_old_pic = self.pix_6
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
        print(self.label_6_drawing.size())


    def btn_zoomout_clicked(self):
        del self.painter_6_pix
        self.pix_6_size_h += 5
        self.pix_6_size_w = self.pix_6_size_h*(16/9)
        img_temp = self.draw_old_pic.copy()
        pix_temp = QPixmap(self.pix_6_size_w, self.pix_6_size_h)
        pp_temp = QPainter(pix_temp)
        pp_temp.drawPixmap(0, 0, self.pix_6_size_w, self.pix_6_size_h, img_temp)
        self.label_6_drawing.setFixedSize(QtCore.QSize(self.pix_6_size_w,self.pix_6_size_h))
        self.label_6_drawing.show()
        self.pix_6 = pix_temp.copy()
        self.painter_6_pix = QPainter(self.pix_6)
        self.label_6_drawing.setPixmap(self.pix_6)
        del pp_temp

        print(self.label_6_drawing.size())


    def btn_zoomin_clicked(self):
        del self.painter_6_pix
        self.pix_6_size_h -= 5
        self.pix_6_size_w = self.pix_6_size_h*(16/9)
        img_temp = self.draw_old_pic.copy()
        pix_temp = QPixmap(self.pix_6_size_w, self.pix_6_size_h)
        pp_temp = QPainter(pix_temp)
        pp_temp.drawPixmap(0, 0, self.pix_6_size_w, self.pix_6_size_h, img_temp)
        self.label_6_drawing.setFixedSize(QtCore.QSize(self.pix_6_size_w,self.pix_6_size_h))
        self.label_6_drawing.show()
        self.pix_6 = pix_temp.copy()
        self.painter_6_pix = QPainter(self.pix_6)
        self.label_6_drawing.setPixmap(self.pix_6)
        del pp_temp
        print(self.label_6_drawing.size())


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
            self.draw_old_pic = self.pix_6.copy()
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
