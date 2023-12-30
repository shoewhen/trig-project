from manim import *
import numpy as np

class unit_circle(Scene):
    def construct(self):

        # Axes
        axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        self.add(axes)
        
        # Circle
        circle = Circle.from_three_points(axes.c2p(-1, 0), axes.c2p(1, 0), axes.c2p(0, 1), color=WHITE)
        
        # Lines
        l0 = DashedLine(ORIGIN, end=axes.c2p(1, 0)).set_color(YELLOW)
        l30 = DashedLine(ORIGIN, end=axes.c2p(np.sqrt(3)/2, 1/2)).set_color(GREEN)
        l45 = DashedLine(ORIGIN, end=axes.c2p(np.sqrt(2)/2, np.sqrt(2)/2)).set_color(BLUE)
        l60 = DashedLine(ORIGIN, end=axes.c2p(1/2, np.sqrt(3)/2)).set_color(RED)
        l90 = DashedLine(ORIGIN, end=axes.c2p(0, 1)).set_color(YELLOW)
        l120 = DashedLine(ORIGIN, end=axes.c2p(-1/2, np.sqrt(3)/2)).set_color(GREEN)
        l135 = DashedLine(ORIGIN, end=axes.c2p(-np.sqrt(2)/2, np.sqrt(2)/2)).set_color(BLUE)
        l150 = DashedLine(ORIGIN, end=axes.c2p(-np.sqrt(3)/2, 1/2)).set_color(RED)
        l180 = DashedLine(ORIGIN, end=axes.c2p(-1, 0)).set_color(YELLOW)
        l210 = DashedLine(ORIGIN, end=axes.c2p(-np.sqrt(3)/2, -1/2)).set_color(GREEN)
        l225 = DashedLine(ORIGIN, end=axes.c2p(-np.sqrt(2)/2, -np.sqrt(2)/2)).set_color(BLUE)
        l240 = DashedLine(ORIGIN, end=axes.c2p(-1/2, -np.sqrt(3)/2)).set_color(RED)
        l270 = DashedLine(ORIGIN, end=axes.c2p(0, -1)).set_color(YELLOW)
        l300 = DashedLine(ORIGIN, end=axes.c2p(1/2, -np.sqrt(3)/2)).set_color(GREEN)
        l315 = DashedLine(ORIGIN, end=axes.c2p(np.sqrt(2)/2, -np.sqrt(2)/2)).set_color(BLUE)
        l330 = DashedLine(ORIGIN, end=axes.c2p(np.sqrt(3)/2, -1/2)).set_color(RED)
        
        # Angles in radians, represented using TAU
        t0 = MathTex(r"0", color=WHITE, font_size=25).move_to(axes.c2p(0.75, 0.125))
        t30 = MathTex(r"\frac{\tau}{12}", color=WHITE, font_size=25).move_to(axes.c2p(3 * np.sqrt(3) / 8, 0.375))
        t45 = MathTex(r"\frac{\tau}{8}", color=WHITE, font_size=25).move_to(axes.c2p(3 * np.sqrt(2) / 8, 3 * np.sqrt(2) / 8))
        t60 = MathTex(r"\frac{\tau}{6}", color=WHITE, font_size=25).move_to(axes.c2p(0.375, 3 * np.sqrt(3) / 8))
        t90 = MathTex(r"\frac{\tau}{4}", color=WHITE, font_size=25).move_to(axes.c2p(0.125, 0.75))
        t120 = MathTex(r"\frac{\tau}{3}", color=WHITE, font_size=25).move_to(axes.c2p(-0.375, 3 * np.sqrt(3) / 8))
        t135 = MathTex(r"\frac{3\tau}{8}", color=WHITE, font_size=25).move_to(axes.c2p(-3 * np.sqrt(2) / 8, 3 * np.sqrt(2) / 8))
        t150 = MathTex(r"\frac{5\tau}{12}", color=WHITE, font_size=25).move_to(axes.c2p(-3 * np.sqrt(3) / 8, 0.375))
        t180 = MathTex(r"\frac{\tau}{2}", color=WHITE, font_size=25).move_to(axes.c2p(-0.75, 0.125))
        t210 = MathTex(r"\frac{7\tau}{12}", color=WHITE, font_size=25).move_to(axes.c2p(-3 * np.sqrt(3) / 8, -0.375))
        t225 = MathTex(r"\frac{5\tau}{8}", color=WHITE, font_size=25).move_to(axes.c2p(-3 * np.sqrt(2) / 8, -3 * np.sqrt(2) / 8))
        t240 = MathTex(r"\frac{2\tau}{3}", color=WHITE, font_size=25).move_to(axes.c2p(-0.375, -3 * np.sqrt(3) / 8))
        t270 = MathTex(r"\frac{3\tau}{4}", color=WHITE, font_size=25).move_to(axes.c2p(-0.125, -0.75))
        t300 = MathTex(r"\frac{5\tau}{6}", color=WHITE, font_size=25).move_to(axes.c2p(0.375, -3 * np.sqrt(3) / 8))
        t315 = MathTex(r"\frac{7\tau}{8}", color=WHITE, font_size=25).move_to(axes.c2p(3 * np.sqrt(2) / 8, -3 * np.sqrt(2) / 8))
        t330 = MathTex(r"\frac{11\tau}{12}", color=WHITE, font_size=25).move_to(axes.c2p(3 * np.sqrt(3) / 8, -0.375))
        

        # Coordinate Labels
        c0 = MathTex(r"(1, 0)", color=YELLOW, font_size=30).next_to(l0, RIGHT + UP * 0.75)
        c30 = MathTex(r"\left(\frac{\sqrt{3}}{2}, \frac{1}{2}\right)", color=GREEN, font_size=25).move_to(circle.point_at_angle(TAU/12)).shift(axes.c2p(0.25, 0))
        c45 = MathTex(r"\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)", color=BLUE, font_size=25).move_to(circle.point_at_angle(TAU/8)).shift(axes.c2p(0.25, 0.15))
        c60 = MathTex(r"\left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)", color=RED, font_size=25).move_to(circle.point_at_angle(TAU/6)).shift(axes.c2p(0, 0.25))
        c90 = MathTex(r"(0, 1)", color=YELLOW, font_size=30).next_to(l90, UP * 0.75)
        c120 = MathTex(r"\left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right)", color=GREEN, font_size=25).move_to(circle.point_at_angle(TAU/3)).shift(axes.c2p(0, 0.25))
        c135 = MathTex(r"\left(-\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)", color=BLUE, font_size=25).move_to(circle.point_at_angle(3 * TAU/8)).shift(axes.c2p(-0.25, 0.15))
        c150 = MathTex(r"\left(-\frac{\sqrt{3}}{2}, \frac{1}{2}\right)", color=RED, font_size=25).move_to(circle.point_at_angle(5 * TAU/12)).shift(axes.c2p(-0.3, 0))
        c180 = MathTex(r"(-1, 0)", color=YELLOW, font_size=30).next_to(l180, LEFT + UP * 0.75)
        c210 = MathTex(r"\left(-\frac{\sqrt{3}}{2}, -\frac{1}{2}\right)", color=GREEN, font_size=25).move_to(circle.point_at_angle(7 * TAU/12)).shift(axes.c2p(-0.35, 0))
        c225 = MathTex(r"\left(-\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}\right)", color=BLUE, font_size=25).move_to(circle.point_at_angle(5 * TAU/8)).shift(axes.c2p(-0.3, -0.15))
        c240 = MathTex(r"\left(-\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)", color=RED, font_size=25).move_to(circle.point_at_angle(2 * TAU/3)).shift(axes.c2p(0, -0.25))
        c270 = MathTex(r"(0, -1)", color=YELLOW, font_size=30).next_to(l270, DOWN * 0.75)
        c300 = MathTex(r"\left(\frac{1}{2}, -\frac{\sqrt{3}}{2}\right)", color=GREEN, font_size=25).move_to(circle.point_at_angle(5 * TAU/6)).shift(axes.c2p(0, -0.25))
        c315 = MathTex(r"\left(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}\right)", color=BLUE, font_size=25).move_to(circle.point_at_angle(7 * TAU/8)).shift(axes.c2p(0.25, -0.15))
        c330 = MathTex(r"\left(\frac{\sqrt{3}}{2}, -\frac{1}{2}\right)", color=RED, font_size=25).move_to(circle.point_at_angle(11 * TAU/12)).shift(axes.c2p(0.3, 0))

        # Points
        p0 = Dot(point=circle.point_at_angle(0), color=YELLOW)
        p30 = Dot(point=circle.point_at_angle(TAU / 12), color=GREEN)
        p45 = Dot(point=circle.point_at_angle(TAU / 8), color=BLUE)
        p60 = Dot(point=circle.point_at_angle(TAU / 6), color=RED)
        p90 = Dot(point=circle.point_at_angle(TAU / 4), color=YELLOW)
        p120 = Dot(point=circle.point_at_angle(TAU / 3), color=GREEN)
        p135 = Dot(point=circle.point_at_angle(3 * TAU / 8), color=BLUE)
        p150 = Dot(point=circle.point_at_angle(5 * TAU / 12), color=RED)
        p180 = Dot(point=circle.point_at_angle(TAU / 2), color=YELLOW)
        p210 = Dot(point=circle.point_at_angle(7 * TAU / 12), color=GREEN)
        p225 = Dot(point=circle.point_at_angle(5 * TAU / 8), color=BLUE)
        p240 = Dot(point=circle.point_at_angle(2 * TAU / 3), color=RED)
        p270 = Dot(point=circle.point_at_angle(3 * TAU / 4), color=YELLOW)
        p300 = Dot(point=circle.point_at_angle(5 * TAU / 6), color=GREEN)
        p315 = Dot(point=circle.point_at_angle(7 * TAU / 8), color=BLUE)
        p330 = Dot(point=circle.point_at_angle(11 * TAU / 12), color=RED)
        
        # Animation
        self.play(Write(circle), run_time=2, rate_func=linear)
        self.play(GrowFromPoint(l0, ORIGIN), run_time=0.25)
        self.play(p0.animate, run_time=0.2)
        self.play(GrowFromPoint(l30, ORIGIN), run_time=0.25)
        self.play(p30.animate, run_time=0.2)
        self.play(GrowFromPoint(l45, ORIGIN), run_time=0.25)
        self.play(p45.animate, run_time=0.2)
        self.play(GrowFromPoint(l60, ORIGIN), run_time=0.25)
        self.play(p60.animate, run_time=0.2)
        self.play(GrowFromPoint(l90, ORIGIN), run_time=0.25)
        self.play(p90.animate, run_time=0.2)
        self.play(GrowFromPoint(l120, ORIGIN), run_time=0.25)
        self.play(p120.animate, run_time=0.2)
        self.play(GrowFromPoint(l135, ORIGIN), run_time=0.25)
        self.play(p135.animate, run_time=0.2)
        self.play(GrowFromPoint(l150, ORIGIN), run_time=0.25)
        self.play(p150.animate, run_time=0.2)
        self.play(GrowFromPoint(l180, ORIGIN), run_time=0.25)
        self.play(p180.animate, run_time=0.2)
        self.play(GrowFromPoint(l210, ORIGIN), run_time=0.25)
        self.play(p210.animate, run_time=0.2)
        self.play(GrowFromPoint(l225, ORIGIN), run_time=0.25)
        self.play(p225.animate, run_time=0.2)
        self.play(GrowFromPoint(l240, ORIGIN), run_time=0.25)
        self.play(p240.animate, run_time=0.2)
        self.play(GrowFromPoint(l270, ORIGIN), run_time=0.25)
        self.play(p270.animate, run_time=0.2)
        self.play(GrowFromPoint(l300, ORIGIN), run_time=0.25)
        self.play(p300.animate, run_time=0.2)
        self.play(GrowFromPoint(l315, ORIGIN), run_time=0.25)
        self.play(p315.animate, run_time=0.2)
        self.play(GrowFromPoint(l330, ORIGIN), run_time=0.25)
        self.play(p330.animate, run_time=0.2)

        self.play(Write(t0), run_time=0.2)
        self.play(Write(t30), run_time=0.2)
        self.play(Write(t45), run_time=0.2)
        self.play(Write(t60), run_time=0.2)
        self.play(Write(t90), run_time=0.2)
        self.play(Write(t120), run_time=0.2)
        self.play(Write(t135), run_time=0.2)
        self.play(Write(t150), run_time=0.2)
        self.play(Write(t180), run_time=0.2)
        self.play(Write(t210), run_time=0.2)
        self.play(Write(t225), run_time=0.2)
        self.play(Write(t240), run_time=0.2)
        self.play(Write(t270), run_time=0.2)
        self.play(Write(t300), run_time=0.2)
        self.play(Write(t315), run_time=0.2)
        self.play(Write(t330), run_time=0.2)

        self.play(Write(c0), Write(c30), Write(c45), Write(c60), Write(c90), Write(c120), Write(c150), Write(c135), Write(c180), Write(c210), Write(c225), Write(c240), Write(c270), Write(c300), Write(c315), Write(c330), run_time=1)

        self.wait()


