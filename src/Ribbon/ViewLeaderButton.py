#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   ViewLeaderButton.py
# @Time          :   2025/10/03 07:33:18
# @Author        :   XuMing
# @Version       :   1.1
# @Email         :   920972751@qq.com
# @Description   :   ViewLeaderButton 测试
# ****************************************************

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QToolButton, QApplication, QMainWindow, QHBoxLayout, QWidget
from PyQt5 import QtCore, QtGui
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet


class ViewLeaderButton(QToolButton):
    def __init__(self, parent=None, object_name=None, icon_name=None,
                 icon_size=None, action_tip=None, action=None):
        super(ViewLeaderButton, self).__init__(parent)

        sc = gui_scale()
        size = int(38 * sc)

        self.setFixedSize(size, size)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.setStyleSheet("background-color: transparent;")

        # 设置图标
        self._create_icon_button(object_name, icon_name, icon_size, action_tip, action)

    def _create_icon_button(self, object_name, icon_name, icon_size, action_tip, action):
        self.setObjectName(object_name)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"icons/{icon_name}.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)

        if icon_size:
            self.setIconSize(QtCore.QSize(int(icon_size[0]), int(icon_size[1])))

        if action_tip:
            self.setToolTip(action_tip)

        if action:
            self.add_action(action)

    def add_action(self, action):
        """给按钮绑定事件"""
        self.clicked.connect(action)


class TittleBarButton_windown(QToolButton):
    def __init__(self, parent=None, object_name=None, icon_name=None, icon_size=None, action=None):
        super().__init__(parent)
        self.checked = 1

        sc = gui_scale()
        self.setFixedSize(int(30 * sc), int(50 * sc))
        self.setStyleSheet(get_stylesheet("tittlebarButtonWindown"))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        self._create_icon_button(object_name, icon_name, icon_size)
        if action:
            self.add_action(action)

    def _create_icon_button(self, object_name, icon_name, icon_size):
        self.setObjectName(object_name)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"icons/{icon_name}.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)

        if icon_size:
            self.setIconSize(QtCore.QSize(int(icon_size[0]), int(icon_size[1])))

    def add_action(self, action_1=None, action_2=None):
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


if __name__ == "__main__":
    import sys

    def on_click():
        print("按钮被点击")

    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setWindowTitle("ViewLeaderButton 测试")
    main_win.resize(300, 200)

    central_widget = QWidget()
    layout = QHBoxLayout()
    central_widget.setLayout(layout)

    btn1 = ViewLeaderButton(main_win, "leaderBtn", "test_icon", (32, 32), "点击我", on_click)
    btn2 = TittleBarButton_windown(main_win, "titleBtn", "test_icon", (24, 24), on_click)

    layout.addWidget(btn1)
    layout.addWidget(btn2)

    main_win.setCentralWidget(central_widget)
    main_win.show()

    sys.exit(app.exec_())
