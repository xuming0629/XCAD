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

from PyQt5.QtWidgets import QToolBar, QTabWidget, QApplication, QWidget, QVBoxLayout
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet
from src.Ribbon.RibbonTab import RibbonTab


class RibbonWidget(QToolBar):
    """
    Ribbon 主工具栏
    ----------------
    包含一个 QTabWidget，可以添加多个 RibbonTab。
    提供切换 tab 的方法，以及预留接口添加按钮。
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(get_stylesheet("ribbon"))
        self.setObjectName("ribbonWidget")
        self.setWindowTitle("Ribbon")

        # 内部的 QTabWidget
        self._ribbon_widget = QTabWidget(self)
        self._ribbon_widget.setMaximumHeight(int(120 * gui_scale()))
        self._ribbon_widget.setMinimumHeight(int(110 * gui_scale()))

        self.setMovable(False)
        self.addWidget(self._ribbon_widget)

        # 保存 tab 的字典
        self.ribbon_tab_dict = {}

    def add_ribbon_tab(self, name):
        """
        添加一个新的 RibbonTab
        ----------------------
        :param name: tab 名称
        :return: RibbonTab 对象
        """
        tab = RibbonTab(self, name)
        tab.setObjectName("tab_" + name)
        self.ribbon_tab_dict[name] = tab
        self._ribbon_widget.addTab(tab, name)
        return tab

    def set_active(self, name):
        """
        切换到指定的 tab
        ----------------
        :param name: tab 名称
        """
        if name in self.ribbon_tab_dict:
            self._ribbon_widget.setCurrentWidget(self.ribbon_tab_dict[name])

    def add_ribbon_button(self, name):
        """
        预留接口：在 tab 中添加按钮
        -------------------------
        :param name: 按钮名称
        """
        pass


if __name__ == "__main__":
    """
    测试 RibbonWidget
    """
    import sys

    app = QApplication(sys.argv)
    main_window = QWidget()
    main_window.setWindowTitle("RibbonWidget 测试")
    main_window.resize(800, 600)

    layout = QVBoxLayout(main_window)

    ribbon = RibbonWidget(main_window)
    layout.addWidget(ribbon)

    # 添加测试 tab
    tab1 = ribbon.add_ribbon_tab("主页")
    tab2 = ribbon.add_ribbon_tab("绘图")

    # 切换到“绘图” tab
    ribbon.set_active("绘图")

    main_window.show()
    sys.exit(app.exec_())