class tau_over_eight(Scene):
    def construct(self):

        self.axes = axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        self.circle = circle = Circle.from_three_points(self.axes.c2p(-1, 0), self.axes.c2p(1, 0), self.axes.c2p(0, 1), color=WHITE)
        self.radius = radius = self.get_radius(0)
        self.angle  = angle  = self.get_angle()
        self.point = point = self.get_point()
        self.h = h = self.get_h()
        self.v = v = self.get_v()
        self.c_tex = c_tex = MathTex(r"\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)", color=WHITE, font_size=40).move_to(axes.c2p(np.sqrt(2)/2, np.sqrt(2)/2)).shift(axes.c2p(0.4, 0.2))
        self.angle_text = angle_tex = MathTex(r"\theta=\frac{\tau}{8}", font_size=35).move_to(np.array([-5, 2.5, 0]))
        self.sin_tex = sin_tex = MathTex(r"sin\left(\frac{\tau}{8}\right)=\frac{\sqrt{2}}{2}", font_size=40, color=BLUE).move_to(np.array([4, -2.5, 0]))
        self.cos_tex = cos_tex = MathTex(r"cos\left(\frac{\tau}{8}\right)=\frac{\sqrt{2}}{2}", font_size=40, color=RED).move_to(np.array([-4, -2.5, 0]))
 
        circle_group = VGroup(radius, angle, point, h, v)
 
        def update_group(vg, alpha):
            theta = interpolate(0, TAU / 8, alpha)
            r,a,p,h,v = vg
            r.become(self.get_radius(theta))
            a.become(self.get_angle(theta))
            p.become(self.get_point())
            h.become(self.get_h())
            v.become(self.get_v())
 
        self.add(axes, angle)
        self.play(Create(circle), run_time=1)
        self.play(Write(angle_tex))
        self.play(GrowFromPoint(radius, ORIGIN))
        self.play(
            UpdateFromAlphaFunc(
                circle_group,
                update_group,
                rate_func=linear,
            ),
        )
        self.play(Write(c_tex))
        self.play(Write(sin_tex), Write(cos_tex))
        self.wait()

    def get_radius(self,theta=0):
        return Line(
            self.circle.get_center(),
            self.circle.point_at_angle(theta),
            color=GREEN
        )

    def get_angle(self,theta=0):
        return Arc(
            radius=self.circle.radius*0.18,
            arc_center=self.circle.get_center(),
            start_angle=0,
            angle=theta,
        )
    
    def get_point(self):
        return Dot(self.radius.get_end(), color=WHITE)

    def get_h(self):
        return DashedLine(
            (0, self.radius.get_end()[1], 0),
            self.radius.get_end(),
            color=RED
        )
    
    def get_v(self):
        return DashedLine(
            self.radius.get_end(),
            (self.radius.get_end()[0], 0, 0),
            color=BLUE
        )
    

