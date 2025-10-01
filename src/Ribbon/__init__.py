#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2025/09/14 23:32:17
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   
'''

from PyQt5.QtWidgets import QApplication




def gui_scale():
    screen = QApplication.screens()[0]
    dpi = screen.logicalDotsPerInch()
    return dpi / 96
