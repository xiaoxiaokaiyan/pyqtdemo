from PyQt5.Qt import *
import  sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("demo")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        lable=QLabel()
        lable.setText("haha")


if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)

    window=Window()
    window.show()

    sys.exit(app.exec_())


