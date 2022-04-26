from manimlib.imports import *

class Euler(Scene):
 
    def construct(self):
        formula1 = TexMobject(
            "e^{i \pi}+1=?"
        )
        formula2 = TexMobject(
            "e^{i \pi}+1=0"
        )
        formula2_1 = TexMobject(
            'e^{i \pi}',
            '+',
            '1',
            '=',
            '0'
        )

        formula2_1.to_corner(UP + LEFT)
        self.play(Write(formula2), run_time = 2)
        self.play(Transform(formula2,formula2_1), run_time = 3)
        # #欧拉恒等式向左上方移动
        text1 = TextMobject(
            "自然常数 e"
        )
        text1.to_corner(3*UP + 1*LEFT)
        self.play(Transform(formula2_1[0],text1), run_time = 3)
        text2 = TexMobject(
            "圆周率 \pi"
        )
        text2.to_corner(5*UP + 1*LEFT)
        self.play(Write(text2), run_time = 2)
        text3 = TextMobject(
            "虚数单位 i"
        )
        text3.to_corner(7*UP + 1*LEFT)
        self.play(Write(text3), run_time = 2)
        
        text4 = TextMobject(
            "自然数 1"
        )
        text4.to_corner(9*UP + 1*LEFT)
        self.play(Transform(formula2_1[2],text4), run_time = 3)

        text5 = TextMobject(
            "以及 0"
        )
        text5.to_corner(11*UP + 1*LEFT)
        self.play(Transform(formula2_1[4],text5), run_time = 3)
        
        # #依次解释欧拉恒等式的成分