#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   RibbonButton.py
@Time    :   2025/09/22 23:03:14
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   自定义 Ribbon 按钮，支持大按钮和小按钮样式，绑定 QAction。
'''

from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QToolButton

from src.Ribbon import gui_scale  # 用于获取界面缩放比例
from src.Ribbon.StyleSheets import get_stylesheet  # 获取 CSS 样式表


class RibbonButton(QToolButton):
    """
    自定义 Ribbon 按钮类
    支持大按钮和小按钮样式，绑定 QAction 实现状态同步
    """

    def __init__(self, owner, action, is_large: bool):
        """
        初始化 RibbonButton

        :param owner: 父窗口或父控件
        :param action: 关联的 QAction，对应按钮事件、图标、文本
        :param is_large: 是否为大按钮
        """
        super().__init__(owner)

        sc = gui_scale()  # 获取界面缩放比例
        self._actionOwner = action

        # 初始化按钮状态
        self.update_button_status_from_action()

        # 点击按钮时触发 QAction 的 trigger 信号
        self.clicked.connect(self._actionOwner.trigger)

        # 当 QAction 状态改变时，更新按钮状态
        self._actionOwner.changed.connect(self.update_button_status_from_action)

        if is_large:
            self._init_large_button(sc)
        else:
            self._init_small_button(sc)

    def _init_large_button(self, sc: float):
        """初始化大按钮样式"""
        self.setMaximumWidth(int(80 * sc))
        self.setMinimumWidth(int(50 * sc))
        self.setMinimumHeight(int(75 * sc))
        self.setMaximumHeight(int(80 * sc))

        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.setIconSize(QSize(int(32 * sc), int(32 * sc)))
        self.setStyleSheet(get_stylesheet("ribbonButton"))

    def _init_small_button(self, sc: float):
        """初始化小按钮样式"""
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.setMaximumWidth(int(120 * sc))
        self.setIconSize(QSize(int(16 * sc), int(16 * sc)))
        self.setStyleSheet(get_stylesheet("ribbonSmallButton"))

    def update_button_status_from_action(self):
        """
        根据关联的 QAction 更新按钮状态
        包括：文本、状态提示、工具提示、图标、是否可用、是否可选中
        """
        self.setText(self._actionOwner.text())
        self.setStatusTip(self._actionOwner.statusTip())
        self.setToolTip(self._actionOwner.toolTip())
        self.setIcon(self._actionOwner.icon())
        self.setEnabled(self._actionOwner.isEnabled())
        self.setCheckable(self._actionOwner.isCheckable())
        self.setChecked(self._actionOwner.isChecked())


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QAction, QMainWindow

    app = QApplication(sys.argv)

    main_window = QMainWindow()
    main_window.resize(400, 200)
    main_window.setWindowTitle("RibbonButton 测试")

    action = QAction("测试按钮", main_window)
    action.setToolTip("这是一个测试按钮")
    action.setStatusTip("按钮状态提示")
    action.setIcon(main_window.style().standardIcon(main_window.style().SP_ComputerIcon))

    def on_triggered():
        print("按钮触发了！")

    action.triggered.connect(on_triggered)

    ribbon_button_large = RibbonButton(main_window, action, is_large=True)
    ribbon_button_small = RibbonButton(main_window, action, is_large=False)

    main_window.setCentralWidget(ribbon_button_large)
    main_window.show()

    sys.exit(app.exec_())