class tau_over_six(Scene):
    def construct(self):

        self.axes = axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        self.circle = circle = Circle.from_three_points(self.axes.c2p(-1, 0), self.axes.c2p(1, 0), self.axes.c2p(0, 1), color=WHITE)
        self.radius = radius = self.get_radius(0)
        self.angle  = angle  = self.get_angle()
        self.point = point = self.get_point()
        self.h = h = self.get_h()
        self.v = v = self.get_v()
        self.c_tex = c_tex = MathTex(r"\left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)", color=WHITE, font_size=40).move_to(axes.c2p(np.sqrt(1)/2, np.sqrt(3)/2)).shift(axes.c2p(0.4, 0.2))
        self.angle_text = angle_tex = MathTex(r"\theta=\frac{\tau}{6}", font_size=40).move_to(np.array([-5, 2.5, 0]))
        self.sin_tex = sin_tex = MathTex(r"sin\left(\frac{\tau}{6}\right)=\frac{\sqrt{3}}{2}", font_size=40, color=BLUE).move_to(np.array([4, -2.5, 0]))
        self.cos_tex = cos_tex = MathTex(r"cos\left(\frac{\tau}{6}\right)=\frac{1}{2}", font_size=40, color=RED).move_to(np.array([-4, -2.5, 0]))
 
        circle_group = VGroup(radius, angle, point, h, v)
 
        def update_group(vg, alpha):
            theta = interpolate(0, TAU / 6, alpha)
            r,a,p,h,v = vg
            r.become(self.get_radius(theta))
            a.become(self.get_angle(theta))
            p.become(self.get_point())
            h.become(self.get_h())
            v.become(self.get_v())
 
        self.add(axes, angle)
        self.play(Create(circle), run_time=1)
        self.play(Write(angle_tex))
        self.play(GrowFromPoint(radius, ORIGIN))
        self.play(
            UpdateFromAlphaFunc(
                circle_group,
                update_group,
                rate_func=linear,
            ),
        )
        self.play(Write(c_tex))
        self.play(Write(sin_tex), Write(cos_tex))
        self.wait()

    def get_radius(self,theta=0):
        return Line(
            self.circle.get_center(),
            self.circle.point_at_angle(theta),
            color=GREEN
        )

    def get_angle(self,theta=0):
        return Arc(
            radius=self.circle.radius*0.18,
            arc_center=self.circle.get_center(),
            start_angle=0,
            angle=theta,
        )
    
    def get_point(self):
        return Dot(self.radius.get_end(), color=WHITE)

    def get_h(self):
        return DashedLine(
            (0, self.radius.get_end()[1], 0),
            self.radius.get_end(),
            color=RED
        )
    
    def get_v(self):
        return DashedLine(
            self.radius.get_end(),
            (self.radius.get_end()[0], 0, 0),
            color=BLUE
        )
    

