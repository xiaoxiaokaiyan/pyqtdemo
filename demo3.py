from PyQt5.Qt import *
import  sys
from demo2 import Window


import sys
app=QApplication(sys.argv)

window=Window()
window.show()

sys.exit(app.exec_())


