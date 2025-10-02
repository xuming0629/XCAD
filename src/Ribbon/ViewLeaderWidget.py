#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ****************************************************
# @FileName      :   ViewLeaderWidget.py
# @Time          :   2025/10/03 07:31:19
# @Author        :   XuMing
# @Version       :   1.0
# @Email         :   920972751@qq.com
# @Description   :   None
# @Copyright     :   XuMing. All Rights Reserved.
# ****************************************************


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QSize
from Win64.Ribbon import gui_scale
from Win64.Ribbon.StyleSheets import get_stylesheet
from Win64.Ribbon.RibbonTab import RibbonTab
from Win64.Ribbon.ViewLeaderButton import ViewLeaderButton


__author__ = 'loujiand'


class ViewLeaderWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ViewLeaderWidget, self).__init__(parent)

        # 主容器
        self._ViewLeader_Widget = QtWidgets.QWidget(parent)
        self._ViewLeader_Widget.setMaximumHeight(int(45 * gui_scale()))
        self._ViewLeader_Widget.setMinimumHeight(int(45 * gui_scale()))

        # 水平布局
        self.HBOX = QtWidgets.QHBoxLayout(self._ViewLeader_Widget)
        HBOX_Logo = QtWidgets.QHBoxLayout()
        HBOX_Left = QtWidgets.QHBoxLayout()
        HBOX_Center = QtWidgets.QHBoxLayout()
        HBOX_Right = QtWidgets.QHBoxLayout()

        self.HBOX.addLayout(HBOX_Logo)
        self.HBOX.addLayout(HBOX_Left)
        self.HBOX.addLayout(HBOX_Center, 280)
        self.HBOX.addLayout(HBOX_Right, 0)

        # 左侧按钮区域
        self.folder_pushButton = ViewLeaderButton(parent, "folder_pushButton", "view_top", QSize(32, 32), "打开")
        HBOX_Left.addWidget(self.folder_pushButton)

        self.undo_pushButton = ViewLeaderButton(parent, "undo_pushButton", "view_tfr_tri", QSize(32, 32), "撤销")
        HBOX_Left.addWidget(self.undo_pushButton)

        self.redo_pushButton = ViewLeaderButton(parent, "redo_pushButton", "view_tfr_iso", QSize(32, 32), "重做")
        HBOX_Left.addWidget(self.redo_pushButton)

        self.save_pushButton = ViewLeaderButton(parent, "save_pushButton", "view_right", QSize(32, 32), "保存")
        HBOX_Left.addWidget(self.save_pushButton)

        self.copy_pushButton = ViewLeaderButton(parent, "copy_pushButton", "view_left", QSize(32, 32), "复制")
        HBOX_Left.addWidget(self.copy_pushButton)

        self.paste_pushButton = ViewLeaderButton(parent, "paste_pushButton", "view_front", QSize(32, 32), "粘贴")
        HBOX_Left.addWidget(self.paste_pushButton)

        self.about_pushButton = ViewLeaderButton(parent, "about_pushButton", "view_bottom", QSize(32, 32), "关于")
        HBOX_Left.addWidget(self.about_pushButton)

        # 字体
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(15)

        # 中间标题（可选）
        # self.label = QtWidgets.QLabel("BrepCAD", self)
        # self.label.setFont(font)
        # HBOX_Center.addWidget(self.label, 0, Qt.AlignCenter)

        # 内部 tab 容器（供 add_ribbon_tab 使用）
        self._ribbon_widget = QtWidgets.QTabWidget(self)


    def add_ribbon_tab(self, name):
        """添加一个 RibbonTab"""
        ribbon_tab = RibbonTab(self, name)
        ribbon_tab.setObjectName("tab_" + name)
        self._ribbon_widget.addTab(ribbon_tab, name)
        return ribbon_tab

    def set_active(self, name):
        """激活某个 tab"""
        tab = self.findChild(RibbonTab, "tab_" + name)
        if tab:
            self._ribbon_widget.setCurrentWidget(tab)
