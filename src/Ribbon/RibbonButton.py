#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   RibbonButton.py
@Time    :   2025/09/22 23:03:14
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   
'''


from PyQt5 import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *

from src.Ribbon import gui_scale  # 用于获取界面缩放比例
from src.Ribbon.StyleSheets import get_stylesheet  # 获取 CSS 样式表


class RibbonButton(QToolButton):
    """
    自定义 Ribbon 按钮，支持大按钮和小按钮样式
    绑定 QAction，实现文本、图标、状态同步
    """
    def __init__(self, owner, action, is_large):
        """
        :param owner: 父窗口或父控件
        :param action: 关联的 QAction，用于按钮事件、图标、文本
        :param is_large: 是否为大按钮
        """
        QPushButton.__init__(self, owner)  # 初始化 QToolButton 父类
        # sc = 1
        sc = gui_scale()  # 获取界面缩放比例

        # 保存关联的 QAction
        self._actionOwner = action

        # 根据 QAction 初始化按钮状态（文本、图标、是否可用等）
        self.update_button_status_from_action()

        # 点击按钮时触发 QAction 的 trigger 信号
        self.clicked.connect(self._actionOwner.trigger)

        # 当 QAction 状态改变时，同步更新按钮
        self._actionOwner.changed.connect(self.update_button_status_from_action)

        if is_large:
            # 大按钮尺寸设置
            self.setMaximumWidth(int(80 * sc))
            self.setMinimumWidth(int(50 * sc))
            self.setMinimumHeight(int(75 * sc))
            self.setMaximumHeight(int(80 * sc))
            self.setIconSize(QSize(int(32*sc), int(32*sc)))

            # 应用大按钮样式
            self.setStyleSheet(get_stylesheet("ribbonButton"))

            # 设置按钮文本和图标显示方式
            # 3 表示 Qt.ToolButtonTextUnderIcon，即文本在图标下方
            self.setToolButtonStyle(3)

            # 设置图标大小
            self.setIconSize(QSize(int(32 * sc), int(32 * sc)))
        else:
            # 小按钮尺寸设置
            self.setToolButtonStyle(2)  # 2 表示 Qt.ToolButtonTextBesideIcon，文本在图标旁边
            self.setMaximumWidth(int(120 * sc))
            self.setIconSize(QSize(int(16*sc), int(16*sc)))

            # 应用小按钮样式
            self.setStyleSheet(get_stylesheet("ribbonSmallButton"))

    def update_button_status_from_action(self):
        """
        根据关联的 QAction 更新按钮状态
        包括文本、状态提示、工具提示、图标、可用性、是否可选中
        """
        self.setText(self._actionOwner.text())  # 设置按钮文本
        self.setStatusTip(self._actionOwner.statusTip())  # 状态栏提示
        self.setToolTip(self._actionOwner.toolTip())  # 鼠标悬停提示
        self.setIcon(self._actionOwner.icon())  # 设置图标
        self.setEnabled(self._actionOwner.isEnabled())  # 是否可用
        self.setCheckable(self._actionOwner.isCheckable())  # 是否可切换选中状态
        self.setChecked(self._actionOwner.isChecked())  # 是否当前选中
