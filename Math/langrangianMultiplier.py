from manim import *

class LagrangeMultipliers(Scene):
    def construct(self):
        # 创建文本和数学表达式
        title = Text("拉格朗日乘数法")
        lagrange_text = Text("L(x, y, λ) = f(x, y) - λ * g(x, y)")

        # 定义函数f和g
        f = Tex("f(x, y) = x^2 + y^2")
        g = Tex("g(x, y) = x + y - 1")

        # 定义拉格朗日函数
        lagrange = Tex("$L(x, y, \\lambda) =", f, "-", "\\lambda *", g)

        # 添加箭头指向各个部分
        arrow_f = Arrow(lagrange[1].get_top(), f.get_bottom(), color=BLUE)
        arrow_g = Arrow(lagrange[3].get_top(), g.get_bottom(), color=BLUE)
        arrow_lambda = Arrow(lagrange[2].get_top(), lagrange[0].get_bottom(), color=BLUE)

        # 布局
        title.to_edge(UP)
        lagrange.next_to(title, DOWN, MED_LARGE_BUFF)
        f.next_to(lagrange, RIGHT, aligned_edge=DOWN)
        g.next_to(f, RIGHT, aligned_edge=DOWN)
        arrow_f.next_to(lagrange, RIGHT, buff=0.2)
        arrow_g.next_to(lagrange, RIGHT, buff=0.2)
        arrow_lambda.next_to(lagrange, RIGHT, buff=0.2)

        # 动画
        self.play(Write(title))
        self.play(Write(lagrange), Write(f), Write(g), run_time=1)
        self.wait(1)
        #self.play(ShowCreation(arrow_f), ShowCreation(arrow_g), ShowCreation(arrow_lambda), run_time=1)
        self.play(Create(arrow_f), Create(arrow_g), Create(arrow_lambda), run_time=1)
        self.wait(2)

# 为了运行这个场景，你需要在命令行中使用以下命令：
# manim -pql lagrange_multipliers.py LagrangeMultipliers
