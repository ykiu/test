import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication)


class TheWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        price = QLabel('値段')
        priceEdit = QLineEdit()
        
        money = QLabel('お預り')
        moneyEdit = QLineEdit()
        
        button = QPushButton('OK')
        
        change = QLabel('おつり')
        changeValue = QLabel('1234')
        

        grid = QGridLayout()

        grid.addWidget(price, 1, 0)
        grid.addWidget(priceEdit, 1, 1)

        grid.addWidget(money, 2, 0)
        grid.addWidget(moneyEdit, 2, 1)

        grid.addWidget(button, 3, 2)

        grid.addWidget(change, 4, 0)
        grid.addWidget(changeValue, 4, 1)

        
        
        
        self.setLayout(grid) 
        
        self.setGeometry(200, 200, 300, 100)
        self.setWindowTitle('電卓的な練習')
        self.show()
        

app = QApplication(sys.argv)
ex = TheWindow()
sys.exit(app.exec_())
