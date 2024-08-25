from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
# Look into plotly or mathlibchart for charts and graphs
from PyQt5.QtWidgets import QWidget

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("R Vs T")               # Sets the name of the window
        self.setMinimumSize(QSize(800, 600))        # Sets the Minimum size of the window
        self.setMaximumSize(QSize(1200, 1000))      # Sets the FIXED size of the window (Length, Width)
        
        label = QLabel("Testing")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()