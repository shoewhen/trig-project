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

class tau_over_two_plus_alpha(Scene):
    def construct(self):

        axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        circle = Circle.from_three_points(axes.c2p(-1, 0), axes.c2p(1, 0), axes.c2p(0, 1), color=WHITE)

        # Triangle
        hz = Line(ORIGIN, axes.c2p(5/13, 0)).set_color(RED)
        vt = Line(axes.c2p(5/13, 0), axes.c2p(5/13, 12/13)).set_color(RED)
        hyp = Line(ORIGIN, axes.c2p(5/13, 12/13)).set_color(RED)

        # Lines for final triangle
        x_line = Line(ORIGIN, axes.c2p(-5/13, 0)).set_color(BLUE)
        y_line = Line(axes.c2p(-5/13, 0), axes.c2p(-5/13, -12/13)).set_color(BLUE)
        
        # Some text
        coord1 = MathTex(r"\left(13, 0\right)", font_size = 25).move_to(axes.c2p(1.15, 0.1))
        coord2 = MathTex(r"\left(0, 13\right)", font_size=25).move_to(axes.c2p(0.15, 1.12))
        coord3 = MathTex(r"\left(-13, 0\right)", font_size=25).move_to(axes.c2p(-1.2, 0.1))
        coord4 = MathTex(r"\left(0, -13\right)", font_size=25).move_to(axes.c2p(0.175, -1.12))
        coord_group = VGroup(coord1, coord2, coord3, coord4)

        alpha = MathTex(r"\alpha", font_size=30, color=RED).move_to(axes.c2p(0.125, 0.09375))
        theta_alpha = MathTex(r"\theta=\alpha", font_size=40, color=WHITE).move_to(np.array([-5, 3, 0]))
        theta_equals = MathTex(r"\theta=\frac{\tau}{2} + \alpha", font_size=40, color=WHITE).move_to(np.array([-5, 3, 0]))
        final_angle = MathTex(r"\frac{\tau}{2}+\alpha", font_size = 20, color=BLUE).move_to(axes.c2p(-5/26, -0.125))

        hz_length = MathTex(r"5", font_size=30, color=RED).move_to(axes.c2p(5/26, -0.1))
        vt_length = MathTex(r"12", font_size=30, color=RED).move_to(axes.c2p(0.5, 12/26))
        hyp_length = MathTex(r"13", font_size=30, color=RED).move_to(axes.c2p(0.125, 0.525))

        final_hz_length = MathTex(r"-5", font_size=30, color=BLUE).move_to(axes.c2p(-5/26, 0.1))
        final_vt_length = MathTex(r"-12", font_size=30, color=BLUE).move_to(axes.c2p(-0.55, -0.4))
        final_hyp_length = MathTex(r"13", font_size=30, color=BLUE).move_to(axes.c2p(-0.125, -0.525))

        # Cosine and sine of theta
        sin_final_angle = MathTex(r"\sin\left(\theta\right)=-\frac{12}{13}", font_size = 35).move_to(np.array([-5, 1.25, 0]))
        cos_final_angle = MathTex(r"\cos\left(\theta\right)=-\frac{5}{13}", font_size = 35).move_to(np.array([-5, -1, 0]))

        # Animations
        self.add(axes)
        self.play(Create(circle))
        self.play(Write(coord_group))
        self.play(GrowFromPoint(hz, ORIGIN), GrowFromPoint(vt, ORIGIN), GrowFromPoint(hyp, ORIGIN))
        self.play(Write(alpha), Write(theta_alpha))
        self.play(Write(hz_length), Write(vt_length), Write(hyp_length))
        self.wait()
        self.play(FadeOut(hz_length), FadeOut(vt_length))
        self.play(hz.animate.set_opacity(0), vt.animate.set_opacity(0))
        self.play(Rotate(hyp, TAU/2, about_point=ORIGIN), ReplacementTransform(theta_alpha, theta_equals), ReplacementTransform(alpha, final_angle), ReplacementTransform(hyp_length, final_hyp_length))
        self.play(GrowFromPoint(x_line, ORIGIN), GrowFromPoint(y_line, axes.c2p(-5/13, -12/13)), hyp.animate.set_color(BLUE))
        self.play(Write(final_hz_length), Write(final_vt_length), FadeOut(final_angle))
        self.play(Write(sin_final_angle), Write(cos_final_angle))
        self.wait()


