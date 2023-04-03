from PySide6.QtCore import QPropertyAnimation, QRect, QSize, Qt
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout


class SlidingStackedWidget(QStackedWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_widget_index = 0
        self.setWindowFlags(Qt.Widget)

        self.animation = None

    def slide_in_next(self):
        current_widget = self.currentWidget()
        next_widget_index = (self.currentIndex() + 1) % self.count()
        next_widget = self.widget(next_widget_index)

        self.animation = QPropertyAnimation(next_widget, b"geometry")
        self.animation.setDuration(250)
        self.animation.setStartValue(QRect(0, self.height(), next_widget.width(), next_widget.height()))
        self.animation.setEndValue(QRect(0, 0, next_widget.width(), next_widget.height()))
        self.animation.start(QPropertyAnimation.DeleteWhenStopped)

        self.setCurrentIndex(next_widget_index)
        self.current_widget_index = next_widget_index

    def slide_in_previous(self):
        current_widget = self.currentWidget()
        previous_widget_index = (self.currentIndex() - 1) % self.count()
        previous_widget = self.widget(previous_widget_index)

        self.animation = QPropertyAnimation(previous_widget, b"geometry")
        self.animation.setDuration(250)
        self.animation.setStartValue(QRect(0, 0, previous_widget.width(), previous_widget.height()))
        self.animation.setEndValue(QRect(0, 0, previous_widget.width(), previous_widget.height()))
        self.animation.start(QPropertyAnimation.DeleteWhenStopped)

        self.setCurrentIndex(previous_widget_index)
        self.current_widget_index = previous_widget_index

    # def resizeEvent(self, event: QResizeEvent) -> None:
    #     super().resizeEvent(event)
    #
    #     current_widget = self.currentWidget()
    #     current_widget.setGeometry(0, 0, event.size().width(), current_widget.height())
    #
    # def addWidget(self, widget: QWidget) -> None:
    #     super().addWidget(widget)
    #     self.resize(self.sizeHint())


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        container = QWidget()
        main_layout = QVBoxLayout()

        container.setLayout(main_layout)

        stacked_widget = SlidingStackedWidget()

        widget1 = QWidget()
        widget1.setStyleSheet("background-color: red;")

        widget2 = QWidget()
        widget2.setStyleSheet("background-color: blue;")

        stacked_widget.addWidget(widget1)
        stacked_widget.addWidget(widget2)

        previous_button = QPushButton('Previous')
        previous_button.clicked.connect(stacked_widget.slide_in_previous)

        next_button = QPushButton('Next')
        next_button.clicked.connect(stacked_widget.slide_in_next)

        button_layout = QHBoxLayout()
        button_layout.addWidget(previous_button)
        button_layout.addWidget(next_button)

        main_layout.addWidget(stacked_widget)
        main_layout.addLayout(button_layout)

        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    window.show()

    app.exec()
