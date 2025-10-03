#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   MainWindow.py
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@Desc    :   主窗口类，集成 Ribbon 工具栏
'''

from PyQt5.QtWidgets import (
    QMainWindow, QDockWidget, QAction, QLabel, QMessageBox, QApplication
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence as QKSec

from src.Ribbon.Icons import get_icon
from src.Ribbon.RibbonButton import RibbonButton
from src.Ribbon.RibbonTextbox import RibbonTextbox
from src.Ribbon.RibbonWidget import RibbonWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1280, 800)
        self.setWindowTitle("Main Window")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))

        self._main_dock_widget = QDockWidget(self)
        self._main_dock_widget.setObjectName("MainDock")
        self._main_dock_widget.setWindowTitle("Main dock")
        self.addDockWidget(Qt.LeftDockWidgetArea, self._main_dock_widget)

        self._open_action = self.add_action("Open", "open", "Open file", True, self.on_open_file, QKSec.Open)
        self._save_action = self.add_action("Save", "save", "Save file", True, self.on_save, QKSec.Save)
        self._copy_action = self.add_action("Copy", "copy", "Copy selection", True, self.on_copy, QKSec.Copy)
        self._paste_action = self.add_action("Paste", "paste", "Paste from clipboard", True, self.on_paste, QKSec.Paste)
        self._zoom_action = self.add_action("Zoom", "zoom", "Zoom in", True, self.on_zoom)
        self._about_action = self.add_action("About", "about", "About this software", True, self.on_about)
        self._license_action = self.add_action("License", "license", "License information", True, self.on_license)

        self._text_box1 = RibbonTextbox("Text 1", self.on_text_box1_changed, 80)
        self._text_box2 = RibbonTextbox("Text 2", self.on_text_box2_changed, 80)
        self._text_box3 = RibbonTextbox("Text 3", self.on_text_box3_changed, 80)

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut:
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

    def closeEvent(self, event):
        pass

    def on_open_file(self):
        print("Open file action triggered")

    def on_save(self):
        print("Save file action triggered")

    def on_text_box1_changed(self):
        print("TextBox1 changed:", self._text_box1.text())

    def on_text_box2_changed(self):
        print("TextBox2 changed:", self._text_box2.text())

    def on_text_box3_changed(self):
        print("TextBox3 changed:", self._text_box3.text())

    def on_copy(self):
        print("Copy action triggered")

    def on_paste(self):
        print("Paste action triggered")

    def on_zoom(self):
        print("Zoom action triggered")

    def on_about(self):
        QMessageBox.about(self, "About", "QupyRibbon\nCreated by XuMing")

    def on_license(self):
        QMessageBox.information(self, "License", "License information...")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