class tau_minus_alpha(Scene):
    def construct(self):

        axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        circle = Circle.from_three_points(axes.c2p(-1, 0), axes.c2p(1, 0), axes.c2p(0, 1), color=WHITE)

        hyp = Line(ORIGIN, axes.c2p(1, 0), color=RED)
        hyp2 = DashedLine(ORIGIN, axes.c2p(5/13, -12/13), color=BLUE)

        # Some text
        coord1 = MathTex(r"\left(13, 0\right)", font_size = 25).move_to(axes.c2p(1.15, 0.1))
        coord2 = MathTex(r"\left(0, 13\right)", font_size=25).move_to(axes.c2p(0.15, 1.12))
        coord3 = MathTex(r"\left(-13, 0\right)", font_size=25).move_to(axes.c2p(-1.2, 0.1))
        coord4 = MathTex(r"\left(0, -13\right)", font_size=25).move_to(axes.c2p(0.175, -1.12))
        coord_group = VGroup(coord1, coord2, coord3, coord4)

        theta_tau = MathTex(r"\theta=\tau", font_size=40).move_to(np.array([-5, 3, 0]))
        theta_equals = MathTex(r"\theta=\tau-\alpha", font_size=40).move_to(np.array([-5, 3, 0]))

        hz_length = MathTex(r"5", font_size=30, color=BLUE).move_to(axes.c2p(5/26, 0.1))
        vt_length = MathTex(r"-12", font_size=30, color=BLUE).move_to(axes.c2p(0.55, -0.4))
        hyp_length = MathTex(r"13", font_size=30, color=BLUE).move_to(axes.c2p(0.125, -0.525))

        alpha = MathTex(r"\alpha", font_size=30, color=BLUE).move_to(axes.c2p(0.125, -0.09375))

        # Lines for final triangle
        x_line = Line(ORIGIN, axes.c2p(5/13, 0), color=BLUE)
        y_line = Line(axes.c2p(5/13, -12/13), axes.c2p(5/13, 0), color=BLUE)

        # Cosine and sine of theta
        sin_final_angle = MathTex(r"\sin\left(\theta\right)=-\frac{12}{13}", font_size = 35).move_to(np.array([-5, 1.25, 0]))
        cos_final_angle = MathTex(r"\cos\left(\theta\right)=\frac{5}{13}", font_size = 35).move_to(np.array([-5, -1, 0]))

        # Animations
        self.add(axes)
        self.play(Create(circle))
        self.play(Write(coord_group))
        self.play(GrowFromPoint(hyp, ORIGIN))
        self.play(Rotate(hyp, TAU, about_point=ORIGIN), Write(theta_tau), run_time=2)
        self.wait()
        self.play(GrowFromPoint(hyp2, ORIGIN), Write(alpha))
        self.play(Rotate(hyp, -67.38013505*DEGREES, about_point=ORIGIN), ReplacementTransform(theta_tau, theta_equals))
        self.remove(hyp2)
        self.play(GrowFromPoint(x_line, ORIGIN), GrowFromPoint(y_line, axes.c2p(5/13, -12/13)), hyp.animate.set_color(BLUE))
        self.play(Write(hz_length), Write(vt_length), Write(hyp_length))
        self.play(Write(sin_final_angle), Write(cos_final_angle))
        self.wait()

class three_tau_over_two_minus_alpha(Scene):
    def construct(self):

        axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        circle = Circle.from_three_points(axes.c2p(-1, 0), axes.c2p(1, 0), axes.c2p(0, 1), color=WHITE)

        hyp = Line(ORIGIN, axes.c2p(1, 0), color=RED)
        hyp2 = DashedLine(ORIGIN, axes.c2p(-5/13, 12/13), color=BLUE)

        # Some text
        coord1 = MathTex(r"\left(13, 0\right)", font_size = 25).move_to(axes.c2p(1.15, 0.1))
        coord2 = MathTex(r"\left(0, 13\right)", font_size=25).move_to(axes.c2p(0.15, 1.12))
        coord3 = MathTex(r"\left(-13, 0\right)", font_size=25).move_to(axes.c2p(-1.2, 0.1))
        coord4 = MathTex(r"\left(0, -13\right)", font_size=25).move_to(axes.c2p(0.175, -1.12))
        coord_group = VGroup(coord1, coord2, coord3, coord4)

        theta_three_tau_over_2 = MathTex(r"\theta=\frac{3\tau}{2}", font_size=40).move_to(np.array([-5, 3, 0]))
        theta_minus_alpha = MathTex(r"\theta=\frac{3\tau}{2}-\alpha", font_size=40).move_to(np.array([-5, 3, 0]))

        hz_length = MathTex(r"-5", font_size=30, color=BLUE).move_to(axes.c2p(-5/26, -0.1))
        vt_length = MathTex(r"12", font_size=30, color=BLUE).move_to(axes.c2p(-0.55, 0.4))
        hyp_length = MathTex(r"13", font_size=30, color=BLUE).move_to(axes.c2p(-0.125, 0.525))

        alpha = MathTex(r"\alpha", font_size=30, color=BLUE).move_to(axes.c2p(-0.125, 0.09375))

        # Lines for final triangle
        x_line = Line(ORIGIN, axes.c2p(-5/13, 0), color=BLUE)
        y_line = Line(axes.c2p(-5/13, 12/13), axes.c2p(-5/13, 0), color=BLUE)

        # Cosine and sine of theta
        sin_final_angle = MathTex(r"\sin\left(\theta\right)=\frac{12}{13}", font_size = 35).move_to(np.array([-5, 1.25, 0]))
        cos_final_angle = MathTex(r"\cos\left(\theta\right)=-\frac{5}{13}", font_size = 35).move_to(np.array([-5, -1, 0]))

        self.add(axes)
        self.play(Create(circle))
        self.play(Write(coord_group))
        self.play(GrowFromPoint(hyp, ORIGIN))
        self.play(Rotate(hyp, 3*TAU/2, about_point=ORIGIN), Write(theta_three_tau_over_2), run_time=2.5)
        self.wait()
        self.play(GrowFromPoint(hyp2, ORIGIN), Write(alpha))
        self.play(Rotate(hyp, -67.38013505*DEGREES, about_point=ORIGIN), ReplacementTransform(theta_three_tau_over_2, theta_minus_alpha))
        self.remove(hyp2)
        self.play(GrowFromPoint(x_line, ORIGIN), GrowFromPoint(y_line, axes.c2p(-5/13, 12/13)), hyp.animate.set_color(BLUE))
        self.play(Write(hz_length), Write(vt_length), Write(hyp_length))
        self.play(Write(sin_final_angle), Write(cos_final_angle))
        self.wait()

