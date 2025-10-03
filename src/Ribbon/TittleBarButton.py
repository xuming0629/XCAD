#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   TittleBarButton.py
# @Time          :   2025/10/03 07:34:48
# @Author        :   XuMing
# @Version       :   1.1
# @Email         :   920972751@qq.com
# @Description   :   标题栏按钮类，支持 QSize、元组、列表作为 icon_size
# @Copyright     :   XuMing. All Rights Reserved.
# ****************************************************

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QToolButton
from PyQt5 import QtGui
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet


class TittleBarButton(QToolButton):
    def __init__(self, parent=None, object_name=None, icon_name=None,
                 icon_size=None, action_tip=None, action=None):
        super().__init__(parent)

        sc = gui_scale()
        self.setFixedSize(int(25 * sc), int(50 * sc))
        self.setStyleSheet(get_stylesheet("tittlebarButton"))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setIconSize(QSize(int(32 * sc), int(32 * sc)))

        self._create_icon_button(object_name, icon_name, icon_size, action_tip, action)

    def _create_icon_button(self, object_name, icon_name, icon_size, action_tip, action):
        self.setObjectName(object_name or "tittlebar_btn")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"./src/icons/{icon_name}.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)

        if icon_size:
            w, h = 32, 32
            if isinstance(icon_size, QSize):
                w, h = icon_size.width(), icon_size.height()
            elif isinstance(icon_size, (tuple, list)) and len(icon_size) == 2:
                w, h = int(icon_size[0]), int(icon_size[1])
            self.setIconSize(QSize(w, h))

        if action_tip:
            self.setToolTip(action_tip)

        if action:
            self.add_action(action)

    def add_action(self, action):
        if action:
            self.clicked.connect(action)


class TittleBarButton_windown(QToolButton):
    def __init__(self, parent=None, object_name=None, icon_name=None,
                 icon_size=None, action=None):
        super().__init__(parent)
        self.checked = 1

        sc = gui_scale()
        self.setFixedSize(int(30 * sc), int(50 * sc))
        self.setStyleSheet(get_stylesheet("tittlebarButtonWindown"))
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setIconSize(QSize(int(32 * sc), int(32 * sc)))

        self._create_icon_button(object_name, icon_name, icon_size)
        if action:
            self.add_action(action)

    def _create_icon_button(self, object_name, icon_name, icon_size):
        self.setObjectName(object_name or "tittlebar_wnd_btn")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"./Win64/icons/{icon_name}.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)

        if icon_size:
            w, h = 32, 32
            if isinstance(icon_size, QSize):
                w, h = icon_size.width(), icon_size.height()
            elif isinstance(icon_size, (tuple, list)) and len(icon_size) == 2:
                w, h = int(icon_size[0]), int(icon_size[1])
            self.setIconSize(QSize(w, h))

    def add_action(self, action_1=None, action_2=None):
        """支持单事件 或者 双事件切换"""
        if action_1 and action_2:
            def toggle_action():
                if self.checked == 1:
                    action_1()
                else:
                    action_2()
                self.checked *= -1
            self.clicked.connect(toggle_action)
        elif action_1:
            self.clicked.connect(action_1)


# ------------------- __main__ 测试 -------------------
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    def test_action():
        print("标题栏按钮被点击")

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.resize(300, 200)
    win.setWindowTitle("TittleBarButton 测试")

    btn = TittleBarButton(win, "test_btn", "view_top", (32, 32), "测试按钮", test_action)
    win.setCentralWidget(btn)

    win.show()
    sys.exit(app.exec_())
