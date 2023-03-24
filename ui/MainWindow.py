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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from utils.widget import CustomComboBox
from  . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1006, 575)
        MainWindow.setStyleSheet(u" QGroupBox {\n"
"            border: none;\n"
" }")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
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
        self.centralwidget.setStyleSheet(u"QComboBox {\n"
"	combobox-popup: 0;\n"
"}")
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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.mp_main = QStackedWidget(self.centralwidget)
        self.mp_main.setObjectName(u"mp_main")
        self.mp_main.setFrameShape(QFrame.Box)
        self.page_cycle = QWidget()
        self.page_cycle.setObjectName(u"page_cycle")
        self.page_cycle.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.page_cycle)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tab_widget_cycle = QTabWidget(self.page_cycle)
        self.tab_widget_cycle.setObjectName(u"tab_widget_cycle")
        self.tab_widget_cycle.setTabPosition(QTabWidget.North)
        self.tab_widget_cycle.setTabShape(QTabWidget.Rounded)
        self.tab_widget_cycle.setElideMode(Qt.ElideLeft)
        self.tab_widget_cycle.setUsesScrollButtons(True)
        self.tab_widget_cycle.setDocumentMode(False)
        self.tab_widget_cycle.setTabsClosable(False)
        self.tab_widget_cycle.setMovable(False)
        self.tab_widget_cycle.setTabBarAutoHide(True)
        self.tab_cycle = QWidget()
        self.tab_cycle.setObjectName(u"tab_cycle")
        self.tab_cycle.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.tab_cycle)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.tab_cycle)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame)
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.cb_kiln_cycle = QComboBox(self.frame)
        self.cb_kiln_cycle.setObjectName(u"cb_kiln_cycle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_kiln_cycle.sizePolicy().hasHeightForWidth())
        self.cb_kiln_cycle.setSizePolicy(sizePolicy1)
        self.cb_kiln_cycle.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_3.addWidget(self.cb_kiln_cycle)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.txt_cycle_cycle = QLineEdit(self.frame)
        self.txt_cycle_cycle.setObjectName(u"txt_cycle_cycle")

        self.horizontalLayout_5.addWidget(self.txt_cycle_cycle)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.cb_entry_date_cycle = CustomComboBox(self.frame)
        self.cb_entry_date_cycle.setObjectName(u"cb_entry_date_cycle")
        self.cb_entry_date_cycle.setMinimumSize(QSize(100, 0))
        self.cb_entry_date_cycle.setEditable(True)
        self.cb_entry_date_cycle.setInsertPolicy(QComboBox.NoInsert)
        self.cb_entry_date_cycle.setFrame(True)

        self.horizontalLayout_9.addWidget(self.cb_entry_date_cycle)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.cb_exit_date_cycle = CustomComboBox(self.frame)
        self.cb_exit_date_cycle.setObjectName(u"cb_exit_date_cycle")
        self.cb_exit_date_cycle.setMinimumSize(QSize(100, 0))
        self.cb_exit_date_cycle.setEditable(True)
        self.cb_exit_date_cycle.setInsertPolicy(QComboBox.NoInsert)
        self.cb_exit_date_cycle.setFrame(True)

        self.horizontalLayout_10.addWidget(self.cb_exit_date_cycle)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rb_kd_cycle = QRadioButton(self.groupBox)
        self.rb_kd_cycle.setObjectName(u"rb_kd_cycle")
        self.rb_kd_cycle.setChecked(True)

        self.horizontalLayout.addWidget(self.rb_kd_cycle)

        self.rb_ht_cycle = QRadioButton(self.groupBox)
        self.rb_ht_cycle.setObjectName(u"rb_ht_cycle")

        self.horizontalLayout.addWidget(self.rb_ht_cycle)


        self.horizontalLayout_11.addWidget(self.groupBox)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addWidget(self.frame)

        self.frame_13 = QFrame(self.tab_cycle)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)

        self.gridLayout_12.addWidget(self.label_59, 0, 0, 1, 1)

        self.label_58 = QLabel(self.frame_13)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_12.addWidget(self.label_58, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.txt_volume_cycle = QLineEdit(self.frame_13)
        self.txt_volume_cycle.setObjectName(u"txt_volume_cycle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txt_volume_cycle.sizePolicy().hasHeightForWidth())
        self.txt_volume_cycle.setSizePolicy(sizePolicy3)
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

        self.txt_packs_cycle = QLineEdit(self.frame_13)
        self.txt_packs_cycle.setObjectName(u"txt_packs_cycle")
        sizePolicy3.setHeightForWidth(self.txt_packs_cycle.sizePolicy().hasHeightForWidth())
        self.txt_packs_cycle.setSizePolicy(sizePolicy3)
        self.txt_packs_cycle.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_12.addWidget(self.txt_packs_cycle, 1, 1, 1, 1)

        self.txt_bitola_cycle = QLineEdit(self.frame_13)
        self.txt_bitola_cycle.setObjectName(u"txt_bitola_cycle")
        sizePolicy3.setHeightForWidth(self.txt_bitola_cycle.sizePolicy().hasHeightForWidth())
        self.txt_bitola_cycle.setSizePolicy(sizePolicy3)
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
        self.bt_add_bitola_cycle = QPushButton(self.frame_13)
        self.bt_add_bitola_cycle.setObjectName(u"bt_add_bitola_cycle")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bt_add_bitola_cycle.sizePolicy().hasHeightForWidth())
        self.bt_add_bitola_cycle.setSizePolicy(sizePolicy4)
        self.bt_add_bitola_cycle.setMinimumSize(QSize(0, 0))
        self.bt_add_bitola_cycle.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/add-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_add_bitola_cycle.setIcon(icon4)
        self.bt_add_bitola_cycle.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.bt_add_bitola_cycle)

        self.bt_remove_bitola_cycle = QPushButton(self.frame_13)
        self.bt_remove_bitola_cycle.setObjectName(u"bt_remove_bitola_cycle")
        sizePolicy4.setHeightForWidth(self.bt_remove_bitola_cycle.sizePolicy().hasHeightForWidth())
        self.bt_remove_bitola_cycle.setSizePolicy(sizePolicy4)
        self.bt_remove_bitola_cycle.setMinimumSize(QSize(0, 0))
        self.bt_remove_bitola_cycle.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/remove-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_remove_bitola_cycle.setIcon(icon5)
        self.bt_remove_bitola_cycle.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.bt_remove_bitola_cycle)


        self.gridLayout_14.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.tw_cycle = QTableWidget(self.frame_13)
        if (self.tw_cycle.columnCount() < 4):
            self.tw_cycle.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_cycle.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_cycle.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_cycle.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_cycle.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tw_cycle.setObjectName(u"tw_cycle")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tw_cycle.sizePolicy().hasHeightForWidth())
        self.tw_cycle.setSizePolicy(sizePolicy5)
        self.tw_cycle.setMinimumSize(QSize(400, 0))
        self.tw_cycle.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_cycle.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_cycle.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_cycle.setGridStyle(Qt.SolidLine)
        self.tw_cycle.setSortingEnabled(False)
        self.tw_cycle.setColumnCount(4)
        self.tw_cycle.verticalHeader().setVisible(False)

        self.gridLayout_14.addWidget(self.tw_cycle, 1, 2, 4, 15)


        self.horizontalLayout_16.addLayout(self.gridLayout_14)


        self.verticalLayout.addWidget(self.frame_13)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bt_new_cycle = QPushButton(self.tab_cycle)
        self.bt_new_cycle.setObjectName(u"bt_new_cycle")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bt_new_cycle.sizePolicy().hasHeightForWidth())
        self.bt_new_cycle.setSizePolicy(sizePolicy6)
        self.bt_new_cycle.setMinimumSize(QSize(0, 50))
        self.bt_new_cycle.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/new-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_new_cycle.setIcon(icon6)
        self.bt_new_cycle.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_new_cycle)

        self.bt_save_cycle = QPushButton(self.tab_cycle)
        self.bt_save_cycle.setObjectName(u"bt_save_cycle")
        sizePolicy6.setHeightForWidth(self.bt_save_cycle.sizePolicy().hasHeightForWidth())
        self.bt_save_cycle.setSizePolicy(sizePolicy6)
        self.bt_save_cycle.setMinimumSize(QSize(0, 50))
        self.bt_save_cycle.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/save-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_save_cycle.setIcon(icon7)
        self.bt_save_cycle.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_save_cycle)

        self.bt_delete_cycle = QPushButton(self.tab_cycle)
        self.bt_delete_cycle.setObjectName(u"bt_delete_cycle")
        sizePolicy6.setHeightForWidth(self.bt_delete_cycle.sizePolicy().hasHeightForWidth())
        self.bt_delete_cycle.setSizePolicy(sizePolicy6)
        self.bt_delete_cycle.setMinimumSize(QSize(0, 50))
        self.bt_delete_cycle.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/delete-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_delete_cycle.setIcon(icon8)
        self.bt_delete_cycle.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.bt_delete_cycle)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/tag-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_widget_cycle.addTab(self.tab_cycle, icon9, "")
        self.tab_historic_cycle = QWidget()
        self.tab_historic_cycle.setObjectName(u"tab_historic_cycle")
        self.verticalLayout_7 = QVBoxLayout(self.tab_historic_cycle)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.mp_cycle_historic = QStackedWidget(self.tab_historic_cycle)
        self.mp_cycle_historic.setObjectName(u"mp_cycle_historic")
        self.mp_cycle_historic.setStyleSheet(u"")
        self.page_cycle_historic = QWidget()
        self.page_cycle_historic.setObjectName(u"page_cycle_historic")
        self.verticalLayout_12 = QVBoxLayout(self.page_cycle_historic)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.page_cycle_historic)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 0, 0, -1)
        self.label_47 = QLabel(self.frame_14)
        self.label_47.setObjectName(u"label_47")
        sizePolicy.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_47)

        self.cb_kiln_cycle_history = QComboBox(self.frame_14)
        self.cb_kiln_cycle_history.setObjectName(u"cb_kiln_cycle_history")
        sizePolicy6.setHeightForWidth(self.cb_kiln_cycle_history.sizePolicy().hasHeightForWidth())
        self.cb_kiln_cycle_history.setSizePolicy(sizePolicy6)
        self.cb_kiln_cycle_history.setMinimumSize(QSize(90, 0))
        self.cb_kiln_cycle_history.setMaxVisibleItems(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_kiln_cycle_history)

        self.label_56 = QLabel(self.frame_14)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_56)

        self.cb_cycle_cycle_history = QComboBox(self.frame_14)
        self.cb_cycle_cycle_history.setObjectName(u"cb_cycle_cycle_history")
        sizePolicy6.setHeightForWidth(self.cb_cycle_cycle_history.sizePolicy().hasHeightForWidth())
        self.cb_cycle_cycle_history.setSizePolicy(sizePolicy6)
        self.cb_cycle_cycle_history.setMaxVisibleItems(10)
        self.cb_cycle_cycle_history.setFrame(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cb_cycle_cycle_history)


        self.horizontalLayout_17.addLayout(self.formLayout)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(-1, 0, 0, -1)
        self.label_46 = QLabel(self.frame_14)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_46)

        self.label_61 = QLabel(self.frame_14)
        self.label_61.setObjectName(u"label_61")
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_61)

        self.cb_entry_date_cycle_history = CustomComboBox(self.frame_14)
        self.cb_entry_date_cycle_history.setObjectName(u"cb_entry_date_cycle_history")
        self.cb_entry_date_cycle_history.setMinimumSize(QSize(100, 0))
        self.cb_entry_date_cycle_history.setEditable(True)
        self.cb_entry_date_cycle_history.setInsertPolicy(QComboBox.NoInsert)
        self.cb_entry_date_cycle_history.setFrame(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.cb_entry_date_cycle_history)

        self.cb_exit_date_cycle_history = CustomComboBox(self.frame_14)
        self.cb_exit_date_cycle_history.setObjectName(u"cb_exit_date_cycle_history")
        self.cb_exit_date_cycle_history.setMinimumSize(QSize(100, 0))
        self.cb_exit_date_cycle_history.setEditable(True)
        self.cb_exit_date_cycle_history.setInsertPolicy(QComboBox.NoInsert)
        self.cb_exit_date_cycle_history.setFrame(True)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.cb_exit_date_cycle_history)


        self.horizontalLayout_17.addLayout(self.formLayout_6)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(-1, 0, 0, -1)
        self.label_60 = QLabel(self.frame_14)
        self.label_60.setObjectName(u"label_60")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_60)

        self.label_51 = QLabel(self.frame_14)
        self.label_51.setObjectName(u"label_51")
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_51)

        self.txt_bitola_cycle_history = QLineEdit(self.frame_14)
        self.txt_bitola_cycle_history.setObjectName(u"txt_bitola_cycle_history")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.txt_bitola_cycle_history)

        self.groupBox_5 = QGroupBox(self.frame_14)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setMaximumSize(QSize(16777215, 33))
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.rb_kd_cycle_history = QRadioButton(self.groupBox_5)
        self.rb_kd_cycle_history.setObjectName(u"rb_kd_cycle_history")
        sizePolicy1.setHeightForWidth(self.rb_kd_cycle_history.sizePolicy().hasHeightForWidth())
        self.rb_kd_cycle_history.setSizePolicy(sizePolicy1)
        self.rb_kd_cycle_history.setChecked(True)

        self.horizontalLayout_19.addWidget(self.rb_kd_cycle_history)

        self.rb_ht_cycle_history = QRadioButton(self.groupBox_5)
        self.rb_ht_cycle_history.setObjectName(u"rb_ht_cycle_history")

        self.horizontalLayout_19.addWidget(self.rb_ht_cycle_history)


        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.groupBox_5)


        self.horizontalLayout_17.addLayout(self.formLayout_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, 0, -1)
        self.bt_search_cycle_history = QPushButton(self.frame_14)
        self.bt_search_cycle_history.setObjectName(u"bt_search_cycle_history")
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/search-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_search_cycle_history.setIcon(icon10)
        self.bt_search_cycle_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.bt_search_cycle_history)

        self.bt_clear_cycle_history = QPushButton(self.frame_14)
        self.bt_clear_cycle_history.setObjectName(u"bt_clear_cycle_history")
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/erase-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_clear_cycle_history.setIcon(icon11)
        self.bt_clear_cycle_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.bt_clear_cycle_history)

        self.bt_edit_cycle_history = QPushButton(self.frame_14)
        self.bt_edit_cycle_history.setObjectName(u"bt_edit_cycle_history")
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/edit-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_edit_cycle_history.setIcon(icon12)
        self.bt_edit_cycle_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.bt_edit_cycle_history)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_21)


        self.verticalLayout_12.addWidget(self.frame_14)

        self.tv_cycle_history = QTableView(self.page_cycle_historic)
        self.tv_cycle_history.setObjectName(u"tv_cycle_history")
        self.tv_cycle_history.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_cycle_history.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_cycle_history.setShowGrid(True)
        self.tv_cycle_history.horizontalHeader().setDefaultSectionSize(80)
        self.tv_cycle_history.horizontalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_12.addWidget(self.tv_cycle_history)

        self.mp_cycle_historic.addWidget(self.page_cycle_historic)
        self.page_cycle_track_historic = QWidget()
        self.page_cycle_track_historic.setObjectName(u"page_cycle_track_historic")
        self.verticalLayout_13 = QVBoxLayout(self.page_cycle_track_historic)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.page_cycle_track_historic)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy3.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy3)
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.label_62 = QLabel(self.frame_15)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_62)

        self.label_63 = QLabel(self.frame_15)
        self.label_63.setObjectName(u"label_63")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_63)

        self.txt_kiln_track_history = QLineEdit(self.frame_15)
        self.txt_kiln_track_history.setObjectName(u"txt_kiln_track_history")
        self.txt_kiln_track_history.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.txt_kiln_track_history)

        self.txt_cycle_track_history = QLineEdit(self.frame_15)
        self.txt_cycle_track_history.setObjectName(u"txt_cycle_track_history")
        self.txt_cycle_track_history.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.txt_cycle_track_history)


        self.horizontalLayout_22.addLayout(self.formLayout_2)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.label_64 = QLabel(self.frame_15)
        self.label_64.setObjectName(u"label_64")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_64)

        self.label_65 = QLabel(self.frame_15)
        self.label_65.setObjectName(u"label_65")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_65)

        self.txt_exit_date_track_history = QLineEdit(self.frame_15)
        self.txt_exit_date_track_history.setObjectName(u"txt_exit_date_track_history")
        sizePolicy3.setHeightForWidth(self.txt_exit_date_track_history.sizePolicy().hasHeightForWidth())
        self.txt_exit_date_track_history.setSizePolicy(sizePolicy3)
        self.txt_exit_date_track_history.setReadOnly(True)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.txt_exit_date_track_history)

        self.txt_entry_date_track_history = QLineEdit(self.frame_15)
        self.txt_entry_date_track_history.setObjectName(u"txt_entry_date_track_history")
        sizePolicy3.setHeightForWidth(self.txt_entry_date_track_history.sizePolicy().hasHeightForWidth())
        self.txt_entry_date_track_history.setSizePolicy(sizePolicy3)
        self.txt_entry_date_track_history.setReadOnly(True)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.txt_entry_date_track_history)


        self.horizontalLayout_22.addLayout(self.formLayout_8)

        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.label_67 = QLabel(self.frame_15)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_67)

        self.label_66 = QLabel(self.frame_15)
        self.label_66.setObjectName(u"label_66")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_66)

        self.txt_bitola_track_history = QLineEdit(self.frame_15)
        self.txt_bitola_track_history.setObjectName(u"txt_bitola_track_history")
        self.txt_bitola_track_history.setReadOnly(True)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.txt_bitola_track_history)

        self.groupBox_6 = QGroupBox(self.frame_15)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(16777215, 33))
        self.horizontalLayout_24 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.rb_kd_track_history = QRadioButton(self.groupBox_6)
        self.rb_kd_track_history.setObjectName(u"rb_kd_track_history")
        self.rb_kd_track_history.setCheckable(True)
        self.rb_kd_track_history.setChecked(True)

        self.horizontalLayout_24.addWidget(self.rb_kd_track_history)

        self.rb_ht_track_history = QRadioButton(self.groupBox_6)
        self.rb_ht_track_history.setObjectName(u"rb_ht_track_history")
        self.rb_ht_track_history.setCheckable(False)

        self.horizontalLayout_24.addWidget(self.rb_ht_track_history)


        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.groupBox_6)


        self.horizontalLayout_22.addLayout(self.formLayout_9)

        self.horizontalSpacer_6 = QSpacerItem(94, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_6)

        self.bt_back_track_history = QPushButton(self.frame_15)
        self.bt_back_track_history.setObjectName(u"bt_back_track_history")
        self.bt_back_track_history.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/back-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_back_track_history.setIcon(icon13)
        self.bt_back_track_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_22.addWidget(self.bt_back_track_history)


        self.verticalLayout_13.addWidget(self.frame_15)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_7, 3, 1, 1, 1)

        self.tv_track_history = QTableView(self.page_cycle_track_historic)
        self.tv_track_history.setObjectName(u"tv_track_history")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tv_track_history.sizePolicy().hasHeightForWidth())
        self.tv_track_history.setSizePolicy(sizePolicy7)
        self.tv_track_history.setMinimumSize(QSize(560, 0))
        self.tv_track_history.setMaximumSize(QSize(16777215, 16777215))
        self.tv_track_history.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_track_history.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_21.addWidget(self.tv_track_history, 0, 0, 4, 1)

        self.frame_16 = QFrame(self.page_cycle_track_historic)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy3.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy3)
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_16)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_68 = QLabel(self.frame_16)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_22.addWidget(self.label_68, 1, 0, 1, 1)

        self.label_69 = QLabel(self.frame_16)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_22.addWidget(self.label_69, 2, 0, 1, 1)

        self.label_70 = QLabel(self.frame_16)
        self.label_70.setObjectName(u"label_70")
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_70, 0, 0, 1, 2)

        self.txt_leaving_date_track_history = QLineEdit(self.frame_16)
        self.txt_leaving_date_track_history.setObjectName(u"txt_leaving_date_track_history")
        sizePolicy4.setHeightForWidth(self.txt_leaving_date_track_history.sizePolicy().hasHeightForWidth())
        self.txt_leaving_date_track_history.setSizePolicy(sizePolicy4)
        self.txt_leaving_date_track_history.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_22.addWidget(self.txt_leaving_date_track_history, 1, 1, 1, 1)

        self.txt_leaving_volume_track_history = QLineEdit(self.frame_16)
        self.txt_leaving_volume_track_history.setObjectName(u"txt_leaving_volume_track_history")
        sizePolicy4.setHeightForWidth(self.txt_leaving_volume_track_history.sizePolicy().hasHeightForWidth())
        self.txt_leaving_volume_track_history.setSizePolicy(sizePolicy4)
        self.txt_leaving_volume_track_history.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_22.addWidget(self.txt_leaving_volume_track_history, 2, 1, 1, 1)


        self.gridLayout_21.addWidget(self.frame_16, 0, 1, 1, 1)

        self.frame_17 = QFrame(self.page_cycle_track_historic)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QSize(0, 40))
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_17)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_71 = QLabel(self.frame_17)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_23.addWidget(self.label_71, 2, 0, 1, 1)

        self.label_72 = QLabel(self.frame_17)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_72, 0, 0, 1, 2)

        self.txt_stock_volume_track_history = QLineEdit(self.frame_17)
        self.txt_stock_volume_track_history.setObjectName(u"txt_stock_volume_track_history")
        sizePolicy4.setHeightForWidth(self.txt_stock_volume_track_history.sizePolicy().hasHeightForWidth())
        self.txt_stock_volume_track_history.setSizePolicy(sizePolicy4)
        self.txt_stock_volume_track_history.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_23.addWidget(self.txt_stock_volume_track_history, 2, 1, 1, 1)


        self.gridLayout_21.addWidget(self.frame_17, 2, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_21)

        self.mp_cycle_historic.addWidget(self.page_cycle_track_historic)

        self.verticalLayout_7.addWidget(self.mp_cycle_historic)

        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/history-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_widget_cycle.addTab(self.tab_historic_cycle, icon14, "")

        self.verticalLayout_3.addWidget(self.tab_widget_cycle)

        self.mp_main.addWidget(self.page_cycle)
        self.page_nfe = QWidget()
        self.page_nfe.setObjectName(u"page_nfe")
        self.verticalLayout_5 = QVBoxLayout(self.page_nfe)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tab_widget_nfe = QTabWidget(self.page_nfe)
        self.tab_widget_nfe.setObjectName(u"tab_widget_nfe")
        self.tab_nfe = QWidget()
        self.tab_nfe.setObjectName(u"tab_nfe")
        self.verticalLayout_18 = QVBoxLayout(self.tab_nfe)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_2 = QFrame(self.tab_nfe)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.cb_date_nfe = CustomComboBox(self.frame_2)
        self.cb_date_nfe.setObjectName(u"cb_date_nfe")
        self.cb_date_nfe.setMinimumSize(QSize(100, 0))
        self.cb_date_nfe.setEditable(True)
        self.cb_date_nfe.setInsertPolicy(QComboBox.NoInsert)
        self.cb_date_nfe.setFrame(True)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.cb_date_nfe)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.cb_client_nfe = QComboBox(self.frame_2)
        self.cb_client_nfe.setObjectName(u"cb_client_nfe")
        sizePolicy6.setHeightForWidth(self.cb_client_nfe.sizePolicy().hasHeightForWidth())
        self.cb_client_nfe.setSizePolicy(sizePolicy6)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.cb_client_nfe)


        self.horizontalLayout_23.addLayout(self.formLayout_7)

        self.formLayout_15 = QFormLayout()
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.formLayout_15.setContentsMargins(-1, -1, 0, -1)
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_15.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_15.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.txt_nfe_nfe = QLineEdit(self.frame_2)
        self.txt_nfe_nfe.setObjectName(u"txt_nfe_nfe")

        self.formLayout_15.setWidget(0, QFormLayout.FieldRole, self.txt_nfe_nfe)

        self.txt_total_volume_nfe = QLineEdit(self.frame_2)
        self.txt_total_volume_nfe.setObjectName(u"txt_total_volume_nfe")

        self.formLayout_15.setWidget(1, QFormLayout.FieldRole, self.txt_total_volume_nfe)


        self.horizontalLayout_23.addLayout(self.formLayout_15)

        self.formLayout_16 = QFormLayout()
        self.formLayout_16.setObjectName(u"formLayout_16")
        self.formLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_16.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_16.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.txt_packs_nfe = QLineEdit(self.frame_2)
        self.txt_packs_nfe.setObjectName(u"txt_packs_nfe")

        self.formLayout_16.setWidget(0, QFormLayout.FieldRole, self.txt_packs_nfe)

        self.cb_foot_nfe = QComboBox(self.frame_2)
        self.cb_foot_nfe.setObjectName(u"cb_foot_nfe")

        self.formLayout_16.setWidget(1, QFormLayout.FieldRole, self.cb_foot_nfe)


        self.horizontalLayout_23.addLayout(self.formLayout_16)


        self.verticalLayout_18.addWidget(self.frame_2)

        self.frame_12 = QFrame(self.tab_nfe)
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
        self.txt_rework_nfe = QLineEdit(self.frame_12)
        self.txt_rework_nfe.setObjectName(u"txt_rework_nfe")
        sizePolicy3.setHeightForWidth(self.txt_rework_nfe.sizePolicy().hasHeightForWidth())
        self.txt_rework_nfe.setSizePolicy(sizePolicy3)
        self.txt_rework_nfe.setMinimumSize(QSize(0, 0))
        self.txt_rework_nfe.setMaximumSize(QSize(16777215, 16777215))
        self.txt_rework_nfe.setFont(font2)
        self.txt_rework_nfe.setFrame(True)
        self.txt_rework_nfe.setEchoMode(QLineEdit.Normal)
        self.txt_rework_nfe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_rework_nfe.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.txt_rework_nfe.setClearButtonEnabled(False)

        self.gridLayout_7.addWidget(self.txt_rework_nfe, 3, 1, 1, 1)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)

        self.cb_bitola_nfe = QComboBox(self.frame_12)
        self.cb_bitola_nfe.setObjectName(u"cb_bitola_nfe")
        sizePolicy3.setHeightForWidth(self.cb_bitola_nfe.sizePolicy().hasHeightForWidth())
        self.cb_bitola_nfe.setSizePolicy(sizePolicy3)
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

        self.txt_volume_nfe = QLineEdit(self.frame_12)
        self.txt_volume_nfe.setObjectName(u"txt_volume_nfe")
        sizePolicy3.setHeightForWidth(self.txt_volume_nfe.sizePolicy().hasHeightForWidth())
        self.txt_volume_nfe.setSizePolicy(sizePolicy3)
        self.txt_volume_nfe.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.txt_volume_nfe, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)

        self.cb_cycle_nfe = QComboBox(self.frame_12)
        self.cb_cycle_nfe.setObjectName(u"cb_cycle_nfe")
        sizePolicy3.setHeightForWidth(self.cb_cycle_nfe.sizePolicy().hasHeightForWidth())
        self.cb_cycle_nfe.setSizePolicy(sizePolicy3)
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
        self.bt_add_bitola_nfe = QPushButton(self.frame_12)
        self.bt_add_bitola_nfe.setObjectName(u"bt_add_bitola_nfe")
        sizePolicy4.setHeightForWidth(self.bt_add_bitola_nfe.sizePolicy().hasHeightForWidth())
        self.bt_add_bitola_nfe.setSizePolicy(sizePolicy4)
        self.bt_add_bitola_nfe.setMinimumSize(QSize(0, 0))
        self.bt_add_bitola_nfe.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_add_bitola_nfe.setIcon(icon4)
        self.bt_add_bitola_nfe.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.bt_add_bitola_nfe)

        self.bt_remove_bitola_nfe = QPushButton(self.frame_12)
        self.bt_remove_bitola_nfe.setObjectName(u"bt_remove_bitola_nfe")
        sizePolicy4.setHeightForWidth(self.bt_remove_bitola_nfe.sizePolicy().hasHeightForWidth())
        self.bt_remove_bitola_nfe.setSizePolicy(sizePolicy4)
        self.bt_remove_bitola_nfe.setMinimumSize(QSize(0, 0))
        self.bt_remove_bitola_nfe.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_remove_bitola_nfe.setIcon(icon5)
        self.bt_remove_bitola_nfe.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.bt_remove_bitola_nfe)


        self.gridLayout_6.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.tw_nfe = QTableWidget(self.frame_12)
        if (self.tw_nfe.columnCount() < 5):
            self.tw_nfe.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_nfe.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_nfe.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_nfe.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_nfe.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tw_nfe.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tw_nfe.setObjectName(u"tw_nfe")
        sizePolicy5.setHeightForWidth(self.tw_nfe.sizePolicy().hasHeightForWidth())
        self.tw_nfe.setSizePolicy(sizePolicy5)
        self.tw_nfe.setMinimumSize(QSize(400, 0))
        self.tw_nfe.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_nfe.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_nfe.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_nfe.horizontalHeader().setVisible(True)
        self.tw_nfe.horizontalHeader().setCascadingSectionResizes(False)
        self.tw_nfe.horizontalHeader().setHighlightSections(False)
        self.tw_nfe.horizontalHeader().setProperty("showSortIndicator", False)
        self.tw_nfe.horizontalHeader().setStretchLastSection(False)
        self.tw_nfe.verticalHeader().setVisible(False)
        self.tw_nfe.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_6.addWidget(self.tw_nfe, 1, 2, 4, 15)


        self.horizontalLayout_15.addLayout(self.gridLayout_6)


        self.verticalLayout_18.addWidget(self.frame_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.bt_new_nfe = QPushButton(self.tab_nfe)
        self.bt_new_nfe.setObjectName(u"bt_new_nfe")
        self.bt_new_nfe.setMinimumSize(QSize(0, 50))
        self.bt_new_nfe.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_new_nfe.setIcon(icon6)
        self.bt_new_nfe.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_new_nfe)

        self.bt_save_nfe = QPushButton(self.tab_nfe)
        self.bt_save_nfe.setObjectName(u"bt_save_nfe")
        self.bt_save_nfe.setMinimumSize(QSize(0, 50))
        self.bt_save_nfe.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_save_nfe.setIcon(icon7)
        self.bt_save_nfe.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_save_nfe)

        self.bt_delete_nfe = QPushButton(self.tab_nfe)
        self.bt_delete_nfe.setObjectName(u"bt_delete_nfe")
        self.bt_delete_nfe.setMinimumSize(QSize(0, 50))
        self.bt_delete_nfe.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_delete_nfe.setIcon(icon8)
        self.bt_delete_nfe.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_delete_nfe)


        self.verticalLayout_18.addLayout(self.horizontalLayout_8)

        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/document-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_widget_nfe.addTab(self.tab_nfe, icon15, "")
        self.tab_historic_nfe = QWidget()
        self.tab_historic_nfe.setObjectName(u"tab_historic_nfe")
        self.verticalLayout_8 = QVBoxLayout(self.tab_historic_nfe)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_24 = QFrame(self.tab_historic_nfe)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy3.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy3)
        self.frame_24.setMinimumSize(QSize(0, 0))
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setFrameShape(QFrame.Box)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.label_97 = QLabel(self.frame_24)
        self.label_97.setObjectName(u"label_97")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_97)

        self.label_95 = QLabel(self.frame_24)
        self.label_95.setObjectName(u"label_95")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_95)

        self.txt_nfe_nfe_history = QLineEdit(self.frame_24)
        self.txt_nfe_nfe_history.setObjectName(u"txt_nfe_nfe_history")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.txt_nfe_nfe_history)

        self.cb_client_nfe_history = QComboBox(self.frame_24)
        self.cb_client_nfe_history.setObjectName(u"cb_client_nfe_history")

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.cb_client_nfe_history)


        self.horizontalLayout_35.addLayout(self.formLayout_10)

        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.label_94 = QLabel(self.frame_24)
        self.label_94.setObjectName(u"label_94")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_94)

        self.label_93 = QLabel(self.frame_24)
        self.label_93.setObjectName(u"label_93")

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.label_93)

        self.cb_start_date_nfe_history = CustomComboBox(self.frame_24)
        self.cb_start_date_nfe_history.setObjectName(u"cb_start_date_nfe_history")
        sizePolicy6.setHeightForWidth(self.cb_start_date_nfe_history.sizePolicy().hasHeightForWidth())
        self.cb_start_date_nfe_history.setSizePolicy(sizePolicy6)
        self.cb_start_date_nfe_history.setMinimumSize(QSize(100, 0))
        self.cb_start_date_nfe_history.setEditable(True)
        self.cb_start_date_nfe_history.setInsertPolicy(QComboBox.NoInsert)
        self.cb_start_date_nfe_history.setFrame(True)

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.cb_start_date_nfe_history)

        self.cb_end_date_nfe_history = CustomComboBox(self.frame_24)
        self.cb_end_date_nfe_history.setObjectName(u"cb_end_date_nfe_history")
        sizePolicy6.setHeightForWidth(self.cb_end_date_nfe_history.sizePolicy().hasHeightForWidth())
        self.cb_end_date_nfe_history.setSizePolicy(sizePolicy6)
        self.cb_end_date_nfe_history.setMinimumSize(QSize(100, 0))
        self.cb_end_date_nfe_history.setEditable(True)
        self.cb_end_date_nfe_history.setInsertPolicy(QComboBox.NoInsert)
        self.cb_end_date_nfe_history.setFrame(True)

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.cb_end_date_nfe_history)


        self.horizontalLayout_35.addLayout(self.formLayout_11)

        self.formLayout_12 = QFormLayout()
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.label_96 = QLabel(self.frame_24)
        self.label_96.setObjectName(u"label_96")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.label_96)

        self.cb_foot_nfe_history = QComboBox(self.frame_24)
        self.cb_foot_nfe_history.setObjectName(u"cb_foot_nfe_history")

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.cb_foot_nfe_history)


        self.horizontalLayout_35.addLayout(self.formLayout_12)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, -1, 0, -1)
        self.bt_search_nfe_history = QPushButton(self.frame_24)
        self.bt_search_nfe_history.setObjectName(u"bt_search_nfe_history")
        self.bt_search_nfe_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_search_nfe_history.setIcon(icon10)
        self.bt_search_nfe_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_36.addWidget(self.bt_search_nfe_history)

        self.bt_clear_nfe_history = QPushButton(self.frame_24)
        self.bt_clear_nfe_history.setObjectName(u"bt_clear_nfe_history")
        self.bt_clear_nfe_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_clear_nfe_history.setIcon(icon11)
        self.bt_clear_nfe_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_36.addWidget(self.bt_clear_nfe_history)

        self.bt_edit_nfe_history = QPushButton(self.frame_24)
        self.bt_edit_nfe_history.setObjectName(u"bt_edit_nfe_history")
        self.bt_edit_nfe_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_edit_nfe_history.setIcon(icon12)
        self.bt_edit_nfe_history.setIconSize(QSize(32, 32))

        self.horizontalLayout_36.addWidget(self.bt_edit_nfe_history)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_36)


        self.verticalLayout_8.addWidget(self.frame_24)

        self.tv_nfe_history = QTableView(self.tab_historic_nfe)
        self.tv_nfe_history.setObjectName(u"tv_nfe_history")
        self.tv_nfe_history.setMinimumSize(QSize(0, 0))
        self.tv_nfe_history.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_nfe_history.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_nfe_history.horizontalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_8.addWidget(self.tv_nfe_history)

        self.tab_widget_nfe.addTab(self.tab_historic_nfe, icon14, "")

        self.verticalLayout_5.addWidget(self.tab_widget_nfe)

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
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_12.addWidget(self.label_20)

        self.cb_cycle_stock = QComboBox(self.frame_3)
        self.cb_cycle_stock.setObjectName(u"cb_cycle_stock")
        sizePolicy6.setHeightForWidth(self.cb_cycle_stock.sizePolicy().hasHeightForWidth())
        self.cb_cycle_stock.setSizePolicy(sizePolicy6)
        self.cb_cycle_stock.setMaxVisibleItems(10)

        self.horizontalLayout_12.addWidget(self.cb_cycle_stock)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, 0, -1)
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_14.addWidget(self.label_22)

        self.cb_bitola_stock = QComboBox(self.frame_3)
        self.cb_bitola_stock.setObjectName(u"cb_bitola_stock")
        sizePolicy6.setHeightForWidth(self.cb_bitola_stock.sizePolicy().hasHeightForWidth())
        self.cb_bitola_stock.setSizePolicy(sizePolicy6)

        self.horizontalLayout_14.addWidget(self.cb_bitola_stock)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_13.addWidget(self.label_21)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rb_kd_stock = QRadioButton(self.groupBox_2)
        self.rb_kd_stock.setObjectName(u"rb_kd_stock")
        self.rb_kd_stock.setChecked(True)

        self.horizontalLayout_4.addWidget(self.rb_kd_stock)

        self.rb_ht_stock = QRadioButton(self.groupBox_2)
        self.rb_ht_stock.setObjectName(u"rb_ht_stock")

        self.horizontalLayout_4.addWidget(self.rb_ht_stock)


        self.horizontalLayout_13.addWidget(self.groupBox_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, 0, -1)
        self.bt_search_stock = QPushButton(self.frame_3)
        self.bt_search_stock.setObjectName(u"bt_search_stock")
        sizePolicy4.setHeightForWidth(self.bt_search_stock.sizePolicy().hasHeightForWidth())
        self.bt_search_stock.setSizePolicy(sizePolicy4)
        self.bt_search_stock.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_search_stock.setIcon(icon10)
        self.bt_search_stock.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.bt_search_stock)

        self.bt_clear_stock = QPushButton(self.frame_3)
        self.bt_clear_stock.setObjectName(u"bt_clear_stock")
        sizePolicy4.setHeightForWidth(self.bt_clear_stock.sizePolicy().hasHeightForWidth())
        self.bt_clear_stock.setSizePolicy(sizePolicy4)
        self.bt_clear_stock.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_clear_stock.setIcon(icon11)
        self.bt_clear_stock.setIconSize(QSize(32, 32))

        self.horizontalLayout_20.addWidget(self.bt_clear_stock)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_20)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.tv_stock = QTableView(self.page_stock)
        self.tv_stock.setObjectName(u"tv_stock")
        self.tv_stock.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_stock.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_stock.horizontalHeader().setDefaultSectionSize(80)
        self.tv_stock.horizontalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.tv_stock)

        self.frame_4 = QFrame(self.page_stock)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_39.setSpacing(10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(-1, -1, 0, -1)
        self.bt_discount_stock = QPushButton(self.frame_4)
        self.bt_discount_stock.setObjectName(u"bt_discount_stock")
        self.bt_discount_stock.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_discount_stock.setIcon(icon15)
        self.bt_discount_stock.setIconSize(QSize(32, 32))

        self.horizontalLayout_38.addWidget(self.bt_discount_stock)

        self.bt_leaving_stock = QPushButton(self.frame_4)
        self.bt_leaving_stock.setObjectName(u"bt_leaving_stock")
        self.bt_leaving_stock.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/assets/recycling-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_leaving_stock.setIcon(icon16)
        self.bt_leaving_stock.setIconSize(QSize(32, 32))

        self.horizontalLayout_38.addWidget(self.bt_leaving_stock)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_38)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_3)

        self.formLayout_17 = QFormLayout()
        self.formLayout_17.setObjectName(u"formLayout_17")
        self.formLayout_17.setContentsMargins(-1, -1, 0, -1)
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_17.setWidget(0, QFormLayout.LabelRole, self.label_23)

        self.txt_treatment_stock = QLineEdit(self.frame_4)
        self.txt_treatment_stock.setObjectName(u"txt_treatment_stock")
        self.txt_treatment_stock.setReadOnly(True)

        self.formLayout_17.setWidget(0, QFormLayout.FieldRole, self.txt_treatment_stock)

        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_17.setWidget(1, QFormLayout.LabelRole, self.label_25)

        self.txt_leaving_stock = QLineEdit(self.frame_4)
        self.txt_leaving_stock.setObjectName(u"txt_leaving_stock")
        self.txt_leaving_stock.setReadOnly(True)

        self.formLayout_17.setWidget(1, QFormLayout.FieldRole, self.txt_leaving_stock)


        self.horizontalLayout_39.addLayout(self.formLayout_17)

        self.formLayout_18 = QFormLayout()
        self.formLayout_18.setObjectName(u"formLayout_18")
        self.formLayout_18.setContentsMargins(-1, -1, 0, -1)
        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_18.setWidget(0, QFormLayout.LabelRole, self.label_24)

        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_18.setWidget(1, QFormLayout.LabelRole, self.label_26)

        self.txt_sold_stock = QLineEdit(self.frame_4)
        self.txt_sold_stock.setObjectName(u"txt_sold_stock")
        self.txt_sold_stock.setReadOnly(True)

        self.formLayout_18.setWidget(0, QFormLayout.FieldRole, self.txt_sold_stock)

        self.txt_stock_stock = QLineEdit(self.frame_4)
        self.txt_stock_stock.setObjectName(u"txt_stock_stock")
        self.txt_stock_stock.setReadOnly(True)

        self.formLayout_18.setWidget(1, QFormLayout.FieldRole, self.txt_stock_stock)


        self.horizontalLayout_39.addLayout(self.formLayout_18)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.mp_main.addWidget(self.page_stock)

        self.gridLayout.addWidget(self.mp_main, 5, 1, 2, 1)

        self.fr_menu = QFrame(self.centralwidget)
        self.fr_menu.setObjectName(u"fr_menu")
        self.fr_menu.setMinimumSize(QSize(160, 0))
        self.fr_menu.setFrameShape(QFrame.Box)
        self.fr_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.fr_menu)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.bt_cycle_menu = QPushButton(self.fr_menu)
        self.bt_cycle_menu.setObjectName(u"bt_cycle_menu")
        sizePolicy1.setHeightForWidth(self.bt_cycle_menu.sizePolicy().hasHeightForWidth())
        self.bt_cycle_menu.setSizePolicy(sizePolicy1)
        self.bt_cycle_menu.setMinimumSize(QSize(0, 50))
        self.bt_cycle_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cycle_menu.setIcon(icon9)
        self.bt_cycle_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_cycle_menu)

        self.bt_nfe_menu = QPushButton(self.fr_menu)
        self.bt_nfe_menu.setObjectName(u"bt_nfe_menu")
        self.bt_nfe_menu.setMinimumSize(QSize(0, 50))
        self.bt_nfe_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_nfe_menu.setIcon(icon15)
        self.bt_nfe_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_nfe_menu)

        self.bt_stock_menu = QPushButton(self.fr_menu)
        self.bt_stock_menu.setObjectName(u"bt_stock_menu")
        self.bt_stock_menu.setMinimumSize(QSize(0, 50))
        self.bt_stock_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/assets/stock-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_stock_menu.setIcon(icon17)
        self.bt_stock_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_stock_menu)

        self.bt_kiln_menu = QPushButton(self.fr_menu)
        self.bt_kiln_menu.setObjectName(u"bt_kiln_menu")
        self.bt_kiln_menu.setMinimumSize(QSize(0, 50))
        self.bt_kiln_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/assets/stove-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_kiln_menu.setIcon(icon18)
        self.bt_kiln_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_kiln_menu)

        self.bt_client_menu = QPushButton(self.fr_menu)
        self.bt_client_menu.setObjectName(u"bt_client_menu")
        self.bt_client_menu.setMinimumSize(QSize(0, 50))
        self.bt_client_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/assets/customer-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_client_menu.setIcon(icon19)
        self.bt_client_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_client_menu)

        self.bt_exit_menu = QPushButton(self.fr_menu)
        self.bt_exit_menu.setObjectName(u"bt_exit_menu")
        self.bt_exit_menu.setMinimumSize(QSize(0, 50))
        self.bt_exit_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u":/icons/assets/exit-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_exit_menu.setIcon(icon20)
        self.bt_exit_menu.setIconSize(QSize(32, 32))

        self.verticalLayout_11.addWidget(self.bt_exit_menu)


        self.gridLayout.addWidget(self.fr_menu, 5, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.fr_menu.raise_()
        self.mp_main.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1006, 22))
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_config = QMenu(self.menubar)
        self.menu_config.setObjectName(u"menu_config")
        self.menu_db = QMenu(self.menu_config)
        self.menu_db.setObjectName(u"menu_db")
        icon21 = QIcon()
        icon21.addFile(u":/icons/assets/db.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_db.setIcon(icon21)
        MainWindow.setMenuBar(self.menubar)
#if QT_CONFIG(shortcut)
        self.label_9.setBuddy(self.cb_kiln_cycle)
        self.label_2.setBuddy(self.txt_cycle_cycle)
        self.label_3.setBuddy(self.cb_entry_date_cycle)
        self.label_4.setBuddy(self.cb_exit_date_cycle)
        self.label_5.setBuddy(self.rb_kd_cycle)
        self.label_59.setBuddy(self.txt_bitola_cycle)
        self.label_58.setBuddy(self.txt_volume_cycle)
        self.label_57.setBuddy(self.txt_packs_cycle)
        self.label_47.setBuddy(self.cb_kiln_cycle_history)
        self.label_56.setBuddy(self.cb_cycle_cycle_history)
        self.label_46.setBuddy(self.cb_entry_date_cycle_history)
        self.label_61.setBuddy(self.cb_exit_date_cycle_history)
        self.label_60.setBuddy(self.txt_bitola_cycle_history)
        self.label_51.setBuddy(self.rb_kd_cycle_history)
        self.label_13.setBuddy(self.cb_date_nfe)
        self.label_17.setBuddy(self.cb_client_nfe)
        self.label_16.setBuddy(self.txt_nfe_nfe)
        self.label_14.setBuddy(self.txt_total_volume_nfe)
        self.label_18.setBuddy(self.txt_packs_nfe)
        self.label_19.setBuddy(self.cb_foot_nfe)
        self.label_12.setBuddy(self.cb_cycle_nfe)
        self.label_11.setBuddy(self.cb_bitola_nfe)
        self.label_15.setBuddy(self.txt_rework_nfe)
        self.label_10.setBuddy(self.txt_volume_nfe)
        self.label_97.setBuddy(self.txt_nfe_nfe_history)
        self.label_95.setBuddy(self.cb_client_nfe_history)
        self.label_94.setBuddy(self.cb_start_date_nfe_history)
        self.label_93.setBuddy(self.cb_end_date_nfe_history)
        self.label_96.setBuddy(self.cb_foot_nfe_history)
        self.label_20.setBuddy(self.cb_cycle_stock)
        self.label_22.setBuddy(self.cb_bitola_stock)
        self.label_21.setBuddy(self.rb_kd_stock)
        self.label_23.setBuddy(self.txt_treatment_stock)
        self.label_25.setBuddy(self.txt_leaving_stock)
        self.label_24.setBuddy(self.txt_sold_stock)
        self.label_26.setBuddy(self.txt_stock_stock)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.bt_cycle_menu, self.bt_nfe_menu)
        QWidget.setTabOrder(self.bt_nfe_menu, self.bt_stock_menu)
        QWidget.setTabOrder(self.bt_stock_menu, self.bt_kiln_menu)
        QWidget.setTabOrder(self.bt_kiln_menu, self.bt_client_menu)
        QWidget.setTabOrder(self.bt_client_menu, self.bt_exit_menu)
        QWidget.setTabOrder(self.bt_exit_menu, self.tab_widget_cycle)
        QWidget.setTabOrder(self.tab_widget_cycle, self.cb_kiln_cycle)
        QWidget.setTabOrder(self.cb_kiln_cycle, self.txt_cycle_cycle)
        QWidget.setTabOrder(self.txt_cycle_cycle, self.cb_entry_date_cycle)
        QWidget.setTabOrder(self.cb_entry_date_cycle, self.cb_exit_date_cycle)
        QWidget.setTabOrder(self.cb_exit_date_cycle, self.rb_kd_cycle)
        QWidget.setTabOrder(self.rb_kd_cycle, self.rb_ht_cycle)
        QWidget.setTabOrder(self.rb_ht_cycle, self.txt_bitola_cycle)
        QWidget.setTabOrder(self.txt_bitola_cycle, self.txt_packs_cycle)
        QWidget.setTabOrder(self.txt_packs_cycle, self.txt_volume_cycle)
        QWidget.setTabOrder(self.txt_volume_cycle, self.bt_add_bitola_cycle)
        QWidget.setTabOrder(self.bt_add_bitola_cycle, self.bt_remove_bitola_cycle)
        QWidget.setTabOrder(self.bt_remove_bitola_cycle, self.tw_cycle)
        QWidget.setTabOrder(self.tw_cycle, self.bt_new_cycle)
        QWidget.setTabOrder(self.bt_new_cycle, self.bt_save_cycle)
        QWidget.setTabOrder(self.bt_save_cycle, self.bt_delete_cycle)
        QWidget.setTabOrder(self.bt_delete_cycle, self.cb_kiln_cycle_history)
        QWidget.setTabOrder(self.cb_kiln_cycle_history, self.cb_cycle_cycle_history)
        QWidget.setTabOrder(self.cb_cycle_cycle_history, self.cb_entry_date_cycle_history)
        QWidget.setTabOrder(self.cb_entry_date_cycle_history, self.cb_exit_date_cycle_history)
        QWidget.setTabOrder(self.cb_exit_date_cycle_history, self.txt_bitola_cycle_history)
        QWidget.setTabOrder(self.txt_bitola_cycle_history, self.rb_kd_cycle_history)
        QWidget.setTabOrder(self.rb_kd_cycle_history, self.rb_ht_cycle_history)
        QWidget.setTabOrder(self.rb_ht_cycle_history, self.bt_search_cycle_history)
        QWidget.setTabOrder(self.bt_search_cycle_history, self.bt_clear_cycle_history)
        QWidget.setTabOrder(self.bt_clear_cycle_history, self.bt_edit_cycle_history)
        QWidget.setTabOrder(self.bt_edit_cycle_history, self.tv_cycle_history)
        QWidget.setTabOrder(self.tv_cycle_history, self.tab_widget_nfe)
        QWidget.setTabOrder(self.tab_widget_nfe, self.cb_date_nfe)
        QWidget.setTabOrder(self.cb_date_nfe, self.cb_client_nfe)
        QWidget.setTabOrder(self.cb_client_nfe, self.txt_nfe_nfe)
        QWidget.setTabOrder(self.txt_nfe_nfe, self.txt_total_volume_nfe)
        QWidget.setTabOrder(self.txt_total_volume_nfe, self.txt_packs_nfe)
        QWidget.setTabOrder(self.txt_packs_nfe, self.cb_foot_nfe)
        QWidget.setTabOrder(self.cb_foot_nfe, self.cb_cycle_nfe)
        QWidget.setTabOrder(self.cb_cycle_nfe, self.cb_bitola_nfe)
        QWidget.setTabOrder(self.cb_bitola_nfe, self.txt_volume_nfe)
        QWidget.setTabOrder(self.txt_volume_nfe, self.txt_rework_nfe)
        QWidget.setTabOrder(self.txt_rework_nfe, self.bt_add_bitola_nfe)
        QWidget.setTabOrder(self.bt_add_bitola_nfe, self.bt_remove_bitola_nfe)
        QWidget.setTabOrder(self.bt_remove_bitola_nfe, self.tw_nfe)
        QWidget.setTabOrder(self.tw_nfe, self.bt_new_nfe)
        QWidget.setTabOrder(self.bt_new_nfe, self.bt_save_nfe)
        QWidget.setTabOrder(self.bt_save_nfe, self.bt_delete_nfe)
        QWidget.setTabOrder(self.bt_delete_nfe, self.txt_nfe_nfe_history)
        QWidget.setTabOrder(self.txt_nfe_nfe_history, self.cb_client_nfe_history)
        QWidget.setTabOrder(self.cb_client_nfe_history, self.cb_start_date_nfe_history)
        QWidget.setTabOrder(self.cb_start_date_nfe_history, self.cb_end_date_nfe_history)
        QWidget.setTabOrder(self.cb_end_date_nfe_history, self.cb_foot_nfe_history)
        QWidget.setTabOrder(self.cb_foot_nfe_history, self.bt_search_nfe_history)
        QWidget.setTabOrder(self.bt_search_nfe_history, self.bt_clear_nfe_history)
        QWidget.setTabOrder(self.bt_clear_nfe_history, self.bt_edit_nfe_history)
        QWidget.setTabOrder(self.bt_edit_nfe_history, self.cb_cycle_stock)
        QWidget.setTabOrder(self.cb_cycle_stock, self.cb_bitola_stock)
        QWidget.setTabOrder(self.cb_bitola_stock, self.rb_kd_stock)
        QWidget.setTabOrder(self.rb_kd_stock, self.rb_ht_stock)
        QWidget.setTabOrder(self.rb_ht_stock, self.bt_search_stock)
        QWidget.setTabOrder(self.bt_search_stock, self.bt_clear_stock)
        QWidget.setTabOrder(self.bt_clear_stock, self.tv_stock)
        QWidget.setTabOrder(self.tv_stock, self.bt_discount_stock)
        QWidget.setTabOrder(self.bt_discount_stock, self.bt_leaving_stock)
        QWidget.setTabOrder(self.bt_leaving_stock, self.txt_treatment_stock)
        QWidget.setTabOrder(self.txt_treatment_stock, self.txt_leaving_stock)
        QWidget.setTabOrder(self.txt_leaving_stock, self.txt_sold_stock)
        QWidget.setTabOrder(self.txt_sold_stock, self.txt_stock_stock)
        QWidget.setTabOrder(self.txt_stock_stock, self.tv_track_history)
        QWidget.setTabOrder(self.tv_track_history, self.rb_ht_track_history)
        QWidget.setTabOrder(self.rb_ht_track_history, self.bt_back_track_history)
        QWidget.setTabOrder(self.bt_back_track_history, self.txt_leaving_volume_track_history)
        QWidget.setTabOrder(self.txt_leaving_volume_track_history, self.txt_leaving_date_track_history)
        QWidget.setTabOrder(self.txt_leaving_date_track_history, self.txt_stock_volume_track_history)
        QWidget.setTabOrder(self.txt_stock_volume_track_history, self.txt_entry_date_track_history)
        QWidget.setTabOrder(self.txt_entry_date_track_history, self.txt_kiln_track_history)
        QWidget.setTabOrder(self.txt_kiln_track_history, self.rb_kd_track_history)
        QWidget.setTabOrder(self.rb_kd_track_history, self.txt_bitola_track_history)
        QWidget.setTabOrder(self.txt_bitola_track_history, self.txt_cycle_track_history)
        QWidget.setTabOrder(self.txt_cycle_track_history, self.txt_exit_date_track_history)

        self.menubar.addAction(self.menu_config.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_about.addAction(self.action_license)
        self.menu_config.addAction(self.menu_db.menuAction())
        self.menu_db.addAction(self.action_config)
        self.menu_db.addAction(self.action_import_backup)

        self.retranslateUi(MainWindow)

        self.mp_main.setCurrentIndex(2)
        self.tab_widget_cycle.setCurrentIndex(0)
        self.mp_cycle_historic.setCurrentIndex(0)
        self.tab_widget_nfe.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_kiln.setText(QCoreApplication.translate("MainWindow", u"Ver estufas", None))
        self.action_license.setText(QCoreApplication.translate("MainWindow", u"Licen\u00e7a", None))
        self.action_config.setText(QCoreApplication.translate("MainWindow", u"Configurar", None))
        self.action_import_backup.setText(QCoreApplication.translate("MainWindow", u"Importar backup", None))
        self.actionaa.setText(QCoreApplication.translate("MainWindow", u"aa", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CONTROLE DE MADEIRA TRATADA", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ESTUFA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ENTRADA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"FINALIDADE", None))
        self.groupBox.setTitle("")
        self.rb_kd_cycle.setText(QCoreApplication.translate("MainWindow", u"KD", None))
        self.rb_ht_cycle.setText(QCoreApplication.translate("MainWindow", u"HT", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.txt_volume_cycle.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"FARDOS", None))
        self.bt_add_bitola_cycle.setText("")
        self.bt_remove_bitola_cycle.setText("")
        ___qtablewidgetitem = self.tw_cycle.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tw_cycle.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None));
        ___qtablewidgetitem2 = self.tw_cycle.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"FARDOS", None));
        ___qtablewidgetitem3 = self.tw_cycle.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None));
        self.bt_new_cycle.setText(QCoreApplication.translate("MainWindow", u" NOVO", None))
        self.bt_save_cycle.setText(QCoreApplication.translate("MainWindow", u" SALVAR", None))
        self.bt_delete_cycle.setText(QCoreApplication.translate("MainWindow", u" DELETAR", None))
        self.tab_widget_cycle.setTabText(self.tab_widget_cycle.indexOf(self.tab_cycle), QCoreApplication.translate("MainWindow", u"CICLOS", None))
