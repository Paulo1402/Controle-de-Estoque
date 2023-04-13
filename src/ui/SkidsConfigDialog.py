# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SkidsConfigDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from  . import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 131)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.txt_short_skids = QLineEdit(self.frame)
        self.txt_short_skids.setObjectName(u"txt_short_skids")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txt_short_skids)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.txt_long_skids = QLineEdit(self.frame)
        self.txt_long_skids.setObjectName(u"txt_long_skids")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txt_long_skids)


        self.verticalLayout.addLayout(self.formLayout)

        self.bt_reset = QPushButton(self.frame)
        self.bt_reset.setObjectName(u"bt_reset")
        icon = QIcon()
        icon.addFile(u":/icons/assets/reset-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_reset.setIcon(icon)
        self.bt_reset.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.bt_reset)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"CONSTANTE SKIDS", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SKIDS CURTO", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"SKIDS LONGO", None))
        self.bt_reset.setText(QCoreApplication.translate("Dialog", u" RESETAR", None))
#if QT_CONFIG(shortcut)
        self.bt_reset.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