class tau_over_four(Scene):
    def construct(self):

        self.axes = axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        self.circle = circle = Circle.from_three_points(self.axes.c2p(-1, 0), self.axes.c2p(1, 0), self.axes.c2p(0, 1), color=WHITE)
        self.radius = radius = self.get_radius(0)
        self.angle  = angle  = self.get_angle()
        self.point = point = self.get_point()
        self.h = h = self.get_h()
        self.v = v = self.get_v()
        self.c_text = c_tex = MathTex(r"\left(0, 1)", font_size=40).move_to(axes.c2p(np.sqrt(0)/2, np.sqrt(4)/2)).shift(axes.c2p(0.3, 0.15))
        self.angle_text = angle_tex = MathTex(r"\theta=\frac{\tau}{4}", font_size=40).move_to(np.array([-5, 2.5, 0]))
        self.sin_tex = sin_tex = MathTex(r"sin\left(\frac{\tau}{4}\right)=1", font_size=40, color=BLUE).move_to(np.array([4, -2.5, 0]))
        self.cos_tex = cos_tex = MathTex(r"cos\left(\frac{\tau}{4}\right)=0", font_size=40, color=RED).move_to(np.array([-4, -2.5, 0]))
 
        circle_group = VGroup(radius, angle, point, h, v)
 
        def update_group(vg, alpha):
            theta = interpolate(0, TAU / 4, alpha)
            r,a,p,h,v = vg
            r.become(self.get_radius(theta))
            a.become(self.get_angle(theta))
            p.become(self.get_point())
            h.become(self.get_h())
            v.become(self.get_v())
 
        self.add(axes, angle)
        self.play(Create(circle), run_time=1)
        self.play(Write(angle_tex))
        self.play(GrowFromPoint(radius, ORIGIN))
        self.play(
            UpdateFromAlphaFunc(
                circle_group,
                update_group,
                rate_func=linear,
            ),
        )
        self.play(Write(c_tex))
        self.play(Write(sin_tex), Write(cos_tex))
        self.wait()

    def get_radius(self,theta=0):
        return Line(
            self.circle.get_center(),
            self.circle.point_at_angle(theta),
            color=GREEN
        )

    def get_angle(self,theta=0):
        return Arc(
            radius=self.circle.radius*0.18,
            arc_center=self.circle.get_center(),
            start_angle=0,
            angle=theta,
        )
    
    def get_point(self):
        return Dot(self.radius.get_end(), color=WHITE)

    def get_h(self):
        return DashedLine(
            (0, self.radius.get_end()[1], 0),
            self.radius.get_end(),
            color=RED
        )
    
    def get_v(self):
        return DashedLine(
            self.radius.get_end(),
            (self.radius.get_end()[0], 0, 0),
            color=BLUE
        )
        

