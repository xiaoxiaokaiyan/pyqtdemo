
import untitled
from PyQt5.QtWidgets  import QApplication,QWidget,QMainWindow

import sys

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=QMainWindow()

    ui=untitled.Ui_MainWindow()

    ui.setupUi(w)
    w.show()




    sys.exit(app.exec_())