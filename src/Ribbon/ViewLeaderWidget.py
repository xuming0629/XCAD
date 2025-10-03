#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   RibbonButton.py
@Time    :   2025/09/22 23:03:14
@Author  :   XuMing
@Version :   v1.1
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   Ribbon 自定义按钮，支持 QSize、列表/元组作为 icon_size
'''

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QToolButton
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet


class RibbonButton(QToolButton):
    def __init__(self, owner, action, is_large):
        super().__init__(owner)

        sc = gui_scale()

        self._actionOwner = action
        self.update_button_status_from_action()

        self.clicked.connect(self._actionOwner.trigger)
        self._actionOwner.changed.connect(self.update_button_status_from_action)

        if is_large:
            self.setMaximumWidth(int(80 * sc))
            self.setMinimumWidth(int(50 * sc))
            self.setMinimumHeight(int(75 * sc))
            self.setMaximumHeight(int(80 * sc))
            self.setIconSize(QSize(int(32*sc), int(32*sc)))
            self.setStyleSheet(get_stylesheet("ribbonButton"))
            self.setToolButtonStyle(3)  # 文本在图标下方
            self.setIconSize(QSize(int(32 * sc), int(32 * sc)))
        else:
            self.setToolButtonStyle(2)  # 文本在图标旁边
            self.setMaximumWidth(int(120 * sc))
            self.setIconSize(QSize(int(16*sc), int(16*sc)))
            self.setStyleSheet(get_stylesheet("ribbonSmallButton"))

    def update_button_status_from_action(self):
        self.setText(self._actionOwner.text())
        self.setStatusTip(self._actionOwner.statusTip())
        self.setToolTip(self._actionOwner.toolTip())
        self.setIcon(self._actionOwner.icon())
        self.setEnabled(self._actionOwner.isEnabled())
        self.setCheckable(self._actionOwner.isCheckable())
        self.setChecked(self._actionOwner.isChecked())


class ViewLeaderButton(QToolButton):
    def __init__(self, parent=None, object_name=None, icon_name=None,
                 icon_size=None, action_tip=None, action=None):
        super(ViewLeaderButton, self).__init__(parent)

        sc = gui_scale()
        size = int(38 * sc)
        self.setFixedSize(size, size)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.setStyleSheet("background-color: transparent;")

        self._create_icon_button(object_name, icon_name, icon_size, action_tip, action)

    def _create_icon_button(self, object_name, icon_name, icon_size, action_tip, action):
        self.setObjectName(object_name)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"icons/{icon_name}.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)

        if icon_size:
            if isinstance(icon_size, QSize):
                w, h = icon_size.width(), icon_size.height()
            elif isinstance(icon_size, (tuple, list)) and len(icon_size) == 2:
                w, h = int(icon_size[0]), int(icon_size[1])
            else:
                w, h = 32, 32
            self.setIconSize(QtCore.QSize(w, h))

        if action_tip:
            self.setToolTip(action_tip)

        if action:
            self.add_action(action)

    def add_action(self, action):
        self.clicked.connect(action)


# -------------------------- __main__ 测试 --------------------------
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    def on_click():
        print("按钮点击了")

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.resize(400, 300)
    main_window.setWindowTitle("ViewLeaderButton 测试")

    button = ViewLeaderButton(main_window, "testButton", "view_top", QSize(32, 32), "点击测试", on_click)
    main_window.setCentralWidget(button)

    main_window.show()
    sys.exit(app.exec_())
