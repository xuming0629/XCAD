#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_ribbon_textbox.py
@Time    :   2025/09/14 23:35:37
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   
'''


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

# 导入 RibbonTextbox 模块l
from src.Ribbon.RibbonTextbox import RibbonTextbox

def test_ribbon_textbox():
    def on_text_change(text):
        status_label.setText(f"当前输入: {text}")

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("RibbonTextbox 测试")
    main_window.resize(400, 100)

    # 工具栏
    toolbar = QToolBar("Ribbon Toolbar")
    main_window.addToolBar(Qt.TopToolBarArea, toolbar)

    # 添加自定义文本框
    textbox = RibbonTextbox("默认文本", on_text_change, max_width=150)
    toolbar.addWidget(textbox)

    # 状态显示标签
    status_label = QLabel("当前输入: ")
    central_widget = QWidget()
    layout = QHBoxLayout()
    layout.addWidget(status_label)
    central_widget.setLayout(layout)
    main_window.setCentralWidget(central_widget)

    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    test_ribbon_textbox()
