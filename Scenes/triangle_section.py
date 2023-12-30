from manim import *
import numpy as np

# If cos(alpha) = 5/13, use the tau circle to find the sine and cosine of the following angles
class original_triangle(Scene):
    def construct(self):

        axes = Axes(x_range =[-8, 8, 1], y_range=[-8, 8, 1], x_length=7, y_length=7)

        # Triangle
        triangle = Polygon(axes.c2p(-2.5, -6), axes.c2p(2.5, -6), axes.c2p(2.5, 6)).set_color(WHITE)

        # Right angle
        ghost_line1 = Line(axes.c2p(0, -6), axes.c2p(2.5, -6)).set_opacity(0)
        ghost_line2 = Line(axes.c2p(2.5, 0), axes.c2p(2.5, -6)).set_opacity(0)
        right_angle = RightAngle(ghost_line1, ghost_line2, length=0.25, quadrant=(-1,-1)).set_color(WHITE)

        # Some text
        cos = MathTex(r"\cos", font_size=40).move_to(axes.c2p(4.5, 3))
        alpha = MathTex(r"\alpha", font_size=40).next_to(cos, axes.c2p(1, 0))
        equals = MathTex(r"=", font_size=40).next_to(alpha, axes.c2p(1, 0))
        divide = Line(axes.c2p(7, 3), axes.c2p(8, 3), color=WHITE)
        adj_tex = MathTex(r"5", font_size=40).next_to(divide, UP * 0.75)
        hyp_tex = MathTex(r"13", font_size=40).next_to(divide, DOWN * 0.75)
        adj = MathTex(r"adj", font_size=40).next_to(divide, UP * 0.75)
        hyp = MathTex(r"hyp", font_size=40).next_to(divide, DOWN * 0.75)

        # Solving for b
        pythag_tex = Tex('Pythagorean Theorem:').move_to(np.array([-4, 3, 0]))
        pythag_theorem = MathTex('a^2 + b^2 = c^2').next_to(pythag_tex, DOWN)
        pythag_replace = MathTex('b = \sqrt{169 - 25}').next_to(pythag_tex, DOWN)
        b_equals = MathTex('b=12').next_to(pythag_tex, DOWN)
        opp = MathTex('12', font_size=40).move_to(axes.c2p(3.75, 0))

        # Cosine and sine of alpha
        cosine = MathTex(r"\cos{\alpha}=\frac{5}{13}").move_to(np.array([-4, 2, 0]))
        sine = MathTex(r"\sin{\alpha}=\frac{12}{13}").move_to(np.array([-4, -2, 0]))

        # Animations
        self.play(Create(triangle), run_time=1)
        self.play(GrowFromPoint(right_angle, axes.c2p(2.5, -6)))
        self.play(Write(cos), Write(alpha), Write(equals), GrowFromPoint(divide, axes.c2p(7, 3)), Write(adj), Write(hyp))
        self.play(Transform(adj, adj_tex), Transform(hyp, hyp_tex))
        self.play(alpha.animate.move_to(axes.c2p(-1.5, -5.25)))
        self.play(adj.animate.move_to(axes.c2p(0, -7)), hyp.animate.move_to(axes.c2p(-1, 1)), Unwrite(cos), Unwrite(equals), Unwrite(divide))
        self.play(Write(pythag_tex), run_time=1)
        self.play(Write(pythag_theorem))
        self.wait(0.5)
        self.play(ReplacementTransform(pythag_theorem, pythag_replace))
        self.wait(0.5)
        self.play(ReplacementTransform(pythag_replace, b_equals))
        self.wait(0.5)
        self.play(Unwrite(pythag_tex), ReplacementTransform(b_equals, opp))
        self.play(Write(cosine), Write(sine))
        self.wait(2.5)