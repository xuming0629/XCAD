#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   RibbonTab.py
# @Time          :   2025/10/01 21:35:20
# @Author        :   XuMing
# @Version       :   1.0
# @Email         :   920972751@qq.com
# @Description   :   RibbonTab 类
# @Copyright     :   XuMing. All Rights Reserved.
# ****************************************************



from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from src.Ribbon.RibbonPane import RibbonPane


class RibbonTab(QWidget):
    """
    RibbonTab 类
    ----------------
    用于在 RibbonBar 中创建一个“选项卡”容器，内部可以水平添加 RibbonPane（功能分组）。
    """

    def __init__(self, parent, name: str):
        """
        初始化 RibbonTab

        参数:
            parent : 父级 QWidget（通常是 RibbonBar）
            name   : 当前选项卡的名称（可用于标识）
        """
        super(RibbonTab, self).__init__(parent)

        # RibbonTab 使用水平布局，存放 RibbonPane
        layout = QHBoxLayout()
        self.setLayout(layout)

        # 去掉边距和间隔，保证 RibbonPane 紧贴排列
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft)

        # 保存名称
        self._name = name

    def add_ribbon_pane(self, name: str) -> RibbonPane:
        """
        向当前 Tab 添加一个 RibbonPane

        参数:
            name : RibbonPane 的名称

        返回:
            ribbon_pane : 新建的 RibbonPane 实例
        """
        ribbon_pane = RibbonPane(self, name)
        self.layout().addWidget(ribbon_pane)
        return ribbon_pane

    def add_spacer(self):
        """
        在 RibbonPane 后面添加一个可伸缩的空白填充，
        用于将 RibbonPane 靠左对齐，右侧留空。
        """
        spacer = QSpacerItem(1, 1, QSizePolicy.MinimumExpanding)
        self.layout().addSpacerItem(spacer)
        # 设置最后一个项（spacer）可伸缩
        self.layout().setStretch(self.layout().count() - 1, 1)

    def set_ribbon_pane(self, ribbon_pane: RibbonPane, stretch: int = 0):
        """
        设置某个 RibbonPane 的伸缩比例（可选）

        参数:
            ribbon_pane : 目标 RibbonPane
            stretch     : 伸缩因子，默认为 0（不伸缩）
        """
        index = self.layout().indexOf(ribbon_pane)
        if index >= 0:
            self.layout().setStretch(index, stretch)
