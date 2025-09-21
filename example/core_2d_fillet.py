#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   core_2d_fillet.py
@Time    :   2025/09/21 21:02:16
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   2D 圆角示例
'''


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   core_2d_fillet.py
@Time    :   2025/09/21 21:02:16
@Author  :   XuMing
@Version :   v1.0
@Contact :   920972751@qq.com
@License :   Copyright (c) 2021-2025 XuMing. All Rights Reserved.
@Desc    :   使用 PythonOCC 在二维平面上实现圆角（Fillet）的示例。

-------------------------------------------------
【示例说明】
- OpenCASCADE (OCC) 是一个强大的 CAD 内核库，支持几何建模、布尔运算、
  网格划分、几何分析等。
- 本示例展示如何在 2D 平面上，利用 OCC 的 `ChFi2d_AnaFilletAlgo`，
  对两条直线边在交点处生成圆角（Fillet）。

【运行效果】
- 创建两条直线 (p3→p2, p2→p1)。
- 在交点处生成半径为 radius 的圆角。
- 最终结果是由直线和圆角组合成的线框 (Wire)，并在窗口中显示。

运行代码后，会弹出基于 Qt/VTK 的交互窗口，支持缩放、旋转、平移。
-------------------------------------------------
'''

# ========== 底层库导入 ==========
from OCC.Core.gp import gp_Pnt, gp_Pln                       # 几何点 & 平面
from OCC.Core.ChFi2d import ChFi2d_AnaFilletAlgo             # 2D 圆角算法
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge  # 创建边
from OCC.Extend.ShapeFactory import make_wire                # 创建线框 (Wire)
from OCC.Display.SimpleGui import init_display               # 显示工具


class Fillet2DExample:
    """
    一个简单的 2D 圆角 (Fillet) 示例类
    使用 OpenCASCADE (OCC) 库在 2D 平面上创建两条直线，并在交点处生成圆角。
    """

    def __init__(self, radius=2.0):
        """
        初始化 Fillet 示例类

        :param radius: float
            圆角半径，决定圆弧大小。
        """
        self.radius = radius

        # 初始化显示器 (基于 Qt/VTK 的交互窗口)
        self.display, self.start_display, self.add_menu, self.add_functionto_menu = init_display()

    def make_edges(self):
        """
        创建两条直线边，并返回。

        :return: (TopoDS_Edge, TopoDS_Edge)
            ed1: 第一条直线 (p3 → p2)
            ed2: 第二条直线 (p2 → p1)
        """
        # 定义三个点（位于 XY 平面）
        p1 = gp_Pnt(0, 0, 0)     # 原点
        p2 = gp_Pnt(5, 5, 0)     # 右上点
        p3 = gp_Pnt(-5, 5, 0)    # 左上点

        # 创建两条直线：p3→p2 和 p2→p1
        ed1 = BRepBuilderAPI_MakeEdge(p3, p2).Edge()
        ed2 = BRepBuilderAPI_MakeEdge(p2, p1).Edge()

        return ed1, ed2

    def make_fillet(self, ed1, ed2):
        """
        在两条边之间生成一个 2D 圆角。

        :param ed1: TopoDS_Edge
            第一条边
        :param ed2: TopoDS_Edge
            第二条边
        :return: TopoDS_Edge
            圆角边 (圆弧)
        """
        # 定义一个 2D 圆角算法对象
        f = ChFi2d_AnaFilletAlgo()

        # 在 XY 平面上初始化两条边
        f.Init(ed1, ed2, gp_Pln())

        # 执行圆角计算
        f.Perform(self.radius)

        # 返回圆角结果（一个圆弧边）
        return f.Result(ed1, ed2)

    def build_wire(self, ed1, ed2, fillet_edge):
        """
        把直线和圆角组合成一个线框 (Wire)。

        :param ed1: TopoDS_Edge
            第一条直线
        :param ed2: TopoDS_Edge
            第二条直线
        :param fillet_edge: TopoDS_Edge
            圆角边
        :return: TopoDS_Wire
            组合后的线框
        """
        return make_wire([ed1, fillet_edge, ed2])

    def show(self):
        """
        主入口：创建直线、生成圆角并显示。
        """
        # 1. 创建两条直线
        ed1, ed2 = self.make_edges()

        # 2. 生成圆角
        fillet_edge = self.make_fillet(ed1, ed2)

        # 3. 组合成线框
        wire = self.build_wire(ed1, ed2, fillet_edge)

        # 4. 显示结果
        self.display.DisplayShape(wire, update=True)

        # 启动显示窗口（阻塞运行，直到用户关闭窗口）
        self.start_display()


# ========== 程序入口 ==========
if __name__ == "__main__":
    # 创建一个示例对象，圆角半径 = 1.0
    example = Fillet2DExample(radius=1.0)

    # 显示结果
    example.show()

