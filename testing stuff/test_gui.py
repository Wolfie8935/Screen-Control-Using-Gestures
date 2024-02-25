import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QProcess


class VirtualMouseGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AI Virtual Mouse')
        self.setGeometry(100, 100, 400, 200)  # x, y, width, height

        layout = QVBoxLayout()

        welcome_label = QLabel('Welcome to the AI Virtual Mouse Application!')
        description_label = QLabel(
            'This application allows you to control your mouse cursor using AI-driven gestures. Enjoy a new way of interacting with your computer!')
        self.run_button = QPushButton('Start Virtual Mouse')
        self.run_button.clicked.connect(self.AiVirtualMouse)

        layout.addWidget(welcome_label)
        layout.addWidget(description_label)
        layout.addWidget(self.run_button)

        self.setLayout(layout)

    def AiVirtualMouse(self):
        self.process = QProcess(self)
        self.process.start('python', ['AiVirtualMouse.py'])


def main():
    app = QApplication(sys.argv)
    ex = VirtualMouseGUI()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
