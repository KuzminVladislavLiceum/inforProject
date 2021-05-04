import requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
from PIL import Image
import os.path


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("")
        mainLayout = QHBoxLayout(self)
        vLayout1 = QVBoxLayout(self)
        vLayout2 = QVBoxLayout(self)
        mainLayout.setSizeConstraint(mainLayout.SetFixedSize)
        self.inputText = QLabel('Введите ссылку на фото')
        self.inputLink = QLineEdit(self)
        self.inputText2 = QLabel('Введите имя фото')
        self.inputName = QLineEdit(self)
        self.inputBtn = QPushButton('OK')
        vLayout1.addWidget(self.inputText)
        vLayout1.addWidget(self.inputLink)
        vLayout1.addWidget(self.inputText2)
        vLayout1.addWidget(self.inputName)
        vLayout1.addWidget(self.inputBtn)
        self.selectFileBtn = QPushButton('Выбрать фото')
        self.hText = QLabel('Введите высоту фото')
        self.h = QLineEdit(self)
        self.wText = QLabel('Введите ширину фото')
        self.w = QLineEdit(self)
        self.newNameText = QLabel('Введите новое название фото')
        self.newName = QLineEdit(self)
        self.okBtn = QPushButton('OK')
        vLayout2.addWidget(self.selectFileBtn)
        vLayout2.addWidget(self.hText)
        vLayout2.addWidget(self.h)
        vLayout2.addWidget(self.wText)
        vLayout2.addWidget(self.w)
        vLayout2.addWidget(self.newNameText)
        vLayout2.addWidget(self.newName)
        vLayout2.addWidget(self.okBtn)
        mainLayout.addLayout(vLayout1)
        mainLayout.addLayout(vLayout2)
        self.inputBtn.clicked.connect(self.inputBtnClicked1)
        self.selectFileBtn.clicked.connect(self.inputBtnClicked2)
        self.okBtn.clicked.connect(self.inputBtnClicked3)

    def inputBtnClicked1(self):
        try:
            self.folder = QFileDialog.getExistingDirectory(
                self, "Выбрать папку", ".")
            url = self.inputLink.text()
            r = requests.get(url)
            with open(f'{self.folder}/{self.inputName.text()}.jpg', 'wb') as f:
                f.write(r.content)
        except:
            ew.show()

    def inputBtnClicked2(self):
        try:
            self.fileName = QFileDialog.getOpenFileName(
                self, "Выбрать файл", ".")
        except:
            ew.show()

    def inputBtnClicked3(self):
        try:
            self.folder1 = QFileDialog.getExistingDirectory(
                self, "Выбрать папку", ".")
            im = Image.open(self.fileName[0])
            out = im.resize((int(self.w.text()), int(self.h.text())))
            print(self.fileName[0])
            self.d = ''
            if self.newName.text() == '':
                self.d = self.fileName[0].split('/')[-1]
            if self.w.text() == '':
                self.w = im.size()[0]
            if self.h.text() == '':
                self.h = im.size()[1]
            else:
                if os.path.exists(f'{self.newName.text()}.jpg') is True:
                    ew2.show()
                    if ew2.ans() is True:
                        self.d = self.newName.text()
                    else:
                        d = ''
                else:
                    self.d = self.newName.text()
            if self.d != '':
                out.save(f'{self.folder1}/{self.d}.jpg')
        except:
            ew.show()


class errorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Error")
        mainLayout = QVBoxLayout(self)
        mainLayout.setSizeConstraint(mainLayout.SetFixedSize)
        self.errorText = QLabel('При выполнении команды произошла ошибка')
        self.okBtn = QPushButton('OK')
        mainLayout.addWidget(self.errorText)
        mainLayout.addWidget(self.okBtn)
        self.okBtn.clicked.connect(self.BtnClicked)

    def BtnClicked(self):
        ew.hide()


class errorWindow2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.flag = False
        self.setWindowTitle("Error")
        mainLayout = QVBoxLayout(self)
        dLayout = QHBoxLayout(self)
        mainLayout.setSizeConstraint(mainLayout.SetFixedSize)
        self.errorText = QLabel('Файл с таким названием уже есть')
        self.okBtn1 = QPushButton('Заменить файл')
        self.okBtn2 = QPushButton('Назад')
        dLayout.addWidget(self.okBtn1)
        dLayout.addWidget(self.okBtn2)
        mainLayout.addWidget(self.errorText)
        mainLayout.addLayout(dLayout)
        self.okBtn1.clicked.connect(self.BtnClicked1)
        self.okBtn2.clicked.connect(self.BtnClicked2)

    def BtnClicked1(self):
        self.flag = True
        ew2.hide()

    def BtnClicked2(self):
        self.flag = False
        ew2.hide()

    def ans(self):
        return self.flag


app = QApplication([])
w = Window()
ew = errorWindow()
ew2 = errorWindow2()
w.show()
app.exec()
