from manim import *
import numpy as np

# Find all the angles that satisfy the given equation
class sin_equals_one_half(Scene):
    def construct(self):
        axes_right = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        axes_left = axes_right.copy()
        axes = VGroup(axes_left, axes_right).arrange(RIGHT, buff=2).scale_to_fit_width(12)
        self.add(axes)

        circle_right = Circle.from_three_points(axes_right.c2p(-1, 0), axes_right.c2p(1, 0), axes_right.c2p(0, 1), color=WHITE)
        circle_left = Circle.from_three_points(axes_left.c2p(-1, 0), axes_left.c2p(1, 0), axes_left.c2p(0, 1), color=WHITE)

        self.play(Create(circle_right), Create(circle_left), run_time=1)
        
        # Rotating radius line on the right axes
        rotation_center = axes_right.c2p(0, 0)
        theta_tracker = ValueTracker(0.01)
        line1 = Line(axes_right.c2p(0,0), axes_right.c2p(1,0)).set_opacity(0)
        line_moving = Line(axes_right.c2p(0,0), axes_right.c2p(1,0)).set_color(BLUE)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        # Rotating radius line on the left axes
        rotation_center_left = axes_left.c2p(0, 0)
        theta_tracker_left = ValueTracker(0.01)
        line1_left = Line(axes_left.c2p(0,0), axes_left.c2p(1,0)).set_opacity(0)
        line_moving_left = Line(axes_left.c2p(0,0), axes_left.c2p(1,0)).set_color(BLUE)
        line_ref_left = line_moving_left.copy()
        line_moving_left.rotate(
            theta_tracker_left.get_value() * DEGREES, about_point=rotation_center_left
        )

        # Animates the creation of the radius lines
        self.play(GrowFromPoint(line1, axes_right.c2p(0,0)), GrowFromPoint(line_moving, axes_right.c2p(0,0)), GrowFromPoint(line1_left, axes_left.c2p(0,0)), GrowFromPoint(line_moving_left, axes_left.c2p(0,0)))

        # Updaters for rotating radius lines
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        line_moving_left.add_updater(
            lambda x: x.become(line_ref_left.copy()).rotate(
                theta_tracker_left.get_value() * DEGREES, about_point=rotation_center_left
            )
        )

        # All the tex and the rest of the frontend
        y_line_left = DashedLine(axes_left.c2p(-np.sqrt(3)/2, 0), axes_left.c2p(-np.sqrt(3)/2, 1/2)).set_color(GREEN)
        y_line = DashedLine(axes_right.c2p(np.sqrt(3)/2, 0), axes_right.c2p(np.sqrt(3)/2, 1/2)).set_color(GREEN)

        equation1 = MathTex(r"\sin\left(\theta\right)=\frac{1}{2}", font_size=30).move_to(np.array([-5, 3, 0]))
        one_half_left = MathTex(r"\frac{1}{2}", font_size=30, color=GREEN).move_to(axes_left.c2p(-1.125, 0.25))
        one_half = MathTex(r"\frac{1}{2}", font_size=30, color=GREEN).move_to(axes_right.c2p(1.125, 0.25))

        theta_equals1_left = MathTex(r"\theta=\frac{5\tau}{12}", font_size=30).move_to(np.array([-5, 3, 0]))
        theta_equals1 = MathTex(r"\theta=\frac{\tau}{12}", font_size=30).move_to(np.array([5, 3, 0]))

        theta_equals2_left = MathTex(r"\theta=\frac{5\tau}{12} + \tau", font_size=30).move_to(np.array([-5, 3, 0]))
        theta_equals2 = MathTex(r"\theta=\frac{\tau}{12} + \tau", font_size=30).move_to(np.array([5, 3, 0]))

        equation2_left = MathTex(r"\sin\left(\frac{5\tau}{12}+\tau\right)=\frac{1}{2}", font_size=30).move_to(np.array([-5, 3, 0]))
        equation2 = MathTex(r"\sin\left(\frac{\tau}{12}+\tau\right)=\frac{1}{2}", font_size=30).move_to(np.array([5, 3, 0]))

        theta_equals3_left = MathTex(r"\theta=\frac{5\tau}{12}+k\ \cdot\ \tau", font_size=30).move_to(np.array([-5, 3, 0]))
        theta_equals3 = MathTex(r"\theta=\frac{\tau}{12}+k\ \cdot\ \tau", font_size=30).move_to(np.array([5, 3, 0]))

        equation3_left = MathTex(r"\sin\left(\frac{5\tau}{12}+k\ \cdot\ \tau\right)=\frac{1}{2}", font_size=30).move_to(np.array([-5, 3, 0]))
        equation3 = MathTex(r"\sin\left(\frac{\tau}{12}+k\ \cdot\ \tau\right)=\frac{1}{2}", font_size=30).move_to(np.array([5, 3, 0]))

        # Full animation
        self.play(Write(equation1))
        self.play(theta_tracker.animate.set_value(29.9), theta_tracker_left.animate.set_value(149.9))
        self.play(GrowFromPoint(y_line_left, axes_left.c2p(-np.sqrt(3)/2, 0)), GrowFromPoint(y_line, axes_right.c2p(np.sqrt(3)/2, 0)))
        self.play(Write(one_half_left), Write(one_half))
        self.play(ReplacementTransform(equation1, theta_equals1_left), Write(theta_equals1))
        self.wait()
        self.play(FadeOut(y_line), FadeOut(y_line_left), FadeOut(one_half), FadeOut(one_half_left))
        self.play(theta_tracker.animate.set_value(389.9), theta_tracker_left.animate.set_value(509.9), ReplacementTransform(theta_equals1_left, theta_equals2_left), ReplacementTransform(theta_equals1, theta_equals2))
        self.play(GrowFromPoint(y_line_left, axes_left.c2p(-np.sqrt(3)/2, 0)), GrowFromPoint(y_line, axes_right.c2p(np.sqrt(3)/2, 0)))
        self.play(Write(one_half_left), Write(one_half))
        self.play(ReplacementTransform(theta_equals2_left, equation2_left), ReplacementTransform(theta_equals2, equation2))
        self.wait()
        self.play(FadeOut(y_line), FadeOut(y_line_left), FadeOut(one_half), FadeOut(one_half_left))
        self.play(theta_tracker.animate.set_value(2189.9), theta_tracker_left.animate.set_value(2309.9), ReplacementTransform(equation2_left, theta_equals3_left), ReplacementTransform(equation2, theta_equals3), run_time=5)
        self.play(GrowFromPoint(y_line_left, axes_left.c2p(-np.sqrt(3)/2, 0)), GrowFromPoint(y_line, axes_right.c2p(np.sqrt(3)/2, 0)))
        self.play(Write(one_half_left), Write(one_half))
        self.play(ReplacementTransform(theta_equals3_left, equation3_left), ReplacementTransform(theta_equals3, equation3))
        # self.play(theta_tracker.animate.increment_value(120))
        self.wait(2)


