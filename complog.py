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
        
        ## MOBJECTS ##
        # Title
        title = Text("Calculating the complex logarithm", font='Quicksand', color=PURPLE, weight="SEMIBOLD", line_spacing=0.2).scale(0.25).move_to(ORIGIN)

        # Logo
        logo = ImageMobject('./Sowiso-logo-primary.png').scale(0.03)

        # Example 1
        example1_rect = swRoundedRectangle(height=2, width=2.5)
        ex1_title = TNT().txt('Let ').tx('z=2\\cdot e^{\\frac{\\pi}{3}\\cdot i}, ').txt('calculate ').tx('\\ln(z)')
        ex1_title.set_color_by_string('z', BLUE)

        sol_ex1_0 = TNT().tx('\\ln(z)=\\ln\\left(2\\cdot e^{\\frac{\\pi}{3}\\cdot i}\\right)')
        sol_ex1_0.set_color_by_string('z', BLUE)
        sol_ex1_1 = TNT().tx('=\\ln(2)+ \\ln\\left(e^{\\frac{\\pi}{3}\\cdot i}\\right)')
        sol_ex1_2 = TNT().tx('=\\ln(2)+ \\dfrac{\\pi}{3}\\cdot i')

        ex1_content = VGroup(sol_ex1_0, sol_ex1_1, sol_ex1_2)
        example1_rect.set_title(ex1_title)
        example1_rect.create_content(ex1_content, offset=0.15)

        # Example 2
        example2_rect = swRoundedRectangle(height=2, width=2.5)
        ex2_title = TNT().txt('Let ').tx('z=6\\cdot e^{\\frac{7}{5}\\cdot\\pi\\cdot i}, ').txt('calculate ').tx('\\ln(z)')
        ex2_title.set_color_by_string('z', BLUE)

        sol_ex2_0 = TNT().tx('\\ln(z)=\\ln\\left(6\\cdot e^{\\frac{7}{5}\\cdot\\pi\\cdot i}\\right)')
        sol_ex2_0.set_color_by_string('z', BLUE)
        sol_ex2_1 = TNT().tx('=\\ln(6)+ \\ln\\left(e^{\\frac{7}{5}\\cdot\\pi\\cdot\\mathrm{i}}\\right)')
        sol_ex2_2 = TNT().tx('=\\ln(6)+ \\left(\\dfrac{7}{5}\\cdot\\pi - 2\\cdot\\pi\\right)\\cdot\\mathrm{i}')
        sol_ex2_3 = TNT().tx('=\\ln(6) - \\dfrac{3}{5}\\cdot\\pi\\cdot\\mathrm{i}')

        ex2_content = VGroup(sol_ex2_0, sol_ex2_1, sol_ex2_2, sol_ex2_3)
        example2_rect.set_title(ex2_title)
        example2_rect.create_content(ex2_content, offset=0.15)

        # Computational Properties
        theory_rect = swRoundedRectangle(height=1.2, width=2)
        theory_title = TNT().txt("Computational properties", color=PINK, weight="SEMIBOLD")
        prop1 = TNT().tx('\\ln(z_1\\cdot z_2)=\\ln(z_1)+\\ln(z_2)')
        prop1.set_color_by_string('z_1', BLUE)
        prop1.set_color_by_string('z_2', BLUE)

        prop2 = TNT().tx('\\ln(z^n)=n\\cdot\\ln(z)')
        prop2.set_color_by_string('z', BLUE)

        prop3 = TNT().tx('e^{\\ln(z)}=\\ln(e^z)=z')
        prop3.set_color_by_string('z', BLUE)

        theory_rect.set_title(theory_title, remove_line=True)
        theory_content = VGroup(prop1, prop2, prop3)
        theory_rect.create_content(theory_content, offset=0.075)

        ## ANIMATIONS ##
        self.add(logo)
        self.wait(1)
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))

        # Display Title
        with self.voiceover(text="In this video, we will explore how to calculate the complex logarithm.") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        # Example 1
        with self.voiceover(text="Let's begin by calculating the natural logarithm of a complex number. We have z equal to 2 times e raised to the pi over 3 times i.") as tracker:
            self.play(Create(example1_rect))

        with self.voiceover(text="First, write ln of z as ln of 2 times e raised to the pi over 3 times i.") as tracker:
            self.play(swWrite(sol_ex1_0))
        
        with self.voiceover(text="We can split this using the property of logarithm of a product.") as tracker:
            self.play(swWrite(sol_ex1_1))
        
        with self.voiceover(text="This becomes ln of 2 plus pi over 3 times i.") as tracker:
            self.play(swWrite(sol_ex1_2))

        self.wait(1)
        self.play(FadeOut(VGroup(example1_rect, ex1_content)))

        # Example 2
        with self.voiceover(text="Now, we will calculate the natural logarithm for a complex number z equals 6 times e raised to 7/5 times pi times i.") as tracker:
            self.play(Create(example2_rect))

        with self.voiceover(text="First, write ln of z as ln of 6 times e raised to 7/5 times pi times i.") as tracker:
            self.play(swWrite(sol_ex2_0))
        
        with self.voiceover(text="Split this using the product property of logarithms.") as tracker:
            self.play(swWrite(sol_ex2_1))
        
        with self.voiceover(text="The principal value range for the argument is from minus pi to pi. Subtract 2 pi times i to bring it within this range.") as tracker:
            self.play(swWrite(sol_ex2_2))
        
        with self.voiceover(text="This simplifies to ln of 6 minus 3/5 times pi times i.") as tracker:
            self.play(swWrite(sol_ex2_3))

        self.wait(1)
        self.play(FadeOut(VGroup(example2_rect, ex2_content)))

        # Show properties
        with self.voiceover(text="Finally, let's conclude with some important computational properties of the complex logarithm. These properties are the same when applying the logarithm on a real number.") as tracker:
            self.play(Create(theory_rect))
        
        with self.voiceover(text="When z1 and z2 are complex numbers, the logarithm of a product is equal to the sum of the logarithms.") as tracker:
            self.play(swWrite(prop1))
        
        with self.voiceover(text="If 'z' is a complex number, then the logarithm of a number raised to a power is equal to the exponent times the log of the base.") as tracker:
            self.play(swWrite(prop2))
        
        with self.voiceover(text="Furthermore, e raised to the log of 'z' or the log of e raised to 'z', where 'z' is a complex number, is equal to 'z'.") as tracker:
            self.play(swWrite(prop3))
        
        with self.voiceover(text="This concludes our exploration of the complex logarithm. Thank you for watching.") as tracker:
            self.wait(1)

        self.wait(2)

        # Fade out all objects
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)