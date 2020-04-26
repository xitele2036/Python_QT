from PyQt5 import QtWidgets
from counter import Ui_Form
class MyWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)

    def Button_0(self):
        self.textBrowser.insertPlainText('0')

    def Button_1(self):
        self.textBrowser.insertPlainText('1')

    def Button_2(self):
        self.textBrowser.insertPlainText('2')

    def Button_3(self):
        self.textBrowser.insertPlainText('3')

    def Button_4(self):
        self.textBrowser.insertPlainText('4')

    def Button_5(self):
        self.textBrowser.insertPlainText('5')

    def Button_6(self):
        self.textBrowser.insertPlainText('6')

    def Button_7(self):
        self.textBrowser.insertPlainText('7')

    def Button_8(self):
        self.textBrowser.insertPlainText('8')

    def Button_9(self):
        self.textBrowser.insertPlainText('9')

    def Button_add(self):
        self.textBrowser.insertPlainText('+')

    def Button_sub(self):
        self.textBrowser.insertPlainText('-')

    def Button_mul(self):
        self.textBrowser.insertPlainText('*')

    def Button_div(self):
        self.textBrowser.insertPlainText('/')

    def Button_point(self):
        self.textBrowser.insertPlainText('.')

    def clear(self):
        self.textBrowser.clear()

    def equal(self):
        text = self.textBrowser.toPlainText()
        try:
            eval(text)
            self.textBrowser.setText(str(eval(text)))
        except:
            self.textBrowser.setText("请重新填写！感谢你的配合！！！")



if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())