# Find all the angles that staisfy the given equation
class cos_equals_negative_sqrt3_over_2(Scene):
    def construct(self):
        axes_right = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        axes_left = axes_right.copy()
        axes = VGroup(axes_left, axes_right).arrange(RIGHT, buff=2).scale_to_fit_width(12)
        self.add(axes)

        circle_right = Circle.from_three_points(axes_right.c2p(-1, 0), axes_right.c2p(1, 0), axes_right.c2p(0, 1), color=WHITE)
        circle_left = Circle.from_three_points(axes_left.c2p(-1, 0), axes_left.c2p(1, 0), axes_left.c2p(0, 1), color=WHITE)

        self.play(Create(circle_right), Create(circle_left), run_time=1)
        
        # Rotating radius line on the right axes
        rotation_center = axes_right.c2p(0, 0)
        theta_tracker = ValueTracker(0.01)
        line1 = Line(axes_right.c2p(0,0), axes_right.c2p(1,0)).set_opacity(0)
        line_moving = Line(axes_right.c2p(0,0), axes_right.c2p(1,0)).set_color(RED)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        # Rotating radius line on the left axes
        rotation_center_left = axes_left.c2p(0, 0)
        theta_tracker_left = ValueTracker(0.01)
        line1_left = Line(axes_left.c2p(0,0), axes_left.c2p(1,0)).set_opacity(0)
        line_moving_left = Line(axes_left.c2p(0,0), axes_left.c2p(1,0)).set_color(RED)
        line_ref_left = line_moving_left.copy()
        line_moving_left.rotate(
            theta_tracker_left.get_value() * DEGREES, about_point=rotation_center_left
        )

        # Animates the creation of the radius lines
        self.play(GrowFromPoint(line1, axes_right.c2p(0,0)), GrowFromPoint(line_moving, axes_right.c2p(0,0)), GrowFromPoint(line1_left, axes_left.c2p(0,0)), GrowFromPoint(line_moving_left, axes_left.c2p(0,0)))

        # Updaters for rotating radius lines
        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        line_moving_left.add_updater(
            lambda x: x.become(line_ref_left.copy()).rotate(
                theta_tracker_left.get_value() * DEGREES, about_point=rotation_center_left
            )
        )

        # All the tex and the rest of the frontend
        x_line_left = DashedLine(axes_left.c2p(-np.sqrt(3)/2, 0.5), axes_left.c2p(0, 0.5)).set_color(YELLOW)
        x_line = DashedLine(axes_right.c2p(-np.sqrt(3)/2, -0.5), axes_right.c2p(0, -0.5)).set_color(YELLOW)

        equation1 = MathTex(r"\cos\left(\theta\right)=-\frac{\sqrt{3}}{2}", font_size=30).move_to(np.array([-5, 3, 0]))
        one_half_left = MathTex(r"-\frac{\sqrt{3}}{2}", font_size=25, color=YELLOW).move_to(axes_left.c2p(-0.45, 0.7))
        one_half = MathTex(r"-\frac{\sqrt{3}}{2}", font_size=25, color=YELLOW).move_to(axes_right.c2p(-0.45, -0.7))

        theta_equals1_left = MathTex(r"\theta=\frac{5\tau}{12}", font_size=30).move_to(np.array([-5, 3, 0]))
        theta_equals1 = MathTex(r"\theta=\frac{7\tau}{12}", font_size=30).move_to(np.array([5, 3, 0]))

        theta_equals2_left = MathTex(r"\theta=\frac{5\tau}{12} + \tau", font_size=30).move_to(np.array([-5, 3, 0]))
        theta_equals2 = MathTex(r"\theta=\frac{7\tau}{12} + \tau", font_size=30).move_to(np.array([5, 3, 0]))

        equation2_left = MathTex(r"\cos\left(\frac{5\tau}{12}+\tau\right)=-\frac{\sqrt{3}}{2}", font_size=30).move_to(np.array([-5, 3, 0]))
        equation2 = MathTex(r"\cos\left(\frac{7\tau}{12}+\tau\right)=-\frac{\sqrt{3}}{2}", font_size=30).move_to(np.array([5, 3, 0]))

        theta_equals3_left = MathTex(r"\theta=\frac{5\tau}{12}+k\ \cdot\ \tau", font_size=30).move_to(np.array([-5, 3, 0]))
        theta_equals3 = MathTex(r"\theta=\frac{7\tau}{12}+k\ \cdot\ \tau", font_size=30).move_to(np.array([5, 3, 0]))

        equation3_left = MathTex(r"\cos\left(\frac{5\tau}{12}+k\ \cdot\ \tau\right)=-\frac{\sqrt{3}}{2}", font_size=30).move_to(np.array([-4.5, 3.2, 0]))
        equation3 = MathTex(r"\cos\left(\frac{7\tau}{12}+k\ \cdot\ \tau\right)=-\frac{\sqrt{3}}{2}", font_size=30).move_to(np.array([4.5, 3.2, 0]))

        # Full animation
        self.play(Write(equation1))
        self.play(theta_tracker.animate.set_value(209.9), theta_tracker_left.animate.set_value(149.9))
        self.play(GrowFromPoint(x_line_left, axes_left.c2p(-np.sqrt(3)/2, 1/2)), GrowFromPoint(x_line, axes_right.c2p(-np.sqrt(3)/2, -0.5)))
        self.play(Write(one_half_left), Write(one_half))
        self.play(ReplacementTransform(equation1, theta_equals1_left), Write(theta_equals1))
        self.wait()
        self.play(FadeOut(x_line), FadeOut(x_line_left), FadeOut(one_half), FadeOut(one_half_left))
        self.play(theta_tracker.animate.set_value(569.9), theta_tracker_left.animate.set_value(509.9), ReplacementTransform(theta_equals1_left, theta_equals2_left), ReplacementTransform(theta_equals1, theta_equals2))
        self.play(GrowFromPoint(x_line_left, axes_left.c2p(-np.sqrt(3)/2, 1/2)), GrowFromPoint(x_line, axes_right.c2p(-np.sqrt(3)/2, -0.5)))
        self.play(Write(one_half_left), Write(one_half))
        self.play(ReplacementTransform(theta_equals2_left, equation2_left), ReplacementTransform(theta_equals2, equation2))
        self.wait()
        self.play(FadeOut(x_line), FadeOut(x_line_left), FadeOut(one_half), FadeOut(one_half_left))
        self.play(theta_tracker.animate.set_value(2369.9), theta_tracker_left.animate.set_value(2309.9), ReplacementTransform(equation2_left, theta_equals3_left), ReplacementTransform(equation2, theta_equals3), run_time=5)
        self.play(GrowFromPoint(x_line_left, axes_left.c2p(-np.sqrt(3)/2, 1/2)), GrowFromPoint(x_line, axes_right.c2p(-np.sqrt(3)/2, -0.5)))
        self.play(Write(one_half_left), Write(one_half))
        self.play(ReplacementTransform(theta_equals3_left, equation3_left), ReplacementTransform(theta_equals3, equation3))
        # self.play(theta_tracker.animate.increment_value(120))
        self.wait(2)