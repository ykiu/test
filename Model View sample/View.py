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
        self.money_input = QLineEdit()
        okButton = QPushButton('OK')
        change = QLabel('おつり')
        self.changeValue = QLabel('')
        
        grid = QGridLayout()
        grid.addWidget(price, 1, 0)
        grid.addWidget(self.price_input, 1, 1)
        grid.addWidget(money, 2, 0)
        grid.addWidget(self.money_input, 2, 1)
        grid.addWidget(okButton, 3, 2)
        grid.addWidget(change, 4, 0)
        grid.addWidget(self.changeValue, 4, 1)

        #下のsetLayoutはQWidgetのメソッド
        self.setLayout(grid)

        okButton.clicked.connect(self.button_command)
        
        self.setGeometry(200, 200, 300, 100)
        self.setWindowTitle('電卓的な練習')
        self.show()

    def button_command(self):
        price_input_value = int(self.price_input.text())
        money_input_value = int(self.money_input.text())
        calculatedValue = str(Model.calculate(price_input_value, money_input_value))
        print(calculatedValue)
        self.changeValue.setText(calculatedValue)


app = QApplication(sys.argv)
ex = TheWindow()
sys.exit(app.exec_())