#if QT_CONFIG(tooltip)
        self.tab_widget_cycle.setTabToolTip(self.tab_widget_cycle.indexOf(self.tab_cycle), QCoreApplication.translate("MainWindow", u"CICLOS", None))
#endif // QT_CONFIG(tooltip)
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"ESTUFA", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"ENTRADA", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"FINALIDADE", None))
        self.groupBox_5.setTitle("")
        self.rb_kd_cycle_history.setText(QCoreApplication.translate("MainWindow", u"KD", None))
        self.rb_ht_cycle_history.setText(QCoreApplication.translate("MainWindow", u"HT", None))
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
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"ESTUFA", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"ENTRADA", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"SA\u00cdDA", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"FINALIDADE", None))
        self.groupBox_6.setTitle("")
        self.rb_kd_track_history.setText(QCoreApplication.translate("MainWindow", u"KD", None))
        self.rb_ht_track_history.setText(QCoreApplication.translate("MainWindow", u"HT", None))
        self.bt_back_track_history.setText("")
#if QT_CONFIG(shortcut)
        self.bt_back_track_history.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"MERCADO INTERNO", None))
        self.txt_leaving_date_track_history.setText("")
        self.txt_leaving_volume_track_history.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.txt_stock_volume_track_history.setText("")
        self.tab_widget_cycle.setTabText(self.tab_widget_cycle.indexOf(self.tab_historic_cycle), QCoreApplication.translate("MainWindow", u"HIST\u00d3RICO", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"NFE", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"VOLUME TOTAL", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"FARDOS", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CICLO PEZINHO", None))
        self.txt_rework_nfe.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"RETRABALHO", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None))
        self.bt_add_bitola_nfe.setText("")
        self.bt_remove_bitola_nfe.setText("")
        ___qtablewidgetitem4 = self.tw_nfe.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.tw_nfe.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CICLO", None));
        ___qtablewidgetitem6 = self.tw_nfe.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None));
        ___qtablewidgetitem7 = self.tw_nfe.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"VOLUME", None));
        ___qtablewidgetitem8 = self.tw_nfe.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"RETRABALHO", None));
        self.bt_new_nfe.setText(QCoreApplication.translate("MainWindow", u" NOVO", None))
        self.bt_save_nfe.setText(QCoreApplication.translate("MainWindow", u" SALVAR", None))
        self.bt_delete_nfe.setText(QCoreApplication.translate("MainWindow", u" DELETAR", None))
        self.tab_widget_nfe.setTabText(self.tab_widget_nfe.indexOf(self.tab_nfe), QCoreApplication.translate("MainWindow", u"NFE", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"NFE", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"DATA INICIAL", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"DATA FINAL", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"CICLO PEZINHO", None))
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
        self.tab_widget_nfe.setTabText(self.tab_widget_nfe.indexOf(self.tab_historic_nfe), QCoreApplication.translate("MainWindow", u"HIST\u00d3RICO", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"CICLO", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"BITOLA", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"FINALIDADE", None))
        self.groupBox_2.setTitle("")
        self.rb_kd_stock.setText(QCoreApplication.translate("MainWindow", u"KD", None))
        self.rb_ht_stock.setText(QCoreApplication.translate("MainWindow", u"HT", None))
        self.bt_search_stock.setText("")
        self.bt_clear_stock.setText("")
        self.bt_discount_stock.setText(QCoreApplication.translate("MainWindow", u" BAIXAR NFE", None))
        self.bt_leaving_stock.setText(QCoreApplication.translate("MainWindow", u" MERCADO INTERNO", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"VOLUME TRATADO", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RES\u00cdDUO", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"VOLUME VENDIDO", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.bt_cycle_menu.setText(QCoreApplication.translate("MainWindow", u" CICLOS", None))
        self.bt_nfe_menu.setText(QCoreApplication.translate("MainWindow", u" NFE", None))
        self.bt_stock_menu.setText(QCoreApplication.translate("MainWindow", u" ESTOQUE", None))
        self.bt_kiln_menu.setText(QCoreApplication.translate("MainWindow", u" ESTUFAS", None))
        self.bt_client_menu.setText(QCoreApplication.translate("MainWindow", u" CLIENTES", None))
        self.bt_exit_menu.setText(QCoreApplication.translate("MainWindow", u" SAIR", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.menu_config.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.menu_db.setTitle(QCoreApplication.translate("MainWindow", u"Banco de dados", None))
    # retranslateUi

