#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   RibbonPane.py
# @Time          :   2025/10/01 21:35:49
# @Author        :   XuMing
# @Version       :   1.0
# @Email         :   920972751@qq.com
# @Description   :   
# @Copyright     :   XuMing. All Rights Reserved.
# ****************************************************

from PyQt5 import QtGui
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from src.Ribbon import gui_scale
from src.Ribbon.StyleSheets import get_stylesheet



class RibbonPane(QWidget):
    """
    RibbonPane 类
    ----------------
    表示 RibbonTab 内的一个功能分组区域。

    功能:
        - 显示一个标题（组名）
        - 提供一个 contentLayout（水平布局）放置子控件
        - 支持网格布局（add_grid_widget）方便放置多按钮
        - 自动在右侧添加一个 RibbonSeparator（分隔条）
    """

    def __init__(self, parent, name: str):
        """
        初始化 RibbonPane

        参数:
            parent : 父级 QWidget（通常是 RibbonTab）
            name   : 分组标题
        """
        super(RibbonPane, self).__init__(parent)

        # 应用样式表（来自外部 StyleSheets）
        self.setStyleSheet(get_stylesheet("ribbonPane"))

        # 水平布局，包含 [vertical_widget | 分隔条]
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setSpacing(0)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(horizontal_layout)

        # 垂直容器（内容 + 标签）
        vertical_widget = QWidget(self)
        horizontal_layout.addWidget(vertical_widget)

        # 分隔条（位于每个 Pane 的右侧）
        horizontal_layout.addWidget(RibbonSeparator(self))

        # 垂直布局：内容区（content_widget） + 标签
        vertical_layout = QVBoxLayout()
        vertical_layout.setSpacing(0)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_widget.setLayout(vertical_layout)

        # 标签：显示分组名称
        label = QLabel(name)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color:#666;")

        # 内容容器：实际放按钮、控件的地方
        content_widget = QWidget(self)

        vertical_layout.addWidget(content_widget)
        vertical_layout.addWidget(label)

        # 内容区使用水平布局，控件从左到右放置
        content_layout = QHBoxLayout()
        content_layout.setAlignment(Qt.AlignLeft)
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)
        self.contentLayout = content_layout
        content_widget.setLayout(content_layout)

    def add_ribbon_widget(self, widget: QWidget):
        """
        向 Pane 添加一个普通控件（如按钮）

        参数:
            widget : 要添加的 QWidget
        """
        self.contentLayout.addWidget(widget, 0, Qt.AlignTop)

    def add_grid_widget(self, width: int) -> QGridLayout:
        """
        向 Pane 添加一个固定宽度的网格容器（用于排列按钮）

        参数:
            width : 宽度（像素）

        返回:
            grid_layout : 新建的 QGridLayout，用户可以在上面 addWidget()
        """
        widget = QWidget()
        widget.setMaximumWidth(width)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(4)
        grid_layout.setContentsMargins(4, 4, 4, 4)
        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        widget.setLayout(grid_layout)
        self.contentLayout.addWidget(widget)

        return grid_layout


class RibbonSeparator(QWidget):
    """
    RibbonSeparator 类
    ----------------
    用于在 RibbonPane 之间绘制一条竖直分隔线。
    """

    def __init__(self, parent):
        """
        初始化分隔条，高度固定，宽度为 1px。
        """
        super().__init__(parent)

        fixed_height = gui_scale() * 80
        self.setMinimumHeight(fixed_height)
        self.setMaximumHeight(fixed_height)
        self.setMinimumWidth(1)
        self.setMaximumWidth(1)

        # 设置一个空布局（避免 Qt 警告）
        self.setLayout(QHBoxLayout())

    def paintEvent(self, event):
        """
        绘制分隔条（浅灰色竖线）。
        """
        qp = QtGui.QPainter(self)
        qp.fillRect(event.rect(), Qt.lightGray)
