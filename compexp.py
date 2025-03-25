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
                voice="ballad",
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

        solution0 = TNT().tx('e^z=e^{3+2\\cdot\\mathrm{i}}')
        solution1 = TNT().tx('e^z=e^3\\cdot e^{2\\cdot\\mathrm{i}}')
        solution2 = TNT().tx('e^z=e^3\\cdot\\left(\\cos(2) + \\cdot\\mathrm{i}\\cdot \\sin(2)\\right)')
        solution3 = TNT().tx('\\|e^z\\|=e^3')
        solution4 = TNT().tx('\\text{Arg}(e^z)=2')


        sol_group = Group(solution0, solution1, solution2, solution3, solution4)


        ex1_rect.set_title(problem)

        sol_group = ex1_rect.create_content(sol_group, offset=0.075)

        sol_group[-2:].shift(DOWN * 0.1)

        theory_rect = swRoundedRectangle(height=0.8, width=2)
        up_ex1 = ex1_rect.get_edge_center(UP)
        up_tr = theory_rect.get_edge_center(UP)

        theory_rect.shift(RIGHT * 1.1 + UP * (up_ex1[1] - up_tr[1]))
        
        theory_rect_title = TNT().txt("Complex exponential function", color=PINK, weight="SEMIBOLD")
        theory_rect.set_title(theory_rect_title, remove_line=True)

        comp_exp_func = TNT()


        
        ### ANIMATIONS ###
        self.add(logo)

        self.wait(1)

        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))


        with self.voiceover(text="In this video, we will discuss the complex exponential function.") as tracker:
            self.play(swWrite(title), run_time=tracker.duration)

        self.play(FadeOut(title))
        self.wait(1)

        self.play(swWrite(complex_exponential_title))

        self.play(Create(ex1_rect))

        self.add(sol_group)
        self.play(Create(theory_rect))

        return
        # with self.voiceover(text="This concludes the examples. Thanks for watching") as tracker:
        #     self.wait(tracker.duration)
    
        # fade out everything still on the screen
        self.wait(2)

        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)