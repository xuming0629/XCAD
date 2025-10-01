#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : RibbonWidget.py
@Author  : XuMing
@Version : v1.0
@Contact : 920972751@qq.com
@License : Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    : Ribbon 主工具栏，包含多个 RibbonTab
"""

from PyQt5.QtWidgets import QToolBar, QTabWidget

from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet
from src.Ribbon.RibbonTab import RibbonTab


class RibbonWidget(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(get_stylesheet("ribbon"))
        self.setObjectName("ribbonWidget")
        self.setWindowTitle("Ribbon")

        # 内部的 QTabWidget
        self._ribbon_widget = QTabWidget(self)
        self._ribbon_widget.setMaximumHeight(120 * gui_scale())
        self._ribbon_widget.setMinimumHeight(110 * gui_scale())

        self.setMovable(False)
        self.addWidget(self._ribbon_widget)

        # 保存 tab 的字典
        self.ribbon_tab_dict = {}

    def add_ribbon_tab(self, name):
        """添加一个新的 RibbonTab"""
        tab = RibbonTab(self, name)
        tab.setObjectName("tab_" + name)
        self.ribbon_tab_dict[name] = tab
        self._ribbon_widget.addTab(tab, name)
        return tab

    def set_active(self, name):
        """切换到指定的 tab"""
        if name in self.ribbon_tab_dict:
            self._ribbon_widget.setCurrentWidget(self.ribbon_tab_dict[name])

    def add_ribbon_button(self, name):
        """预留接口：在 tab 中添加按钮"""
        pass
