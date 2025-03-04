from manim import *
from manim_extensions import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

class Test(MovingCameraScene, VoiceoverScene):
    def construct(self):

        self.camera.background_color = BLUEISHGREY

        self.set_speech_service(
            OpenAIService(
                voice="alloy",
                model="tts-1-hd",
            )
        )

        ## Title
        title = Text("""Calculating the quotient \nof two complex numbers""", font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'quotient':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)

        ## setup example rectangle
        example = Text('Quotient of complex numbers', font="Quicksand", color=PINK, weight="SEMIBOLD")
        example.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.75 + DOWN * 0.15)
        ex1_rect = swRoundedRectangle(height=2, width=2.5)
        ex1_rect.shift(LEFT*0.9)

        ## state problem
        problem = TNT().txt('Calculate ').tx('\\dfrac{3 + 4\\cdot\\mathrm{i}}{1 - 2\\cdot\\mathrm{i}}').create().shift(UP * 0.75 + LEFT * 0.9)

        problem[1][0][0:5].set_color(BLUE)
        problem[1][0][6:].set_color(GREEN)

        problem_underline = Line(problem[1][0].get_corner(DL) + LEFT*1.2 , problem[1][0].get_corner(DR) + RIGHT * 0.7, color=GREY, stroke_width=0.2).shift(DOWN*0.03)


        ## setup conjugate theory
        conj_rect = swRoundedRectangle(height=0.8, width=1.5)
        conj_rect.shift(UP*0.6+RIGHT*1.3)
        comp_conj = TNT().add_text('Complex conjugate', weight="SEMIBOLD", color=PINK).create().shift(UP*0.85+RIGHT*1.3)
        z_normal = TNT().tx('z=a+b\\cdot\\mathrm{i}').create().shift(UP*0.65+RIGHT*1.25)
        z_conj = TNT().tx('\\overline{z}=a-b\\cdot\\mathrm{i}').create().move_to(z_normal.get_center() + DOWN*0.2)


        ## start solving problem
        equation = TNT().tx('\\dfrac{3 + 4\\cdot\\mathrm{i}}{1 - 2\\cdot\\mathrm{i}}=\\dfrac{3 + 4\\cdot\\mathrm{i}}{1 - 2\\cdot\\mathrm{i}} \cdot \\dfrac{1 + 2\\cdot\\mathrm{i}}{1 + 2\\cdot\\mathrm{i}}').create().shift(LEFT *1.4 + UP * 0.5)

        equation[0][0][0:5].set_color(BLUE)
        equation[0][0][6:11].set_color(GREEN)

        equation[0][0][12:17].set_color(BLUE)
        equation[0][0][18:23].set_color(GREEN)

        equation[0][0][24:29].set_color(GOLDY)
        equation[0][0][30:35].set_color(GOLDY)


        line1 = TNT().tx('=\\dfrac{(3+4\\cdot\\mathrm{i})\\cdot(1 + 2 \\cdot\\mathrm{i})}{||1-2\\cdot\\mathrm{i}||^2}').create()

        line1[0][0][2:7].set_color(BLUE)
        line1[0][0][10:15].set_color(GOLDY)
        line1[0][0][19:24].set_color(GREEN)

        line2 = TNT().tx('=\\dfrac{3+6\\cdot\\mathrm{i}+4\\cdot\\mathrm{i}+8\\cdot\\mathrm{i}^2}{1^2+(-2)^2}').create()
        line3 = TNT().tx('=\\dfrac{3+10\\cdot\\mathrm{i}-8}{1+4}').create()
        line4 = TNT().tx('=\\dfrac{-5+10\\cdot\\mathrm{i}}{5}=-1+2\\cdot\\mathrm{i}').create()

        group_of_solution = VGroup(line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT, buff=0.1).shift(DOWN*0.3 + LEFT*1.09)


        ## setup norm theory
        norm_rect = swRoundedRectangle(height=0.8, width=1.5)
        norm_rect.shift(UP*0.6+RIGHT*1.3)
        norm = TNT().add_text('Norm of complex number', weight="SEMIBOLD", color=PINK).create().shift(UP*0.85+RIGHT*1.3)
        z = TNT().tx('z=a+b\\cdot\\mathrm{i}').create().shift(UP*0.65+RIGHT*1.25)
        norm_z = TNT().tx('z\\cdot \\overline{z} =||z||^2=a^2+b^2').create().move_to(z.get_center() + DOWN*0.2)

        norm_group = VGroup(norm_rect, norm, z, norm_z).shift(DOWN)



        self.next_section()

        ### EXAMPLE 2 ###

        reciprocal = Text('Reciprocal of complex number', font="Quicksand", color=PINK, weight="SEMIBOLD")
        reciprocal.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.8 + DOWN * 0.15)

        problem_2 = TNT().txt('Calculate ').tx('\\dfrac{1}{-3 - 2\\cdot\\mathrm{i}}').create().move_to(problem.get_center() + UP *0.04)

        problem_2[1][0][2:].set_color(GREEN)

        ## start solving problem
        equation_2 = TNT().tx('\\dfrac{1}{-3 - 2\\cdot\\mathrm{i}}=\\dfrac{1}{-3 - 2\\cdot\\mathrm{i}} \\cdot \\dfrac{-3+2\\cdot\\mathrm{i}}{-3+2\\cdot\\mathrm{i}}').create().move_to(equation.get_center() + RIGHT * 0.07)
        
        equation_2[0][0][2:8].set_color(GREEN)
        equation_2[0][0][11:17].set_color(GREEN)
        equation_2[0][0][18:24].set_color(GOLDY)
        equation_2[0][0][25:].set_color(GOLDY)


        line1_2 = TNT().tx('=\\dfrac{1\cdot(-3+2\\cdot\\mathrm{i})}{||-3-2\\cdot\\mathrm{i}||^2}').create().move_to(line1.get_center())

        line1_2[0][0][4:9].set_color(GOLDY)
        line1_2[0][0][14:20].set_color(GREEN)

        line2_2 = TNT().tx('=\\dfrac{-3+2\\cdot\\mathrm{i}}{(-3)^2+(-2)^2}').create().move_to(line2.get_center())
        line3_2 = TNT().tx('=\\dfrac{-3+2\\cdot\\mathrm{i}}{9+4}').create().move_to(line3.get_center())
        line4_2 = TNT().tx('=\\dfrac{-3+2\\cdot\\mathrm{i}}{13}=-\\dfrac{3}{13}+\\dfrac{2}{13}\\cdot\\mathrm{i}').create().move_to(line4.get_center())
        
        group_of_solution_2 = VGroup(line1_2, line2_2, line3_2, line4_2).arrange(DOWN, aligned_edge=LEFT, buff=0.1).shift(DOWN*0.3 + LEFT)




        ### Animation ###

        with self.voiceover(text="In this video, we will show how to calculate the quotient of two complex numbers.") as tracker:
            self.play(swWrite(title), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.play(FadeOut(title))
        self.wait(1)

        self.play(swWrite(example), Create(ex1_rect))

        with self.voiceover(text="We will calculate 3 + 4 times 'i' divided by 1 minus 2 times 'i'.") as tracker:
            self.play(swWrite(problem), run_time=tracker.duration * 0.5)
            self.play(Create(problem_underline), run_time=tracker.duration * 0.5)
        self.wait(1)

        with self.voiceover(text="We can solve this problem by multiplying the numerator and denominator by the complex conjugate of the denominator.") as tracker:
            self.wait(tracker.duration * 0.1)

        self.play(Create(conj_rect))
        self.wait(1)
        self.play(swWrite(comp_conj))
        self.wait(1)
        with self.voiceover(text="if 'z' is 'a' + 'b' times 'i', then the complex conjugate of 'z' is 'a' minus 'b' times 'i'.") as tracker:
            self.play(swWrite(z_normal), run_time=tracker.duration * 0.5)
            self.play(swWrite(z_conj), run_time=tracker.duration * 0.5)

        self.wait(1)

        with self.voiceover(text="Now, we can multiply the numerator and denominator by the complex conjugate of the denominator.") as tracker:
            self.play(swWrite(equation), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)

        with self.voiceover(text="To simplify this fraction, we can use the fact that multiplying a complex number 'z' by its complex conjugate, equals the norm squared of z, which is 'a' + 'b' times 'i'.") as tracker:

            self.play(Create(norm_rect), run_time=tracker.duration * 0.1)
            self.wait(0.1)
            self.play(swWrite(norm), run_time=tracker.duration * 0.1)
            self.wait(0.1)
            self.play(swWrite(z),run_time= tracker.duration * 0.1)
            self.wait(0.5)
            self.play(swWrite(norm_z),run_time= tracker.duration * 0.6)
        
        self.wait(1)

        with self.voiceover(text="Therefore, the fraction is equal to 3 plus 4 times i multiplied by 1 plus 2 times i, divided by the norm squared of 1 minus 2 times i.") as tracker:
            self.play(swWrite(line1), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)

        with self.voiceover(text="As we know, the norm squared of 1 minus 2 times 'i' is equal to 1 squared plus -2 squared.") as tracker:
            self.play(swWrite(line2), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)

        self.play(swWrite(line3))
        self.wait(1)

        with self.voiceover(text="Simplifying the numerator and the denominator gives us minus 5 plus 10 times 'i' divided by 5. This is equal to minus 1 + 2 times 'i'") as tracker:
            self.play(swWrite(line4), run_time=tracker.duration * 0.7)
            self.wait(tracker.duration * 0.3)

        self.wait(1)

        self.play(FadeOut(group_of_solution), FadeOut(problem), FadeOut(equation), FadeOut(example))
        self.wait(1)
        
        self.play(swWrite(reciprocal))
        self.wait(1)

        with self.voiceover(text="Now, we will calculate the reciprocal of the 1 divided by minus 3 minus 2 times 'i'.") as tracker:
            self.play(swWrite(problem_2), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)

        self.wait(1)

        with self.voiceover(text="Once again, we can solve this problem by multiplying the numerator and denominator by the complex conjugate of the denominator.") as tracker:
            self.play(swWrite(equation_2), run_time = tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)
        
        self.wait(1)
        
        self.play(swWrite(line1_2))
        self.wait(1)

        with self.voiceover(text="The norm squared of minus 3 minus 2 times 'i' is equal to minus 3 squared plus minus 2 squared.") as tracker:
            self.play(swWrite(line2_2), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)
        self.wait(1)
        self.play(swWrite(line3_2))
        self.wait(1)

        with self.voiceover(text="This simplifies to minus 3 plus 2 times 'i' over 13, which is equal to minus 3 over 13 plus 2 over 13 times 'i'.") as tracker:
            self.play(swWrite(line4_2), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)

        self.wait(1)

        all = Group(*self.mobjects)
        with self.voiceover(text="This concludes the examples. Thanks for watching.") as tracker:
            self.play(FadeOut(all), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration)