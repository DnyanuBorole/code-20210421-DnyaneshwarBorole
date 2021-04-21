from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sys

health_risks = {'Underweight': 'Malnutrition risk',
                'Normal weight': 'Low risk',
                'Overweight': 'Enhanced risk',
                'Moderately obese': 'Medium risk',
                'Severely obese': 'High risk',
                'Very severely obese': 'Very high risk'}
Category = ['Underweight','Normal weight','Overweight','Moderately obese','Severely obese','Very severely obese']

class Ui_Dialog(object):
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Warning)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()

    def clear(self):
        self.viewdata.clear()
        self.healthrisk.clear()
        self.NoP.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def view(self):
        try:
            peoples = open('../Calculator/Peoples.json')
            data = json.load(peoples)
            # print(data)
            for persons in data['Peoples']:
                self.viewdata.append(str(persons))
        except Exception as e:
            print("err" + e.args[0])
            tb = sys.exc_info()[2]
            print("ln no :", tb.tb_lineno)

    def JsonCalc(self, count):

        try:
            peoples = open('../Calculator/Peoples.json')
            data = json.load(peoples)
            count = 0
            for person in data['Peoples']:
                weight = float(person['WeightKg'])
                height = float(person['HeightCm'])
                ID = str(person['Id'])
                bmi = (weight / (height * height) * 10000)
                # print(bmi)

                if bmi <= 24.9:
                    # print('Your BMI is', bmi, 'which means you are Underweight')
                    hr = health_risks["Underweight"]
                    self.healthrisk.append(ID)
                    self.healthrisk.append(Category[0])
                    self.healthrisk.append(health_risks["Underweight"])

                elif 25 < bmi < 29.9:
                    # print('your BMI is', bmi, ' which means you are Normal weight')
                    self.healthrisk.append(ID)
                    self.healthrisk.append(Category[1])
                    self.healthrisk.append(health_risks["Normal weight"])
                    # print("Low risk")
                elif 30 < bmi < 34.9:
                    # print('your BMI is', bmi, ' which means you are Overweight')
                    self.healthrisk.append(ID)
                    self.healthrisk.append(Category[2])
                    self.healthrisk.append(health_risks["Overweight"])
                    # print("Enhanced risk")
                    count = count + 1
                elif 35 < bmi < 39.9:
                    # print('your BMI is', bmi, ' which means you are Moderately obese')
                    self.healthrisk.append(ID)
                    self.healthrisk.append(Category[3])
                    self.healthrisk.append(health_risks["Moderately obese"])
                    # print("Medium risk")
                elif bmi > 40:
                    # print('Your BMI is', bmi, 'which means you are Severely obese')
                    self.healthrisk.append(ID)
                    self.healthrisk.append(Category[4])
                    self.healthrisk.append(health_risks["Severely obese"])
                    # print("High risk")
            print(count)
            return count

        except Exception as e:
            print("err :" + e.args[0])
            tb = sys.exc_info()[1]
            print("ln no :", tb.tb_lineno)

    def owt(self, count):
        OWP = self.JsonCalc(count)
        self.NoP.setNum(OWP)

    def calculate(self, bmi):
        try:

            wt = self.lineEdit.text()
            print(wt)
            ht = self.lineEdit_2.text()
            print(ht)
            if wt == "" or wt == "null" or ht == "" or ht == "null":
                self.alertmsg("Error", "Please Enter Weight And Height")
            else:
                calculation = (int(wt) / (int(ht) * int(ht)) * 10000)
                print(float(calculation))
                self.viewdata.append(str(calculation))
                if calculation <= 24.9:
                    # print('Your BMI is', calculation, 'which means you are Underweight')
                    self.healthrisk.append(Category[0])
                    self.healthrisk.append(health_risks["Underweight"])
                elif 25 < calculation < 29.9:
                    # print('your BMI is', calculation, ' which means you are Normal weight')
                    self.healthrisk.append(Category[1])
                    self.healthrisk.append(health_risks["Normal weight"])

                    # print("Low risk")
                elif 30 < calculation < 34.9:
                    # print('your BMI is', bmi, ' which means you are Overweight')
                    # print("Enhanced risk")
                    self.healthrisk.append(Category[2])
                    self.healthrisk.append(health_risks["Overweight"])
                    self.alertmsg("Alert", "You are Overweight")
                elif 35 < calculation < 39.9:
                    # print('your BMI is', calculation, ' which means you are Moderately obese')
                    # print("Medium risk")
                    self.healthrisk.append(Category[3])
                    self.healthrisk.append(health_risks["Moderately obese"])

                elif calculation > 40:
                    # print('Your BMI is', calculation, 'which means you are Severely obese')
                    # print("High risk")
                    self.healthrisk.append(Category[4])
                    self.healthrisk.append(health_risks["Severely obese"])
                    self.alertmsg("Alert","You are in High Risk")
        except Exception as e:
            print("err" + e.args[0])
            tb = sys.exc_info()[2]
            print("ln no :", tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(809, 560)
        Dialog.setStyleSheet(
            "QDialog{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 164, 155, 255));}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(207, 207, 207, 255));")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.viewdata = QtWidgets.QTextBrowser(Dialog)
        self.viewdata.setGeometry(QtCore.QRect(20, 60, 431, 201))
        self.viewdata.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 9pt \"Arial\";")
        self.viewdata.setFrameShape(QtWidgets.QFrame.Box)
        self.viewdata.setFrameShadow(QtWidgets.QFrame.Plain)
        self.viewdata.setLineWidth(2)
        self.viewdata.setObjectName("viewdata")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(200, 79, 97);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 270, 141, 31))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(200, 79, 97);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(200, 79, 97);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 350, 471, 181))
        self.frame.setStyleSheet("background-color: rgb(251, 233, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(28, 57, 151, 31))
        self.lineEdit.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(268, 57, 151, 31))
        self.lineEdit_2.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(210, 60, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(48, 31, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(290, 31, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(158, 137, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(124, 134, 200);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 310, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(510, 340, 271, 191))
        self.frame_2.setStyleSheet(
            "QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 156, 184, 255));}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.NoP = QtWidgets.QLabel(self.frame_2)
        self.NoP.setGeometry(QtCore.QRect(80, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.NoP.setFont(font)
        self.NoP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NoP.setFrameShape(QtWidgets.QFrame.Box)
        self.NoP.setLineWidth(2)
        self.NoP.setText("")
        self.NoP.setAlignment(QtCore.Qt.AlignCenter)
        self.NoP.setObjectName("NoP")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 130, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color: rgb(124, 134, 200);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.healthrisk = QtWidgets.QTextBrowser(Dialog)
        self.healthrisk.setGeometry(QtCore.QRect(450, 60, 351, 201))
        self.healthrisk.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 12pt \"Arial\";")
        self.healthrisk.setFrameShape(QtWidgets.QFrame.Box)
        self.healthrisk.setFrameShadow(QtWidgets.QFrame.Plain)
        self.healthrisk.setLineWidth(2)
        self.healthrisk.setObjectName("healthrisk")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_5.clicked.connect(self.view)
        self.pushButton.clicked.connect(self.JsonCalc)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.calculate)
        self.pushButton_4.clicked.connect(self.owt)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BMI Calculator"))
        self.viewdata.setHtml(_translate("Dialog",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.viewdata.setPlaceholderText(_translate("Dialog", "Data"))
        self.pushButton.setText(_translate("Dialog", "Calculate"))
        self.pushButton_5.setText(_translate("Dialog", "View Data"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Weight(kg)"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Height(cm)"))
        self.label_3.setText(_translate("Dialog", "*"))
        self.label_4.setText(_translate("Dialog", "Enter Weight"))
        self.label_5.setText(_translate("Dialog", "Enter Height"))
        self.pushButton_3.setText(_translate("Dialog", "Calculate"))
        self.label_2.setText(_translate("Dialog", "Calculate BMI"))
        self.label_6.setText(_translate("Dialog", "Total No. of Overweighted\n"
                                                  "People\'s in our Data"))
        self.pushButton_4.setText(_translate("Dialog", "Get OverWeighted\n"
                                                       "People"))
        self.healthrisk.setHtml(_translate("Dialog",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.healthrisk.setPlaceholderText(_translate("Dialog", "Health Risk"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
