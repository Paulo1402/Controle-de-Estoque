# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GenericDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from  . import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(497, 198)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(6)
        self.lv_items = QListView(self.frame)
        self.lv_items.setObjectName(u"lv_items")

        self.gridLayout.addWidget(self.lv_items, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txt_name = QLineEdit(self.frame)
        self.txt_name.setObjectName(u"txt_name")

        self.horizontalLayout.addWidget(self.txt_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bt_new = QPushButton(self.frame)
        self.bt_new.setObjectName(u"bt_new")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_new.sizePolicy().hasHeightForWidth())
        self.bt_new.setSizePolicy(sizePolicy)
        self.bt_new.setMinimumSize(QSize(0, 50))
        self.bt_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_new.setFocusPolicy(Qt.TabFocus)
        icon = QIcon()
        icon.addFile(u":/icons/assets/new-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_new.setIcon(icon)
        self.bt_new.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_new)

        self.bt_save = QPushButton(self.frame)
        self.bt_save.setObjectName(u"bt_save")
        sizePolicy.setHeightForWidth(self.bt_save.sizePolicy().hasHeightForWidth())
        self.bt_save.setSizePolicy(sizePolicy)
        self.bt_save.setMinimumSize(QSize(0, 50))
        self.bt_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_save.setFocusPolicy(Qt.TabFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/save-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_save.setIcon(icon1)
        self.bt_save.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_save)

        self.bt_delete = QPushButton(self.frame)
        self.bt_delete.setObjectName(u"bt_delete")
        sizePolicy.setHeightForWidth(self.bt_delete.sizePolicy().hasHeightForWidth())
        self.bt_delete.setSizePolicy(sizePolicy)
        self.bt_delete.setMinimumSize(QSize(0, 50))
        self.bt_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_delete.setFocusPolicy(Qt.TabFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/delete-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_delete.setIcon(icon2)
        self.bt_delete.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.txt_name)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.txt_name, self.bt_new)
        QWidget.setTabOrder(self.bt_new, self.bt_save)
        QWidget.setTabOrder(self.bt_save, self.bt_delete)
        QWidget.setTabOrder(self.bt_delete, self.lv_items)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"NOME", None))
#if QT_CONFIG(tooltip)
        self.bt_new.setToolTip(QCoreApplication.translate("Dialog", u"NOVO", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.bt_new.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.bt_new.setText("")
#if QT_CONFIG(shortcut)
        self.bt_new.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.bt_save.setToolTip(QCoreApplication.translate("Dialog", u"SALVAR", None))
#endif // QT_CONFIG(tooltip)
        self.bt_save.setText("")
#if QT_CONFIG(shortcut)
        self.bt_save.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.bt_delete.setToolTip(QCoreApplication.translate("Dialog", u"DELETAR", None))
#endif // QT_CONFIG(tooltip)
        self.bt_delete.setText("")
#if QT_CONFIG(shortcut)
        self.bt_delete.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

