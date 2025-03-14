# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enigma_facts.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: #0D1B2B ;")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setWindowTitle("Enigma Machine")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 181, 41))
        self.label.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 250, 201, 41))
        self.label_2.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 371, 61))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 390, 371, 31))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 430, 371, 61))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 320, 181, 171))
        self.label_3.setStyleSheet("background-color: rgb(28, 38, 61);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/CoDWWII_Enigma_0.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 320, 181, 171))
        self.label_4.setStyleSheet("background-color: rgb(28, 38, 61);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/DrSTONE_Enigma_0.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 500, 181, 31))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(600, 500, 181, 31))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 80, 371, 61))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 160, 371, 71))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(400, 80, 381, 61))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(400, 160, 381, 71))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("background-color: rgb(28, 38, 61);\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enigma Facts"))
        self.label_2.setText(_translate("MainWindow", "Références dans la pop culture"))
        self.label_5.setText(_translate("MainWindow", "Dans les jeux vidéos, Enigma est pas mal référencée. C\'est le cas dans le jeu Call of duty : WWII, où une mission du jeu fait référence au vol d\'une machine Enigma. C\'est aussi le cas pour le fameux jeu Wolfenstein : The New Order où une quête incluant un décryptage de code grâce à la machine Enigma  "))
        self.label_6.setText(_translate("MainWindow", "A noter que les designs sont un peu différents du design historique dans le but d\'adapter la machine au plaisir et au confort des joueurs"))
        self.label_7.setText(_translate("MainWindow", "La machine Enigma est aussi représentée dans la litérature avec des récits historique comme Cryptonomicon de Neal Stephenson. La machine Enigma est aussi utilisée dans l\'anime Dr. STONE par Inagaki & Boichi "))
        self.label_8.setText(_translate("MainWindow", "Enigma dans Call of Duty : WWII"))
        self.label_9.setText(_translate("MainWindow", "Enigma dans Dr.STONE"))
        self.label_10.setText(_translate("MainWindow", "Des millions de combinaisons possibles : Enigma utilisait plusieurs rotors et câblages interchangeables, offrant environ 150 quintillons (10^18) de configurations possibles, rendant son code extrêmement difficiles a craquer "))
        self.label_11.setText(_translate("MainWindow", "Les opérateurs allemands utilisaient souvent des phrases prévisibles comme : \" Heil Hitler \" ou des noms courants dans leurs messages"))
        self.label_12.setText(_translate("MainWindow", "Certaines machines Enigma ont été vendues à d\'autres pays par les soldats allemands après la fin de la guerre, sans qu\'ils sachent que les Alliés savaient déjà la déchiffrer. Cette erreur a permis aux Alliés d\'intercepter des communications italiennes et japonaises"))
        self.label_13.setText(_translate("MainWindow", "En 2017, une machine Enigma a été achetée pour 45 000 € lors d\'une vente aux enchères en Roumanie... après avoir été trouvée dans un marché aux puces !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
