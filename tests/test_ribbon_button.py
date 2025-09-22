#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   test_ribbon_button.py
@Time    :   2025/09/22
@Author  :   XuMing
@Desc    :   手动测试 RibbonButton
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QAction
from PyQt5.QtGui import QIcon
from src.Ribbon.RibbonButton import RibbonButton
from src.Ribbon.Icons import get_icon



def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("RibbonButton 测试")
    central = QWidget()
    layout = QVBoxLayout(central)

    # 创建示例 QAction
    action_large = QAction(QIcon(get_icon("folder")), "大按钮", window)
    action_small = QAction(QIcon(get_icon("folder")), "小按钮", window)
    action_toggle = QAction(QIcon(get_icon("folder")), "可切换按钮", window)
    action_toggle.setCheckable(True)

    # 创建大按钮、小按钮、可切换按钮
    btn_large = RibbonButton(window, action_large, is_large=True)
    btn_small = RibbonButton(window, action_small, is_large=False)
    btn_toggle = RibbonButton(window, action_toggle, is_large=True)

    layout.addWidget(btn_large)
    layout.addWidget(btn_small)
    layout.addWidget(btn_toggle)

    central.setLayout(layout)
    window.setCentralWidget(central)
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
