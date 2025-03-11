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
                model="tts-1-hd",
            )
        )

        ## Title
        title = Text("""      Calculating the \npolar-exponential form""", font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'polar-exponential':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)

        ## Logo
        logo = ImageMobject('./Sowiso-logo-primary.png')
        logo.move_to(self.camera.frame.get_corner(DL)).shift(0.15*UP + 0.35*RIGHT)
        logo.scale(0.009)

        ## text top left
        polar_exp_form_title = Text('Polar-exponential form', font="Quicksand", color=PINK, weight="SEMIBOLD")
        polar_exp_form_title.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.6 + DOWN * 0.1)

        ## setup example rectangle
        ex1_rect = swRoundedRectangle(height=2, width=2.5)
        ex1_rect.shift(LEFT*0.9)

        problem = TNT().txt('Write', 'SEMIBOLD').tx('-\\dfrac{3 \\cdot \\sqrt{3}}{2} - \\dfrac{3}{2}\\cdot \\mathrm{i}').txt('in polar-exponential form', 'SEMIBOLD').create()
        problem.move_to(ex1_rect.get_center() + UP * 0.85)
        problem_underline = Line(problem[1][0].get_corner(DL) + LEFT * 0.4, problem[1][0].get_corner(DR) + RIGHT * 1.35, color=GREY, stroke_width=0.2).shift(DOWN*0.03)

        problem[1][0][:12].set_color(BLUE)

        ## Remembering the polar form rules rectangle
        polar_rules_rect = swRoundedRectangle(height=1.1, width=1.6)
        polar_rules_rect.shift(RIGHT*1.3 + UP*0.43)

        polar_form_txt = TNT().txt('Polar form', 'SEMIBOLD', PINK).create()
        polar_form_txt.move_to(polar_rules_rect.get_center() + UP * 0.44)

        z_comp_num = TNT().tx('z = a + b \\cdot \\mathrm{i}').create()
        z_comp_num[0][0][0].set_color(BLUE)
        z_comp_num[0][0][2].set_color(BLUE)
        z_comp_num[0][0][4].set_color(BLUE)
        
        r_formula = TNT().tx('r = \\sqrt{a^2 + b^2}').create()
        r_formula[0][0][0].set_color(GREEN)
        r_formula[0][0][4].set_color(BLUE)
        r_formula[0][0][7].set_color(BLUE)

        theta_formula = TNT().tx('\\theta = \\arctan\\left(\\dfrac{b}{a}\\right)').create()
        theta_formula[0][0][0].set_color(GOLDY)
        theta_formula[0][0][9].set_color(BLUE)
        theta_formula[0][0][11].set_color(BLUE)

        z_comp_num.move_to(polar_rules_rect.get_center() + UP * 0.2)
        r_formula.move_to(polar_rules_rect.get_center()+ DOWN * 0.02)
        theta_formula.move_to(polar_rules_rect.get_center() + DOWN * 0.3)


        ## calculating r 
        calculating_r = TNT().txt('Calculating r', 'NORMAL').create()
        calculating_r.shift(LEFT*1.7 + UP*0.58)
        r_def = r_formula.copy()

        line_r_1 = TNT().tx('r').tx('= \\sqrt{\\left(-\\dfrac{3 \\cdot \\sqrt{3}}{2}\\right)^2 + \\left(-\\dfrac{3}{2}\\right)^2}').create()
        line_r_1[0][0][0].set_color(GREEN)

        line_r_2 = TNT().tx('= \\sqrt{\\dfrac{27}{4}+\\dfrac{9}{4}}').create()
        line_r_3 = TNT().tx('= \\sqrt{\\dfrac{36}{4}}').create()
        line_r_4 = TNT().tx('= \\sqrt{9}').create()
        line_r_5 = TNT().tx('= 3').create()

        line_r_1.move_to(r_def.get_center() + LEFT * 2.45 + DOWN * 0.15)
        line_r_1[0].shift(DOWN*0.03)

        group_of_solution_calc_r = VGroup(line_r_2, line_r_3, line_r_4, line_r_5).arrange(DOWN, aligned_edge=LEFT, buff=0.07).shift(DOWN*0.4 + LEFT*1.47)
        group_of_fadeout_calc_r = VGroup(line_r_1[1], line_r_2, line_r_3, line_r_4)
        r_equals_3 = VGroup(line_r_1[0], line_r_5)

        ## calculating theta
        calculating_theta = TNT().txt('Calculating the angle', 'NORMAL').create()
        calculating_theta.shift(LEFT*1.5 + UP*0.26)
        theta_def = theta_formula.copy()

        line_theta_1 = TNT().tx('\\theta').tx('= \\arctan\\left(\\dfrac{-\\dfrac{3}{2}}{-\\dfrac{3}{2}\\cdot \\sqrt{3}}\\right)').create()
        line_theta_1[0][0][0].set_color(GOLDY)

        where_a_and_b = TNT().txt(', where ', "NORMAL").tx('a<0').txt(' and ', "NORMAL").tx('b<0').create()
        where_a_and_b.move_to(calculating_theta.get_center() + RIGHT * 1.07 + UP * 0.01)
        where_a_and_b[3].shift(UP*0.01)

        minus_pi = TNT().tx('-\\;\\pi').create()
        minus_pi.move_to(line_theta_1.get_center() + LEFT*0.5 + DOWN * 0.28)

        line_theta_2 = TNT().tx('= \\arctan\\left(\\dfrac{1}{\\sqrt{3}}\\right)-\\pi').create()
        line_theta_3 = TNT().tx('= \\dfrac{\\pi}{6}-\\pi').create()

        line_theta_1.move_to(theta_def.get_center() + LEFT * 2.45 + DOWN * 0.2)
        line_theta_1[0].shift(UP*0.01)

        line_theta_simplified = TNT().tx('= -\\dfrac{5\\cdot\\pi}{6}').create()
        line_theta_simplified.move_to(theta_def.get_center() + LEFT * 2.71 + DOWN * 0.2)

        group_of_solution_calc_theta = VGroup(line_theta_2, line_theta_3).arrange(DOWN, aligned_edge=LEFT, buff=0.07).shift(DOWN*0.6 + LEFT*1.12)
        group_of_fadeout_calc_theta = VGroup(line_theta_1[1], line_theta_2, minus_pi)
        theta_equals_pi_6 = VGroup(line_theta_1[0], line_theta_simplified)

        
        ## polar exp form
        this_defines_the_polar_form = TNT().txt('This defines the polar form', 'NORMAL').create()
        this_defines_the_polar_form.shift(LEFT*1.38 + DOWN*0.1)

        polar_form = TNT().tx('3 \\cdot \\left(\\cos(-\\frac{5\\cdot\\pi}{6}) + \\mathrm{i} \\cdot \\sin(-\\frac{5\\cdot\\pi}{6})\\right)').create()
        polar_form[0][0][0].set_color(GREEN)
        polar_form[0][0][7:13].set_color(GOLDY)
        polar_form[0][0][21:27].set_color(GOLDY)

        polar_form.move_to(this_defines_the_polar_form.get_center() + DOWN*0.2 +RIGHT *0.5)

        ## eulers formula rect
        euler_rect = swRoundedRectangle(height=0.8, width=1.6)
        euler_rect.shift(RIGHT*1.3 + DOWN*0.6)

        eulers_formula = TNT().txt('Euler\'s formula', 'SEMIBOLD', PINK).create()
        eulers_formula.move_to(euler_rect.get_center() + UP * 0.28)

        actually_eulers_formula = TNT().tx('e^{\\theta\\cdot \\mathrm{i}} = \\cos(\\theta) + \\mathrm{i} \\cdot \\sin(\\theta)').create()
        actually_eulers_formula.move_to(euler_rect.get_center())
        actually_eulers_formula[0][0][1].set_color(GOLDY)
        actually_eulers_formula[0][0][9].set_color(GOLDY)
        actually_eulers_formula[0][0][-2].set_color(GOLDY)
        

        this_defines_the_polar_exp_form = TNT().txt('This defines the polar-exponential form', 'NORMAL').create()
        this_defines_the_polar_exp_form.move_to(this_defines_the_polar_form.get_center() + DOWN*0.45 + RIGHT * 0.3)

        LHS_euler_formula = actually_eulers_formula.copy().move_to(actually_eulers_formula.get_center())
        LHS_euler_formula_2 = TNT().tx('\\cos(\\theta) + \\mathrm{i} \\cdot \\sin(\\theta) = e^{\\theta\\cdot \\mathrm{i}}').create()
        LHS_euler_formula_2.move_to(actually_eulers_formula.get_center() + LEFT * 2.15 + DOWN * 0.2)
        LHS_euler_formula_2[0][0][4].set_color(GOLDY)
        LHS_euler_formula_2[0][0][13].set_color(GOLDY)
        LHS_euler_formula_2[0][0][-3].set_color(GOLDY)
        

        LHS_euler_formula_3 = TNT().tx('\\cos(-\\dfrac{5\\cdot\\pi}{6}) + \\mathrm{i} \\cdot \\sin(-\\dfrac{5\\cdot\\pi}{6}) = e^{-\\frac{5\\cdot\\pi}{6}\\cdot \\mathrm{i}}').create()
        LHS_euler_formula_3.move_to(actually_eulers_formula.get_center() + LEFT * 2.15 + DOWN * 0.2)
        LHS_euler_formula_3[0][0][4:10].set_color(GOLDY)
        LHS_euler_formula_3[0][0][18:24].set_color(GOLDY)
        LHS_euler_formula_3[0][0][-8:-2].set_color(GOLDY)

        LHS_euler_formula_4 = TNT().tx('3 \\cdot \\left(\\cos(-\\dfrac{5\\cdot\\pi}{6}) + \\mathrm{i} \\cdot \\sin(-\\dfrac{5\\cdot\\pi}{6})\\right) =').tx('3 \\cdot e^{-\\frac{5\\cdot\\pi}{6}\\cdot \\mathrm{i}}').create()
        LHS_euler_formula_4.move_to(actually_eulers_formula.get_center() + LEFT * 2.15 + DOWN * 0.2)
        LHS_euler_formula_4[0][0][0].set_color(GREEN)
        LHS_euler_formula_4[0][0][7:13].set_color(GOLDY)
        LHS_euler_formula_4[0][0][21:27].set_color(GOLDY)
        LHS_euler_formula_4[1][0][0].set_color(GREEN)
        LHS_euler_formula_4[1][0][-8:-2].set_color(GOLDY)      


        ##################
        ### ANIMATIONS ###
        ##################

        ##################
        ### ANIMATIONS ###
        ##################

        with self.voiceover(text='This video shows how to write a complex number in polar exponential form.') as tracker:
            self.play(swWrite(title), run_time=tracker.duration * 0.3)  
            self.wait(tracker.duration * 0.7)
        self.play(FadeOut(title))
        self.wait(1)

        self.add(logo)

        # setup title, example rectangle and problem statement
        self.play(swWrite(polar_exp_form_title, PINK), Create(ex1_rect))
        with self.voiceover(text='We have to find the polar exponential form of minus three times the square root of 3 divided by 2 minus 3 over 2 times "i".') as tracker:
            self.play(swWrite(problem), run_time=tracker.duration * 0.3)
            self.play(Create(problem_underline))
            self.wait(tracker.duration * 0.7)

        # polar form rules
        with self.voiceover(text='First, we need to remember the rules for the polar form.') as tracker:
            self.play(Create(polar_rules_rect))
            self.play(swWrite(polar_form_txt))
            self.play(swWrite(z_comp_num))
        
        with self.voiceover(text='To write a complex number in polar form, we need to calculate the norm "r" and the angle "theta".') as tracker:
            self.play(swWrite(r_formula))
            self.play(swWrite(theta_formula))

        # calculating r
        with self.voiceover(text='First, we calculate the norm "r".') as tracker:
            self.play(swWrite(calculating_r))

        self.play(r_def.animate.shift(LEFT*2.8))
        self.wait(1)

        with self.voiceover(text='"r" is equal to the square root of minus three times the square root of 3 divided by 2 squared plus minus 3 over 2 squared.') as tracker:
            self.play(TransformMatchingShapes(r_def, line_r_1))

        with self.voiceover(text='This simplifies to the square root of 27 over 4 plus 9 over 4.') as tracker:
            self.play(swWrite(line_r_2))

        self.play(swWrite(line_r_3))
        self.wait(1)
        self.play(swWrite(line_r_4))

        with self.voiceover(text='This simplifies to "r" equals 3.') as tracker:
            self.play(swWrite(line_r_5))

        self.wait(1)

        self.play(FadeOut(group_of_fadeout_calc_r))
        self.play(line_r_5.animate.shift(UP*1.04))
        self.play(r_equals_3.animate.shift(UP*0.19))

        self.wait(1)

        # calculating theta
        with self.voiceover(text='Now, we calculate the angle "theta".') as tracker:
            self.play(swWrite(calculating_theta))

        self.play(theta_def.animate.shift(LEFT*2.8 + DOWN * 0.1))
        self.wait(1)

        with self.voiceover(text='"Theta" is equal to the arctangent of minus 3 over 2 divided by minus 3 over 2 times the square root of 3') as tracker:
            self.play(TransformMatchingShapes(theta_def, line_theta_1))
            self.play(swWrite(where_a_and_b))

        self.wait(1)
        with self.voiceover(text='"a" and "b" are both less than zero. We have seen that this requires us to add minus pi at the end of the formula.') as tracker:
            self.wait(tracker.duration * 0.7)
            self.play(swWrite(minus_pi), run_time=tracker.duration * 0.1)

        self.play(swWrite(line_theta_2))
        self.wait(1)

        with self.voiceover(text='This simplifies to pi over six minus pi.') as tracker:
            self.play(swWrite(line_theta_3))
            self.wait(1)
            self.play(FadeOut(group_of_fadeout_calc_theta))

        with self.voiceover(text='And this is equal to minus five times pi over six.') as tracker:
            self.play(line_theta_3.animate.shift(UP*0.67))
            self.play(TransformMatchingShapes(line_theta_3, line_theta_simplified))

        self.play(theta_equals_pi_6.animate.shift(UP*0.15 + LEFT * 0.17))

        self.wait(1)

        # show polar form
        with self.voiceover(text='"r" and theta give us the polar form as shown.') as tracker:
            self.play(swWrite(this_defines_the_polar_form))
            self.play(swWrite(polar_form))
            self.wait(tracker.duration)

        self.wait(1)

        # euler's formula
        with self.voiceover(text='Using Euler\'s famous formula, we can convert this polar form into polar-exponential form.') as tracker:
            self.play(Create(euler_rect))
            self.wait(tracker.duration * 0.5)

        with self.voiceover(text='Euler\'s formula states that "e" to the power of "theta" times "i" is equal to the cosine of "theta" plus "i" times the sine of "theta".') as tracker:
            self.play(swWrite(eulers_formula))
            self.play(swWrite(actually_eulers_formula))

        with self.voiceover(text='We can use this formula to calculate the polar-exponential form.') as tracker:
            self.play(swWrite(this_defines_the_polar_exp_form))

        self.play(LHS_euler_formula.animate.shift(LEFT*2.8), TransformMatchingShapes(LHS_euler_formula, LHS_euler_formula_2))

        with self.voiceover(text='We subsitute our value for theta into Euler\'s formula.') as tracker:
            self.wait(tracker.duration * 0.3)
            self.play(TransformMatchingShapes(LHS_euler_formula_2, LHS_euler_formula_3))

        with self.voiceover(text='And now we can multiply both sides of the equation by "r" which is 3.') as tracker:
            self.play(TransformMatchingShapes(LHS_euler_formula_3, LHS_euler_formula_4))

        with self.voiceover(text='Now, we have written the polar form as 3 times "e" to the power of minus 5 times pi over 6 times "i".') as tracker:
            self.play(FadeOut(LHS_euler_formula_4[0]))
            self.play(LHS_euler_formula_4[1].animate.shift(LEFT*0.8))
            self.wait(tracker.duration * 0.3)

        all_fadeout = Group(*self.mobjects)
        with self.voiceover(text="This is the polar-exponential form of the complex number. Thanks for watching.") as tracker:
            self.wait(tracker.duration * 0.7)
            self.play(FadeOut(all_fadeout), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.3)