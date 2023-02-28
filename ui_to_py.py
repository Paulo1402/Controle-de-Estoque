import os

uis = [
    'MainWindow',
    'CalendarDialog'
]

for ui in uis:
    os.system(fr'pyside6-uic .\ui\{ui}.ui -o .\ui\{ui}.py --from-imports')
