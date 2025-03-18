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
        roots_of_unity_title.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.1)

        ## setup example rectangle
        ex1_rect = swRoundedRectangle(height=2.1, width=2.5)

        ## propose problem
        problem = TNT().txt("We will solve the equation ").tx('z^n=1').shift(UP * 0.8)
        problem[0][1][0][0].set_color(BLUE)
        problem[0][1][0][1].set_color(GOLDY)

        this_equation_has_n_roots = TNT().txt("This equation has ").tx('n', aligned_char='n', color=GOLDY).txt(' solutions').shift(UP * 0.6)

        z_is_1 = TNT().tx('z=1').txt(' is always a solution').shift(UP * 0.5)
        z_is_minus_1 = TNT().tx('z=-1').txt(' is a solution when ').tx('n').txt(' is even').shift(UP * 0.4)

        by_rewriting = TNT().txt("By rewriting the equation using").shift(UP * 0.3)
        the_polar_exp = TNT().txt("the ").txt("polar exponential form,", weight="SEMIBOLD").txt('we get').shift(UP * 0.2)

        polar_exp1 = problem[0][1].copy()
        polar_exp2 = TNT().tx('(\\|z\\|e^{\\mathrm{i}\\cdot \\varphi})^n = \\|1\\|e^{\\mathrm{i}\\cdot 2 \\cdot k \\cdot pi}').shift(DOWN * 0.1)
        polar_exp2_5 = TNT().tx('\\|z\\|^ne^{\\mathrm{i}\\cdot \\varphi \\cdot n} = \\|1\\|e^{\\mathrm{i}\\cdot 2 \\cdot k \\cdot \\pi}').shift(DOWN * 0.1)

        polar_exp3 = TNT().tx('z=e^{\\mathrm{i} \\cdot \\varphi} = e^{\\mathrm{i} \\cdot 2 \\cdot k \\cdot \\pi / n}').shift(DOWN * 0.3)

        polar_exp4 = TNT().txt('We have ').tx('\\varphi = \\dfrac{2\\cdot k \\cdot \\pi}{n}').shift(DOWN * 0.6)

        polar_exp5 = TNT().txt('There are ').tx('n', aligned_char='n', color=GOLDY).txt(' solutions for ').tx('-\\pi < \\varphi \\leq \\pi', aligned_char='<').shift(DOWN * 0.8)

        everything_above = VGroup(problem, this_equation_has_n_roots).shift(UP * 0.1)
        everything_below = VGroup(by_rewriting, the_polar_exp, polar_exp2, polar_exp2_5, polar_exp3, polar_exp4, polar_exp5).shift(DOWN * 0.1)

        fadeout_group = VGroup(problem, this_equation_has_n_roots, z_is_1, z_is_minus_1, by_rewriting, the_polar_exp, polar_exp1, polar_exp2_5, polar_exp3, polar_exp4, polar_exp5)

        ## setup the plane

        polarplane_pi = PolarPlane(
            azimuth_units="PI radians",
            azimuth_step=24, # switch to 12 for increments of pi/6
            size=7,
            azimuth_label_font_size=33.6,
            # radius_config={"font_size": 33.6,
            #                "color": BLACK},
            radius_max=1.5,
            radius_step=0.5,
            background_line_style=BACKGROUND_LINE_STYLE,
            radius_config=AXIS_CONFIG
        ).add_coordinates().scale(0.25)

        polarplane_rect = swRoundedRectangle(height=2.1, width=2.2).move_to(polarplane_pi.get_center())

        

        polarplane_pi[2:].set_color(DARK_GREY)

        # random -1.5 labels i dont want
        polarplane_pi[3][2][0].shift(UP * 9)
        polarplane_pi[4][0][2][0].shift(UP * 9)

        # dot_polar = Dot(polarplane_pi.polar_to_point(np.sqrt(2), PI/4))
        # self.add(dot_polar)

        label_Y_im = TNT().tx('\\mathrm{Im}').shift(UP * 0.8 + LEFT * 0.14)
        label_X_re = TNT().tx('\\mathrm{Re}').shift(RIGHT *0.8 + DOWN * 0.11)


        #####################
        ## EXAMPLE n=3
        #####################

        example_n3_rect = swRoundedRectangle(height=2.1, width=2).shift(LEFT * 1.15)

        solve_n3_is_1 = TNT().txt('Solve ').tx('z^3=1').move_to(example_n3_rect.get_center() + UP * 0.9)
        # title_underline = Line(solve_n3_is_1.get_corner(DL) + LEFT * 0.65 + DOWN * 0.1, solve_n3_is_1.get_corner(DR) + RIGHT * 0.65 + DOWN * 0.1, color=GREY, stroke_width=0.2)
        title_underline = Line(solve_n3_is_1.get_corner(DL) + LEFT*0.65 , solve_n3_is_1.get_corner(DR) + RIGHT * 0.65, color=GREY, stroke_width=0.2).shift(DOWN*0.07)

        since_n_is_odd = TNT().txt('Since ').tx('n', aligned_char='n').txt(' is odd, ').tx('z=1').txt(' is a solution').move_to(example_n3_rect.get_center()).shift(UP * 0.7)

        the_other_solutions = TNT().txt('The other solutions are of form ').tx('z=e^{\\mathrm{i} \\cdot \\varphi}').move_to(example_n3_rect).shift(UP * 0.5)
        where_phi = TNT().txt(' where ').tx('\\varphi=\\dfrac{2\\cdot k \\cdot \\pi}{3}').move_to(example_n3_rect.get_center()).shift(UP * 0.3)

        phi_inequalities_must_hold = TNT().tx('-\\pi < \\varphi \\leq \\pi').txt(' must hold').move_to(example_n3_rect.get_center()).shift(UP * 0.1)

        picking_k_is_1 = TNT().txt('Picking ').tx('k=1').txt(' gives ').tx('\\varphi=\\dfrac{2\\cdot \\pi}{3}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.1)
        and_solution_2 = TNT().txt('and ').tx('z=e^{\\frac{2\\cdot\\pi}{3}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.22)

        picking_k_is_minus_1 = TNT().txt('Picking ').tx('k=-1').txt(' gives ').tx('\\varphi=-\\dfrac{2\\cdot \\pi}{3}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.4)
        and_solution_3 = TNT().txt('and ').tx('z=e^{-\\frac{2\\cdot\\pi}{3}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.52)

        solutions = TNT().txt('Solutions:').tx('z=1\\wedge z=e^{\\frac{2\\cdot\\pi}{3}\\cdot \\mathrm{i}}\\wedge z=e^{\\frac{4\\cdot\\pi}{3}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.75)


        # dot1 = Dot(p1:=polarplane_pi.polar_to_point(0,0), color=BLUE, radius=0.01)
        # dot2 = Dot(p2:=polarplane_pi.polar_to_point(1,0), color=RED,radius=0.01)
        org = polarplane_pi.polar_to_point(0,0)
        p1 = polarplane_pi.polar_to_point(1,0)
        p2 = polarplane_pi.polar_to_point(1,PI*2/3)
        p3 = polarplane_pi.polar_to_point(1,PI*4/3)


        vec_1 = Line(org, p1, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP *0.01)
        vec_2 = Line(org, p2, color=RED, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP *0.01)
        vec_3 = Line(org, p3, color=GREEN, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP *0.01)


        polarplane_group = VGroup(ex1_rect, polarplane_pi, label_X_re, label_Y_im)

        ex_n3_group = VGroup(since_n_is_odd, the_other_solutions, where_phi, phi_inequalities_must_hold, picking_k_is_1, and_solution_2, picking_k_is_minus_1, and_solution_3, solutions, vec_1, vec_2, vec_3)

        ##################
        ## example n=4
        ##################

        solve_n4_is_1 = TNT().txt('Solve ').tx('z^4=1').move_to(solve_n3_is_1.get_center())

        since_n_is_even = TNT().txt('Since ').tx('n', aligned_char='n').txt(' is even, ').move_to(example_n3_rect.get_center()).shift(UP * 0.7)
        z_1_minus_1 = TNT().tx('z=1').txt(' and ').tx('z=-1').txt(' are solutions').move_to(example_n3_rect.get_center()).shift(UP * 0.6)

        the_other_solutions_n4 = the_other_solutions.copy().shift(DOWN * 0.1)
        where_phi_n4 = TNT().txt('where ').tx('\\varphi=\\dfrac{2\\cdot k \\cdot \\pi}{4}').move_to(example_n3_rect.get_center()).shift(UP * 0.2)

        picking_k_is_1_n4 = TNT().txt('Picking ').tx('k=1').txt(' gives ').tx('\\varphi=\\dfrac{\\pi}{2}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.1)
        and_solution_3_n4 = TNT().txt('and ').tx('z=e^{\\frac{\\pi}{2}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.25)

        picking_k_is_minus_1_n4 = TNT().txt('Picking ').tx('k=-1').txt(' gives ').tx('\\varphi=-\\dfrac{\\pi}{2}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.5)
        and_solution_4_n4 = TNT().txt('and ').tx('z=e^{-\\frac{\\pi}{2}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.65)


        p1_n4 = polarplane_pi.polar_to_point(1,0)
        p2_n4 = polarplane_pi.polar_to_point(1,1/2 * PI)
        p3_n4 = polarplane_pi.polar_to_point(1,PI)
        p4_n4 = polarplane_pi.polar_to_point(1,3/2 * PI)

        vec_n4_1 = Line(org, p1_n4, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_2 = Line(org, p2_n4, color=RED, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_3 = Line(org, p3_n4, color=GREEN, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_4 = Line(org, p4_n4, color=YELLOW, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP * 0.01) 

        fadeout_group_n4 = VGroup(since_n_is_even, z_1_minus_1, the_other_solutions_n4, where_phi_n4, picking_k_is_1_n4, and_solution_3_n4, picking_k_is_minus_1_n4, and_solution_4_n4, vec_n4_1, vec_n4_2, vec_n4_3, vec_n4_4)

        ##################
        ## example n=5
        ##################

        new_polarplane_pi = PolarPlane(
            azimuth_units="PI radians",
            azimuth_step=20, # switch to 12 for increments of pi/6
            size=7,
            azimuth_label_font_size=33.6,
            # radius_config={"font_size": 33.6,
            #                "color": BLACK},
            radius_max=1.5,
            radius_step=0.5,
            background_line_style=BACKGROUND_LINE_STYLE,
            radius_config=AXIS_CONFIG
        ).add_coordinates().scale(0.25).move_to(polarplane_pi.get_center())

        new_polarplane_pi[2:].set_color(DARK_GREY)

        # random -1.5 labels i dont want
        new_polarplane_pi[3][2][0].shift(UP * 9)
        new_polarplane_pi[4][0][2][0].shift(UP * 9)


        solve_n5_is_1 = TNT().txt('Solve ').tx('z^5=1').move_to(solve_n3_is_1.get_center())

        since_n_is_odd_n5 = since_n_is_odd.copy()

        picking_k_is_1_n5 = TNT().txt('Picking ').tx('k=1').txt(' gives ').tx('\\varphi=\\dfrac{2\\cdot \\pi}{5}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.1).shift(UP * 0.55)
        and_solution_3_n5 = TNT().txt('and ').tx('z=e^{\\frac{2\\cdot\\pi}{5}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.25).shift(UP * 0.55)

        picking_k_is_minus_1_n5 = TNT().txt('Picking ').tx('k=-1').txt(' gives ').tx('\\varphi=-\\dfrac{2\\cdot \\pi}{5}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.45).shift(UP * 0.55)
        and_solution_4_n5 = TNT().txt('and ').tx('z=e^{-\\frac{2\\cdot\\pi}{5}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.6).shift(UP * 0.55)

        picking_k_is_2_n5 = TNT().txt('Picking ').tx('k=2').txt(' gives ').tx('\\varphi=\\dfrac{4\\cdot \\pi}{5}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.8).shift(UP * 0.55)
        and_solution_5_n5 = TNT().txt('and ').tx('z=e^{\\frac{4\\cdot\\pi}{5}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.95).shift(UP * 0.55)

        picking_k_is_minus_2_n5 = TNT().txt('Picking ').tx('k=-2').txt(' gives ').tx('\\varphi=-\\dfrac{4\\cdot \\pi}{5}').move_to(example_n3_rect.get_center()).shift(DOWN * 1.15).shift(UP * 0.55)
        and_solution_6_n5 = TNT().txt('and ').tx('z=e^{-\\frac{4\\cdot\\pi}{5}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 1.3).shift(UP * 0.55)




        ##################
        ### ANIMATIONS ###
        ##################

        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.1*UP + 0.35 * RIGHT).scale(0.009 / 0.03))
        self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        self.play(swWrite(roots_of_unity_title))

        self.play(Create(ex1_rect))
        self.play(swWrite(problem))
        self.play(swWrite(this_equation_has_n_roots))

        self.play(swWrite(z_is_1))

        self.play(swWrite(z_is_minus_1))

        self.play(swWrite(by_rewriting))    
        self.play(swWrite(the_polar_exp))

        self.play(polar_exp1.animate.move_to(ex1_rect.get_center() + DOWN * 0.05))

        # remember k is an int
        self.play(swWrite(polar_exp2))

        # apply demoivre's theorem
        self.play(TransformMatchingShapes(polar_exp2, polar_exp2_5))

        self.play(swWrite(polar_exp3))

        self.play(swWrite(polar_exp4))

        # notice phi =0 for z=1 solution and phi = pi for z=-1 solution
        self.play(swWrite(polar_exp5))




        ######################
        ## end of theory part
        ## start n = 3 example

        self.play(FadeOut(fadeout_group))

        self.play(Transform(ex1_rect, polarplane_rect))

        self.play(Create(polarplane_pi))
        self.play(swWrite(label_Y_im), swWrite(label_X_re), run_time = 0.4)

        self.play(polarplane_group.animate.shift(RIGHT * 1.1 + UP *0.01))

        self.play(Create(example_n3_rect))

        self.play(swWrite(solve_n3_is_1))
        self.play(Create(title_underline))

        # we draw the position vector in the polar plane
        self.play(swWrite(since_n_is_odd))
        self.play(Create(vec_1))

        # Once again, Since the norm of z is 1, we only need to find the angle of the remaining possible solutions
        self.play(swWrite(the_other_solutions))
        self.play(swWrite(where_phi))

        self.play(swWrite(phi_inequalities_must_hold))

        # notice that if k=0, we get the first solution z=1
        self.play(swWrite(picking_k_is_1))
        self.play(swWrite(and_solution_2))
        # we draw this vector here
        self.play(Create(vec_2))

        self.play(swWrite(picking_k_is_minus_1))
        self.play(swWrite(and_solution_3))
        # we know that -2/3 pi is equal to 4/3 pi in rad so we draw this vector here
        self.play(Create(vec_3))

        self.play(swWrite(solutions))

        # notice how the complex roots are complex conjugates of each other


        self.play(FadeOut(ex_n3_group))

        ## START n=4 example
        self.play(TransformMatchingShapes(solve_n3_is_1, solve_n4_is_1))

        self.play(swWrite(since_n_is_even))
        self.play(swWrite(z_1_minus_1))

        #we draw those solutions
        self.play(Create(vec_n4_1))
        self.play(Create(vec_n4_3))


        self.play(swWrite(the_other_solutions_n4))
        # keep in mind -pi < phi <= pi
        self.play(swWrite(where_phi_n4))

        self.play(swWrite(picking_k_is_1_n4))
        self.play(swWrite(and_solution_3_n4))
        # we draw the point
        self.play(Create(vec_n4_2))


        self.play(swWrite(picking_k_is_minus_1_n4))
        self.play(swWrite(and_solution_4_n4))
        # we draw the point
        self.play(Create(vec_n4_4))


        self.play(FadeOut(fadeout_group_n4))

        ## START n=5 example
        self.play(TransformMatchingShapes(solve_n4_is_1, solve_n5_is_1))

        new_polarplane_pi.move_to(polarplane_pi.get_center()).shift(UP*0.01)
        self.play(Transform(polarplane_pi, new_polarplane_pi))

        new_org = new_polarplane_pi.polar_to_point(0,0)
        p1_n5 = new_polarplane_pi.polar_to_point(1,0)
        p2_n5 = new_polarplane_pi.polar_to_point(1,2/5 * PI)
        p3_n5 = new_polarplane_pi.polar_to_point(1,4/5 * PI)
        p4_n5 = new_polarplane_pi.polar_to_point(1,6/5 * PI)
        p5_n5 = new_polarplane_pi.polar_to_point(1,8/5 * PI)

        vec_n5_1 = Line(new_org, p1_n5, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)
        vec_n5_2 = Line(new_org, p2_n5, color=RED, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)
        vec_n5_3 = Line(new_org, p3_n5, color=GREEN, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)
        vec_n5_4 = Line(new_org, p4_n5, color=GOLDY, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)
        vec_n5_5 = Line(new_org, p5_n5, color=PORPLE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)



        self.play(swWrite(since_n_is_odd_n5))
        self.play(Create(vec_n5_1))

        self.play(swWrite(picking_k_is_1_n5))
        self.play(swWrite(and_solution_3_n5))

        self.play(Create(vec_n5_2))

        self.play(swWrite(picking_k_is_minus_1_n5))
        self.play(swWrite(and_solution_4_n5))

        self.play(Create(vec_n5_3))

        self.play(swWrite(picking_k_is_2_n5))
        self.play(swWrite(and_solution_5_n5))

        self.play(Create(vec_n5_4))

        self.play(swWrite(picking_k_is_minus_2_n5))
        self.play(swWrite(and_solution_6_n5))

        self.play(Create(vec_n5_5))

        # with self.voiceover(text="This concludes the examples. Thanks for watching") as tracker:
        #     self.wait(tracker.duration)
    
        # fade out everything still on the screen
        self.wait(2)

        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)