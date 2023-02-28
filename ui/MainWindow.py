# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from utils.widget import CustomComboBox
from  . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(935, 602)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.action_kiln = QAction(MainWindow)
        self.action_kiln.setObjectName(u"action_kiln")
        icon = QIcon()
        icon.addFile(u":/icons/assets/see-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_kiln.setIcon(icon)
        self.action_license = QAction(MainWindow)
        self.action_license.setObjectName(u"action_license")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/license-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_license.setIcon(icon1)
        self.action_config = QAction(MainWindow)
        self.action_config.setObjectName(u"action_config")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/db-config-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_config.setIcon(icon2)
        self.action_import_backup = QAction(MainWindow)
        self.action_import_backup.setObjectName(u"action_import_backup")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/backup-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_import_backup.setIcon(icon3)
        self.actionaa = QAction(MainWindow)
        self.actionaa.setObjectName(u"actionaa")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Trebuchet MS"])
        font1.setPointSize(22)
        font1.setBold(False)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font1)
        self.label_7.setPixmap(QPixmap(u":/icons/assets/tree-32.png"))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.mp_main = QStackedWidget(self.centralwidget)
        self.mp_main.setObjectName(u"mp_main")
        self.mp_main.setFrameShape(QFrame.Box)
        self.page_cycle = QWidget()
        self.page_cycle.setObjectName(u"page_cycle")
        self.verticalLayout_3 = QVBoxLayout(self.page_cycle)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.page_cycle)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.txt_cycle_cycle = QLineEdit(self.frame)
        self.txt_cycle_cycle.setObjectName(u"txt_cycle_cycle")

        self.gridLayout_2.addWidget(self.txt_cycle_cycle, 1, 4, 1, 1)

        self.cb_exit_date_cycle = CustomComboBox(self.frame)
        self.cb_exit_date_cycle.setObjectName(u"cb_exit_date_cycle")
        self.cb_exit_date_cycle.setMinimumSize(QSize(100, 0))
        self.cb_exit_date_cycle.setEditable(True)
        self.cb_exit_date_cycle.setInsertPolicy(QComboBox.NoInsert)
        self.cb_exit_date_cycle.setFrame(True)

        self.gridLayout_2.addWidget(self.cb_exit_date_cycle, 1, 8, 1, 1)

        self.cb_kiln_cycle = QComboBox(self.frame)
        self.cb_kiln_cycle.addItem("")
        self.cb_kiln_cycle.addItem("")
        self.cb_kiln_cycle.setObjectName(u"cb_kiln_cycle")
        self.cb_kiln_cycle.setMinimumSize(QSize(67, 0))

        self.gridLayout_2.addWidget(self.cb_kiln_cycle, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rb_kd_cycle = QRadioButton(self.groupBox)
        self.rb_kd_cycle.setObjectName(u"rb_kd_cycle")

        self.horizontalLayout.addWidget(self.rb_kd_cycle)

        self.rb_ht_cycle = QRadioButton(self.groupBox)
        self.rb_ht_cycle.setObjectName(u"rb_ht_cycle")

        self.horizontalLayout.addWidget(self.rb_ht_cycle)


        self.gridLayout_2.addWidget(self.groupBox, 1, 10, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 5, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 7, 1, 1)

        self.cb_entry_date_cycle = CustomComboBox(self.frame)
        self.cb_entry_date_cycle.setObjectName(u"cb_entry_date_cycle")
        self.cb_entry_date_cycle.setMinimumSize(QSize(100, 0))
        self.cb_entry_date_cycle.setEditable(True)
        self.cb_entry_date_cycle.setInsertPolicy(QComboBox.NoInsert)
        self.cb_entry_date_cycle.setFrame(True)

        self.gridLayout_2.addWidget(self.cb_entry_date_cycle, 1, 6, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 9, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.frame_13 = QFrame(self.page_cycle)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 50))
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_12.setVerticalSpacing(10)
        self.gridLayout_12.setContentsMargins(-1, -1, 0, 0)
        self.label_59 = QLabel(self.frame_13)
        self.label_59.setObjectName(u"label_59")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.label_59, 0, 0, 1, 1)

        self.label_58 = QLabel(self.frame_13)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_12.addWidget(self.label_58, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.txt_volume_cycle = QLineEdit(self.frame_13)
        self.txt_volume_cycle.setObjectName(u"txt_volume_cycle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_volume_cycle.sizePolicy().hasHeightForWidth())
        self.txt_volume_cycle.setSizePolicy(sizePolicy2)
        self.txt_volume_cycle.setMinimumSize(QSize(0, 0))
        self.txt_volume_cycle.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        self.txt_volume_cycle.setFont(font2)
        self.txt_volume_cycle.setFrame(True)
        self.txt_volume_cycle.setEchoMode(QLineEdit.Normal)
        self.txt_volume_cycle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_volume_cycle.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txt_volume_cycle.setClearButtonEnabled(False)

        self.gridLayout_12.addWidget(self.txt_volume_cycle, 2, 1, 1, 1)

        self.label_57 = QLabel(self.frame_13)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_12.addWidget(self.label_57, 1, 0, 1, 1)

        self.txt_pack_cycle = QLineEdit(self.frame_13)
        self.txt_pack_cycle.setObjectName(u"txt_pack_cycle")
        sizePolicy2.setHeightForWidth(self.txt_pack_cycle.sizePolicy().hasHeightForWidth())
        self.txt_pack_cycle.setSizePolicy(sizePolicy2)
        self.txt_pack_cycle.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_12.addWidget(self.txt_pack_cycle, 1, 1, 1, 1)

        self.txt_bitola_cycle = QLineEdit(self.frame_13)
        self.txt_bitola_cycle.setObjectName(u"txt_bitola_cycle")
        sizePolicy2.setHeightForWidth(self.txt_bitola_cycle.sizePolicy().hasHeightForWidth())
        self.txt_bitola_cycle.setSizePolicy(sizePolicy2)
        self.txt_bitola_cycle.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_12.addWidget(self.txt_bitola_cycle, 0, 1, 1, 1)


        self.horizontalLayout_16.addLayout(self.gridLayout_12)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(6)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.bt_add_cycle = QPushButton(self.frame_13)
        self.bt_add_cycle.setObjectName(u"bt_add_cycle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bt_add_cycle.sizePolicy().hasHeightForWidth())
        self.bt_add_cycle.setSizePolicy(sizePolicy3)
        self.bt_add_cycle.setMinimumSize(QSize(0, 0))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/add-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_add_cycle.setIcon(icon4)
        self.bt_add_cycle.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.bt_add_cycle)

        self.bt_remove_cycle = QPushButton(self.frame_13)
        self.bt_remove_cycle.setObjectName(u"bt_remove_cycle")
        sizePolicy3.setHeightForWidth(self.bt_remove_cycle.sizePolicy().hasHeightForWidth())
        self.bt_remove_cycle.setSizePolicy(sizePolicy3)
        self.bt_remove_cycle.setMinimumSize(QSize(0, 0))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/remove-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_remove_cycle.setIcon(icon5)
        self.bt_remove_cycle.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.bt_remove_cycle)


        self.gridLayout_14.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.tw_cycle = QTableWidget(self.frame_13)
        self.tw_cycle.setObjectName(u"tw_cycle")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tw_cycle.sizePolicy().hasHeightForWidth())
        self.tw_cycle.setSizePolicy(sizePolicy4)
        self.tw_cycle.setMinimumSize(QSize(400, 0))

        self.gridLayout_14.addWidget(self.tw_cycle, 1, 2, 4, 15)


        self.horizontalLayout_16.addLayout(self.gridLayout_14)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bt_new_cycle = QPushButton(self.page_cycle)
        self.bt_new_cycle.setObjectName(u"bt_new_cycle")
        self.bt_new_cycle.setMinimumSize(QSize(0, 50))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/new-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_new_cycle.setIcon(icon6)
        self.bt_new_cycle.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_new_cycle)

        self.bt_save_cycle = QPushButton(self.page_cycle)
        self.bt_save_cycle.setObjectName(u"bt_save_cycle")
        self.bt_save_cycle.setMinimumSize(QSize(0, 50))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/save-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_save_cycle.setIcon(icon7)
        self.bt_save_cycle.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_save_cycle)

        self.bt_delete_cycle = QPushButton(self.page_cycle)
        self.bt_delete_cycle.setObjectName(u"bt_delete_cycle")
        self.bt_delete_cycle.setMinimumSize(QSize(0, 50))
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/delete-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_delete_cycle.setIcon(icon8)
        self.bt_delete_cycle.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_delete_cycle)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.mp_main.addWidget(self.page_cycle)
        self.page_nfe = QWidget()
        self.page_nfe.setObjectName(u"page_nfe")
        self.verticalLayout_5 = QVBoxLayout(self.page_nfe)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.page_nfe)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_pack_nfe = QLineEdit(self.frame_2)
        self.txt_pack_nfe.setObjectName(u"txt_pack_nfe")

        self.gridLayout_4.addWidget(self.txt_pack_nfe, 0, 5, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 0, 2, 1, 1)

        self.cb_date_nfe = CustomComboBox(self.frame_2)
        self.cb_date_nfe.setObjectName(u"cb_date_nfe")
        self.cb_date_nfe.setMinimumSize(QSize(67, 0))
        self.cb_date_nfe.setEditable(True)
        self.cb_date_nfe.setInsertPolicy(QComboBox.NoInsert)
        self.cb_date_nfe.setFrame(True)

        self.gridLayout_4.addWidget(self.cb_date_nfe, 0, 1, 1, 1)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 2, 4, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 2, 2, 1, 1)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 0, 4, 1, 1)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)

        self.txt_client_nfe = QLineEdit(self.frame_2)
        self.txt_client_nfe.setObjectName(u"txt_client_nfe")

        self.gridLayout_4.addWidget(self.txt_client_nfe, 2, 1, 1, 1)

        self.txt_nfe_nfe = QLineEdit(self.frame_2)
        self.txt_nfe_nfe.setObjectName(u"txt_nfe_nfe")

        self.gridLayout_4.addWidget(self.txt_nfe_nfe, 0, 3, 1, 1)

        self.cb_foot_nfe = QComboBox(self.frame_2)
        self.cb_foot_nfe.setObjectName(u"cb_foot_nfe")

        self.gridLayout_4.addWidget(self.cb_foot_nfe, 2, 5, 1, 1)

        self.txt_volume_nfe = QLineEdit(self.frame_2)
        self.txt_volume_nfe.setObjectName(u"txt_volume_nfe")

        self.gridLayout_4.addWidget(self.txt_volume_nfe, 2, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.frame_12 = QFrame(self.page_nfe)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_7.setVerticalSpacing(10)
        self.gridLayout_7.setContentsMargins(-1, -1, 0, 0)
        self.cb_rework_nfe = QLineEdit(self.frame_12)
        self.cb_rework_nfe.setObjectName(u"cb_rework_nfe")
        sizePolicy2.setHeightForWidth(self.cb_rework_nfe.sizePolicy().hasHeightForWidth())
        self.cb_rework_nfe.setSizePolicy(sizePolicy2)
        self.cb_rework_nfe.setMinimumSize(QSize(0, 0))
        self.cb_rework_nfe.setMaximumSize(QSize(16777215, 16777215))
        self.cb_rework_nfe.setFont(font2)
        self.cb_rework_nfe.setFrame(True)
        self.cb_rework_nfe.setEchoMode(QLineEdit.Normal)
        self.cb_rework_nfe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cb_rework_nfe.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.cb_rework_nfe.setClearButtonEnabled(False)

        self.gridLayout_7.addWidget(self.cb_rework_nfe, 3, 1, 1, 1)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)

        self.cb_bitola_nfe = QComboBox(self.frame_12)
        self.cb_bitola_nfe.setObjectName(u"cb_bitola_nfe")
        sizePolicy2.setHeightForWidth(self.cb_bitola_nfe.sizePolicy().hasHeightForWidth())
        self.cb_bitola_nfe.setSizePolicy(sizePolicy2)
        self.cb_bitola_nfe.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.cb_bitola_nfe, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 3, 0, 1, 1)

        self.cb_volume_nfe = QLineEdit(self.frame_12)
        self.cb_volume_nfe.setObjectName(u"cb_volume_nfe")
        sizePolicy2.setHeightForWidth(self.cb_volume_nfe.sizePolicy().hasHeightForWidth())
        self.cb_volume_nfe.setSizePolicy(sizePolicy2)
        self.cb_volume_nfe.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.cb_volume_nfe, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)

        self.cb_cycle_nfe = QComboBox(self.frame_12)
        self.cb_cycle_nfe.setObjectName(u"cb_cycle_nfe")
        sizePolicy2.setHeightForWidth(self.cb_cycle_nfe.sizePolicy().hasHeightForWidth())
        self.cb_cycle_nfe.setSizePolicy(sizePolicy2)
        self.cb_cycle_nfe.setMinimumSize(QSize(0, 0))
        self.cb_cycle_nfe.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.cb_cycle_nfe, 0, 1, 1, 1)


        self.horizontalLayout_15.addLayout(self.gridLayout_7)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.bt_add_nfe = QPushButton(self.frame_12)
        self.bt_add_nfe.setObjectName(u"bt_add_nfe")
        sizePolicy3.setHeightForWidth(self.bt_add_nfe.sizePolicy().hasHeightForWidth())
        self.bt_add_nfe.setSizePolicy(sizePolicy3)
        self.bt_add_nfe.setMinimumSize(QSize(0, 0))
        self.bt_add_nfe.setIcon(icon4)
        self.bt_add_nfe.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.bt_add_nfe)

        self.bt_remove_nfe = QPushButton(self.frame_12)
        self.bt_remove_nfe.setObjectName(u"bt_remove_nfe")
        sizePolicy3.setHeightForWidth(self.bt_remove_nfe.sizePolicy().hasHeightForWidth())
        self.bt_remove_nfe.setSizePolicy(sizePolicy3)
        self.bt_remove_nfe.setMinimumSize(QSize(0, 0))
        self.bt_remove_nfe.setIcon(icon5)
        self.bt_remove_nfe.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.bt_remove_nfe)


        self.gridLayout_6.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.tw_nfe = QTableWidget(self.frame_12)
        self.tw_nfe.setObjectName(u"tw_nfe")
        sizePolicy4.setHeightForWidth(self.tw_nfe.sizePolicy().hasHeightForWidth())
        self.tw_nfe.setSizePolicy(sizePolicy4)
        self.tw_nfe.setMinimumSize(QSize(400, 0))

        self.gridLayout_6.addWidget(self.tw_nfe, 1, 2, 4, 15)


        self.horizontalLayout_15.addLayout(self.gridLayout_6)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.bt_new_nfe = QPushButton(self.page_nfe)
        self.bt_new_nfe.setObjectName(u"bt_new_nfe")
        self.bt_new_nfe.setMinimumSize(QSize(0, 50))
        self.bt_new_nfe.setIcon(icon6)
        self.bt_new_nfe.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_new_nfe)

        self.bt_save_nfe = QPushButton(self.page_nfe)
        self.bt_save_nfe.setObjectName(u"bt_save_nfe")
        self.bt_save_nfe.setMinimumSize(QSize(0, 50))
        self.bt_save_nfe.setIcon(icon7)
        self.bt_save_nfe.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_save_nfe)

        self.bt_delete_nfe = QPushButton(self.page_nfe)
        self.bt_delete_nfe.setObjectName(u"bt_delete_nfe")
        self.bt_delete_nfe.setMinimumSize(QSize(0, 50))
        self.bt_delete_nfe.setIcon(icon8)
        self.bt_delete_nfe.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_delete_nfe)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.mp_main.addWidget(self.page_nfe)
        self.page_stock = QWidget()
        self.page_stock.setObjectName(u"page_stock")
        self.verticalLayout_2 = QVBoxLayout(self.page_stock)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.page_stock)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.cb_cycle_stock = QComboBox(self.frame_3)
        self.cb_cycle_stock.setObjectName(u"cb_cycle_stock")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.cb_cycle_stock.sizePolicy().hasHeightForWidth())
        self.cb_cycle_stock.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.cb_cycle_stock)

        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_6.addWidget(self.label_21)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rb_kd_stock = QRadioButton(self.groupBox_2)
        self.rb_kd_stock.setObjectName(u"rb_kd_stock")

        self.horizontalLayout_4.addWidget(self.rb_kd_stock)

        self.rb_ht_stock = QRadioButton(self.groupBox_2)
        self.rb_ht_stock.setObjectName(u"rb_ht_stock")

        self.horizontalLayout_4.addWidget(self.rb_ht_stock)


        self.horizontalLayout_6.addWidget(self.groupBox_2)

        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_6.addWidget(self.label_22)

        self.cb_bitola_stock = QComboBox(self.frame_3)
        self.cb_bitola_stock.setObjectName(u"cb_bitola_stock")
        sizePolicy5.setHeightForWidth(self.cb_bitola_stock.sizePolicy().hasHeightForWidth())
        self.cb_bitola_stock.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.cb_bitola_stock)

        self.bt_search_stock = QPushButton(self.frame_3)
        self.bt_search_stock.setObjectName(u"bt_search_stock")
        sizePolicy3.setHeightForWidth(self.bt_search_stock.sizePolicy().hasHeightForWidth())
        self.bt_search_stock.setSizePolicy(sizePolicy3)
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/search-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_search_stock.setIcon(icon9)
        self.bt_search_stock.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.bt_search_stock)

        self.bt_clear_stock = QPushButton(self.frame_3)
        self.bt_clear_stock.setObjectName(u"bt_clear_stock")
        sizePolicy3.setHeightForWidth(self.bt_clear_stock.sizePolicy().hasHeightForWidth())
        self.bt_clear_stock.setSizePolicy(sizePolicy3)
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/erase-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_clear_stock.setIcon(icon10)
        self.bt_clear_stock.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.bt_clear_stock)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.tv_stock = QTableView(self.page_stock)
        self.tv_stock.setObjectName(u"tv_stock")

        self.verticalLayout_2.addWidget(self.tv_stock)

        self.frame_4 = QFrame(self.page_stock)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.txt_leaving_stock = QLineEdit(self.frame_4)
        self.txt_leaving_stock.setObjectName(u"txt_leaving_stock")

        self.gridLayout_8.addWidget(self.txt_leaving_stock, 3, 3, 1, 1)

        self.bt_leaving_stock = QPushButton(self.frame_4)
        self.bt_leaving_stock.setObjectName(u"bt_leaving_stock")
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/recycling-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_leaving_stock.setIcon(icon11)
        self.bt_leaving_stock.setIconSize(QSize(32, 32))

        self.gridLayout_8.addWidget(self.bt_leaving_stock, 1, 1, 3, 1)

        self.txt_treatment_stock = QLineEdit(self.frame_4)
        self.txt_treatment_stock.setObjectName(u"txt_treatment_stock")

        self.gridLayout_8.addWidget(self.txt_treatment_stock, 1, 3, 1, 1)

        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_8.addWidget(self.label_24, 1, 4, 1, 1)

        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_8.addWidget(self.label_25, 3, 2, 1, 1)

        self.bt_discount_stock = QPushButton(self.frame_4)
        self.bt_discount_stock.setObjectName(u"bt_discount_stock")
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/document-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_discount_stock.setIcon(icon12)
        self.bt_discount_stock.setIconSize(QSize(32, 32))

        self.gridLayout_8.addWidget(self.bt_discount_stock, 1, 0, 3, 1)

        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_8.addWidget(self.label_26, 3, 4, 1, 1)

        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_8.addWidget(self.label_23, 1, 2, 1, 1)

        self.txt_stock_stock = QLineEdit(self.frame_4)
        self.txt_stock_stock.setObjectName(u"txt_stock_stock")

        self.gridLayout_8.addWidget(self.txt_stock_stock, 3, 5, 1, 1)

        self.txt_sold_stock = QLineEdit(self.frame_4)
        self.txt_sold_stock.setObjectName(u"txt_sold_stock")

        self.gridLayout_8.addWidget(self.txt_sold_stock, 1, 5, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.mp_main.addWidget(self.page_stock)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.verticalLayout_8 = QVBoxLayout(self.page_history)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.page_history)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bt_cycle_history = QPushButton(self.frame_5)
        self.bt_cycle_history.setObjectName(u"bt_cycle_history")
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/tag-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cycle_history.setIcon(icon13)
        self.bt_cycle_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.bt_cycle_history)

        self.bt_nfe_history = QPushButton(self.frame_5)
        self.bt_nfe_history.setObjectName(u"bt_nfe_history")
        self.bt_nfe_history.setIcon(icon12)
        self.bt_nfe_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.bt_nfe_history)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.mp_history = QStackedWidget(self.page_history)
        self.mp_history.setObjectName(u"mp_history")
        self.mp_history.setMinimumSize(QSize(0, 50))
        self.mp_history.setFrameShape(QFrame.Box)
        self.page_history_cycle = QWidget()
        self.page_history_cycle.setObjectName(u"page_history_cycle")
        self.verticalLayout_7 = QVBoxLayout(self.page_history_cycle)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.page_history_cycle)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setVerticalSpacing(6)
        self.txt_bitola_cycle_history = QLineEdit(self.frame_7)
        self.txt_bitola_cycle_history.setObjectName(u"txt_bitola_cycle_history")

        self.gridLayout_5.addWidget(self.txt_bitola_cycle_history, 0, 6, 1, 1)

        self.label_32 = QLabel(self.frame_7)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 0, 2, 1, 2)

        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_34, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.rb_kd_cycle_history = QRadioButton(self.groupBox_3)
        self.rb_kd_cycle_history.setObjectName(u"rb_kd_cycle_history")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.rb_kd_cycle_history.sizePolicy().hasHeightForWidth())
        self.rb_kd_cycle_history.setSizePolicy(sizePolicy6)

        self.horizontalLayout_10.addWidget(self.rb_kd_cycle_history)

        self.rb_ht_cycle_history = QRadioButton(self.groupBox_3)
        self.rb_ht_cycle_history.setObjectName(u"rb_ht_cycle_history")

        self.horizontalLayout_10.addWidget(self.rb_ht_cycle_history)


        self.gridLayout_5.addWidget(self.groupBox_3, 1, 6, 2, 1)

        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_36, 1, 5, 2, 1)

        self.label_31 = QLabel(self.frame_7)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.label_31, 1, 0, 2, 1)

        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_5.addWidget(self.label_35, 0, 5, 1, 1)

        self.label_33 = QLabel(self.frame_7)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.label_33, 1, 2, 2, 2)

        self.txt_cycle_cycle_history = QLineEdit(self.frame_7)
        self.txt_cycle_cycle_history.setObjectName(u"txt_cycle_cycle_history")

        self.gridLayout_5.addWidget(self.txt_cycle_cycle_history, 1, 1, 2, 1)

        self.cb_kiln_cycle_history_2 = QComboBox(self.frame_7)
        self.cb_kiln_cycle_history_2.setObjectName(u"cb_kiln_cycle_history_2")

        self.gridLayout_5.addWidget(self.cb_kiln_cycle_history_2, 0, 1, 1, 1)

        self.cb_entry_date_cycle_history = CustomComboBox(self.frame_7)
        self.cb_entry_date_cycle_history.setObjectName(u"cb_entry_date_cycle_history")
        self.cb_entry_date_cycle_history.setMinimumSize(QSize(67, 0))
        self.cb_entry_date_cycle_history.setEditable(True)
        self.cb_entry_date_cycle_history.setInsertPolicy(QComboBox.NoInsert)
        self.cb_entry_date_cycle_history.setFrame(True)

        self.gridLayout_5.addWidget(self.cb_entry_date_cycle_history, 0, 4, 1, 1)

        self.cb_exit_date_cycle_history = CustomComboBox(self.frame_7)
        self.cb_exit_date_cycle_history.setObjectName(u"cb_exit_date_cycle_history")
        self.cb_exit_date_cycle_history.setMinimumSize(QSize(67, 0))
        self.cb_exit_date_cycle_history.setEditable(True)
        self.cb_exit_date_cycle_history.setInsertPolicy(QComboBox.NoInsert)
        self.cb_exit_date_cycle_history.setFrame(True)

        self.gridLayout_5.addWidget(self.cb_exit_date_cycle_history, 1, 4, 2, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout_5)

        self.bt_search_cycle_history = QPushButton(self.frame_7)
        self.bt_search_cycle_history.setObjectName(u"bt_search_cycle_history")
        self.bt_search_cycle_history.setIcon(icon9)
        self.bt_search_cycle_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.bt_search_cycle_history)

        self.bt_clear_cycle_history = QPushButton(self.frame_7)
        self.bt_clear_cycle_history.setObjectName(u"bt_clear_cycle_history")
        self.bt_clear_cycle_history.setIcon(icon10)
        self.bt_clear_cycle_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.bt_clear_cycle_history)

        self.bt_edit_cycle_history = QPushButton(self.frame_7)
        self.bt_edit_cycle_history.setObjectName(u"bt_edit_cycle_history")
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/edit-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_edit_cycle_history.setIcon(icon14)
        self.bt_edit_cycle_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.bt_edit_cycle_history)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.tv_cycle_history = QTableView(self.page_history_cycle)
        self.tv_cycle_history.setObjectName(u"tv_cycle_history")

        self.verticalLayout_7.addWidget(self.tv_cycle_history)

        self.mp_history.addWidget(self.page_history_cycle)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_9 = QFrame(self.page_2)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setFrameShape(QFrame.Box)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(6)
        self.label_39 = QLabel(self.frame_9)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_9.addWidget(self.label_39, 0, 5, 1, 1)

        self.label_42 = QLabel(self.frame_9)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_9.addWidget(self.label_42, 1, 2, 2, 2)

        self.label_38 = QLabel(self.frame_9)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_9.addWidget(self.label_38, 0, 2, 1, 2)

        self.label_37 = QLabel(self.frame_9)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 27))

        self.gridLayout_9.addWidget(self.label_37, 0, 0, 1, 1)

        self.txt_bitola_track_history = QLineEdit(self.frame_9)
        self.txt_bitola_track_history.setObjectName(u"txt_bitola_track_history")

        self.gridLayout_9.addWidget(self.txt_bitola_track_history, 0, 6, 1, 1)

        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_9.addWidget(self.label_41, 1, 5, 2, 1)

        self.txt_cycle_track_history = QLineEdit(self.frame_9)
        self.txt_cycle_track_history.setObjectName(u"txt_cycle_track_history")

        self.gridLayout_9.addWidget(self.txt_cycle_track_history, 1, 1, 2, 1)

        self.txt_entry_date_track_history = QLineEdit(self.frame_9)
        self.txt_entry_date_track_history.setObjectName(u"txt_entry_date_track_history")

        self.gridLayout_9.addWidget(self.txt_entry_date_track_history, 0, 4, 1, 1)

        self.groupBox_4 = QGroupBox(self.frame_9)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.rb_kd_track_history = QRadioButton(self.groupBox_4)
        self.rb_kd_track_history.setObjectName(u"rb_kd_track_history")

        self.horizontalLayout_11.addWidget(self.rb_kd_track_history)

        self.rb_ht_track_history = QRadioButton(self.groupBox_4)
        self.rb_ht_track_history.setObjectName(u"rb_ht_track_history")

        self.horizontalLayout_11.addWidget(self.rb_ht_track_history)


        self.gridLayout_9.addWidget(self.groupBox_4, 1, 6, 2, 1)

        self.cb_kiln_track_history = QComboBox(self.frame_9)
        self.cb_kiln_track_history.setObjectName(u"cb_kiln_track_history")

        self.gridLayout_9.addWidget(self.cb_kiln_track_history, 0, 1, 1, 1)

        self.label_40 = QLabel(self.frame_9)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_9.addWidget(self.label_40, 1, 0, 2, 1)

        self.txt_exit_date_track_history = QLineEdit(self.frame_9)
        self.txt_exit_date_track_history.setObjectName(u"txt_exit_date_track_history")

        self.gridLayout_9.addWidget(self.txt_exit_date_track_history, 1, 4, 2, 1)

        self.gridLayout_9.setRowMinimumHeight(0, 34)
        self.gridLayout_9.setRowMinimumHeight(1, 34)

        self.horizontalLayout_12.addLayout(self.gridLayout_9)

        self.horizontalSpacer_3 = QSpacerItem(94, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.bt_back_track_history = QPushButton(self.frame_9)
        self.bt_back_track_history.setObjectName(u"bt_back_track_history")
        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/back-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_back_track_history.setIcon(icon15)
        self.bt_back_track_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.bt_back_track_history)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.tv_track_history = QTableView(self.page_2)
        self.tv_track_history.setObjectName(u"tv_track_history")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tv_track_history.sizePolicy().hasHeightForWidth())
        self.tv_track_history.setSizePolicy(sizePolicy7)
        self.tv_track_history.setMinimumSize(QSize(560, 0))
        self.tv_track_history.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.tv_track_history, 0, 0, 4, 1)

        self.frame_10 = QFrame(self.page_2)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.Box)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_45 = QLabel(self.frame_10)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_10.addWidget(self.label_45, 1, 0, 1, 1)

        self.label_44 = QLabel(self.frame_10)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_10.addWidget(self.label_44, 2, 0, 1, 1)

        self.label_43 = QLabel(self.frame_10)
        self.label_43.setObjectName(u"label_43")
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_43, 0, 0, 1, 2)

        self.txt_leaving_date_track_history = QLineEdit(self.frame_10)
        self.txt_leaving_date_track_history.setObjectName(u"txt_leaving_date_track_history")
        sizePolicy5.setHeightForWidth(self.txt_leaving_date_track_history.sizePolicy().hasHeightForWidth())
        self.txt_leaving_date_track_history.setSizePolicy(sizePolicy5)

        self.gridLayout_10.addWidget(self.txt_leaving_date_track_history, 1, 1, 1, 1)

        self.txt_leaving_volume_track_history = QLineEdit(self.frame_10)
        self.txt_leaving_volume_track_history.setObjectName(u"txt_leaving_volume_track_history")

        self.gridLayout_10.addWidget(self.txt_leaving_volume_track_history, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_10, 0, 1, 1, 1)

        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(0, 40))
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_50 = QLabel(self.frame_11)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_11.addWidget(self.label_50, 2, 0, 1, 1)

        self.label_52 = QLabel(self.frame_11)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_52, 0, 0, 1, 2)

        self.txt_stock_volume_track_history = QLineEdit(self.frame_11)
        self.txt_stock_volume_track_history.setObjectName(u"txt_stock_volume_track_history")

        self.gridLayout_11.addWidget(self.txt_stock_volume_track_history, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_11, 2, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_3)

        self.mp_history.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_10 = QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_6 = QFrame(self.page_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, -1, -1, 0)
        self.label_54 = QLabel(self.frame_6)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_13.addWidget(self.label_54, 2, 2, 1, 1)

        self.label_53 = QLabel(self.frame_6)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_13.addWidget(self.label_53, 0, 2, 2, 1)

        self.label_48 = QLabel(self.frame_6)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_13.addWidget(self.label_48, 2, 0, 1, 1)

        self.label_55 = QLabel(self.frame_6)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_13.addWidget(self.label_55, 0, 4, 2, 1)

        self.label_49 = QLabel(self.frame_6)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_13.addWidget(self.label_49, 0, 0, 2, 1)

        self.txt_client_nfe_history = QLineEdit(self.frame_6)
        self.txt_client_nfe_history.setObjectName(u"txt_client_nfe_history")

        self.gridLayout_13.addWidget(self.txt_client_nfe_history, 2, 1, 1, 1)

        self.txt_foot_nfe_history = QLineEdit(self.frame_6)
        self.txt_foot_nfe_history.setObjectName(u"txt_foot_nfe_history")

        self.gridLayout_13.addWidget(self.txt_foot_nfe_history, 0, 5, 2, 1)

        self.txt_nfe_nfe_history = QLineEdit(self.frame_6)
        self.txt_nfe_nfe_history.setObjectName(u"txt_nfe_nfe_history")

        self.gridLayout_13.addWidget(self.txt_nfe_nfe_history, 0, 1, 2, 1)

        self.cb_end_date_nfe_history = CustomComboBox(self.frame_6)
        self.cb_end_date_nfe_history.setObjectName(u"cb_end_date_nfe_history")
        self.cb_end_date_nfe_history.setMinimumSize(QSize(67, 0))
        self.cb_end_date_nfe_history.setEditable(True)
        self.cb_end_date_nfe_history.setInsertPolicy(QComboBox.NoInsert)
        self.cb_end_date_nfe_history.setFrame(True)

        self.gridLayout_13.addWidget(self.cb_end_date_nfe_history, 2, 3, 1, 1)

        self.cb_start_date_nfe_history = CustomComboBox(self.frame_6)
        self.cb_start_date_nfe_history.setObjectName(u"cb_start_date_nfe_history")
        self.cb_start_date_nfe_history.setMinimumSize(QSize(67, 0))
        self.cb_start_date_nfe_history.setEditable(True)
        self.cb_start_date_nfe_history.setInsertPolicy(QComboBox.NoInsert)
        self.cb_start_date_nfe_history.setFrame(True)

        self.gridLayout_13.addWidget(self.cb_start_date_nfe_history, 0, 3, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_13)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, 0, -1)
        self.bt_search_nfe_history = QPushButton(self.frame_6)
        self.bt_search_nfe_history.setObjectName(u"bt_search_nfe_history")
        self.bt_search_nfe_history.setIcon(icon9)
        self.bt_search_nfe_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.bt_search_nfe_history)

        self.bt_clear_nfe_history = QPushButton(self.frame_6)
        self.bt_clear_nfe_history.setObjectName(u"bt_clear_nfe_history")
        self.bt_clear_nfe_history.setIcon(icon10)
        self.bt_clear_nfe_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.bt_clear_nfe_history)

        self.bt_edit_nfe_history = QPushButton(self.frame_6)
        self.bt_edit_nfe_history.setObjectName(u"bt_edit_nfe_history")
        self.bt_edit_nfe_history.setIcon(icon14)
        self.bt_edit_nfe_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.bt_edit_nfe_history)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_20)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.tv_nfe_history = QTableView(self.page_3)
        self.tv_nfe_history.setObjectName(u"tv_nfe_history")

        self.verticalLayout_10.addWidget(self.tv_nfe_history)

        self.mp_history.addWidget(self.page_3)

        self.verticalLayout_8.addWidget(self.mp_history)

        self.mp_main.addWidget(self.page_history)

        self.gridLayout.addWidget(self.mp_main, 5, 1, 2, 1)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(160, 0))
        self.frame_8.setFrameShape(QFrame.Box)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.bt_cycle_menu = QPushButton(self.frame_8)
        self.bt_cycle_menu.setObjectName(u"bt_cycle_menu")
        sizePolicy6.setHeightForWidth(self.bt_cycle_menu.sizePolicy().hasHeightForWidth())
        self.bt_cycle_menu.setSizePolicy(sizePolicy6)
        self.bt_cycle_menu.setMinimumSize(QSize(0, 50))
        self.bt_cycle_menu.setIcon(icon13)
        self.bt_cycle_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_cycle_menu)

        self.bt_nfe_menu = QPushButton(self.frame_8)
        self.bt_nfe_menu.setObjectName(u"bt_nfe_menu")
        self.bt_nfe_menu.setMinimumSize(QSize(0, 50))
        self.bt_nfe_menu.setIcon(icon12)
        self.bt_nfe_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_nfe_menu)

        self.bt_stock_menu = QPushButton(self.frame_8)
        self.bt_stock_menu.setObjectName(u"bt_stock_menu")
        self.bt_stock_menu.setMinimumSize(QSize(0, 50))
        icon16 = QIcon()
        icon16.addFile(u":/icons/assets/stock-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_stock_menu.setIcon(icon16)
        self.bt_stock_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_stock_menu)

        self.bt_history_menu = QPushButton(self.frame_8)
        self.bt_history_menu.setObjectName(u"bt_history_menu")
        self.bt_history_menu.setMinimumSize(QSize(0, 50))
        icon17 = QIcon()
        icon17.addFile(u":/icons/assets/history-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_history_menu.setIcon(icon17)
        self.bt_history_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_history_menu)

        self.bt_exit_menu = QPushButton(self.frame_8)
        self.bt_exit_menu.setObjectName(u"bt_exit_menu")
        self.bt_exit_menu.setMinimumSize(QSize(0, 50))
        icon18 = QIcon()
        icon18.addFile(u":/icons/assets/exit-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_exit_menu.setIcon(icon18)
        self.bt_exit_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_exit_menu)


        self.gridLayout.addWidget(self.frame_8, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 935, 22))
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_kiln = QMenu(self.menubar)
        self.menu_kiln.setObjectName(u"menu_kiln")
        self.menu_config = QMenu(self.menubar)
        self.menu_config.setObjectName(u"menu_config")
        self.menu_db = QMenu(self.menu_config)
        self.menu_db.setObjectName(u"menu_db")
        icon19 = QIcon()
        icon19.addFile(u":/icons/assets/db.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_db.setIcon(icon19)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_config.menuAction())
        self.menubar.addAction(self.menu_kiln.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_about.addAction(self.action_license)
        self.menu_kiln.addAction(self.action_kiln)
        self.menu_config.addAction(self.menu_db.menuAction())
        self.menu_db.addAction(self.action_config)
        self.menu_db.addAction(self.action_import_backup)

        self.retranslateUi(MainWindow)

        self.mp_main.setCurrentIndex(3)
        self.mp_history.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_kiln.setText(QCoreApplication.translate("MainWindow", u"Ver estufas", None))
        self.action_license.setText(QCoreApplication.translate("MainWindow", u"Licen\u00e7a", None))
        self.action_config.setText(QCoreApplication.translate("MainWindow", u"Configurar", None))
        self.action_import_backup.setText(QCoreApplication.translate("MainWindow", u"Importar backup", None))
        self.actionaa.setText(QCoreApplication.translate("MainWindow", u"aa", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CONTROLE DE MADERA TRATADA", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ESTUFA", None))
        self.cb_kiln_cycle.setItemText(0, QCoreApplication.translate("MainWindow", u"Estufa 1", None))
        self.cb_kiln_cycle.setItemText(1, QCoreApplication.translate("MainWindow", u"Estufa 2", None))

        self.groupBox.setTitle("")
        self.rb_kd_cycle.setText(QCoreApplication.translate("MainWindow", u"KD", None))
        self.rb_ht_cycle.setText(QCoreApplication.translate("MainWindow", u"HT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ENTRADA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"FINALIDADE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.txt_volume_cycle.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"FARDOS", None))
        self.bt_add_cycle.setText("")
        self.bt_remove_cycle.setText("")
        self.bt_new_cycle.setText(QCoreApplication.translate("MainWindow", u" NOVO", None))
        self.bt_save_cycle.setText(QCoreApplication.translate("MainWindow", u" SALVAR", None))
        self.bt_delete_cycle.setText(QCoreApplication.translate("MainWindow", u" DELETAR", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"NFE", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CICLO PEZINHO", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"VOLUME TOTAL", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"FARDOS", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.cb_rework_nfe.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"RETRABALHO", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.bt_add_nfe.setText("")
        self.bt_remove_nfe.setText("")
        self.bt_new_nfe.setText(QCoreApplication.translate("MainWindow", u" NOVO", None))
        self.bt_save_nfe.setText(QCoreApplication.translate("MainWindow", u" SALVAR", None))
        self.bt_delete_nfe.setText(QCoreApplication.translate("MainWindow", u" DELETAR", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"FINALIDADE", None))
        self.groupBox_2.setTitle("")
        self.rb_kd_stock.setText(QCoreApplication.translate("MainWindow", u"KD", None))
        self.rb_ht_stock.setText(QCoreApplication.translate("MainWindow", u"HT", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.bt_search_stock.setText("")
        self.bt_clear_stock.setText("")
        self.bt_leaving_stock.setText(QCoreApplication.translate("MainWindow", u" MERCADO INTERNO", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"VOLUME VENDIDO", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RES\u00cdDUO", None))
        self.bt_discount_stock.setText(QCoreApplication.translate("MainWindow", u" BAIXAR NFE", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"VOLUME TRATADO", None))
        self.bt_cycle_history.setText(QCoreApplication.translate("MainWindow", u" CICLOS", None))
        self.bt_nfe_history.setText(QCoreApplication.translate("MainWindow", u" NFE", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"ENTRADA", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"ESTUFA", None))
        self.groupBox_3.setTitle("")
        self.rb_kd_cycle_history.setText(QCoreApplication.translate("MainWindow", u"KD", None))
        self.rb_ht_cycle_history.setText(QCoreApplication.translate("MainWindow", u"HT", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"FINALIDADE", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        self.bt_search_cycle_history.setText("")
#if QT_CONFIG(shortcut)
        self.bt_search_cycle_history.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.bt_clear_cycle_history.setText("")
#if QT_CONFIG(shortcut)
        self.bt_clear_cycle_history.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.bt_edit_cycle_history.setText("")
#if QT_CONFIG(shortcut)
        self.bt_edit_cycle_history.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"ENTRADA", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"ESTUFA", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"FINALIDADE", None))
        self.groupBox_4.setTitle("")
        self.rb_kd_track_history.setText(QCoreApplication.translate("MainWindow", u"KD", None))
        self.rb_ht_track_history.setText(QCoreApplication.translate("MainWindow", u"HT", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.bt_back_track_history.setText("")
#if QT_CONFIG(shortcut)
        self.bt_back_track_history.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"MERCADO INTERNO", None))
        self.txt_leaving_date_track_history.setText(QCoreApplication.translate("MainWindow", u"14/11/2023", None))
        self.txt_leaving_volume_track_history.setText(QCoreApplication.translate("MainWindow", u"15,258 M\u00b3", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.txt_stock_volume_track_history.setText(QCoreApplication.translate("MainWindow", u"14,389 M\u00b3", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"DATA FINAL", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"DATA INICIAL", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"CICLO PEZINHO", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"NFE", None))
        self.bt_search_nfe_history.setText("")
#if QT_CONFIG(shortcut)
        self.bt_search_nfe_history.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.bt_clear_nfe_history.setText("")
#if QT_CONFIG(shortcut)
        self.bt_clear_nfe_history.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.bt_edit_nfe_history.setText("")
#if QT_CONFIG(shortcut)
        self.bt_edit_nfe_history.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.bt_cycle_menu.setText(QCoreApplication.translate("MainWindow", u" CICLOS", None))
        self.bt_nfe_menu.setText(QCoreApplication.translate("MainWindow", u" NFE", None))
        self.bt_stock_menu.setText(QCoreApplication.translate("MainWindow", u" ESTOQUE", None))
        self.bt_history_menu.setText(QCoreApplication.translate("MainWindow", u" HIST\u00d3RICO", None))
        self.bt_exit_menu.setText(QCoreApplication.translate("MainWindow", u" SAIR", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.menu_kiln.setTitle(QCoreApplication.translate("MainWindow", u"Estufas", None))
        self.menu_config.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.menu_db.setTitle(QCoreApplication.translate("MainWindow", u"Banco de dados", None))
    # retranslateUi

