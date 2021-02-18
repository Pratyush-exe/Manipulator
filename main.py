from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PIL import ImageOps
from PIL import Image
import webbrowser
import PIL
import os


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()

        self.website = "https://github.com/Pratyush-exe"
        self.done = None
        self.temp = None
        self.path = None

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 710)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 130, 641, 321))
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

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 342, 321, 31))
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
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit_2.setPalette(palette)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.image_area = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image_area.setGeometry(QtCore.QRect(0, 0, 641, 321))
        self.image_area.setFixedWidth(641)
        self.image_area.setText("")
        self.image_area.setScaledContents(True)
        self.verticalLayout.addWidget(self.image_area)
        self.image_area.setObjectName("image_area")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(10, 580, 641, 61))
        self.about_button.setObjectName("about_button")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 550, 501, 30))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.quality_display_text = QtWidgets.QLabel(self.centralwidget)
        self.quality_display_text.setGeometry(QtCore.QRect(520, 540, 121, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.quality_display_text.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quality_display_text.setFont(font)
        self.quality_display_text.setObjectName("quality_display_text")

        self.done_Button = QtWidgets.QPushButton(self.centralwidget)
        self.done_Button.setGeometry(QtCore.QRect(10, 600, 641, 61))
        self.done_Button.setObjectName("done_Button")

        self.gray_background = QtWidgets.QLabel(self.centralwidget)
        self.gray_background.setGeometry(QtCore.QRect(0, -5, 661, 721))
        self.gray_background.setText("")
        self.gray_background.setPixmap(QtGui.QPixmap(r"img_data/background.png"))
        self.gray_background.setScaledContents(True)
        self.gray_background.setAlignment(QtCore.Qt.AlignCenter)
        self.gray_background.setObjectName("gray_background")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 500, 501, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.choose_img_button = QtWidgets.QPushButton(self.centralwidget)
        self.choose_img_button.setGeometry(QtCore.QRect(520, 500, 121, 31))
        self.choose_img_button.setObjectName("choose_img_button")

        self.imgDetails_button = QtWidgets.QPushButton(self.centralwidget)
        self.imgDetails_button.setGeometry(QtCore.QRect(130, 460, 111, 28))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.imgDetails_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.imgDetails_button.setFont(font)
        self.imgDetails_button.setFlat(True)
        self.imgDetails_button.setObjectName("imgDetails_button")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 452, 321, 31))
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
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit_2.setPalette(palette)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(434, 470, 211, 21))
        self.loading.setText("")
        self.loading.setObjectName("loading")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 460, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.checkBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(120, 20, 421, 81))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img_data/manipulator.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setGeometry(QtCore.QRect(522, 670, 131, 28))
        self.about_button.setObjectName("about_button")

        self.gray_background.raise_()
        self.frame.raise_()
        self.about_button.raise_()
        self.done_Button.raise_()
        self.lineEdit.raise_()
        self.choose_img_button.raise_()
        self.imgDetails_button.raise_()
        self.lineEdit_2.raise_()
        self.logo.raise_()
        self.checkBox.raise_()
        self.quality_display_text.raise_()
        self.horizontalSlider.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.choose_img_button.clicked.connect(self.file_dialogue)
        self.imgDetails_button.clicked.connect(self.img_details)
        self.done_Button.clicked.connect(self.Done)
        self.about_button.clicked.connect(lambda: webbrowser.open_new(self.website))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
            msg.setText("Image size: " + str(w) + "x" + str(h) + "\nFile Size: " + str(os.path.getsize(det)/1024) + " KB")
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

    def file_dialogue(self):

        while True:
            self.path, _ = QtWidgets.QFileDialog.getOpenFileName()
            x = self.path.split(".")
            y = self.path.split(".")
            self.lineEdit_2.setText("No Image")

            if (x[-1] == "jpeg") or (x[-1] == "png") or (x[-1] == "jpg"):
                self.lineEdit.setText(self.path)
                img = Image.open(self.path)
                self.temp = y[-2] + "_temp." + x[-1]
                img.save(self.temp)
                img.thumbnail((300, 300))
                w, h = img.size
                if h < w:
                    self.image_area.setFixedHeight(321)
                else:
                    self.image_area.setFixedHeight(700)

                self.image_area.setPixmap(QtGui.QPixmap(self.temp))
                os.remove(self.temp)
                self.lineEdit_2.setText("Image might look distorted but output wont")
                break

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.done_Button.setText(_translate("MainWindow", "DONE"))
        self.choose_img_button.setText(_translate("MainWindow", "Choose Image"))
        self.imgDetails_button.setText(_translate("MainWindow", "Image Details"))
        self.lineEdit_2.setText(_translate("MainWindow", "No Image"))
        self.checkBox.setText(_translate("MainWindow", "GrayScale"))
        self.about_button.setText(_translate("MainWindow", "About"))
        self.quality_display_text.setText(_translate("MainWindow", "QUALITY\nREDUCTION"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon(r"img_data/icon.ico"))
    MainWindow.setWindowTitle("Manipulator")
    MainWindow.show()
    sys.exit(app.exec_())
