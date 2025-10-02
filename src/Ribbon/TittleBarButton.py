#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   TittleBarButton.py
# @Time          :   2025/10/03 07:34:48
# @Author        :   XuMing
# @Version       :   1.0
# @Email         :   920972751@qq.com
# @Description   :   
# @Copyright     :   XuMing. All Rights Reserved.
# ****************************************************


from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QToolButton
from PyQt5 import QtGui
from Win64.Ribbon import gui_scale
from Win64.Ribbon.StyleSheets import get_stylesheet




class TittleBarButton(QToolButton):
    def __init__(self, parent=None, object_name=None, icon_name=None,
                 icon_size=None, action_tip=None, action=None):
        super(QToolButton, self).__init__(parent)

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
            self.setIconSize(QSize(int(icon_size[0]), int(icon_size[1])))

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
            self.setIconSize(QSize(int(icon_size[0]), int(icon_size[1])))

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