class tau_over_four_plus_alpha(Scene):
    def construct(self):

        axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        circle = Circle.from_three_points(axes.c2p(-1, 0), axes.c2p(1, 0), axes.c2p(0, 1), color=WHITE)

        hyp = Line(ORIGIN, axes.c2p(1, 0), color=RED)

        ghost_line1 = Line(ORIGIN, axes.c2p(0, 1))
        ghost_line2 = Line(ORIGIN, axes.c2p(1, 0))
        ghost_line3 = Line(ORIGIN, axes.c2p(-12/13, 5/13))

        # Angles
        right_angle = RightAngle(ghost_line1, ghost_line2)
        final_angle = Angle(ghost_line1, ghost_line3)

        # Some text
        coord1 = MathTex(r"\left(13, 0\right)", font_size = 25).move_to(axes.c2p(1.15, 0.1))
        coord2 = MathTex(r"\left(0, 13\right)", font_size=25).move_to(axes.c2p(0.15, 1.12))
        coord3 = MathTex(r"\left(-13, 0\right)", font_size=25).move_to(axes.c2p(-1.2, -0.1))
        coord4 = MathTex(r"\left(0, -13\right)", font_size=25).move_to(axes.c2p(0.175, -1.12))
        coord_group = VGroup(coord1, coord2, coord3, coord4)

        tau_over_four = MathTex(r"\frac{\tau}{4}", font_size=25).move_to(axes.c2p(.25, .25))
        alpha = MathTex(r"\alpha", font_size=30).move_to(axes.c2p(-0.125, 0.2))

        theta_tau_over_four = MathTex(r"\theta=\frac{\tau}{4}", font_size=40).move_to(np.array([-5, 3, 0]))
        theta_equals = MathTex(r"\theta=\frac{\tau}{4}+\alpha", font_size=40).move_to(np.array([-5, 3, 0]))

        hz_length = MathTex(r"-12", font_size=30, color=RED).move_to(axes.c2p(-12/26, -0.1))
        vt_length = MathTex(r"5", font_size=30, color=RED).move_to(axes.c2p(-1.0625, 5/26))
        hyp_length = MathTex(r"13", font_size=30, color=RED).move_to(axes.c2p(-0.45, 0.3))

        # Lines for final triangle
        x_line = Line(ORIGIN, axes.c2p(-12/13, 0), color=RED)
        y_line = Line(axes.c2p(-12/13, 5/13), axes.c2p(-12/13, 0), color=RED)

        # Cosine and sine of theta
        sin_final_angle = MathTex(r"\sin\left(\theta\right)=\frac{5}{13}", font_size = 35).move_to(np.array([-5, 1.25, 0]))
        cos_final_angle = MathTex(r"\cos\left(\theta\right)=-\frac{12}{13}", font_size = 35).move_to(np.array([-5, -1, 0]))

        self.add(axes, ghost_line1)
        self.play(Create(circle))
        self.play(Write(coord_group))
        self.play(GrowFromPoint(hyp, ORIGIN))
        self.play(Rotate(hyp, TAU/4, about_point=ORIGIN), Write(theta_tau_over_four))
        self.play(Create(right_angle), Write(tau_over_four))
        self.wait()
        self.play(Rotate(hyp, 67.38013505*DEGREES, about_point=ORIGIN), ReplacementTransform(theta_tau_over_four, theta_equals))
        self.play(Create(final_angle), Write(alpha))
        self.play(GrowFromPoint(x_line, ORIGIN), GrowFromPoint(y_line, axes.c2p(-12/13, 5/13)))
        self.play(Write(hz_length), Write(vt_length), Write(hyp_length))
        self.play(Write(sin_final_angle), Write(cos_final_angle))
        self.wait()
        
