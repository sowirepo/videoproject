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
                model="gpt-4o-mini-tts",
            )
        )
        
        ## MOBJECTS ##
        # Title
        title = Text("Calculating the complex logarithm", font='Quicksand', color=PURPLE, weight="SEMIBOLD", line_spacing=0.2).scale(0.25).move_to(ORIGIN)

        # Logo
        logo = ImageMobject('./Sowiso-logo-primary.png').scale(0.03)

        # Example 1
        example1_rect = swRoundedRectangle(height=2, width=2.2).shift(LEFT * 1.05)  # Adjusted position and width
        ex1_title = TNT().txt('Let ').tx('z=2\\cdot \\mathrm{e}^{\\frac{\\pi}{3}\\cdot \\mathrm{i}}, ').txt('calculate ').tx('\\ln(z)')
        ex1_title.set_color_by_string('z', BLUE)
        ex1_title.set_color_by_string('2', GREEN)
        ex1_title.set_color_by_string('\\frac{\\pi}{3}', swGOLD)

        # Steps for calculating using the complex logarithm function
        sol_ex1_0 = TNT().tx('\\ln(z)=\\ln(2\\cdot \\mathrm{e}^{\\frac{\\pi}{3}\\cdot \\mathrm{i}})')
        sol_ex1_0.set_color_by_string('z', BLUE)
        sol_ex1_0.set_color_by_string('2', GREEN)
        sol_ex1_0.set_color_by_string('\\frac{\\pi}{3}', swGOLD)
        
        sol_ex1_1 = TNT().tx('=\\ln(2)+ \\dfrac{\\pi}{3}\\cdot \\mathrm{i}')
        sol_ex1_1.set_color_by_string('2', GREEN)
        sol_ex1_1.set_color_by_string('\\frac{\\pi}{3}', swGOLD)

        ex1_content = VGroup(sol_ex1_0, sol_ex1_1)
        example1_rect.set_title(ex1_title)
        example1_rect.create_content(ex1_content, offset=0.15)

        # Smaller rectangle for the complex logarithm function, positioned on the right
        complex_log_rect = swRoundedRectangle(height=1.0, width=2).shift(RIGHT * 1.15 + UP * 0.5)  # Increased height
        complex_log_title = TNT().txt("Complex logarithm function", color=PINK, weight="SEMIBOLD")
        complex_log_rect.set_title(complex_log_title, remove_line=True)

        complex_log_line1 = TNT().tx('z=r\\cdot\\mathrm{e}^{\\varphi \\cdot \\mathrm{i}}')
        complex_log_line1.set_color_by_string('r', GREEN)
        complex_log_line1.set_color_by_string('\\varphi', swGOLD)
        complex_log_line1.set_color_by_string('z', BLUE)

        complex_log_line2 = TNT().tx('\\ln(z) = \\ln(r) + \\varphi \\cdot \\mathrm{i}')
        complex_log_line2.set_color_by_string('r', GREEN)
        complex_log_line2.set_color_by_string('\\varphi', swGOLD)
        complex_log_line2.set_color_by_string('z', BLUE)

        # New line showing bounds
        complex_log_line3 = TNT().tx('-\\pi < \\varphi \\leq \\pi')
        complex_log_line3.set_color_by_string('\\varphi', swGOLD)

        complex_log_content = VGroup(complex_log_line1, complex_log_line2, complex_log_line3)
        complex_log_rect.create_content(complex_log_content, offset=0.075)


        # Example 2
        example2_rect = swRoundedRectangle(height=2, width=2.2).shift(LEFT * 1.05)
        ex2_title = TNT().txt('Let ').tx('z=6\\cdot \\mathrm{e}^{\\frac{7\\cdot\\pi}{5}\\cdot \\mathrm{i}}, ').txt('calculate ').tx('\\ln(z)')
        ex2_title.set_color_by_string('z', BLUE)
        ex2_title.set_color_by_string('6', GREEN)
        ex2_title.set_color_by_string('\\frac{7\\cdot\\pi}{5}', swGOLD)

        sol_ex2_0 = TNT().tx('z=6\\cdot \\mathrm{e}^{\\frac{7\\cdot\\pi}{5}\\cdot \\mathrm{i}}')
        sol_ex2_0.set_color_by_string('z', BLUE)
        sol_ex2_0.set_color_by_string('6', GREEN)
        sol_ex2_0.set_color_by_string('\\frac{7\\cdot\\pi}{5}', swGOLD)
        
        sol_ex2_1 = TNT().tx('z=6\\cdot \\mathrm{e}^{-\\frac{3\\cdot\\pi}{5}\\cdot \\mathrm{i}}')
        sol_ex2_1.set_color_by_string('z', BLUE)
        sol_ex2_1.set_color_by_string('6', GREEN)
        sol_ex2_1.set_color_by_string('-\\frac{3\\cdot\\pi}{5}', swGOLD)
        
        sol_ex2_2 = TNT().tx('\\ln(z)=\\ln(6\\cdot \\mathrm{e}^{-\\frac{3\\cdot\\pi}{5}\\cdot \\mathrm{i}})')
        sol_ex2_2.set_color_by_string('z', BLUE)
        sol_ex2_2.set_color_by_string('6', GREEN)
        sol_ex2_2.set_color_by_string('-\\frac{3\\cdot\\pi}{5}', swGOLD)

        sol_ex2_3 = TNT().tx('=\\ln(6) - \\dfrac{3\\cdot\\pi}{5}\\cdot \\mathrm{i}')
        sol_ex2_3.set_color_by_string('6', GREEN)
        sol_ex2_3.set_color_by_string('-\\frac{3\\cdot\\pi}{5}', swGOLD)

        ex2_content = VGroup(sol_ex2_0, sol_ex2_2, sol_ex2_3)
        example2_rect.set_title(ex2_title)
        example2_rect.create_content(ex2_content, offset=0.15)
        sol_ex2_1.move_to(sol_ex2_0.get_center())

        # Computational Properties
        theory_rect = swRoundedRectangle(height=1.2, width=2)
        theory_title = TNT().txt("Computational properties", color=PINK, weight="SEMIBOLD")
        prop1 = TNT().tx('\\ln(z_1\\cdot z_2)=\\ln(z_1)+\\ln(z_2)')
        prop1.set_color_by_string('z_1', BLUE)
        prop1.set_color_by_string('z_2', BLUE)

        prop2 = TNT().tx('\\ln(z^n)=n\\cdot\\ln(z)')
        prop2.set_color_by_string('z', BLUE)

        prop3 = TNT().tx('\\mathrm{e}^{\\ln(z)}=\\ln(\\mathrm{e}^z)=z')
        prop3.set_color_by_string('z', BLUE)

        theory_rect.set_title(theory_title, remove_line=True)
        theory_content = VGroup(prop1, prop2, prop3)
        theory_rect.create_content(theory_content, offset=0.075)

        ## ANIMATIONS ##
        self.add(logo)
        self.wait(1)
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL) + 0.15 * UP + 0.35 * RIGHT).scale(0.009 / 0.03))

        # Display Title
        with self.voiceover(text="This video shows how to calculate a complex logarithm.") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        # Example 1
        with self.voiceover(text="Let's begin by calculating the natural logarithm of a complex number. We have z is equal to 2 times e to the power of pi over 3 times i.") as tracker:
            self.play(Create(example1_rect))

        with self.voiceover(text="First, we write ellen of z equals ellen of 2 times e to the power of pi over 3 times i.") as tracker:
            self.play(swWrite(sol_ex1_0))

        # Show support box with complex logarithm function
        with self.voiceover(text="We can define the complex natural logarithm as follows") as tracker:
            self.play(Create(complex_log_rect))

        with self.voiceover(text="If we take 'z' equal to a complex number in polar exponential form, 'z' equals the norm 'r' times 'e' to the power of the principal value phi times 'i'.") as tracker:
            self.play(swWrite(complex_log_line1))

        with self.voiceover(text="Then the ellen of z equals ellen of r plus phi times i") as tracker:
            self.play(swWrite(complex_log_line2))   

        with self.voiceover(text="This function is only defined for complex numbers whose angle is the principal value, which means that the angle of 'z' needs to be greater than minus pi and less than or equal to pi. If this is not the case, we must rewrite 'z'") as tracker:
            self.play(swWrite(complex_log_line3))
        
        # Continue with the main example now that the supporting idea has been shown
        with self.voiceover(text="As the angle of our example 'z' is already the principal value, we can directly apply the formula, giving us ellen of 2, plus pi over 3 times i. This is the solution.") as tracker:
            self.play(swWrite(sol_ex1_1))

        self.wait(1)
        self.play(FadeOut(VGroup(example1_rect, ex1_content)))

        # Example 2
        with self.voiceover(text="Now, we will calculate the natural logarithm for the complex number z equals 6 times e to the power of 7 times pi over 5 times i. Note that this complex number has an angle outside of the principal value range.") as tracker:
            self.play(Create(example2_rect))

        with self.voiceover(text="First, write z as 6 times e to the power of 7 times pi over 5 times i.") as tracker:
            self.play(swWrite(sol_ex2_0))


        with self.voiceover(text="Since the argument is not in the principal value range, we have to rewrite 'z' such that the angle is in the proper range. We can do this by adding or subtracting increments of 2 times pi.") as tracker:
            pass

        with self.voiceover(text="In this case, we can subtract 2 times pi from the angle to get a new angle of minus 3 times pi over 5.") as tracker:
            # Swapping to 'z' with corrected angle
            self.play(TransformMatchingShapes(sol_ex2_0, sol_ex2_1))

        with self.voiceover(text="Now we write ellen of the adjusted 'z', which is equal to ellen of 6 minus 3 times pi over 5 times i.") as tracker:
            self.play(swWrite(sol_ex2_2))

        with self.voiceover(text="Finally, we can apply the complex logarithm function to get the result.") as tracker:
            self.play(swWrite(sol_ex2_3))


        self.wait(1)
        self.play(FadeOut(VGroup(example2_rect, ex2_content.remove(sol_ex2_0).add(sol_ex2_1), complex_log_rect, complex_log_content)))

        # Show properties
        with self.voiceover(text="Finally, let's conclude with some important computational properties of the complex logarithm. These properties are the same when applying the logarithm on a real number.") as tracker:
            self.play(Create(theory_rect))
        
        with self.voiceover(text="When z1 and z2 are complex numbers, the logarithm of z1 times z2 is equal to the logarithm of z1 plus the logarithm of z2.") as tracker:
            self.play(swWrite(prop1))
        
        with self.voiceover(text="The logarithm of a complex number 'z' to the power of a number 'n', is equal to 'n' times the logarithm of 'z'.") as tracker:
            self.play(swWrite(prop2))
        
        with self.voiceover(text="And finally, e raised to the power of the logarithm of 'z' is equal to the logarithm of e to the power of 'z', and this is equal to 'z'.") as tracker:
            self.play(swWrite(prop3))
        
        with self.voiceover(text="This concludes the explaination of the complex logarithm. Thanks for watching.") as tracker:
            self.wait(1)

        self.wait(2)

        # Fade out all objects
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)