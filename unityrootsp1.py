from manim import *
from lib import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

class MainScene(MovingCameraScene, VoiceoverScene):

    def construct(self):
        self.create_subcaption = False
        self.camera.background_color = BLUEISHGREY

        self.set_speech_service(
            OpenAIService(
                voice="alloy",
                model="gpt-4o-mini-tts",
            )
        )

        # Title
        title = TNT().txt("Roots of unity", weight="SEMIBOLD", color=PURPLE).scale(2)

        # Logo
        logo = ImageMobject('Sowiso-logo-primary.png').scale(0.03)

        # text top left
        roots_of_unity_title = TNT().txt(
            'Roots of unity',
            color=PINK,
            weight="SEMIBOLD"
        ).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.1)

        # setup example rectangle
        ex1_rect = swRoundedRectangle(height=2.1, width=2.5)

        # propose problem
        problem = TNT()\
            .txt("We will solve the equation ")\
            .tx('z^n=1')\
            .shift(UP * 0.8)\
            .set_color_by_string('z', BLUE)\
            .set_color_by_string('n', swGOLD)

        this_equation_has_n_roots = TNT()\
            .txt("This equation has ")\
            .tx('n', aligned_char='n', color=swGOLD)\
            .txt(' distinct solutions')\
            .shift(UP * 0.6)\
            .set_color_by_string('n', swGOLD)

        z_is_1 = TNT()\
            .tx('z=1')\
            .txt(' is always a solution')\
            .shift(UP * 0.5)\
            .set_color_by_string('z', BLUE)

        z_is_minus_1 = TNT()\
            .tx('z=-1')\
            .txt(' is a solution when ')\
            .tx('n')\
            .txt(' is even')\
            .shift(UP * 0.4)\
            .set_color_by_string('z', BLUE)\
            .set_color_by_string('n', swGOLD)

        by_rewriting = TNT()\
            .txt("By rewriting the equation using")\

        the_polar_exp = TNT()\
            .txt("the ")\
            .txt("polar-exponential form,", weight="SEMIBOLD")\
            .txt('we get')\

        polar_exp1 = TNT().tx('z^n=1')\
            .set_color_by_string('z', BLUE)\
            .set_color_by_string('n', swGOLD)

        polar_exp2 = TNT()\
            .tx('(\\|z\\|\\cdot \\mathrm{e}^{\\varphi \\cdot \\mathrm{i}})^n = \\|1\\|\\cdot \\mathrm{e}^{2 \\cdot k \\cdot \\pi \\cdot \\mathrm{i}}')\
            .set_color_by_string('z', BLUE)\
            .set_color_by_string('n', swGOLD)\
            .set_color_by_string('\\varphi', GREEN)

        polar_exp2_5 = TNT()\
            .tx('\\|z\\|^n\\cdot \\mathrm{e}^{n \\cdot \\varphi \\cdot \\mathrm{i}} = \\|1\\|\\cdot \\mathrm{e}^{2 \\cdot k \\cdot \\pi \\cdot \\mathrm{i}}')\
            .set_color_by_string('z', BLUE)\
            .set_color_by_string('n', swGOLD)\
            .set_color_by_string('\\varphi', GREEN)

        polar_exp3 = TNT()\
            .txt('The norm')\
            .tx('\\|z\\|^n=\\|1\\|')\
            .set_color_by_string('z', BLUE)\
            .set_color_by_string('n', swGOLD)

        polar_exp3_1 = TNT()\
            .txt('The norm')\
            .tx('\\|z\\|=1')\
            .set_color_by_string('z', BLUE)

        polar_exp4 = TNT()\
            .txt('The argument ')\
            .tx('\\varphi = \\dfrac{2\\cdot k \\cdot \\pi}{n}')\
            .set_color_by_string('\\varphi', GREEN)\
            .set_color_by_string('n', swGOLD)

        polar_exp5 = TNT()\
            .txt('There are ')\
            .tx('n', aligned_char='n', color=swGOLD)\
            .txt(' solutions for ')\
            .tx('-\\pi < \\varphi \\leq \\pi', aligned_char='<')\
            .set_color_by_string('n', swGOLD)\
            .set_color_by_string('\\varphi', GREEN)

        first_scene_tnts = VGroup(
            problem,
            this_equation_has_n_roots,
            z_is_1,
            z_is_minus_1,
            by_rewriting,
            the_polar_exp,
            polar_exp1,
            polar_exp2,
            polar_exp3,
            polar_exp4,
            polar_exp5
        )

        ex1_rect.create_content(first_scene_tnts, offset=0.075)
        polar_exp2_5.move_to(polar_exp2.get_center())
        polar_exp3_1.move_to(polar_exp3.get_center())

        fadeout_group = VGroup(
            problem,
            this_equation_has_n_roots,
            z_is_1, z_is_minus_1,
            by_rewriting, the_polar_exp,
            polar_exp1, polar_exp2_5,
            polar_exp3_1, polar_exp4,
            polar_exp5
        )

        # #####################
        # EXAMPLE n=3
        # #####################

        # setup the plane
        polarplane_pi = swPolarPlane(
            angle_step=np.pi/12,
            add_complex_labels=True
        ).scale(0.25)
    
        # right rectangle
        polarplane_rect = swRoundedRectangle(height=2.1, width=2.2)\
            .move_to(polarplane_pi.get_center())

        example_n3_rect = swRoundedRectangle(height=2.1, width=2)\
            .shift(LEFT * 1.15)

        solve_n3_is_1 = TNT()\
            .txt('Solve ')\
            .tx('z^3=1')\
            .move_to(example_n3_rect.get_center() + UP * 0.9)\
            .set_color_by_string('3', swGOLD)\
            .set_color_by_string('z', BLUE)

        the_other_solutions = TNT()\
            .txt('We have ')\
            .tx('\\|z\\|=1')\
            .move_to(example_n3_rect.get_center())\
            .shift(UP * 0.6)\
            .set_color_by_string('z', BLUE)

        where_phi = TNT()\
            .txt('and ')\
            .tx('\\varphi=\\dfrac{2\\cdot k \\cdot \\pi}{3}')\
            .move_to(example_n3_rect.get_center())\
            .shift(UP * 0.4)\
            .set_color_by_string('3', swGOLD)\
            .set_color_by_string('\\varphi', GREEN)

        phi_inequalities_must_hold = TNT()\
            .tx('-\\pi < \\varphi \\leq \\pi')\
            .txt(' must hold')\
            .move_to(example_n3_rect.get_center())\
            .shift(UP * 0.2)\
            .set_color_by_string('\\varphi', GREEN)

        picking_k_is_0 = TNT()\
            .txt('For ')\
            .tx('k=0,')\
            .txt(' we get ')\
            .tx('z = 1')\
            .move_to(example_n3_rect.get_center())\
            .shift(DOWN * 0.0)\
            .set_color_by_string('z', BLUE)

        picking_k_is_1 = TNT()\
            .txt('For ')\
            .tx('k=1,')\
            .txt(' we get ')\
            .tx('z = \\mathrm{e}^{\\frac{2\\cdot \\pi}{3}\\cdot \\mathrm{i}}')\
            .move_to(example_n3_rect.get_center())\
            .shift(DOWN * 0.2)\
            .set_color_by_string('3', swGOLD)\
            .set_color_by_string('z', BLUE)

        picking_k_is_2 = TNT()\
            .txt('For ')\
            .tx('k=2,')\
            .txt(' we get ')\
            .tx('z = \\mathrm{e}^{\\frac{4\\cdot \\pi}{3}\\cdot \\mathrm{i}}')\
            .move_to(example_n3_rect.get_center())\
            .shift(DOWN * 0.4)\
            .set_color_by_string('3', swGOLD)\
            .set_color_by_string('z', BLUE)

        picking_k_is_minus_1 = TNT()\
            .txt('For ')\
            .tx('k=2,')\
            .txt(' we get ')\
            .tx('z = \\mathrm{e}^{-\\frac{2\\cdot \\pi}{3}\\cdot \\mathrm{i}}')\
            .move_to(example_n3_rect.get_center())\
            .shift(DOWN * 0.4)\
            .set_color_by_string('3', swGOLD)\
            .set_color_by_string('z', BLUE)

        solutions = TNT()\
            .txt('Solutions:')\
            .tx('z=1\\vee z=\\mathrm{e}^{\\frac{2\\cdot \\pi}{3}\\cdot \\mathrm{i}}\\vee z=\\mathrm{e}^{-\\frac{2\\cdot \\pi}{3}\\cdot \\mathrm{i}}')\
            .move_to(example_n3_rect.get_center())\
            .set_color_by_string('3', swGOLD)\
            .set_color_by_string('z', BLUE)

        n3_content_group = VGroup(
            the_other_solutions,
            where_phi,
            phi_inequalities_must_hold,
            picking_k_is_0,
            picking_k_is_1,
            picking_k_is_2,
            solutions
        )

        example_n3_rect.set_title(solve_n3_is_1)
        example_n3_rect.create_content(n3_content_group, offset=0.1)
        picking_k_is_minus_1.move_to(picking_k_is_2.get_center())

        org = polarplane_pi.polar_to_point(0,0)
        p1 = polarplane_pi.polar_to_point(1,0)
        p2 = polarplane_pi.polar_to_point(1,PI*2/3)
        p3 = polarplane_pi.polar_to_point(1,PI*4/3)

        vec_1 = Line(org, p1, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)\
            .shift(RIGHT * 1.1 + UP *0.01)
        vec_2 = Line(org, p2, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)\
            .shift(RIGHT * 1.1 + UP *0.01)
        vec_3 = Line(org, p3, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)\
            .shift(RIGHT * 1.1 + UP *0.01)

        polarplane_group = VGroup(ex1_rect, polarplane_pi)


        # ANIMATIONS
        self.add(logo)
        self.wait(1)
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.1*UP + 0.35 * RIGHT)
            .scale(0.009 / 0.03))

        with self.voiceover(text="This video shows how to calculate the roots of unity.") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)
        self.play(swWrite(roots_of_unity_title))

        with self.voiceover(text="We will solve the equation 'z' to the power of 'n' is equal to 1.") as tracker:
            self.play(Create(ex1_rect))
            self.play(swWrite(problem))

        with self.voiceover(text="This equation has n distinct solutions.") as tracker:
            self.play(swWrite(this_equation_has_n_roots))

        self.wait(0.3)

        with self.voiceover(text="'z' equals 1 is always a solution") as tracker:
            self.play(swWrite(z_is_1))

        with self.voiceover(text="and 'z' equals -1 is a solution when n is even") as tracker:
            self.play(swWrite(z_is_minus_1))

        self.wait(0.3)

        with self.voiceover(text="By rewriting the equation using the polar exponential form, we get the following equations.") as tracker:
            self.play(swWrite(by_rewriting))
            self.play(swWrite(the_polar_exp))

        self.play(swWrite(polar_exp1))

        with self.voiceover(text="We can write 'z' to the power of n and 1 in polar exponential form like this. Remember that 'k' can be any integer.") as tracker:
            self.play(swWrite(polar_exp2))

        self.wait(0.5)

        with self.voiceover(text="We can apply De Moivre's theorem to the left side of the equation to distribute the power of n.") as tracker:
            self.play(TransformMatchingShapes(polar_exp2, polar_exp2_5))

        with self.voiceover(text="To solve, we equate the norms of each side to each other and do the same thing for the arguments.") as tracker:
            self.play(swWrite(polar_exp3))

        with self.voiceover(text="This means that the norm of 'z' is equal to 1.") as tracker:
            self.play(TransformMatchingShapes(polar_exp3, polar_exp3_1))

        self.wait(0.5)

        with self.voiceover(text="The argument φ of 'z' is equal to 2 times k times π divided by n.") as tracker:
            self.play(swWrite(polar_exp4))

        with self.voiceover(text="notice that when 'k'=0 we also get φ=0 so 'z'=1. When 'k' over 'n' is one half, then φ is π, which means z equals minus 1. This can only happen if 'n' is 'even'") as tracker:
            self.wait(1)

        with self.voiceover(text="Therefore, there are n solutions for φ larger than minus π and smaller than or equal to pi. ") as tracker:
            self.play(swWrite(polar_exp5))

        # end of theory part / start n = 3 example
        self.play(FadeOut(fadeout_group))
        self.play(Transform(ex1_rect, polarplane_rect))

        with self.voiceover(text="We will now take a look at an example and draw the solutions in an Argand diagram.") as tracker:
            self.play(Create(polarplane_pi))

        self.play(polarplane_group.animate.shift(RIGHT * 1.1 + UP * 0.01))

        with self.voiceover(text="We will start with the example of 'z' to the power of 3 equals 1.") as tracker:
            self.play(Create(example_n3_rect))

        with self.voiceover(text="We have the norm of 'z' equals 1 and the argument φ of 'z' equals 2 times k times π divided by 3.") as tracker:
            self.play(swWrite(the_other_solutions))
            self.play(swWrite(where_phi))

        with self.voiceover(text="φ must be greater than minus π and less than or equal to π") as tracker:
            self.play(swWrite(phi_inequalities_must_hold))

        with self.voiceover(text="For k equals 0, we get 'z' equals 1.") as tracker:
            self.play(swWrite(picking_k_is_0))
        self.play(Create(vec_1))

        with self.voiceover(text="For k equals 1, we get 'z' equals e to the power of 2 times π over 3 times i.") as tracker:
            self.play(swWrite(picking_k_is_1))
        self.play(Create(vec_2))

        with self.voiceover(text="For k equals 2, we get 'z' equals e to the power of 4 times π over 3 times i.") as tracker:
            self.play(swWrite(picking_k_is_2))

        with self.voiceover(text="we must subtract 2 π, since this argument is greater than π. We end up with e to the power of minus 2 times π over 3 times i. This result also could have been found by using k is minus one") as tracker:
            self.play(TransformMatchingShapes(picking_k_is_2, picking_k_is_minus_1))
        self.play(Create(vec_3))

        with self.voiceover(text="The solutions are z equals 1 or z equals e to the power of 2 times π over 3 times i or z equals e to the power of -2 times π over 3 times i. Notice that the complex solutions form complex conjugates of eachother.") as tracker:
            self.play(swWrite(solutions))

        # Outro
        with self.voiceover(text="This concludes the explanation. Thanks for watching") as tracker:
            self.wait(1)


        self.wait(2)
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)

        return
