import sys

from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QStackedWidget, QWidget, QApplication, QMainWindow, QPushButton, QGridLayout, \
    QGraphicsOpacityEffect


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        self.stacked = Example(self)
        self.next_button = QPushButton('next', self)
        self.back_button = QPushButton('back', self)

        self.next_button.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
        self.back_button.clicked.connect(lambda: self.stacked.setCurrentIndex(0))

        layout = QGridLayout(self)
        layout.addWidget(self.stacked, 0, 0, 1, 2)
        layout.addWidget(self.back_button, 1, 0)
        layout.addWidget(self.next_button, 1, 1)

        widget.setLayout(layout)


class Example(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.addWidget(Color('red'))
        self.addWidget(Color('green'))

        self.setCurrentIndex(0)

        self.animation = None

    def setCurrentIndex(self, index):
        if index != self.currentIndex():
            widget = self.widget(index)
            self.fade_in(widget)

        super().setCurrentIndex(index)

    def fade_in(self, widget: QWidget):
        # effect = QGraphicsOpacityEffect(widget, opacity=1)
        # widget.setGraphicsEffect(effect)
        #
        # self.animation = QPropertyAnimation(
        #     widget,
        #     propertyName=b'opacity',
        #     targetObject=effect,
        #     duration=1000,
        #     startValue=0.0,
        #     endValue=1.0,
        # )
        #
        # self.animation.start()

        self.animation = QPropertyAnimation(widget, b"windowOpacity")

        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation.start(QPropertyAnimation.DeleteWhenStopped)


qt = QApplication(sys.argv)
window = MainWindow()
window.show()
qt.exec()
