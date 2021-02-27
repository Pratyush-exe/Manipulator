from PIL import ImageOps
from PIL import Image
import webbrowser
import PIL
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.website = "https://github.com/Pratyush-exe"
        self.done = None
        self.temp = None
        self.path = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(25, 155, 611, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 641, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.view_image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.view_image.setGeometry(QtCore.QRect(0, 0, 631, 321))
        self.view_image.setStyleSheet("background:white;")
        self.view_image.setText("")
        self.view_image.setScaledContents(True)
        self.verticalLayout.addWidget(self.view_image)
        self.view_image.setObjectName("view_image")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(128, 35, 421, 81))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img_data/manipulator.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.quality_label = QtWidgets.QLabel(self.centralwidget)
        self.quality_label.setGeometry(QtCore.QRect(530, 618, 121, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.quality_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quality_label.setFont(font)
        self.quality_label.setObjectName("quality_label")
        self.about_us = QtWidgets.QPushButton(self.centralwidget)
        self.about_us.setGeometry(QtCore.QRect(515, 778, 130, 31))
        self.about_us.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                    "border-radius: 12px;\n"
                                    "")
        self.about_us.setObjectName("about_us")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 628, 501, 30))
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.Done_button = QtWidgets.QPushButton(self.centralwidget)
        self.Done_button.setGeometry(QtCore.QRect(8, 691, 641, 61))
        self.Done_button.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                       "border-radius: 30px;\n"
                                       "")
        self.Done_button.setObjectName("Done_button")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 500, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.checkBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                    "border-radius: 10px;\n"
                                    "padding-left:10px;\n"
                                    "color: black;\n"
                                    "")
        self.checkBox.setObjectName("checkBox")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 701, 841))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("img_data/background.png"))
        self.background.setScaledContents(True)
        self.background.setAlignment(QtCore.Qt.AlignCenter)
        self.background.setObjectName("background")
        self.status = QtWidgets.QLineEdit(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(330, 502, 321, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.status.setPalette(palette)
        self.status.setInputMask("")
        self.status.setFrame(False)
        self.status.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.status.setObjectName("status")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 556, 511, 31))
        self.lineEdit.setStyleSheet("border-radius: 10px;"
                                    "padding-left: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.img_details = QtWidgets.QPushButton(self.centralwidget)
        self.img_details.setGeometry(QtCore.QRect(130, 500, 111, 28))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 242, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.img_details.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.img_details.setFont(font)
        self.img_details.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                       "border-radius: 10px;\n"
                                       "color: black;\n"
                                       "")
        self.img_details.setFlat(True)
        self.img_details.setObjectName("img_details")
        self.choose_image = QtWidgets.QLabel(self.centralwidget)
        self.choose_image.setGeometry(QtCore.QRect(530, 556, 121, 31))
        self.choose_image.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                        "border-radius: 10px;\n"
                                        "")
        self.choose_image.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_image.setObjectName("choose_image")
        self.Image_details_shadow = QtWidgets.QLabel(self.centralwidget)
        self.Image_details_shadow.setGeometry(QtCore.QRect(133, 502, 111, 31))
        self.Image_details_shadow.setStyleSheet("background-color: rgb(253, 209, 0);\n"
                                                "border-radius: 10px;\n"
                                                "")
        self.Image_details_shadow.setText("")
        self.Image_details_shadow.setAlignment(QtCore.Qt.AlignCenter)
        self.Image_details_shadow.setObjectName("Image_details_shadow")
        self.Checkbox_shadow = QtWidgets.QLabel(self.centralwidget)
        self.Checkbox_shadow.setGeometry(QtCore.QRect(13, 504, 111, 31))
        self.Checkbox_shadow.setStyleSheet("background-color: rgb(253, 209, 0);\n"
                                           "border-radius: 10px;\n"
                                           "")
        self.Checkbox_shadow.setText("")
        self.Checkbox_shadow.setAlignment(QtCore.Qt.AlignCenter)
        self.Checkbox_shadow.setObjectName("Checkbox_shadow")
        self.choose_image_shadow = QtWidgets.QLabel(self.centralwidget)
        self.choose_image_shadow.setGeometry(QtCore.QRect(533, 561, 121, 31))
        self.choose_image_shadow.setStyleSheet("background-color: rgb(253, 209, 0);\n"
                                               "border-radius: 10px;\n"
                                               "")
        self.choose_image_shadow.setText("")
        self.choose_image_shadow.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_image_shadow.setObjectName("choose_image_shadow")
        self.line_edit_shadow = QtWidgets.QLabel(self.centralwidget)
        self.line_edit_shadow.setGeometry(QtCore.QRect(13, 561, 511, 31))
        self.line_edit_shadow.setStyleSheet("background-color: rgb(253, 209, 0);\n"
                                            "border-radius: 10px;\n"
                                            "")
        self.line_edit_shadow.setText("")
        self.line_edit_shadow.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_shadow.setObjectName("line_edit_shadow")
        self.about_us_shadow = QtWidgets.QLabel(self.centralwidget)
        self.about_us_shadow.setGeometry(QtCore.QRect(517, 783, 131, 30))
        self.about_us_shadow.setStyleSheet("background-color: rgb(253, 209, 0);\n"
                                           "border-radius: 12px;\n"
                                           "")
        self.about_us_shadow.setText("")
        self.about_us_shadow.setAlignment(QtCore.Qt.AlignCenter)
        self.about_us_shadow.setObjectName("about_us_shadow")
        self.Done_shadow = QtWidgets.QLabel(self.centralwidget)
        self.Done_shadow.setGeometry(QtCore.QRect(12, 698, 641, 61))
        self.Done_shadow.setStyleSheet("background-color: rgb(253, 209, 0);\n"
                                       "border-radius: 30px;\n"
                                       "")
        self.Done_shadow.setText("")
        self.Done_shadow.setAlignment(QtCore.Qt.AlignCenter)
        self.Done_shadow.setObjectName("Done_shadow")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 160, 611, 311))
        self.label.setStyleSheet("background:rgb(253, 209, 0);")
        self.label.setObjectName("label")
        self.background.raise_()
        self.logo.raise_()
        self.quality_label.raise_()
        self.horizontalSlider.raise_()
        self.status.raise_()
        self.Image_details_shadow.raise_()
        self.img_details.raise_()
        self.Checkbox_shadow.raise_()
        self.checkBox.raise_()
        self.choose_image_shadow.raise_()
        self.choose_image.raise_()
        self.line_edit_shadow.raise_()
        self.lineEdit.raise_()
        self.about_us_shadow.raise_()
        self.about_us.raise_()
        self.Done_shadow.raise_()
        self.Done_button.raise_()
        self.label.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.choose_image.mousePressEvent = self.file_dialogue
        self.img_details.mousePressEvent = self.img_details
        self.Done_button.clicked.connect(self.Done)
        self.about_us.clicked.connect(lambda: webbrowser.open_new(self.website))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def img_details(self):

        if self.done:
            det = self.temp
        else:
            det = self.path

        print(det)
        if det is not None:
            img = Image.open(det)
            w, h = img.size
            per = self.horizontalSlider.value()
            per = per / 100
            h = int(h) * per
            w = int(w) * per
            size = (int(w), int(h))
            img.thumbnail(size)
            img.save(det)
            msg = QMessageBox()
            msg.setWindowTitle("Current Image Details")
            msg.setIcon(QMessageBox.Information)
            msg.setText(
                "Image size: " + str(w) + "x" + str(h) + "\nFile Size: " + str(os.path.getsize(det) / 1024) + " KB")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("First Choose an Image")
            msg.exec_()

    def Done(self):
        self.done = True
        if self.path is not None:
            per = self.horizontalSlider.value()
            per = 100 - per
            per = per / 100
            x = self.path.split(".")
            y = self.path.split("." + str(x[-1]))
            self.temp = str(y[0]) + "_temp." + str(x[-1])
            self.temp_img = Image.open(self.path)
            img = Image.open(self.path)
            img.save(self.temp)
            if self.checkBox.isChecked():
                img = PIL.ImageOps.grayscale(PIL.Image.open(self.temp))
                img.save(self.temp)

            w, h = img.size
            h = int(h) * per
            w = int(w) * per
            if h == 0:
                h = 1
            if w == 0:
                w = 1
            size = (int(w), int(h))
            img1 = Image.open(self.temp)
            img1.thumbnail(size)
            img1.save(self.temp)

            msg = QMessageBox()
            msg.setWindowTitle("Done")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Image manipulated!!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("First Choose an Image")
            msg.exec_()

    def file_dialogue(self, event):

        while True:
            self.path, _ = QtWidgets.QFileDialog.getOpenFileName()
            x = self.path.split(".")
            y = self.path.split(".")
            self.status.setText("No Image")

            if (x[-1] == "jpeg") or (x[-1] == "png") or (x[-1] == "jpg"):
                self.lineEdit.setText(self.path)
                img = Image.open(self.path)
                self.temp = y[-2] + "_temp." + x[-1]
                img.save(self.temp)
                img.thumbnail((300, 300))
                w, h = img.size
                if h < w:
                    self.view_image.setFixedHeight(h*2)
                    self.view_image.setFixedWidth(w*2)
                else:
                    self.view_image.setFixedHeight(h * 2)
                    self.view_image.setFixedWidth(w * 2)

                self.view_image.setPixmap(QtGui.QPixmap(self.temp))
                os.remove(self.temp)
                self.status.setText("Image might look distorted but output wont")
                break

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quality_label.setText(_translate("MainWindow", "QUALITY\n"
                                                            "REDUCTION"))
        self.about_us.setText(_translate("MainWindow", "About Us"))
        self.Done_button.setText(_translate("MainWindow", "DONE"))
        self.checkBox.setText(_translate("MainWindow", "GrayScale"))
        self.status.setText(_translate("MainWindow", "No Image"))
        self.img_details.setText(_translate("MainWindow", "Image Details"))
        self.choose_image.setText(_translate("MainWindow", "Choose Image"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon(r"img_data/icon.ico"))
    MainWindow.setWindowTitle("manipulator")
    MainWindow.show()
    sys.exit(app.exec_())
