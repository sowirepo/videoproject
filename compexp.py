from manim import *
from manim_extensions import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

class Test(MovingCameraScene, VoiceoverScene):

    def construct(self):
        self.create_subcaption = False

        self.camera.background_color = BLUEISHGREY

        self.set_speech_service(
            OpenAIService(
                voice="alloy",
                # model="tts-1-hd",
                model='gpt-4o-mini-tts',
            )
        )
        
        ## Logo
        logo = ImageMobject('./Sowiso-logo-primary.png').scale(0.03)

        ## Title
        title = Text("""The complex exponential function""", font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'exponential':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)

        complex_exponential_title = TNT().txt("Complex exponential", color=PINK, weight="SEMIBOLD").move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.55 + DOWN * 0.1)

        ex1_rect = swRoundedRectangle(height=2, width=2).shift(LEFT * 1.1)

        problem = TNT().txt('Given ').tx('z={3+2\\cdot \\mathrm{i}},').txt('calculate ').tx('e^z', aligned_char='e')
        problem[0][1][0][0].set_color(BLUE)
        problem[0][1][0][2].set_color(GREEN)
        problem[0][1][0][4].set_color(GOLDY)
        problem[0][1][0][-1].set_color(BLUE)


        solution0 = TNT().tx('e^z=e^{3+2\\cdot\\mathrm{i}}')
        solution0[0][0][0][1].set_color(BLUE)
        solution0[0][0][0][4].set_color(GREEN)
        solution0[0][0][0][6].set_color(GOLDY)

        solution1 = TNT().tx('e^z=e^3\\cdot e^{2\\cdot\\mathrm{i}}')
        solution1[0][0][0][1].set_color(BLUE)
        solution1[0][0][0][4].set_color(GREEN)
        solution1[0][0][0][7].set_color(GOLDY)

        solution2 = TNT().tx('e^z=e^3\\cdot\\left(\\cos(2) + \\sin(2)\\cdot \\mathrm{i}\\right)')
        solution2[0][0][0][1].set_color(BLUE)
        solution2[0][0][0][4].set_color(GREEN)
        solution2[0][0][0][11].set_color(GOLDY)
        solution2[0][0][0][18].set_color(GOLDY)

        solution3 = TNT().tx('\\|e^z\\|=e^3')
        solution3[0][0][0][2].set_color(BLUE)
        solution3[0][0][0][-1].set_color(GREEN)

        solution4 = TNT().tx('\\text{Arg}(e^z)=2')
        solution4[0][0][0][5].set_color(BLUE)
        solution4[0][0][0][-1].set_color(GOLDY)
        


        sol_group = VGroup(solution0, solution1, solution2, solution3, solution4)

        ex1_rect.set_title(problem)

        sol_group = ex1_rect.create_content(sol_group, offset=0.075)

        # sol_group[-2:].shift(DOWN * 0.1)

        theory_rect = swRoundedRectangle(height=1.2, width=2)
        up_ex1 = ex1_rect.get_edge_center(UP)
        up_tr = theory_rect.get_edge_center(UP)

        theory_rect.shift(RIGHT * 1.1 + UP * (up_ex1[1] - up_tr[1]))
        
        theory_rect_title = TNT().txt("Computational properties", color=PINK, weight="SEMIBOLD")
        theory_rect.set_title(theory_rect_title, remove_line=True)

        computational_properties_0 = TNT().tx('e^0=1')
        computational_properties_0[0][0][0][1].set_color(BLUE)

        computational_properties_1 = TNT().tx('e^z\\cdot e^w=e^{z+w}')
        computational_properties_1[0][0][0][1].set_color(BLUE)
        computational_properties_1[0][0][0][4].set_color(BLUE)
        computational_properties_1[0][0][0][7].set_color(BLUE)
        computational_properties_1[0][0][0][9].set_color(BLUE)

        computational_properties_2 = TNT().tx('(e^z)^n=e^{z\\cdot n}')
        computational_properties_2[0][0][0][2].set_color(BLUE)
        computational_properties_2[0][0][0][7].set_color(BLUE)

        computational_properties_3 = TNT().tx('\\overline{e^z}=e^{\\bar{z}}')
        computational_properties_3[0][0][0][2].set_color(BLUE)
        computational_properties_3[0][0][0][6].set_color(BLUE)

        theory_rect_content = VGroup(computational_properties_0, computational_properties_1, computational_properties_2, computational_properties_3)
        theory_rect.create_content(theory_rect_content, offset=0.075)

        
        ### ANIMATIONS ###
        self.add(logo)

        self.wait(1)

        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))


        with self.voiceover(text="In this video, we will discuss the complex exponential function.") as tracker:
            self.play(swWrite(title), run_time=tracker.duration)

        self.play(FadeOut(title))
        self.wait(1)

        self.play(swWrite(complex_exponential_title))

        with self.voiceover(text="We start by considering the problem: Given z equals 3 plus 2 times i, calculate e to the power of z.") as tracker:
            self.play(Create(ex1_rect))

        with self.voiceover(text="The first step is to write the expression e to the power of z as e to the power of 3 plus 2 times i.") as tracker:
            self.play(swWrite(solution0))

        with self.voiceover(text="We can rewrite the expression using the property of exponents.") as tracker:
            self.play(swWrite(solution1))

        self.wait(0.5)

        with self.voiceover(text="Now we can write e to the power of 2 times i in polar form. Then, we can recognize the expression as the polar form of e to the power of z.") as tracker:
            self.play(swWrite(solution2))

        self.wait(0.5)

        with self.voiceover(text="Therefore, the norm of e to the power of z is equal to e to the power of 3.") as tracker:
            self.play(swWrite(solution3))

        with self.voiceover(text="And the argument of e to the power of z is 2") as tracker:
            self.play(swWrite(solution4))

        self.wait(1)

        with self.voiceover(text="Now, let's recall some useful computational properties of the exponential function when applied to complex numbers.") as tracker:
            self.play(Create(theory_rect))

        with self.voiceover(text="e to the power of zero equals one.") as tracker:
            self.play(swWrite(computational_properties_0))

        with self.voiceover(text="The product e to the power of z times e to the power of 'w' is equal to e to the power of z plus 'w'.") as tracker:
            self.play(swWrite(computational_properties_1))

        with self.voiceover(text="Raising an exponential expression to the power of n results in e to the power of z times n.") as tracker:
            self.play(swWrite(computational_properties_2))

        with self.voiceover(text="And finally, the complex conjugate of e to the power of z is equal to e to the power of the complex conjugate of z.") as tracker:
            self.play(swWrite(computational_properties_3))

        
        with self.voiceover(text="This concludes the complex exponential function. Thanks for watching.") as tracker:
            self.wait(0.1)
        # fade out everything still on the screen
        self.wait(2)

        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)

       