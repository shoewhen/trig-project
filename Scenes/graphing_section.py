from manim import *
import numpy as np

class three_sin_x(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-TAU, TAU, TAU/4],
            y_range=[-3, 3, 1],
            x_length=10,
            y_axis_config={"include_numbers": True, "font_size": 30},
            tips=False
        )
        
        function_draft = axes.plot(lambda x: np.sin(x), color=BLUE)
        function = axes.plot(lambda x: 3 * np.sin(x), color=BLUE)
        function_tex1 = MathTex(r"f(x)=\sin\left(x\right)", font_size=40, color=BLUE).move_to(np.array([-4, -2, 0]))
        function_tex = MathTex(r"f(x)=3\sin\left(x\right)", font_size=40, color=BLUE).move_to(np.array([-4, -2, 0]))

        self.add(axes)
        self.add_x_labels()
        self.play(Write(function_tex1))
        self.play(Create(function_draft), run_time=5)
        self.play(ReplacementTransform(function_tex1, function_tex))
        self.play(Transform(function_draft, function))
        self.wait()

    def add_x_labels(self):
        x_labels = [
            MathTex(r"-\tau", font_size=40), MathTex(r"-\frac{\tau}{2}", font_size=30), MathTex(r"0", font_size=40),
            MathTex(r"\frac{\tau}{2}", font_size=30), MathTex(r"\tau", font_size=40),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-4.75 + 2.5*i, 0, 0]), DOWN)
            self.add(x_labels[i])


class sin_three_x(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-TAU, TAU, TAU/4],
            y_range=[-1, 1, 0.5],
            x_length=10,
            y_length=5,
            y_axis_config={"include_numbers": True, "font_size": 30},
            tips=False
        )
        
        function_draft = axes.plot(lambda x: np.sin(x), color=RED)
        function = axes.plot(lambda x: np.sin(3 * x), color=RED)
        function_tex1 = MathTex(r"f(x)=\sin\left(x\right)", font_size=40, color=RED).move_to(np.array([-5, 3.25, 0]))
        function_tex = MathTex(r"f(x)=\sin\left(3x\right)", font_size=40, color=RED).move_to(np.array([-5, 3.25, 0]))

        self.add(axes)
        self.add_x_labels()
        self.play(Write(function_tex1))
        self.play(Create(function_draft), run_time=5)
        self.play(ReplacementTransform(function_tex1, function_tex))
        self.play(Transform(function_draft, function))
        self.wait()

    def add_x_labels(self):
        x_labels = [
            MathTex(r"-\tau", font_size=40), MathTex(r"-\frac{\tau}{2}", font_size=30), MathTex(r"0", font_size=40),
            MathTex(r"\frac{\tau}{2}", font_size=30), MathTex(r"\tau", font_size=40),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-4.75 + 2.5*i, 0, 0]), DOWN)
            self.add(x_labels[i])


class negative_two_cos_x(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-TAU, TAU, TAU/4],
            y_range=[-2, 2, 1],
            x_length=10,
            y_axis_config={"include_numbers": True, "font_size": 30},
            tips=False
        )
        
        function_draft1 = axes.plot(lambda x: np.cos(x), color=GREEN)
        function_draft2 = axes.plot(lambda x: 2 * np.cos(x), color=GREEN)
        function = axes.plot(lambda x: -2 * np.cos(x), color=GREEN)
        function_tex1 = MathTex(r"f(x)=\cos\left(x\right)", font_size=30, color=GREEN).move_to(np.array([-5, 3.25, 0]))
        function_tex2 = MathTex(r"f(x)=2\cos\left(x\right)", font_size=30, color=GREEN).move_to(np.array([-5, 3.25, 0]))
        function_tex = MathTex(r"f(x)=-2\cos\left(x\right)", font_size=30, color=GREEN).move_to(np.array([-5, 3.25, 0]))

        self.add(axes)
        self.add_x_labels()
        self.play(Write(function_tex1))
        self.play(Create(function_draft1), run_time=5)
        self.play(ReplacementTransform(function_tex1, function_tex2))
        self.play(ReplacementTransform(function_draft1, function_draft2))
        self.play(ReplacementTransform(function_tex2, function_tex))
        self.play(ReplacementTransform(function_draft2, function))
        self.wait()

    def add_x_labels(self):
        x_labels = [
            MathTex(r"-\tau", font_size=40), MathTex(r"-\frac{\tau}{2}", font_size=30), MathTex(r"0", font_size=40),
            MathTex(r"\frac{\tau}{2}", font_size=30), MathTex(r"\tau", font_size=40),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-4.75 + 2.5*i, 0, 0]), DOWN)
            self.add(x_labels[i])


