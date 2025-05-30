from manim import *
from lib import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

class MainScene(MovingCameraScene, VoiceoverScene):

    def construct(self):
        # Setting up the voiceover scene
        self.create_subcaption = False

        self.camera.background_color = BLUEISHGREY

        self.set_speech_service(
            OpenAIService(
                voice="alloy",
                model="gpt-4o-mini-tts",
            )
        )

        ## Title Part with Logo ##
        logo = ImageMobject('../Sowiso-logo-primary.png').scale(0.03)
        title = Text("The complex exponential function", font='Quicksand', color=PURPLE, weight="SEMIBOLD").scale(0.25)
        title.move_to(ORIGIN)

        self.add(logo)
        self.wait(1)
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL) + 0.15 * UP + 0.35 * RIGHT).scale(0.009 / 0.03))

        with self.voiceover(text="This video shows how to calculate a complex exponential.") as tracker:
            self.play(swWrite(title))
        
        self.wait(1)
        self.play(FadeOut(title))

        ## Mobjects Part ##
        
        # Main rectangle, positioned on the left
        main_box = swRoundedRectangle(height=2, width=2.2).shift(LEFT * 1.05)
        main_box_title = TNT().txt("Given ").tx('z = 3 + \\frac{\\pi}{4} \\cdot \\mathrm{i},').txt(" calculate ").tx('\\mathrm{e}^z')
        main_box.set_title(main_box_title)

        main_box_title.set_color_by_string('z', BLUE)
        main_box_title.set_color_by_string('3', GREEN)
        main_box_title.set_color_by_string('\\frac{\\pi}{4}', swGOLD)

        # Lines for the main box
        main_step1 = TNT().tx('\\mathrm{e}^z = \\mathrm{e}^{3 + \\frac{\\pi}{4} \\cdot \\mathrm{i}}')
        main_step1.set_color_by_string('z', BLUE)
        main_step1.set_color_by_string('3', GREEN)
        main_step1.set_color_by_string('\\frac{\\pi}{4}', swGOLD)

        main_step3 = TNT().tx('= \\mathrm{e}^3 \\cdot (\\cos(\\frac{\\pi}{4}) + \\sin(\\frac{\\pi}{4}) \\cdot \\mathrm{i})')
        main_step3.set_color_by_string('3', GREEN)
        main_step3.set_color_by_string('\\frac{\\pi}{4}', swGOLD)

        main_step4 = TNT().tx('\\|\\mathrm{e}^z\\| = \\mathrm{e}^3')
        main_step4.set_color_by_string('z', BLUE)
        main_step4.set_color_by_string('3', GREEN)

        main_step5 = TNT().tx('\\text{Arg}(\\mathrm{e}^z) = \\frac{\\pi}{4}')
        main_step5.set_color_by_string('z', BLUE)
        main_step5.set_color_by_string('\\frac{\\pi}{4}', swGOLD)

        main_content = VGroup(main_step1, main_step3, main_step4, main_step5)
        main_box.create_content(main_content, offset=0.075)

        VGroup(main_step4, main_step5).shift(DOWN * 0.25)

        # Smaller rectangle for the complex exponential function, positioned on the right (upper)
        theory_box = swRoundedRectangle(height=0.8, width=2).shift(RIGHT * 1.15 + UP * 0.7)
        theory_title = TNT().txt("Complex exponential function", color=PINK, weight="SEMIBOLD")
        theory_box.set_title(theory_title, remove_line=True)

        theory_line = TNT().tx('\\mathrm{e}^{a + b \\cdot \\mathrm{i}} = \\mathrm{e}^a \\cdot (\\cos(b) + \\sin(b) \\cdot \\mathrm{i})')
        theory_line.set_color_by_string('a', GREEN)
        theory_line.set_color_by_string('b', swGOLD)

        theory_box_content = VGroup(theory_line)
        theory_box.create_content(theory_box_content, offset=0.075)

        # Smaller rectangle for computational properties, positioned on the right (lower)
        properties_box = swRoundedRectangle(height=1.2, width=2).shift(RIGHT * 1.15 + DOWN * 0.5)
        properties_title = TNT().txt("Computational properties", color=PINK, weight="SEMIBOLD")
        properties_box.set_title(properties_title, remove_line=True)

        # Lines for the properties box
        prop1 = TNT().tx('\\mathrm{e}^0 = 1')
        prop1.set_color_by_string('0', BLUE)
        
        prop2 = TNT().tx('\\mathrm{e}^z \\cdot \\mathrm{e}^w = \\mathrm{e}^{z + w}')
        prop2.set_color_by_string('z', BLUE)
        prop2.set_color_by_string('w', swPURPLE)
        
        prop3 = TNT().tx('\\frac{\\mathrm{e}^z}{\\mathrm{e}^w} = \\mathrm{e}^{z - w}')
        prop3.set_color_by_string('z', BLUE)
        prop3.set_color_by_string('w', swPURPLE)
        
        prop4 = TNT().tx('(\\mathrm{e}^z)^n = \\mathrm{e}^{z \\cdot n}')
        prop4.set_color_by_string('z', BLUE)
        
        prop5 = TNT().tx('\\overline{\\mathrm{e}^z} = \\mathrm{e}^{\\bar{z}}')
        prop5.set_color_by_string('z', BLUE)

        properties_box_content = VGroup(prop1, prop2, prop3, prop4, prop5)
        properties_box.create_content(properties_box_content, offset=0.09)

        # Shift all content lines upward in the computational properties box
        for prop in properties_box_content:
            prop.shift(UP * 0.11)
        prop4.shift(DOWN * 0.04)

        ## Animations Part ##
        
        # Animate the main box and its contents
        with self.voiceover(text="Given the complex number 'z' equals 3 plus pi over 4 times i, we will calculate 'e' to the power of 'z'.") as tracker:
            self.play(Create(main_box))

        with self.voiceover(text="We start with the expression 'e' to the power of 'z' is equal to 'e' to the power of 3 plus pi over 4 times i.") as tracker:
            self.play(swWrite(main_step1))

        # Show theory box first
        with self.voiceover(text="Now we can look at the definition of the complex exponential function.") as tracker:
            self.play(Create(theory_box))
        
        with self.voiceover(text="This function is defined as 'e' to the power of a plus b times i is equal to 'e' to the power of a multiplied by the sum of cosine of b plus sine of b times i.") as tracker:
            self.play(swWrite(theory_line))

        # Return back to apply the formula directly
        with self.voiceover(text="Applying the formula directly, we see that the expression is equal to 'e' to the power of 3 multiplied by the sum of cosine of pi over 4 plus the sine of pi over 4 times 'i'. We can recognize this expression as the polar form of 'e' to the power of 'z'.") as tracker:
            self.play(swWrite(main_step3))

        with self.voiceover(text="To clarify, we see that the norm of 'e' to the power of 'z' equals 'e' to the power of 3.") as tracker:
            self.play(swWrite(main_step4))

        with self.voiceover(text="And the angle of 'e' to the power of 'z' is pi over 4.") as tracker:
            self.play(swWrite(main_step5))

        with self.voiceover(text="It is important to point out that the real part of 'z' only affects the norm of 'e' to the power of 'z', while the imaginary part only affects the angle of 'e' to the power of 'z'.") as tracker:
            self.wait(0.5)
        
        # Present computational properties box
        with self.voiceover(text="Finally, let's consider some computational properties of the complex exponential.") as tracker:
            self.play(Create(properties_box))

        with self.voiceover(text="'e' to the power of zero is one.") as tracker:
            self.play(swWrite(prop1))

        with self.voiceover(text="'e' to the power of 'z' times 'e' to the power of 'w' equals 'e' to the power of 'z' plus 'w'.") as tracker:
            self.play(swWrite(prop2))

        with self.voiceover(text="'e' to the power of 'z' divided by 'e' to the power of 'w' equals 'e' to the power of 'z' minus 'w'.") as tracker:
            self.play(swWrite(prop3))

        with self.voiceover(text="Raising 'e' to the power of 'z' to the power of n results in 'e' to the power of 'z' times n.") as tracker:
            self.play(swWrite(prop4))

        with self.voiceover(text="And finally, the conjugate of 'e' to the power of 'z' equals 'e' to the power of the conjugate of 'z'.") as tracker:
            self.play(swWrite(prop5))

        ## Outro Voiceover ##
        with self.voiceover(text="This concludes the complex exponential function. Thanks for watching.") as tracker:
            self.wait(1)

        # Fadeout
        self.wait(2)
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)