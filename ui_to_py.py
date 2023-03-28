import os

uis = [
    'MainWindow',
    'CalendarDialog',
    'GenericDialog',
    'ConfigurationDialog',
    'ImportBackupDialog'
]

# pyside6-rcc ui/resource.qrc -o ui/resource_rc.py

for ui in uis:
    os.system(fr'pyside6-uic .\ui\{ui}.ui -o .\ui\{ui}.py --from-imports')


