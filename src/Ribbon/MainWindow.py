#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MainWindow.py
@Time    :   2025/09/22 22:23:02
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   主窗口类，基于 QMainWindow，集成 Ribbon 风格工具栏和基本功能。
'''

from PyQt5.QtWidgets import QMainWindow, QDockWidget, QAction, QLabel, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence as QKSec

from src.Ribbon.Icons import get_icon       # 获取图标的工具函数
from src.Ribbon.RibbonButton import RibbonButton  # Ribbon 风格按钮
from src.Ribbon.RibbonTextbox import RibbonTextbox  # Ribbon 风格文本框
from src.Ribbon.RibbonWidget import RibbonWidget  # Ribbon 风格控件





class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(1280, 800)                        # 设置主窗口大小
        self.setWindowTitle("Main Window")            # 设置标题
        self.setDockNestingEnabled(True)              # 允许嵌套 Dock
        self.setWindowIcon(get_icon("icon"))          # 设置窗口图标

        # 主 DockWidget
        self._main_dock_widget = QDockWidget(self)
        self._main_dock_widget.setObjectName("MainDock")
        self._main_dock_widget.setWindowTitle("Main dock")
        self.addDockWidget(Qt.LeftDockWidgetArea, self._main_dock_widget)
        self.centralWidget()                          # 占位 central widget（可替换）

        # ----------------- 定义动作 -----------------
        # 文件操作
        self._open_action = self.add_action("Open", "open", "Open file", True, self.on_open_file, QKSec.Open)
        self._save_action = self.add_action("Save", "save", "Save file", True, self.on_save, QKSec.Save)
        # 编辑操作
        self._copy_action = self.add_action("Copy", "copy", "Copy selection", True, self.on_copy, QKSec.Copy)
        self._paste_action = self.add_action("Paste", "paste", "Paste from clipboard", True, self.on_paste, QKSec.Paste)
        # 视图操作
        self._zoom_action = self.add_action("Zoom", "zoom", "Zoom in on document", True, self.on_zoom)
        # 信息相关
        self._about_action = self.add_action("About", "about", "About QupyRibbon", True, self.on_about)
        self._license_action = self.add_action("License", "license", "Licence for this software", True, self.on_license)
        
        # -------------      textboxes       -----------------

        self._text_box1 = RibbonTextbox("Text 1", self.on_text_box1_changed, 80)
        self._text_box2 = RibbonTextbox("Text 2", self.on_text_box1_changed, 80)
        self._text_box3 = RibbonTextbox("Text 3", self.on_text_box1_changed, 80)

        # Ribbon

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()
        
        

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def init_ribbon(self):
        home_tab = self._ribbon.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._open_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._save_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        edit_panel.add_ribbon_widget(RibbonButton(self, self._copy_action, True))
        edit_panel.add_ribbon_widget(RibbonButton(self, self._paste_action, True))
        grid = edit_panel.add_grid_widget(200)
        grid.addWidget(QLabel("Text box 1"), 1, 1)
        grid.addWidget(QLabel("Text box 2"), 2, 1)
        grid.addWidget(QLabel("Text box 3"), 3, 1)
        grid.addWidget(self._text_box1, 1, 2)
        grid.addWidget(self._text_box2, 2, 2)
        grid.addWidget(self._text_box3, 3, 2)

        view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        home_tab.add_spacer()

        about_tab = self._ribbon.add_ribbon_tab("About")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

    # ----------------- 事件和槽函数 -----------------

    def closeEvent(self, close_event):
        """窗口关闭事件，可做资源释放处理"""
        pass

    def on_open_file(self):
        """打开文件"""
        pass

    def on_save_to_excel(self):
        """另存为 Excel"""
        pass

    def on_save(self):
        """保存文件"""
        pass

    def on_text_box1_changed(self):
        """文本框 1 内容变化"""
        pass

    def on_text_box2_changed(self):
        """文本框 2 内容变化"""
        pass

    def on_text_box3_changed(self):
        """文本框 3 内容变化"""
        pass

    def on_copy(self):
        """复制操作"""
        pass

    def on_paste(self):
        """粘贴操作"""
        pass

    def on_zoom(self):
        """缩放操作"""
        pass

    def on_about(self):
        """显示关于对话框"""
        text = "QupyRibbon\n"
        text += "This program was made by Magnus Jørgensen.\n"
        text += "Copyright © 2016 Magnus Jørgensen"
        QMessageBox().about(self, "About QupyRibbon", text)

    def on_license(self):
        """显示许可证信息"""
        file = open('LICENSE', 'r')
        lic = file.read()
        QMessageBox().information(self, "License", lic)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
