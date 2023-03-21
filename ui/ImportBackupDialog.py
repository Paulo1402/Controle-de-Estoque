# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImportBackupDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
from  . import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(477, 155)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.cb_table = QComboBox(self.frame)
        self.cb_table.setObjectName(u"cb_table")

        self.gridLayout_2.addWidget(self.cb_table, 1, 2, 1, 1)

        self.bt_open = QPushButton(self.frame)
        self.bt_open.setObjectName(u"bt_open")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_open.sizePolicy().hasHeightForWidth())
        self.bt_open.setSizePolicy(sizePolicy)
        self.bt_open.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/assets/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_open.setIcon(icon)

        self.gridLayout_2.addWidget(self.bt_open, 0, 3, 1, 1)

        self.txt_source = QLineEdit(self.frame)
        self.txt_source.setObjectName(u"txt_source")
        self.txt_source.setReadOnly(True)

        self.gridLayout_2.addWidget(self.txt_source, 0, 2, 1, 1)

        self.bt_import = QPushButton(self.frame)
        self.bt_import.setObjectName(u"bt_import")
        self.bt_import.setMinimumSize(QSize(0, 40))
        self.bt_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_import.setStyleSheet(u"margin-top: 3px\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/backup-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_import.setIcon(icon1)
        self.bt_import.setIconSize(QSize(32, 32))

        self.gridLayout_2.addWidget(self.bt_import, 3, 0, 1, 4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 2, 1)

#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.txt_source)
        self.label.setBuddy(self.cb_table)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.txt_source, self.bt_open)
        QWidget.setTabOrder(self.bt_open, self.cb_table)
        QWidget.setTabOrder(self.cb_table, self.bt_import)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IMPORTAR BACKUP", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"FONTE", None))
        self.bt_open.setText("")
        self.bt_import.setText(QCoreApplication.translate("Dialog", u"  IMPORTAR", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TABELA", None))
    # retranslateUi

