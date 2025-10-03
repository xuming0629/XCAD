#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   RibbonTextbox.py
@Time    :   2025/09/14 23:34:42
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   自定义 Ribbon 样式文本框，支持默认值、最大宽度和文本变化事件。
'''

from PyQt5.QtWidgets import QLineEdit, QApplication, QWidget, QVBoxLayout


class RibbonTextbox(QLineEdit):
    """
    Ribbon 样式文本框
    -----------------
    参数:
        default_value: str, 默认显示的文本
        change_connector: function, 文本变化时触发的回调函数
        max_width: int, 文本框最大宽度
    """

    def __init__(self, default_value="", change_connector=None, max_width=100):
        super().__init__(None)

        # 设置 Ribbon 样式
        self.setStyleSheet("""
            QLineEdit {
                border: 1px solid rgba(0,0,0,30%);
                padding: 2px;
                border-radius: 3px;
                background-color: white;
            }
        """)

        # 设置默认值
        self.setText(default_value)

        # 限制最大宽度
        self.setMaximumWidth(max_width)

        # 绑定文本变化事件
        if change_connector is not None:
            self.textChanged.connect(change_connector)


if __name__ == "__main__":
    """
    测试 RibbonTextbox
    """
    import sys

    def on_text_changed(text):
        print(f"文本变化: {text}")

    app = QApplication(sys.argv)

    main_window = QWidget()
    main_window.setWindowTitle("RibbonTextbox 测试")
    layout = QVBoxLayout(main_window)

    # 创建 RibbonTextbox 实例
    textbox1 = RibbonTextbox(default_value="请输入内容", change_connector=on_text_changed, max_width=200)
    textbox2 = RibbonTextbox(default_value="测试", max_width=150)

    layout.addWidget(textbox1)
    layout.addWidget(textbox2)

    main_window.show()
    sys.exit(app.exec_())