class cos_x_minus_tau_over_four(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-TAU, TAU, TAU/4],
            y_range=[-1, 1, 0.5],
            x_length=10,
            y_length=5,
            y_axis_config={"include_numbers": True, "font_size": 30},
            tips=False
        )
        
        function_draft = axes.plot(lambda x: np.cos(x), color=BLUE)
        function = axes.plot(lambda x: np.cos(x - TAU/4), color=BLUE)
        function_tex1 = MathTex(r"f(x)=\cos\left(x\right)", font_size=40, color=BLUE).move_to(np.array([-5, 3.25, 0]))
        function_tex = MathTex(r"f(x)=\cos\left(x-\frac{\tau}{4}\right)", font_size=40, color=BLUE).move_to(np.array([-5, 3.25, 0]))

        self.add(axes)
        self.add_x_labels()
        self.play(Write(function_tex1))
        self.play(Create(function_draft), run_time=5)
        self.play(ReplacementTransform(function_tex1, function_tex))
        self.play(Transform(function_draft, function))
        self.wait()

    def add_x_labels(self):
        x_labels = [
            MathTex(r"-\tau", font_size=40), MathTex(r"-\frac{\tau}{2}", font_size=30), MathTex(r"0", font_size=40),
            MathTex(r"\frac{\tau}{2}", font_size=30), MathTex(r"\tau", font_size=40),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-4.75 + 2.5*i, 0, 0]), DOWN)
            self.add(x_labels[i])


class sin_two_x_minus_tau_over_two(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-TAU, TAU, TAU/4],
            y_range=[-1, 1, 0.5],
            x_length=10,
            y_length=5,
            y_axis_config={"include_numbers": True, "font_size": 30},
            tips=False
        )
        
        function_draft1 = axes.plot(lambda x: np.sin(x), color=RED)
        function_draft2 = axes.plot(lambda x: np.sin(x - TAU / 2), color=RED)
        function = axes.plot(lambda x: np.sin(2 * x - TAU / 2), color=RED)
        function_tex1 = MathTex(r"f(x)=\sin\left(x\right)", font_size=30, color=RED).move_to(np.array([-5, 3.25, 0]))
        function_tex2 = MathTex(r"f(x)=\sin\left(x-\frac{\tau}{2}\right)", font_size=30, color=RED).move_to(np.array([-5, 3.25, 0]))
        dist_tex = MathTex(r"f(x)=\sin\left(2x-\frac{\tau}{2}\right)", font_size=30, color=RED).move_to(np.array([-5, 3.25, 0]))

        self.add(axes)
        self.add_x_labels()
        self.play(Write(function_tex1))
        self.play(Create(function_draft1), run_time=5)
        self.play(ReplacementTransform(function_tex1, function_tex2))
        self.play(ReplacementTransform(function_draft1, function_draft2))
        self.play(ReplacementTransform(function_tex2, dist_tex))
        self.play(ReplacementTransform(function_draft2, function))
        self.wait()

    def add_x_labels(self):
        x_labels = [
            MathTex(r"-\tau", font_size=40), MathTex(r"-\frac{\tau}{2}", font_size=30), MathTex(r"0", font_size=40),
            MathTex(r"\frac{\tau}{2}", font_size=30), MathTex(r"\tau", font_size=40),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-4.75 + 2.5*i, 0, 0]), DOWN)
            self.add(x_labels[i])


class cos_three_x_minus_tau_plus_4(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-TAU, TAU, TAU/4],
            y_range=[-2, 6, 1],
            x_length=10,
            y_axis_config={"include_numbers": True, "font_size": 30},
            tips=False
        )
        
        function_draft1 = axes.plot(lambda x: np.cos(x), color=GREEN)
        function_draft2 = axes.plot(lambda x: np.cos(x) + 4, color=GREEN)
        function = axes.plot(lambda x: np.cos(3 * x - TAU) + 4, color=GREEN)
        function_tex1 = MathTex(r"f(x)=\cos\left(x\right)", font_size=40, color=GREEN).move_to(np.array([-5, 3.25, 0]))
        function_tex2 = MathTex(r"f(x)=\cos\left(x\right) + 4", font_size=40, color=GREEN).move_to(np.array([-5, 3.25, 0]))
        function_tex3 = MathTex(r"f(x)=\cos\left(x-\tau\right)+4", font_size=40, color=GREEN).move_to(np.array([-4.5, 3.25, 0]))
        function_tex = MathTex(r"f(x)=\cos\left(3x-\tau\right)+4", font_size=40, color=GREEN).move_to(np.array([-4.5, 3.25, 0]))

        self.add(axes)
        self.add_x_labels()
        self.play(Write(function_tex1))
        self.play(Create(function_draft1), run_time=5)
        self.play(ReplacementTransform(function_tex1, function_tex2))
        self.play(ReplacementTransform(function_draft1, function_draft2))
        self.wait()
        self.play(ReplacementTransform(function_tex2, function_tex3))
        self.wait()
        self.play(ReplacementTransform(function_tex3, function_tex))
        self.play(ReplacementTransform(function_draft2, function))
        self.wait()

    def add_x_labels(self):
        x_labels = [
            MathTex(r"-\tau", font_size=40), MathTex(r"-\frac{\tau}{2}", font_size=30), MathTex(r"0", font_size=40),
            MathTex(r"\frac{\tau}{2}", font_size=30), MathTex(r"\tau", font_size=40),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-4.75 + 2.5*i, 0, 0]), DOWN * 7)
            self.add(x_labels[i])