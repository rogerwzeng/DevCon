from manim import *
from math import sqrt
import numpy as np


class LagrangianMultiplier3D(ThreeDScene):
    def construct(self):
        # Set up the axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-1, 3, 1],
            axis_config={"color": BLUE},
        )

        # Labels for the axes
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # Constraint sphere
        constraint = Sphere(radius=sqrt(3), color=BLUE, fill_opacity=0.6)

        # Surface z = xy
        surface = Surface(
            lambda u, v: axes.c2p(u, v, u * v),
            u_range=[-2, 2],
            v_range=[-2, 2],
            #  checkerboard_colors=[BLUE, YELLOW_E],
            fill_opacity=0,
            resolution=(30, 30)
        )

        # Parametric equation for the intersection
        intersection = ParametricFunction(
            # lambda t: axes.c2p(sqrt(2) * np.sin(t), sqrt(2) * np.cos(t), 2 * np.sin(t) * np.cos(t)),
            lambda t: (sqrt(2) * np.sin(t), sqrt(2) * np.cos(t), 2 * np.sin(t) * np.cos(t)),
            t_range=[0, TAU],
            color=RED
        )

        point_A = Dot3D(point=(1, 1, 1), color=RED)
        point_B = Dot3D(point=(-1, -1, 1), color=RED)
        points = VGroup(point_A, point_B)

        point_A_label = MathTex(r"A \left(1, 1, 1\right)", color=RED).scale(0.5)
        point_B_label = MathTex(r"B \left(-1, -1, 1\right)", color=RED).scale(0.5)
        point_A_label.next_to(point_A, UP+RIGHT, buff=SMALL_BUFF)
        point_B_label.next_to(point_B, DOWN+LEFT, buff=SMALL_BUFF)

        # Title
        title = Text("拉格朗日乘数")
        title.scale(0.8)
        title.to_edge(UP).to_edge(LEFT)

        # Display the Lagrangian equations and gradients
        f_text = Tex(r"$f(x, y) = z = x \times y$").scale(0.75)
        f_text.to_corner(UR)
        g_text = Tex(r"$g(x, y, z) = x^2 + y^2 + z^2 = 3$").scale(0.75)
        g_text.next_to(f_text, DOWN, buff=0.5).to_edge(RIGHT)

        gradient_f = Tex(r"$\nabla f = \left( y, x, 1 \right)$", color=YELLOW).scale(0.75)
        gradient_f.next_to(g_text, DOWN, buff=0.5).to_edge(RIGHT)

        gradient_g = Tex(r"$\nabla g = \left( 2x, 2y, 2z \right)$", color=GREEN).scale(0.75)
        gradient_g.next_to(gradient_f, DOWN, buff=0.5).to_edge(RIGHT)

        gradient_eq = Tex(r"$\nabla f + \lambda \nabla g = 0$", color=WHITE).scale(0.75)
        gradient_eq.next_to(gradient_g, DOWN, buff=0.5).to_edge(RIGHT)

        lagrangian_text = Tex(r"$\mathcal{L}(x, y, \lambda) = xy + \lambda(3 - x^2 - y^2 - z^2)$").scale(0.75)
        lagrangian_text.next_to(gradient_eq, DOWN, buff=0.5).to_edge(RIGHT)


        # Fix text in place, no rotation
        self.add_fixed_in_frame_mobjects(title)
        self.add_fixed_in_frame_mobjects(f_text)
        self.add_fixed_in_frame_mobjects(g_text)
        self.add_fixed_in_frame_mobjects(gradient_g)
        self.add_fixed_in_frame_mobjects(gradient_f)
        self.add_fixed_in_frame_mobjects(gradient_eq)
        self.add_fixed_in_frame_mobjects(lagrangian_text)

        self.play(Write(title))
        self.play(Write(f_text), Write(g_text))
        self.play(Write(gradient_f), Write(gradient_g), Write(gradient_eq))
        self.play(Write(lagrangian_text))

        # Adding axes and graphics
        self.play(Create(axes), Create(labels))
        self.play(Create(constraint), Create(surface))
        self.play(Create(intersection))
        self.play(FadeIn(points), Write(point_A_label), Write(point_B_label))

        # Rotate the camera to view the 3D plot better
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Calculate and display gradients
        gradient_surface = lambda x, y: np.array([y, x, 1])
        gradient_sphere = lambda x, y, z: np.array([2*x, 2*y, 2*z])

        # points_of_interest = [(1, 1, 1), (-1, -1, 1)]
        points_of_interest = [(i, 2-i, i*(2-i)) for i in np.arange(0.5, 1.5, 0.1)]

        for point in points_of_interest:
            x, y, z = point
            grad_surf = gradient_surface(x, y)
            grad_sph = gradient_sphere(x, y, z)

            # Create vectors for the gradients
            # vector_surface = Vector(direction=grad_surf, color=YELLOW).shift(axes.c2p(x, y, z))
            # vector_sphere = Vector(direction=grad_sph, color=GREEN).shift(axes.c2p(x, y, z))
            vector_surface = Vector(direction=grad_surf, color=YELLOW).shift((x, y, z))
            vector_sphere = Vector(direction=grad_sph, color=GREEN).shift((x, y, z))

            # Add gradient vectors to the scene
            self.play(Create(vector_surface), Create(vector_sphere))


        self.wait(8)
