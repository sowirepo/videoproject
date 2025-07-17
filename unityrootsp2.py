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
        title = Text(
            """Roots of unity examples """,
            font='Quicksand',
            color=PURPLE,
            weight="SEMIBOLD",
            t2c={'quotient':PINK},
            line_spacing=0.2
        ).scale(0.25)
        title.move_to(ORIGIN)

        # Logo
        logo = ImageMobject('Sowiso-logo-primary.png').scale(0.03)

        # text top left
        roots_of_unity_title = Text(
            'Roots of unity',
            font="Quicksand",
            color=PINK,
            weight="SEMIBOLD"
        ).scale(0.15)\
         .move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.1)

        

        # ##################
        # example n=4
        # ##################

        example_n4_rect = swRoundedRectangle(height=2.1, width=2)\
            .shift(LEFT * 1.15)
        
        # setup the plane
        polarplane_pi = swPolarPlane(
            angle_step=np.pi/12,
            add_complex_labels=True
        ).scale(0.25)
    
        # right rectangle
        polarplane_rect = swRoundedRectangle(height=2.1, width=2.2)\
            .move_to(polarplane_pi.get_center())


        solve_n4_is_1 = TNT()\
            .txt('Solve ')\
            .tx('z^4=1')\
            .set_color_by_string('4', swGOLD)\
            .set_color_by_string('z', BLUE)

        the_other_solutions_n4 = TNT()\
            .txt('We have ')\
            .tx('\\|z\\|=1')\
            .txt(' and ')\
            .tx('\\varphi = \\dfrac{2\\cdot k \\cdot \\pi}{4}')\
            .set_color_by_string('z', BLUE)\
            .set_color_by_string('4', swGOLD)\
            .set_color_by_string('\\varphi', GREEN)

        picking_k_is_0_n4 = TNT()\
            .txt('For ')\
            .tx('k=0')\
            .txt(' we get ')\
            .tx('z=1')\
            .set_color_by_string('z', BLUE)

        picking_k_is_1_n4 = TNT()\
            .txt('For ')\
            .tx('k=1')\
            .txt(' we get ')\
            .tx('z=\\mathrm{e}^{\\frac{\\pi}{2}\\cdot\\mathrm{i}}')\
            .set_color_by_string('z', BLUE)

        picking_k_is_2_n4 = TNT()\
            .txt('For ')\
            .tx('k=2')\
            .txt(' we get ')\
            .tx('z=\\mathrm{e}^{\\pi \\cdot \\mathrm{i}}=-1')\
            .set_color_by_string('z', BLUE)

        picking_k_is_3_n4 = TNT()\
            .txt('For ')\
            .tx('k=3')\
            .txt(' we get ')\
            .tx('z=\\mathrm{e}^{\\frac{6 \\cdot \\pi}{4}\\cdot\\mathrm{i}}')\
            .set_color_by_string('4', swGOLD)\
            .set_color_by_string('z', BLUE)

        picking_k_is_minus_1_n4 = TNT()\
            .txt('For ')\
            .tx('k=3')\
            .txt(' we get ')\
            .tx('z=\\mathrm{e}^{-\\frac{\\pi}{2}\\cdot\\mathrm{i}}')\
            .set_color_by_string('z', BLUE)

        n4_content = VGroup(
            the_other_solutions_n4,
            picking_k_is_0_n4,
            picking_k_is_1_n4,
            picking_k_is_2_n4,
            picking_k_is_3_n4
        )

        example_n4_rect.set_title(solve_n4_is_1)
        example_n4_rect.create_content(n4_content, offset=0.1)
        picking_k_is_minus_1_n4.move_to(picking_k_is_3_n4.get_center())

        org = polarplane_pi.polar_to_point(0,0)
        p1_n4 = polarplane_pi.polar_to_point(1,0)
        p2_n4 = polarplane_pi.polar_to_point(1,1/2 * PI)
        p3_n4 = polarplane_pi.polar_to_point(1,PI)
        p4_n4 = polarplane_pi.polar_to_point(1,3/2 * PI)

        vec_n4_1 = Line(org, p1_n4, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)\
            .shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_2 = Line(org, p2_n4, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)\
            .shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_3 = Line(org, p3_n4, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)\
            .shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_4 = Line(org, p4_n4, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)\
            .shift(RIGHT * 1.1 + UP * 0.01)

        fadeout_group_n4 = VGroup(
            the_other_solutions_n4,
            picking_k_is_1_n4, picking_k_is_0_n4,
            picking_k_is_minus_1_n4, picking_k_is_2_n4,
            vec_n4_1, vec_n4_2, vec_n4_3, vec_n4_4
        )

        # ##################
        # example n=5
        # ##################
        new_polarplane_pi = swPolarPlane(
            angle_step=np.pi/10,
            add_complex_labels=True
        ).scale(0.25)\
         .move_to(polarplane_pi.get_center())

        example_n5_rect = swRoundedRectangle(height=2.1, width=2)\
            .shift(LEFT * 1.15)

        solve_n5_is_1 = TNT()\
            .txt('Solve ')\
            .tx('z^5=1')\
            .set_color_by_string('5', swGOLD)\
            .set_color_by_string('z', BLUE)

        the_other_solutions_n5 = TNT()\
            .txt('We have ')\
            .tx('\\|z\\|=1')\
            .txt(' and ')\
            .tx('\\varphi = \\dfrac{2\\cdot k \\cdot \\pi}{5}')\
            .set_color_by_string('z', BLUE)\
            .set_color_by_string('5', swGOLD)\
            .set_color_by_string('\\varphi', GREEN)

        picking_k_is_minus_2_n5 = TNT()\
            .txt('For ')\
            .tx('k=-2')\
            .txt(' we get ')\
            .tx('z=\\mathrm{e}^{-\\frac{4\\cdot \\pi}{5}\\cdot \\mathrm{i}}')\
            .set_color_by_string('5', swGOLD)\
            .set_color_by_string('z', BLUE)

        picking_k_is_minus_1_n5 = TNT()\
            .txt('For ')\
            .tx('k=-1')\
            .txt(' we get ')\
            .tx('z=\\mathrm{e}^{-\\frac{2\\cdot \\pi}{5}\\cdot \\mathrm{i}}')\
            .set_color_by_string('5', swGOLD)\
            .set_color_by_string('z', BLUE)

        picking_k_is_0_n5 = TNT()\
            .txt('For ')\
            .tx('k=0')\
            .txt(' we get ')\
            .tx('z=1')\
            .set_color_by_string('z', BLUE)

        picking_k_is_1_n5 = TNT()\
            .txt('For ')\
            .tx('k=1')\
            .txt(' we get ')\
            .tx('z=\\mathrm{e}^{\\frac{2\\cdot \\pi}{5}\\cdot \\mathrm{i}}')\
            .set_color_by_string('5', swGOLD)\
            .set_color_by_string('z', BLUE)

        picking_k_is_2_n5 = TNT()\
            .txt('For ')\
            .tx('k=2')\
            .txt(' we get ')\
            .tx('z=\\mathrm{e}^{\\frac{4\\cdot \\pi}{5}\\cdot \\mathrm{i}}')\
            .set_color_by_string('5', swGOLD)\
            .set_color_by_string('z', BLUE)

        n5_content = VGroup(
            the_other_solutions_n5,
            picking_k_is_minus_2_n5,
            picking_k_is_minus_1_n5,
            picking_k_is_0_n5,
            picking_k_is_1_n5,
            picking_k_is_2_n5
        )

        example_n5_rect.set_title(solve_n5_is_1)
        example_n5_rect.create_content(n5_content, offset=0.1)

        new_org = new_polarplane_pi.polar_to_point(0,0)
        p1_n5 = new_polarplane_pi.polar_to_point(1,0)
        p2_n5 = new_polarplane_pi.polar_to_point(1,2/5 * PI)
        p3_n5 = new_polarplane_pi.polar_to_point(1,4/5 * PI)
        p4_n5 = new_polarplane_pi.polar_to_point(1,6/5 * PI)
        p5_n5 = new_polarplane_pi.polar_to_point(1,8/5 * PI)

        vec_n5_1 = Line(new_org, p1_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)
        vec_n5_2 = Line(new_org, p2_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)
        vec_n5_3 = Line(new_org, p3_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)
        vec_n5_4 = Line(new_org, p4_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)
        vec_n5_5 = Line(new_org, p5_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)

        # ANIMATIONS
        self.add(logo)
        self.wait(1)
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.1*UP + 0.35 * RIGHT)
            .scale(0.009 / 0.03))

        with self.voiceover(text="This video shows 2 examples of how to calculate the roots of unity.") as tracker:
            self.play(swWrite(title))
        polarplane_group = VGroup(polarplane_rect, polarplane_pi)
        polarplane_group.shift(RIGHT * 1.1 + UP * 0.01)

        self.play(FadeOut(title))
        self.wait(1)
        self.play(swWrite(roots_of_unity_title))

        with self.voiceover(text="We will draw the solutions in an Argand diagram.") as tracker:
            self.play(Create(polarplane_rect))
            self.play(Create(polarplane_pi))



        # START n=4 example
        with self.voiceover(text="We will solve 'z' to the power of 4 equals 1.") as tracker:
            self.play(Create(example_n4_rect))

        with self.voiceover(text="We have the norm of 'z' equals 1 and the argument φ of 'z' equals 2 times k times π divided by 4.") as tracker:
            self.play(swWrite(the_other_solutions_n4))

        with self.voiceover(text="For k equals 0, we get 'z' equals 1.") as tracker:
            self.play(swWrite(picking_k_is_0_n4))
        self.play(Create(vec_n4_1))

        with self.voiceover(text="For k equals 1, we get 'z' equals e to the power of π over 2 times i.") as tracker:
            self.play(swWrite(picking_k_is_1_n4))
        self.play(Create(vec_n4_2))

        with self.voiceover(text="For k equals 2, we get 'z' equals e to the power of π times i, which is minus 1.") as tracker:
            self.play(swWrite(picking_k_is_2_n4))
        self.play(Create(vec_n4_3))

        with self.voiceover(text="For k equals 3, we get 'z' equals e to the power of 6 times pi over 4 times i.") as tracker:
            self.play(swWrite(picking_k_is_3_n4))

        with self.voiceover(text="Since this value is greater than pi, we have to subtract 2 times π to get the argument in the proper range. This result can also be obtained by using k equals minus 1.") as tracker:
            self.play(TransformMatchingShapes(picking_k_is_3_n4, picking_k_is_minus_1_n4))
        self.play(Create(vec_n4_4))

        with self.voiceover(text="These are the 4 solutions to the problem. Notice that the complex roots are complex conjugates of each other.") as tracker:
            self.wait(0.1)

        # Start n=5 example
        self.play(FadeOut(fadeout_group_n4))


        with self.voiceover(text="Finally, we will solve 'z' to the power of 5 equals 1.") as tracker:
            self.play(TransformMatchingShapes(example_n4_rect, example_n5_rect))

        new_polarplane_pi.move_to(polarplane_pi.get_center()).shift(UP*0.01)
        self.play(Transform(polarplane_pi, new_polarplane_pi))

        with self.voiceover(text="We have the norm of 'z' equals 1 and the argument φ of 'z' equals 2 times k times π divided by 5.") as tracker:
            self.play(swWrite(the_other_solutions_n5))

        new_org = new_polarplane_pi.polar_to_point(0,0)
        p1_n5 = new_polarplane_pi.polar_to_point(1,0)
        p2_n5 = new_polarplane_pi.polar_to_point(1,2/5 * PI)
        p3_n5 = new_polarplane_pi.polar_to_point(1,4/5 * PI)
        p4_n5 = new_polarplane_pi.polar_to_point(1,6/5 * PI)
        p5_n5 = new_polarplane_pi.polar_to_point(1,8/5 * PI)

        vec_n5_1 = Line(new_org, p1_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)
        vec_n5_2 = Line(new_org, p2_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)
        vec_n5_3 = Line(new_org, p3_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)
        vec_n5_4 = Line(new_org, p4_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)
        vec_n5_5 = Line(new_org, p5_n5, color=BLUE, stroke_width=2)\
            .add_tip(tip_length=0.1, tip_width=0.06)

        with self.voiceover(text="For k equals -2, we get 'z' equals e to the power of -4 times π over 5 times i.") as tracker:
            self.play(swWrite(picking_k_is_minus_2_n5))
        self.play(Create(vec_n5_4))

        with self.voiceover(text="For k equals -1, we get 'z' equals e to the power of -2 times π over 5 times i.") as tracker:
            self.play(swWrite(picking_k_is_minus_1_n5))
        self.play(Create(vec_n5_5))

        with self.voiceover(text="For k equals 0, we get 'z' equals 1.") as tracker:
            self.play(swWrite(picking_k_is_0_n5))
        self.play(Create(vec_n5_1))

        with self.voiceover(text="For k equals 1, we get 'z' equals e to the power of 2 times π over 5 times i.") as tracker:
            self.play(swWrite(picking_k_is_1_n5))
        self.play(Create(vec_n5_2))

        with self.voiceover(text="For k equals 2, we get 'z' equals e to the power of 4 times π over 5 times i.") as tracker:
            self.play(swWrite(picking_k_is_2_n5))
        self.play(Create(vec_n5_3))

        with self.voiceover(text="These are the 5 solutions to the problem. We once again have that the complex roots are complex conjugates of each other, which can be seen in the diagram.") as tracker:
            self.wait(1)

        # Outro
        with self.voiceover(text="This concludes the examples. Thanks for watching") as tracker:
            self.wait(1)

        self.wait(2)
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)
