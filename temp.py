from PySide6.QtWidgets import QApplication, QCalendarWidget, QWidget



app = QApplication([])

widget = QCalendarWidget()
nav: QWidget = widget.findChild(QWidget, "qt_calendar_navigationbar")

for w in nav.children():
    print(w)


widget.show()
app.exec()