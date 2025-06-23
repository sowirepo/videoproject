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

        ## Title
        title = Text("""Roots of unity  """, font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'quotient':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)

        ## Logo
        logo = ImageMobject('../Sowiso-logo-primary.png').scale(0.03)


        ## text top left
        roots_of_unity_title = Text('Roots of unity', font="Quicksand", color=PINK, weight="SEMIBOLD")
        roots_of_unity_title.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.1)

        ## setup example rectangle
        ex1_rect = swRoundedRectangle(height=2.1, width=2.5)

        ## propose problem
        problem = TNT().txt("We will solve the equation ").tx('z^n=1').shift(UP * 0.8)
        problem[0][1][0][0].set_color(BLUE)
        problem[0][1][0][1].set_color(swGOLD)

        this_equation_has_n_roots = TNT().txt("This equation has ").tx('n', aligned_char='n', color=swGOLD).txt(' distinct solutions').shift(UP * 0.6)

        z_is_1 = TNT().tx('z=1').txt(' is always a solution').shift(UP * 0.5)
        z_is_1[0][0][0][0].set_color(BLUE)
        z_is_minus_1 = TNT().tx('z=-1').txt(' is a solution when ').tx('n').txt(' is even').shift(UP * 0.4)
        z_is_minus_1[0][0][0][0].set_color(BLUE)
        z_is_minus_1[0][2][0][0].set_color(swGOLD)

        by_rewriting = TNT().txt("By rewriting the equation using").shift(UP * 0.3)
        the_polar_exp = TNT().txt("the ").txt("polar-exponential form,", weight="SEMIBOLD").txt('we get').shift(UP * 0.2)

        polar_exp1 = problem[0][1].copy()
        polar_exp2 = TNT().tx('(\\|z\\|\\cdot \\mathrm{e}^{\\varphi \\cdot \\mathrm{i}})^n = \\|1\\|\\cdot \\mathrm{e}^{2 \\cdot k \\cdot \\pi \\cdot \\mathrm{i}}').shift(DOWN * 0.1)
        polar_exp2[0][0][0][2].set_color(BLUE)
        polar_exp2[0][0][0][6].set_color(GREEN)
        polar_exp2[0][0][0][10].set_color(swGOLD)
        
        polar_exp2_5 = TNT().tx('\\|z\\|^n\\cdot \\mathrm{e}^{n \\cdot \\varphi \\cdot \\mathrm{i}} = \\|1\\|\\cdot \\mathrm{e}^{2 \\cdot k \\cdot \\pi \\cdot \\mathrm{i}}').shift(DOWN * 0.1)
        polar_exp2_5[0][0][0][1].set_color(BLUE)
        polar_exp2_5[0][0][0][3].set_color(swGOLD)
        polar_exp2_5[0][0][0][8].set_color(swGOLD)
        
        polar_exp3 = TNT().txt('The norm').tx('\\|z\\|^n=\\|1\\|').shift(DOWN * 0.3)
        polar_exp3[0][1][0][1].set_color(BLUE)
        polar_exp3[0][1][0][3].set_color(swGOLD)
        polar_exp3_1 = TNT().txt('The norm').tx('\\|z\\|=1').shift(DOWN * 0.3)
        polar_exp3_1[0][1][0][1].set_color(BLUE)

        polar_exp4 = TNT().txt('The argument ').tx('\\varphi = \\dfrac{2\\cdot k \\cdot \\pi}{n}').shift(DOWN * 0.6)
        polar_exp4[0][1][0][0].set_color(GREEN)
        polar_exp4[0][1][0][-1].set_color(swGOLD)

        polar_exp5 = TNT().txt('There are ').tx('n', aligned_char='n', color=swGOLD).txt(' solutions for ').tx('-\\pi < \\varphi \\leq \\pi', aligned_char='<').shift(DOWN * 0.8)
        polar_exp5[0][3][0][3].set_color(GREEN)

        everything_above = VGroup(problem, this_equation_has_n_roots).shift(UP * 0.1)
        everything_below = VGroup(by_rewriting, the_polar_exp, polar_exp2, polar_exp2_5, polar_exp3, polar_exp3_1, polar_exp4, polar_exp5).shift(DOWN * 0.1)

        fadeout_group = VGroup(problem, this_equation_has_n_roots, z_is_1, z_is_minus_1, by_rewriting, the_polar_exp, polar_exp1, polar_exp2_5, polar_exp3_1, polar_exp4, polar_exp5)

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
        solve_n3_is_1[0][1][0][0].set_color(BLUE)
        solve_n3_is_1[0][1][0][1].set_color(swGOLD)

        title_underline = Line(solve_n3_is_1.get_corner(DL) + LEFT*0.65 , solve_n3_is_1.get_corner(DR) + RIGHT * 0.65, color=GREY, stroke_width=0.2).shift(DOWN*0.07)

        the_other_solutions = TNT().txt('We have ').tx('\\|z\\|=1').move_to(example_n3_rect).shift(UP * 0.6)
        the_other_solutions[0][1][0][1].set_color(BLUE)

        where_phi = TNT().txt('and ').tx('\\varphi=\\dfrac{2\\cdot k \\cdot \\pi}{3}').move_to(example_n3_rect.get_center()).shift(UP * 0.4)
        where_phi[0][1][0][0].set_color(GREEN)
        where_phi[0][1][0][-1].set_color(swGOLD)

        phi_inequalities_must_hold = TNT().tx('-\\pi < \\varphi \\leq \\pi').txt(' must hold').move_to(example_n3_rect.get_center()).shift(UP * 0.2)
        phi_inequalities_must_hold[0][0][0][3].set_color(GREEN)

        picking_k_is_0 = TNT().txt('For ').tx('k=0,').txt(' we get ').tx('z = 1').move_to(example_n3_rect.get_center()).shift(DOWN * 0.0)
        picking_k_is_0[0][3][0][0].set_color(BLUE)

        picking_k_is_1 = TNT().txt('For ').tx('k=1,').txt(' we get ').tx('z = \\mathrm{e}^{\\frac{2\\cdot\\pi}{3}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.2)
        picking_k_is_1[0][3][0][0].set_color(BLUE)
        picking_k_is_1[0][3][0][7].set_color(swGOLD)

        picking_k_is_2 = TNT().txt('For ').tx('k=2,').txt(' we get ').tx('z = \\mathrm{e}^{\\frac{4\\cdot\\pi}{3}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.4)
        picking_k_is_2[0][3][0][0].set_color(BLUE)
        picking_k_is_2[0][3][0][7].set_color(swGOLD)

        picking_k_is_minus_1 = TNT().txt('For ').tx('k=2,').txt(' we get ').tx('z = \\mathrm{e}^{-\\frac{2\\cdot\\pi}{3}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.4)
        picking_k_is_minus_1[0][3][0][0].set_color(BLUE)
        picking_k_is_minus_1[0][3][0][8].set_color(swGOLD)

        solutions = TNT().txt('Solutions:').tx('z=1\\vee z=\\mathrm{e}^{\\frac{2\\cdot\\pi}{3}\\cdot \\mathrm{i}}\\vee z=\\mathrm{e}^{-\\frac{2\\cdot\\pi}{3}\\cdot \\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.65)
        solutions[0][1][0][0].set_color(BLUE)
        solutions[0][1][0][4].set_color(BLUE)
        solutions[0][1][0][15].set_color(BLUE)

        solutions[0][1][0][11].set_color(swGOLD)
        solutions[0][1][0][23].set_color(swGOLD)

        # dot1 = Dot(p1:=polarplane_pi.polar_to_point(0,0), color=BLUE, radius=0.01)
        # dot2 = Dot(p2:=polarplane_pi.polar_to_point(1,0), color=RED,radius=0.01)
        org = polarplane_pi.polar_to_point(0,0)
        p1 = polarplane_pi.polar_to_point(1,0)
        p2 = polarplane_pi.polar_to_point(1,PI*2/3)
        p3 = polarplane_pi.polar_to_point(1,PI*4/3)


        vec_1 = Line(org, p1, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP *0.01)
        vec_2 = Line(org, p2, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP *0.01)
        vec_3 = Line(org, p3, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP *0.01)


        polarplane_group = VGroup(ex1_rect, polarplane_pi, label_X_re, label_Y_im)

        ex_n3_group = VGroup(the_other_solutions, where_phi, phi_inequalities_must_hold, picking_k_is_1, picking_k_is_minus_1, picking_k_is_0, solutions, vec_1, vec_2, vec_3)

        ##################
        ## example n=4
        ##################

        solve_n4_is_1 = TNT().txt('Solve ').tx('z^4=1').move_to(solve_n3_is_1.get_center())
        solve_n4_is_1[0][1][0][0].set_color(BLUE)
        solve_n4_is_1[0][1][0][1].set_color(swGOLD)

        the_other_solutions_n4 = TNT().txt('We have ').tx('\\|z\\|=1').txt(' and ').tx('\\varphi = \\dfrac{2\\cdot k \\cdot \\pi}{4}').move_to(example_n3_rect.get_center()).shift(UP * 0.6)
        the_other_solutions_n4[0][1][0][1].set_color(BLUE)
        the_other_solutions_n4[0][3][0][0].set_color(GREEN)
        the_other_solutions_n4[0][3][0][-1].set_color(swGOLD)

        picking_k_is_0_n4 = TNT().txt('For ').tx('k=0').txt(' we get ').tx('z=1').move_to(example_n3_rect.get_center()).shift(UP * 0.4)
        picking_k_is_0_n4[0][3][0][0].set_color(BLUE)

        picking_k_is_1_n4 = TNT().txt('For ').tx('k=1').txt(' we get ').tx('z=\\mathrm{e}^{\\frac{\\pi}{2}\\cdot\\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(UP * 0.2)
        picking_k_is_1_n4[0][3][0][0].set_color(BLUE)

        picking_k_is_2_n4 = TNT().txt('For ').tx('k=2').txt(' we get ').tx('z=\\mathrm{e}^{\\pi \\cdot \\mathrm{i}}=-1').move_to(example_n3_rect.get_center()).shift(DOWN * 0.0)
        picking_k_is_2_n4[0][3][0][0].set_color(BLUE)

        picking_k_is_3_n4 = TNT().txt('For ').tx('k=3').txt(' we get ').tx('z=\\mathrm{e}^{\\frac{6 \\cdot \\pi}{4}\\cdot\\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.2)
        picking_k_is_3_n4[0][3][0][0].set_color(BLUE)

        picking_k_is_minus_1_n4 = TNT().txt('For ').tx('k=3').txt(' we get ').tx('z=\\mathrm{e}^{-\\frac{\\pi}{2}\\cdot\\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.2)
        picking_k_is_minus_1_n4[0][3][0][0].set_color(BLUE)

        p1_n4 = polarplane_pi.polar_to_point(1,0)
        p2_n4 = polarplane_pi.polar_to_point(1,1/2 * PI)
        p3_n4 = polarplane_pi.polar_to_point(1,PI)
        p4_n4 = polarplane_pi.polar_to_point(1,3/2 * PI)

        vec_n4_1 = Line(org, p1_n4, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_2 = Line(org, p2_n4, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_3 = Line(org, p3_n4, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP * 0.01)
        vec_n4_4 = Line(org, p4_n4, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06).shift(RIGHT * 1.1 + UP * 0.01) 

        fadeout_group_n4 = VGroup(the_other_solutions_n4, picking_k_is_1_n4, picking_k_is_0_n4, picking_k_is_minus_1_n4, picking_k_is_2_n4, vec_n4_1, vec_n4_2, vec_n4_3, vec_n4_4)

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
        solve_n5_is_1[0][1][0][0].set_color(BLUE)
        solve_n5_is_1[0][1][0][1].set_color(swGOLD)

        the_other_solutions_n5 = TNT().txt('We have ').tx('\\|z\\|=1').txt(' and ').tx('\\varphi = \\dfrac{2\\cdot k \\cdot \\pi}{5}').move_to(example_n3_rect.get_center()).shift(UP * 0.6)
        the_other_solutions_n5[0][1][0][1].set_color(BLUE)
        the_other_solutions_n5[0][3][0][0].set_color(GREEN)
        the_other_solutions_n5[0][3][0][-1].set_color(swGOLD)

        picking_k_is_minus_2_n5 = TNT().txt('For ').tx('k=-2').txt(' we get ').tx('z=\\mathrm{e}^{-\\frac{4\\cdot\\pi}{5}\\cdot\\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(UP * 0.4)
        picking_k_is_minus_2_n5[0][3][0][0].set_color(BLUE)
        picking_k_is_minus_2_n5[0][3][0][8].set_color(swGOLD)

        picking_k_is_minus_1_n5 = TNT().txt('For ').tx('k=-1').txt(' we get ').tx('z=\\mathrm{e}^{-\\frac{2\\cdot\\pi}{5}\\cdot\\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(UP * 0.2)
        picking_k_is_minus_1_n5[0][3][0][0].set_color(BLUE)
        picking_k_is_minus_1_n5[0][3][0][8].set_color(swGOLD)

        picking_k_is_0_n5 = TNT().txt('For ').tx('k=0').txt(' we get ').tx('z=1').move_to(example_n3_rect.get_center()).shift(UP * 0.0)
        picking_k_is_0_n5[0][3][0][0].set_color(BLUE)

        picking_k_is_1_n5 = TNT().txt('For ').tx('k=1').txt(' we get ').tx('z=\\mathrm{e}^{\\frac{2\\cdot\\pi}{5}\\cdot\\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.2)
        picking_k_is_1_n5[0][3][0][0].set_color(BLUE)
        picking_k_is_1_n5[0][3][0][7].set_color(swGOLD)

        picking_k_is_2_n5 = TNT().txt('For ').tx('k=2').txt(' we get ').tx('z=\\mathrm{e}^{\\frac{4\\cdot\\pi}{5}\\cdot\\mathrm{i}}').move_to(example_n3_rect.get_center()).shift(DOWN * 0.4)
        picking_k_is_2_n5[0][3][0][0].set_color(BLUE)
        picking_k_is_2_n5[0][3][0][7].set_color(swGOLD)



        ##################
        ### ANIMATIONS ###
        ##################

        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.1*UP + 0.35 * RIGHT).scale(0.009 / 0.03))
        
        with self.voiceover(text="This video shows how to calculate the roots of unity.") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        self.play(swWrite(roots_of_unity_title))

        self.play(Create(ex1_rect))

        with self.voiceover(text="We will solve the equation 'z' to the power of 'n' is equal to 1.") as tracker:
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


        self.play(polar_exp1.animate.move_to(ex1_rect.get_center() + DOWN * 0.05 + LEFT * 0.03))

        with self.voiceover(text="We can write 'z' and 1 in polar exponential form like this. Remember that 'k' can be any integer.") as tracker:
            self.play(swWrite(polar_exp2))

        self.wait(0.5)

        # apply demoivre's theorem
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
            # no new on-screen text: just pause briefly
            self.wait(1)

        # notice phi =0 for z=1 solution and phi = pi for z=-1 solution
        with self.voiceover(text="Therefore, there are n solutions for φ larger than minus π and smaller than or equal to pi. ") as tracker:
            self.play(swWrite(polar_exp5))

        ######################
        ## end of theory part
        ## start n = 3 example
        ####################

        self.play(FadeOut(fadeout_group))

        self.play(Transform(ex1_rect, polarplane_rect))

        with self.voiceover(text="We will now take a look at some examples and draw the solutions in an Argand diagram.") as tracker:
            self.play(Create(polarplane_pi))
            self.play(swWrite(label_Y_im), swWrite(label_X_re), run_time = 0.4)

        self.play(polarplane_group.animate.shift(RIGHT * 1.1 + UP *0.01))

        self.play(Create(example_n3_rect))

        with self.voiceover(text="We will start with the example of 'z' to the power of 3 equals 1.") as tracker:  
            self.play(swWrite(solve_n3_is_1))
            self.play(Create(title_underline))

        # we draw the position vector in the polar plane
        # self.play(swWrite(since_n_is_odd))
        # self.play(Create(vec_1))

        # Once again, Since the norm of z is 1, we only need to find the angle of the remaining possible solutions
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
        # We know that -2/3 pi is equal to 4/3 pi in rad so we draw this vector here
        self.play(Create(vec_3))

        with self.voiceover(text="The solutions are z equals 1 or z equals e to the power of 2 times π over 3 times i or z equals e to the power of -2 times π over 3 times i. Notice that the complex solutions form complex conjugates of eachother.") as tracker:
            self.play(swWrite(solutions))





        # START n=4 example
        # Notice how the complex roots are complex conjugates of each other
        self.play(FadeOut(ex_n3_group))

        # Move on to the next example
        with self.voiceover(text="Next, we will solve 'z' to the power of 4 equals 1.") as tracker:
            self.play(TransformMatchingShapes(solve_n3_is_1, solve_n4_is_1))

        with self.voiceover(text="We have the norm of 'z' equals 1 and the argument φ of 'z' equals 2 times k times π divided by 4.") as tracker:
            self.play(swWrite(the_other_solutions_n4))

        with self.voiceover(text="For k equals 0, we get 'z' equals 1.") as tracker:
            self.play(swWrite(picking_k_is_0_n4))
        self.play(Create(vec_n4_1))

        with self.voiceover(text="For k equals 1, we get 'z' equals e to the power of π over 2 times i.") as tracker:
            self.play(swWrite(picking_k_is_1_n4))
        self.play(Create(vec_n4_2))

        with self.voiceover(text="For k equals 2, we get 'z' equals e to the power of π times i, which is  minus 1.") as tracker:
            self.play(swWrite(picking_k_is_2_n4))
        self.play(Create(vec_n4_3))

        with self.voiceover(text="For k equals 3, we get 'z' equals e to the power of 6 times pi over 4 times i.") as tracker:
            self.play(swWrite(picking_k_is_3_n4))

        with self.voiceover(text="We have to subtract 2 times π to get the argument in the proper range. This is again the same result as the one obtained from using k equals minus 1.") as tracker:
                    self.play(TransformMatchingShapes(picking_k_is_3_n4, picking_k_is_minus_1_n4))

        self.play(Create(vec_n4_4))

        with self.voiceover(text="These are the 4 solutions to the problem. Once again, notice that the complex roots are complex conjugates of each other.") as tracker:
            self.wait(0.1)

        # Start n=5 example
        self.play(FadeOut(fadeout_group_n4))

        with self.voiceover(text="Finally, we will solve 'z' to the power of 5 equals 1.") as tracker:
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
        vec_n5_2 = Line(new_org, p2_n5, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)
        vec_n5_3 = Line(new_org, p3_n5, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)
        vec_n5_4 = Line(new_org, p4_n5, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)
        vec_n5_5 = Line(new_org, p5_n5, color=BLUE, stroke_width=2).add_tip(tip_length=0.1,tip_width=0.06)

        with self.voiceover(text="We have the norm of 'z' equals 1 and the argument φ of 'z' equals 2 times k times π divided by 5.") as tracker:
            self.play(swWrite(the_other_solutions_n5))

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
        


        with self.voiceover(text="These are the 5 solutions to the problem. We once again have that the complex roots are complex conjugates of eachother, which can be seen in the diagram.") as tracker:
            self.play(Create(VGroup()))

        ## Outro ##
        with self.voiceover(text="This concludes the examples. Thanks for watching") as tracker:
            self.wait(1)
    
        # time to let everthing sink in
        self.wait(2)

        # fade out everything still on the screen
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1) # make sure everything is gone before the video ends