class tau_over_three(Scene):
    def construct(self):

        self.axes = axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        self.circle = circle = Circle.from_three_points(self.axes.c2p(-1, 0), self.axes.c2p(1, 0), self.axes.c2p(0, 1), color=WHITE)
        self.radius = radius = self.get_radius(0)
        self.angle  = angle  = self.get_angle()
        self.point = point = self.get_point()
        self.h = h = self.get_h()
        self.v = v = self.get_v()
        self.c_tex = c_tex = MathTex(r"\left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right)", color=WHITE, font_size=40).move_to(axes.c2p(-np.sqrt(1)/2, np.sqrt(3)/2)).shift(axes.c2p(-0.45, 0.2))
        self.angle_text = angle_tex = MathTex(r"\theta=\frac{\tau}{3}", font_size=40).move_to(np.array([5, 2.5, 0]))
        self.sin_tex = sin_tex = MathTex(r"sin\left(\frac{\tau}{3}\right)=\frac{\sqrt{3}}{2}", font_size=40, color=BLUE).move_to(np.array([4, -2.5, 0]))
        self.cos_tex = cos_tex = MathTex(r"cos\left(\frac{\tau}{3}\right)=-\frac{1}{2}", font_size=40, color=RED).move_to(np.array([-4, -2.5, 0]))
 
        circle_group = VGroup(radius, angle, point, h, v)
 
        def update_group(vg, alpha):
            theta = interpolate(0, TAU / 3, alpha)
            r,a,p,h,v = vg
            r.become(self.get_radius(theta))
            a.become(self.get_angle(theta))
            p.become(self.get_point())
            h.become(self.get_h())
            v.become(self.get_v())
 
        self.add(axes, angle)
        self.play(Create(circle), run_time=1)
        self.play(Write(angle_tex))
        self.play(GrowFromPoint(radius, ORIGIN))
        self.play(
            UpdateFromAlphaFunc(
                circle_group,
                update_group,
                rate_func=linear,
            ),
        )
        self.play(Write(c_tex))
        self.play(Write(sin_tex), Write(cos_tex))
        self.wait()

    def get_radius(self,theta=0):
        return Line(
            self.circle.get_center(),
            self.circle.point_at_angle(theta),
            color=GREEN
        )

    def get_angle(self,theta=0):
        return Arc(
            radius=self.circle.radius*0.18,
            arc_center=self.circle.get_center(),
            start_angle=0,
            angle=theta,
        )
    
    def get_point(self):
        return Dot(self.radius.get_end(), color=WHITE)

    def get_h(self):
        return DashedLine(
            (0, self.radius.get_end()[1], 0),
            self.radius.get_end(),
            color=RED
        )
    
    def get_v(self):
        return DashedLine(
            self.radius.get_end(),
            (self.radius.get_end()[0], 0, 0),
            color=BLUE
        )

    
