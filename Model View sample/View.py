import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication
import Model


class TheWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        price = QLabel('値段')
        self.price_input = QLineEdit()
        money = QLabel('お預り')
        moneyEdit = QLineEdit()
        okButton = QPushButton('OK')
        change = QLabel('おつり')
        changeValue = QLabel(Model.changeValue)
        
        grid = QGridLayout()
        grid.addWidget(price, 1, 0)
        grid.addWidget(self.price_input, 1, 1)
        grid.addWidget(money, 2, 0)
        grid.addWidget(moneyEdit, 2, 1)
        grid.addWidget(okButton, 3, 2)
        grid.addWidget(change, 4, 0)
        grid.addWidget(changeValue, 4, 1)
                
        self.setLayout(grid)

        okButton.clicked.connect(self.button_command)
        
        self.setGeometry(200, 200, 300, 100)
        self.setWindowTitle('電卓的な練習')
        self.show()

    def button_command(self):
        price_input_value = self.price_input.text()

app = QApplication(sys.argv)
ex = TheWindow()
sys.exit(app.exec_())
