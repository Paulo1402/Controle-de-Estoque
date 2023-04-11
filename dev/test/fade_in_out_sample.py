from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QPushButton, QGraphicsOpacityEffect, QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget(self)
        self.btn1 = QPushButton("Page 1", self)
        self.btn2 = QPushButton("Page 2", self)

        self.page1 = QWidget(self.stack)
        self.page1.setStyleSheet('background-color: red')

        self.page2 = QWidget(self.stack)
        self.page2.setStyleSheet('background-color: blue')

        self.anim = None

        self.setup_ui()
        self.setMinimumSize(300, 200)

    def setup_ui(self):
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.stack)

        # Connect buttons to change pages
        self.btn1.clicked.connect(lambda: self.change_page(0))
        self.btn2.clicked.connect(lambda: self.change_page(1))

        # Set initial page
        self.change_page(0)

    def change_page(self, index):
        # Get the current page
        current_page = self.stack.currentWidget()

        # Create a new QGraphicsOpacityEffect and set the current page to it
        opacity_effect = QGraphicsOpacityEffect(self)
        current_page.setGraphicsEffect(opacity_effect)

        # Create an opacity animation for the current page
        self.anim = QPropertyAnimation(opacity_effect, b"opacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setEasingCurve(QEasingCurve.OutQuad)

        # Connect the finished signal to change the page
        self.anim.finished.connect(lambda: self.change_page_finished(index))

        # Start the animation
        #self.anim.start()
        self.change_page_finished(index)

    def change_page_finished(self, index):
        # Set the new page and create a new QGraphicsOpacityEffect for it
        new_page = self.stack.widget(index)
        opacity_effect = QGraphicsOpacityEffect(self)
        new_page.setGraphicsEffect(opacity_effect)

        # Create an opacity animation for the new page
        self.anim = QPropertyAnimation(opacity_effect, b"opacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(QEasingCurve.InQuad)

        # Start the animation and set the new page as the current page
        self.anim.start()
        self.stack.setCurrentIndex(index)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()