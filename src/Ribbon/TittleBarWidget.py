#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   TittleBarWidget.py
# @Time          :   2025/10/03 08:05:00
# @Author        :   XuMing
# @Version       :   1.0
# @Description   :   自定义标题栏 Toolbar
# ****************************************************

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QToolBar, QHBoxLayout, QWidget, QLabel
from PyQt5 import QtWidgets, QtGui
from src.Ribbon.RibbonTab import RibbonTab
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet
from src.Ribbon.TittleBarButton import TittleBarButton, TittleBarButton_windown


class TittleBarWidget(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet(get_stylesheet("ribbon"))
        self.setObjectName("TittleWidget")
        self.setWindowTitle("Tittle")

        self._Tittle_widget = QWidget(self)
        self._Tittle_widget.setMaximumHeight(int(37 * gui_scale()))
        self._Tittle_widget.setMinimumHeight(int(37 * gui_scale()))
        self.setMovable(False)
        self.addWidget(self._Tittle_widget)
        self.setStyleSheet("background-color: rgb(45, 93, 135);")

        HBOX = QHBoxLayout()
        HBOX_Logo = QHBoxLayout()
        HBOX_Left = QHBoxLayout()
        HBOX_Center = QHBoxLayout()
        HBOX_Right = QHBoxLayout()

        self._Tittle_widget.setLayout(HBOX)
        HBOX.addLayout(HBOX_Logo)
        HBOX.addLayout(HBOX_Left)
        HBOX.addLayout(HBOX_Center, 280)
        HBOX.addLayout(HBOX_Right, 0)

        # 测试按钮行为
        def dummy_action():
            print("按钮被点击！")

        # 左侧按钮
        self.folder_pushButton = TittleBarButton(self._Tittle_widget, "folder_pushButton", "folder", [20, 20], "打开", dummy_action)
        HBOX_Left.addWidget(self.folder_pushButton, 0)

        self.undo_pushButton = TittleBarButton(self._Tittle_widget, "undo_pushButton", "undo_system_bar", [20, 20], "撤销", dummy_action)
        HBOX_Left.addWidget(self.undo_pushButton, 0)

        self.redo_pushButton = TittleBarButton(self._Tittle_widget, "redo_pushButton", "redo_system_bar", [20, 20], "重做", dummy_action)
        HBOX_Left.addWidget(self.redo_pushButton, 0)

        self.save_pushButton = TittleBarButton(self._Tittle_widget, "save_pushButton", "save", [20, 20], "保存", dummy_action)
        HBOX_Left.addWidget(self.save_pushButton, 0)

        self.copy_pushButton = TittleBarButton(self._Tittle_widget, "copy_pushButton", "copy", [20, 20], "复制", dummy_action)
        HBOX_Left.addWidget(self.copy_pushButton, 0)

        self.paste_pushButton = TittleBarButton(self._Tittle_widget, "paste_pushButton", "paste", [20, 20], "黏贴", dummy_action)
        HBOX_Left.addWidget(self.paste_pushButton, 0)

        self.about_pushButton = TittleBarButton(self._Tittle_widget, "about_pushButton", "about", [20, 20], "关于", dummy_action)
        HBOX_Left.addWidget(self.about_pushButton, 0)

        # 右侧按钮
        self.winwownminimizing_pushButton = TittleBarButton_windown(self._Tittle_widget, "winwownminimizing", "winwownminimizing", [10, 10])
        HBOX_Right.addWidget(self.winwownminimizing_pushButton, 0, Qt.AlignVCenter)

        self.windownre_pushButton = TittleBarButton_windown(self._Tittle_widget, "windownre", "windownre", [10, 10])
        HBOX_Right.addWidget(self.windownre_pushButton, 0, Qt.AlignVCenter)

        self.exit_pushButton = TittleBarButton_windown(self._Tittle_widget, "exit_pushButton_5", "windowclose", [10, 10])
        HBOX_Right.addWidget(self.exit_pushButton, 0, Qt.AlignVCenter)

        # 中间标题
        self.label = QLabel("XCAD", self)
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        HBOX_Center.addWidget(self.label, 0, Qt.AlignCenter)

    def add_ribbon_tab(self, name):
        ribbon_tab = RibbonTab(self, name)
        ribbon_tab.setObjectName("tab_" + name)
        return ribbon_tab

    def set_active(self, name):
        self.setCurrentWidget(self.findChild("tab_" + name))


# ------------------- __main__ 测试 -------------------
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_win = QtWidgets.QMainWindow()
    tbar = TittleBarWidget(main_win)
    main_win.addToolBar(tbar)
    main_win.resize(800, 600)
    main_win.setWindowTitle("TittleBarWidget 测试")
    main_win.show()
    sys.exit(app.exec_())
