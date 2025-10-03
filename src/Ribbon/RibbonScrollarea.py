#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   RibbonScrollarea.py
# @Time          :   2025/10/01 21:56:57
# @Author        :   XuMing
# @Version       :   v1.1
# @Email         :   920972751@qq.com
# @Description   :   Ribbon 自定义滚动区域 + 分隔符控件
# ****************************************************

from PyQt5 import QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QLabel, QPushButton
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet


class RibbonScrollarea(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(get_stylesheet("ribbonButton"))
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.contentWidget = QWidget()
        self.setWidget(self.contentWidget)

        self.contentLayout = QHBoxLayout()
        self.contentLayout.setContentsMargins(0, 0, 0, 0)
        self.contentLayout.setSpacing(2)
        self.contentLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.contentWidget.setLayout(self.contentLayout)

    def add_ribbon_widget(self, widget: QWidget):
        self.contentLayout.addWidget(widget, 0, Qt.AlignTop)

    def add_grid_widget(self, width: int) -> QGridLayout:
        widget = QWidget()
        widget.setMaximumWidth(width)
        widget.setMinimumWidth(width)
        grid_layout = QGridLayout()
        widget.setLayout(grid_layout)
        grid_layout.setSpacing(4)
        grid_layout.setContentsMargins(4, 4, 4, 4)
        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.contentLayout.addWidget(widget)
        return grid_layout


class RibbonSeparator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        height = int(gui_scale() * 80)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        self.setMinimumWidth(1)
        self.setMaximumWidth(1)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.fillRect(event.rect(), Qt.lightGray)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    main_win = QtWidgets.QMainWindow()
    main_win.setWindowTitle("RibbonScrollarea 测试")
    main_win.resize(800, 200)

    scroll_area = RibbonScrollarea(main_win)

    # 添加测试按钮
    for i in range(10):
        btn = QPushButton(f"按钮 {i + 1}")
        btn.setMinimumSize(60, 60)
        scroll_area.add_ribbon_widget(btn)

        # 每 3 个按钮插入一个分隔符
        if (i + 1) % 3 == 0:
            scroll_area.add_ribbon_widget(RibbonSeparator())

    main_win.setCentralWidget(scroll_area)
    main_win.show()
    sys.exit(app.exec_())
