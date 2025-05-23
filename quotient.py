from manim import *
from manim_extensions import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

class MainScene(MovingCameraScene, VoiceoverScene):
    def construct(self):

        self.create_subcaption = False

        self.camera.background_color = BLUEISHGREY

        self.set_speech_service(
            OpenAIService(
                voice="alloy",
                # model="tts-1-hd",
                model="gpt-4o-mini-tts",
            )
        )

        ## Title
        title = Text(""" Calculating the quotient \nof two complex numbers""", font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'quotient':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)


        logo = ImageMobject('../Sowiso-logo-primary.png').scale(0.03)


        ## setup example rectangle
        example = Text('Quotient of complex numbers', font="Quicksand", color=PINK, weight="SEMIBOLD")
        example.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.75 + DOWN * 0.15)
        ex1_rect = swRoundedRectangle(height=2, width=2.5)
        ex1_rect.shift(LEFT*0.9)

        ## state problem
        problem = TNT_Deprecated().txt('Calculate ').tx('\\dfrac{3 + 4\\cdot\\mathrm{i}}{1 - 2\\cdot\\mathrm{i}}').create().shift(UP * 0.75 + LEFT * 0.9)

        problem[1][0][0:5].set_color(BLUE)
        problem[1][0][6:].set_color(GREEN)

        problem_underline = Line(problem[1][0].get_corner(DL) + LEFT*1.2 , problem[1][0].get_corner(DR) + RIGHT * 0.7, color=GREY, stroke_width=0.2).shift(DOWN*0.03)


        ## setup conjugate theory
        conj_rect = swRoundedRectangle(height=0.8, width=1.5)
        conj_rect.shift(UP*0.6+RIGHT*1.3)
        comp_conj = TNT_Deprecated().add_text('Complex conjugate', weight="SEMIBOLD", color=PINK).create().shift(UP*0.85+RIGHT*1.3)
        z_normal = TNT_Deprecated().tx('z=a+b\\cdot\\mathrm{i}').create().shift(UP*0.65+RIGHT*1.25)
        z_conj = TNT_Deprecated().tx('\\overline{z}=a-b\\cdot\\mathrm{i}').create().move_to(z_normal.get_center() + DOWN*0.2)

        z_denom = TNT_Deprecated().tx('z=1-2\\cdot\\mathrm{i}').create().move_to(z_normal.get_center())
        z_denom_conj = TNT_Deprecated().tx('\\overline{z}=1+2\\cdot\\mathrm{i}').create().move_to(z_conj.get_center())
        z_denom[0][0][2:].set_color(GREEN)
        z_denom_conj[0][0][3:].set_color(swGOLD)

        ## start solving problem
        equation = TNT_Deprecated().tx('\\dfrac{3 + 4\\cdot\\mathrm{i}}{1 - 2\\cdot\\mathrm{i}}=\\dfrac{3 + 4\\cdot\\mathrm{i}}{1 - 2\\cdot\\mathrm{i}} \\cdot \\dfrac{1 + 2\\cdot\\mathrm{i}}{1 + 2\\cdot\\mathrm{i}}').create().shift(LEFT *1.4 + UP * 0.5)

        equation[0][0][0:5].set_color(BLUE)
        equation[0][0][6:11].set_color(GREEN)

        equation[0][0][12:17].set_color(BLUE)
        equation[0][0][18:23].set_color(GREEN)

        equation[0][0][24:29].set_color(swGOLD)
        equation[0][0][30:35].set_color(swGOLD)


        line1 = TNT_Deprecated().tx('=\\dfrac{(3+4\\cdot\\mathrm{i})\\cdot(1 + 2 \\cdot\\mathrm{i})}{||1-2\\cdot\\mathrm{i}||^2}').create()

        line1[0][0][2:7].set_color(BLUE)
        line1[0][0][10:15].set_color(swGOLD)
        line1[0][0][19:24].set_color(GREEN)

        line2 = TNT_Deprecated().tx('=\\dfrac{3+6\\cdot\\mathrm{i}+4\\cdot\\mathrm{i}+8\\cdot\\mathrm{i}^2}{1^2+(-2)^2}').create()
        line3 = TNT_Deprecated().tx('=\\dfrac{3+10\\cdot\\mathrm{i}-8}{1+4}').create()
        line4 = TNT_Deprecated().tx('=\\dfrac{-5+10\\cdot\\mathrm{i}}{5}=-1+2\\cdot\\mathrm{i}').create()

        group_of_solution = VGroup(line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT, buff=0.1).shift(DOWN*0.3 + LEFT*1.09)


        ## setup norm theory
        norm_rect = swRoundedRectangle(height=0.8, width=1.5)
        norm_rect.shift(UP*0.6+RIGHT*1.3)
        norm = TNT_Deprecated().add_text('Norm of complex number', weight="SEMIBOLD", color=PINK).create().shift(UP*0.85+RIGHT*1.3)
        z = TNT_Deprecated().tx('z=a+b\\cdot\\mathrm{i}').create().shift(UP*0.65+RIGHT*1.25)
        norm_z = TNT_Deprecated().tx('z\\cdot \\overline{z} =||z||^2=a^2+b^2').create().move_to(z.get_center() + DOWN*0.2)

        norm_group = VGroup(norm_rect, norm, z, norm_z).shift(DOWN)

        z_denom_norm = TNT_Deprecated().tx('z=1-2\\cdot\\mathrm{i}').create().move_to(z.get_center())
        norm_z_denom_norm = TNT_Deprecated().tx('z\\cdot\\overline{z} =||1-2\\cdot\\mathrm{i}||^2=1^2+(-2)^2').create().move_to(norm_z.get_center()).shift(RIGHT * 0.02)

        z_denom_norm[0][0][2:].set_color(GREEN)
        norm_z_denom_norm[0][0][7:12].set_color(GREEN)

        self.next_section()

        ### EXAMPLE 2 ###

        reciprocal = Text('Reciprocal of complex number', font="Quicksand", color=PINK, weight="SEMIBOLD")
        reciprocal.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.8 + DOWN * 0.15)

        problem_2 = TNT_Deprecated().txt('Calculate ').tx('\\dfrac{1}{-3 - 2\\cdot\\mathrm{i}}').create().move_to(problem.get_center() + UP *0.04)

        problem_2[1][0][2:].set_color(GREEN)

        ## start solving problem
        equation_2 = TNT_Deprecated().tx('\\dfrac{1}{-3 - 2\\cdot\\mathrm{i}}=\\dfrac{1}{-3 - 2\\cdot\\mathrm{i}} \\cdot \\dfrac{-3+2\\cdot\\mathrm{i}}{-3+2\\cdot\\mathrm{i}}').create().move_to(equation.get_center() + RIGHT * 0.07)
        
        equation_2[0][0][2:8].set_color(GREEN)
        equation_2[0][0][11:17].set_color(GREEN)
        equation_2[0][0][18:24].set_color(swGOLD)
        equation_2[0][0][25:].set_color(swGOLD)


        line1_2 = TNT_Deprecated().tx('=\\dfrac{1\\cdot(-3+2\\cdot\\mathrm{i})}{||-3-2\\cdot\\mathrm{i}||^2}').create().move_to(line1.get_center())

        line1_2[0][0][4:9].set_color(swGOLD)
        line1_2[0][0][14:20].set_color(GREEN)

        line2_2 = TNT_Deprecated().tx('=\\dfrac{-3+2\\cdot\\mathrm{i}}{(-3)^2+(-2)^2}').create().move_to(line2.get_center())
        line3_2 = TNT_Deprecated().tx('=\\dfrac{-3+2\\cdot\\mathrm{i}}{9+4}').create().move_to(line3.get_center())
        line4_2 = TNT_Deprecated().tx('=\\dfrac{-3+2\\cdot\\mathrm{i}}{13}=-\\dfrac{3}{13}+\\dfrac{2}{13}\\cdot\\mathrm{i}').create().move_to(line4.get_center())
        
        group_of_solution_2 = VGroup(line1_2, line2_2, line3_2, line4_2).arrange(DOWN, aligned_edge=LEFT, buff=0.1).shift(DOWN*0.3 + LEFT)




        ### Animation ###
        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))

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
            self.play(Create(conj_rect))
            self.play(swWrite(comp_conj))
            self.wait(1)


        with self.voiceover(text="if 'z' is 'a' + 'b' times 'i', then the complex conjugate of 'z' is 'a' minus 'b' times 'i'.") as tracker:
            self.play(swWrite(z_normal), run_time=tracker.duration * 0.3)
            self.play(swWrite(z_conj), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)

        self.wait(1)

        with self.voiceover(text="We take the complex conjugate of the denominator.") as tracker:
            self.play(TransformMatchingTex(z_normal, z_denom), run_time=tracker.duration * 0.2)
            self.wait(tracker.duration * 0.3)
            self.play(TransformMatchingTex(z_conj, z_denom_conj), run_time=tracker.duration * 0.2)

        self.wait(1)

        with self.voiceover(text="Now, we can multiply the numerator and denominator by the complex conjugate of the denominator.") as tracker:
            self.play(swWrite(equation), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)

        with self.voiceover(text="To simplify this fraction, we can use the fact that multiplying a complex number 'z' by its complex conjugate, equals the norm squared of z, which is 'a' squared plus 'b' squared.") as tracker:

            self.play(Create(norm_rect), run_time=tracker.duration * 0.1)
            self.wait(0.1)
            self.play(swWrite(norm), run_time=tracker.duration * 0.1)
            self.wait(0.1)
            self.play(swWrite(z),run_time= tracker.duration * 0.1)
            self.wait(0.5)
            self.play(swWrite(norm_z),run_time= tracker.duration * 0.6)
        
        self.wait(1)

        with self.voiceover(text="In this case, z is the denominator and the norm of 'z' squared is equal to 1 squared plus minus 2 squared.") as tracker:
            self.play(TransformMatchingTex(z, z_denom_norm), run_time=tracker.duration * 0.3)
            self.play(TransformMatchingTex(norm_z, norm_z_denom_norm), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)

        self.wait(1)

        with self.voiceover(text="Therefore, the fraction is equal to 3 plus 4 times i multiplied by 1 plus 2 times i, divided by the norm squared of 1 minus 2 times i.") as tracker:
            self.play(swWrite(line1), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)

        with self.voiceover(text="We expand the brackets in the numerator and for the denominator, the norm squared of 1 minus 2 times 'i' is equal to 1 squared plus minus 2 squared.") as tracker:
            self.play(swWrite(line2), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)

        with self.voiceover(text="Since 'i' squared is negative 1, the fraction is equal to 3 plus 10 times 'i' minus 8 divided by 1 plus 4.") as tracker:
            self.play(swWrite(line3), run_time=tracker.duration * 0.4)  
            self.wait(tracker.duration * 0.6)

        with self.voiceover(text="Simplifying the fraction gives us minus 5 plus 10 times 'i' divided by 5. This is equal to minus 1 + 2 times 'i'") as tracker:
            self.play(swWrite(line4), run_time=tracker.duration * 0.4)
            self.wait(tracker.duration * 0.6)

        self.wait(1)

        self.play(FadeOut(group_of_solution), FadeOut(problem), FadeOut(equation), FadeOut(example), TransformMatchingTex(z_denom, z_normal), TransformMatchingTex(z_denom_conj, z_conj), TransformMatchingTex(z_denom_norm, z), TransformMatchingTex(norm_z_denom_norm, norm_z))
        self.wait(1)
        
        self.play(swWrite(reciprocal))
        self.wait(1)

        # why does it pronounce this as i prime????
        with self.voiceover(text="Now, we will calculate the reciprocal of minus 3 minus 2 times i.") as tracker:
            self.play(swWrite(problem_2), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)

        self.wait(1)


        reciprocal_z = TNT_Deprecated().tx('z=-3-2\\cdot\\mathrm{i}').create().move_to(z_normal.get_center())
        reciprocal_z_conj = TNT_Deprecated().tx('\\overline{z}=-3+2\\cdot\\mathrm{i}').create().move_to(z_conj.get_center())

        reciprocal_z[0][0][2:].set_color(GREEN)
        reciprocal_z_conj[0][0][3:].set_color(swGOLD)

        with self.voiceover(text="First off, we know that the complex conjugate of the denominator is minus 3 plus 2 times 'i'.") as tracker:
            self.play(TransformMatchingTex(z_normal, reciprocal_z), run_time=tracker.duration * 0.3)
            self.play(TransformMatchingTex(z_conj, reciprocal_z_conj), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)


        reciprocal_z2 = reciprocal_z.copy().move_to(z.get_center())
        reciprocal_z_norm = TNT_Deprecated().tx('z\\cdot\\overline{z}=||-3-2\\cdot\\mathrm{i}||^2=(-3)^2+(-2)^2').create().move_to(norm_z.get_center()).scale(0.8).shift(RIGHT * 0.02)

        reciprocal_z2[0][0][2:].set_color(GREEN)
        reciprocal_z_norm[0][0][7:13].set_color(GREEN)

        with self.voiceover(text="Next, we can see that the norm squared of z is equal to minus 3 squared plus minus 2 squared") as tracker:
            self.play(TransformMatchingTex(z, reciprocal_z2), run_time=tracker.duration * 0.3)
            self.play(TransformMatchingTex(norm_z, reciprocal_z_norm), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)

        with self.voiceover(text="Now once again, we can solve the problem by first multiplying the numerator and denominator by the complex conjugate of the denominator.") as tracker:
            self.play(swWrite(equation_2), run_time = tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)
        
        self.wait(1)
        
        with self.voiceover(text="if we multiply the denominators, we get the norm squared of minus 3 minus 2 times 'i' in the denominator.") as tracker:
            self.play(swWrite(line1_2), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)
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

        with self.voiceover(text="This concludes the examples. Thanks for watching.") as tracker:
            self.wait(tracker.duration)
    
        # fade out everything still on the screen
        self.wait(2)

        all_fadeout = Group(*self.mobjects)
        self.play(FadeOut(all_fadeout))
        self.wait(1)