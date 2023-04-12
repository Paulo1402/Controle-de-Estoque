"""Script para converter arquivos .ui/.rcc para .py"""

import os

if __name__ == '__main__':
    uis = [
        'MainWindow',
        'CalendarDialog',
        'GenericDialog',
        'DatabaseConfigDialog',
        'ImportBackupDialog',
        'SkidsConfigDialog',
        'LicenseDialog'
    ]

    os.system(fr'pyside6-rcc ..\src\ui\resources\resource.qrc -o ..\src\ui\resource_rc.py')

    for ui in uis:
        os.system(fr'pyside6-uic ..\src\ui\resources\{ui}.ui -o ..\src\ui\{ui}.py --from-imports')