class tau_over_two(Scene):
    def construct(self):

        self.axes = axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        self.circle = circle = Circle.from_three_points(self.axes.c2p(-1, 0), self.axes.c2p(1, 0), self.axes.c2p(0, 1), color=WHITE)
        self.radius = radius = self.get_radius(0)
        self.angle  = angle  = self.get_angle()
        self.point = point = self.get_point()
        self.h = h = self.get_h()
        self.v = v = self.get_v()
        self.c_tex = c_tex = MathTex(r"\left(-1, 0\right)", color=WHITE, font_size=40).move_to(axes.c2p(-np.sqrt(4)/2, np.sqrt(0)/2)).shift(axes.c2p(-0.55, 0))
        self.angle_text = angle_tex = MathTex(r"\theta=\frac{\tau}{2}", font_size=40).move_to(np.array([5, 2.5, 0]))
        self.sin_tex = sin_tex = MathTex(r"sin\left(\frac{\tau}{2}\right)=0", font_size=40, color=BLUE).move_to(np.array([4, -2.5, 0]))
        self.cos_tex = cos_tex = MathTex(r"cos\left(\frac{\tau}{2}\right)=-1", font_size=40, color=RED).move_to(np.array([-4, -2.5, 0]))
 
        circle_group = VGroup(radius, angle, point, h, v)
 
        def update_group(vg, alpha):
            theta = interpolate(0, TAU / 2, alpha)
            r,a,p,h,v = vg
            r.become(self.get_radius(theta))
            a.become(self.get_angle(theta))
            p.become(self.get_point())
            h.become(self.get_h())
            v.become(self.get_v())
 
        self.add(axes, angle)
        self.play(Create(circle), run_time=1)
        self.play(Write(angle_tex))
        self.play(GrowFromPoint(radius, ORIGIN))
        self.play(
            UpdateFromAlphaFunc(
                circle_group,
                update_group,
                rate_func=linear,
            ),
        )
        self.play(Write(c_tex))
        self.play(Write(sin_tex), Write(cos_tex))
        self.wait()

    def get_radius(self,theta=0):
        return Line(
            self.circle.get_center(),
            self.circle.point_at_angle(theta),
            color=GREEN
        )

    def get_angle(self,theta=0):
        return Arc(
            radius=self.circle.radius*0.18,
            arc_center=self.circle.get_center(),
            start_angle=0,
            angle=theta,
        )
    
    def get_point(self):
        return Dot(self.radius.get_end(), color=WHITE)

    def get_h(self):
        return DashedLine(
            (0, self.radius.get_end()[1], 0),
            self.radius.get_end(),
            color=RED
        )
    
    def get_v(self):
        return DashedLine(
            self.radius.get_end(),
            (self.radius.get_end()[0], 0, 0),
            color=BLUE
        )

