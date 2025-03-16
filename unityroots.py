from manim import *
from manim_extensions import *
# from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.openai import OpenAIService

class Test(MovingCameraScene): # VoiceoverScene

    def construct(self):
        self.create_subcaption = False

        self.camera.background_color = BLUEISHGREY

        # self.set_speech_service(
        #     OpenAIService(
        #         voice="alloy",
        #         model="tts-1-hd",
        #     )
        # )

        ## Title
        title = Text("""Roots of Unity  """, font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'quotient':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)

        ## Logo
        logo = ImageMobject('/home/chris/manim/videoproject/Sowiso-logo-primary.png').scale(0.03)


        ## text top left
        roots_of_unity_title = Text('Roots of Unity', font="Quicksand", color=PINK, weight="SEMIBOLD")
        roots_of_unity_title.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.45 + DOWN * 0.1)

        ## setup example rectangle
        ex1_rect = swRoundedRectangle(height=2, width=2.5)

        ## propose problem
        problem = TNT().txt("We will solve the equation ").tx('z^n=1').shift(UP * 0.8)
        problem[0][1][0][0].set_color(BLUE)
        problem[0][1][0][1].set_color(GOLDY)

        this_equation_has_n_roots = TNT().txt("This equation has ").tx('n', aligned_char='n', color=GOLDY).txt(' solutions').shift(UP * 0.6)

        by_rewriting = TNT().txt("By rewriting the equation using").shift(UP * 0.4)
        the_polar_exp = TNT().txt("the ").txt("polar exponential form,", weight="SEMIBOLD").txt('we get').shift(UP * 0.3)

        polar_exp1 = problem[0][1].copy()
        polar_exp2 = TNT().tx('(\\|z\\|e^{\\mathrm{i}\\cdot \\varphi})^n = \\|1\\|e^{\\mathrm{i}\\cdot 0}').shift(DOWN * 0.1)
        polar_exp2_5 = TNT().tx('\\|z\\|^ne^{\\mathrm{i}\\cdot \\varphi \\cdot n} = \\|1\\|e^{\\mathrm{i}\\cdot 2 \\cdot k \\cdot \\pi}').shift(DOWN * 0.1)

        polar_exp3 = TNT().tx('z=e^{\\mathrm{i} \\cdot \\varphi} = e^{\\mathrm{i} \\cdot 2 \\cdot k \\cdot \\pi / n}').shift(DOWN * 0.3)

        polar_exp4 = TNT().txt('We have ').tx('\\varphi = \\dfrac{2\\cdot k \\cdot \\pi}{n}').shift(DOWN * 0.6)

        polar_exp5 = TNT().txt('There are ').tx('n', aligned_char='n', color=GOLDY).txt(' solutions for ').tx('-\\pi < \\varphi \\leq \\pi', aligned_char='<').shift(DOWN * 0.8)

        fadeout_group = VGroup(problem, this_equation_has_n_roots, by_rewriting, the_polar_exp, polar_exp1, polar_exp2_5, polar_exp3, polar_exp4, polar_exp5)

        polarplane_pi = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_label_font_size=33.6,
            # radius_config={"font_size": 33.6,
            #                "color": BLACK},
            radius_max=1.5,
            radius_step=0.5,
            background_line_style=BACKGROUND_LINE_STYLE,
            radius_config=AXIS_CONFIG
        ).add_coordinates().scale(0.25)

        # polarplane_pi[2].set_color(GREEN)
        # polarplane_pi[3].set_color(BLUE)
        # polarplane_pi[4][0].set_color(PORPLE)
        # polarplane_pi[4][1].set_color(GOLDY)
        polarplane_pi[2:].set_color(DARK_GREY)
        # print(polarplane_pi[3])
        # print(polarplane_pi[4][0])
        polarplane_pi[3][2][0].shift(UP * 999)
        polarplane_pi[4][0][2][0].shift(UP * 999)


        ### ANIMATIONS ###
        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))
        self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        self.play(swWrite(roots_of_unity_title))

        self.play(Create(ex1_rect))
        self.play(swWrite(problem))
        self.play(swWrite(this_equation_has_n_roots))
        self.play(swWrite(by_rewriting))    
        self.play(swWrite(the_polar_exp))

        self.play(polar_exp1.animate.move_to(ex1_rect.get_center() + UP * 0.1))
        self.play(swWrite(polar_exp2))

        self.play(TransformMatchingShapes(polar_exp2, polar_exp2_5))

        self.play(swWrite(polar_exp3))

        self.play(swWrite(polar_exp4))

        self.play(swWrite(polar_exp5))

        self.play(FadeOut(fadeout_group))

        self.play(Create(polarplane_pi))