class seven_tau_over_eight(Scene):
    def construct(self):

        self.axes = axes = Axes(x_range =[-1.25, 1.25, 0.25], y_range=[-1.25, 1.25, 0.25], x_length=7, y_length=7, axis_config={"include_tip": False, "font_size": 20})
        self.circle = circle = Circle.from_three_points(self.axes.c2p(-1, 0), self.axes.c2p(1, 0), self.axes.c2p(0, 1), color=WHITE)
        self.radius = radius = self.get_radius(0)
        self.angle  = angle  = self.get_angle()
        self.point = point = self.get_point()
        self.h = h = self.get_h()
        self.v = v = self.get_v()
        self.c_tex = c_tex = MathTex(r"\left(\frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2}\right)", color=WHITE, font_size=40).move_to(axes.c2p(np.sqrt(2)/2, -np.sqrt(2)/2)).shift(axes.c2p(0.45, -0.2))
        self.angle_text = angle_tex = MathTex(r"\theta=\frac{7\tau}{8}", font_size=40).move_to(np.array([-5, -2.5, 0]))
        self.sin_tex = sin_tex = MathTex(r"sin\left(\frac{7\tau}{8}\right)=-\frac{\sqrt{2}}{2}", font_size=40, color=BLUE).move_to(np.array([4, 2.5, 0]))
        self.cos_tex = cos_tex = MathTex(r"cos\left(\frac{7\tau}{8}\right)=\frac{\sqrt{2}}{2}", font_size=40, color=RED).move_to(np.array([-4, 2.5, 0]))
 
        circle_group = VGroup(radius, angle, point, h, v)
 
        def update_group(vg, alpha):
            theta = interpolate(0, 7 * TAU / 8, alpha)
            r,a,p,h,v = vg
            r.become(self.get_radius(theta))
            a.become(self.get_angle(theta))
            p.become(self.get_point())
            h.become(self.get_h())
            v.become(self.get_v())
 
        self.add(axes, angle)
        self.play(Create(circle), run_time=1)
        self.play(Write(angle_tex))
        self.play(GrowFromPoint(radius, ORIGIN))
        self.play(
            UpdateFromAlphaFunc(
                circle_group,
                update_group,
                rate_func=linear,
            ),
        )
        self.play(Write(c_tex))
        self.play(Write(sin_tex), Write(cos_tex))
        self.wait()

    def get_radius(self,theta=0):
        return Line(
            self.circle.get_center(),
            self.circle.point_at_angle(theta),
            color=GREEN
        )

    def get_angle(self,theta=0):
        return Arc(
            radius=self.circle.radius*0.18,
            arc_center=self.circle.get_center(),
            start_angle=0,
            angle=theta,
        )
    
    def get_point(self):
        return Dot(self.radius.get_end(), color=WHITE)

    def get_h(self):
        return DashedLine(
            (0, self.radius.get_end()[1], 0),
            self.radius.get_end(),
            color=RED
        )
    
    def get_v(self):
        return DashedLine(
            self.radius.get_end(),
            (self.radius.get_end()[0], 0, 0),
            color=BLUE
        )