from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
from manim_extensions import *

class TestDifferentWritingStyles(MovingCameraScene):
        
    def construct(self):

        self.camera.background_color = BLUEISHGREY

        text = Text("This is what is was", font="Quicksand", weight="NORMAL", color=BLACK)
        tex = Tex("$\\theta\\dfrac{\\sqrt{a}}{b}$", color=BLACK)
        
        text2 = Text("This is what it will be", font="Quicksand", weight="NORMAL", color=BLACK)
        tex2 = tex.copy()

        text3 = text.copy()
        tex3 = tex.copy()

        text.shift(UP + LEFT)
        tex.shift(UP + RIGHT * 4)

        text2.shift(DOWN + LEFT)
        tex2.shift(DOWN + RIGHT * 4)

        self.play(swWrite(text))
        self.play(swWrite(tex))

        self.play(Write(text2, lag_ratio=9999999, stroke_color=BLACK, stroke_width=1))
        self.play(Write(tex2,  lag_ratio=9999999, stroke_color=BLACK, stroke_width=1))

        print(text2[0])




        self.wait(1)

class Test2(VoiceoverScene):
    def construct(self):
        self.camera.background_color = BLUEISHGREY

        self.set_speech_service(
            OpenAIService(
                voice="alloy",
                model="tts-1-hd",
            )
        )

        tex = TNT().txt('We have that ').tx('z=\\dfrac{a+b\\sqrt{a+ba+}}{b\\arctan(\\dfrac{a+ba+}{b})}').shift(DOWN)

        tex.set_color_by_string(string='a+b', color=RED)



        # tex.set_color_by_string(string='z', color=BLUE)


        self.add(tex)

class Test(MovingCameraScene, VoiceoverScene):
    def construct(self):
        self.camera.background_color = BLUEISHGREY


        self.set_speech_service(
            OpenAIService(
                voice="alloy",
                model="tts-1-hd",
            )
        )

        s = '\\dfrac{a+b\\sqrt{a+ba+}}{a}'

        # tex = MathTex(s, color=BLACK, substrings_to_isolate=['a ', 'b']).set_color_by_tex_to_color_map({'a ': BLUE, 'b': GREEN})
        # tex.set_color_by_tex('a', color=RED)
        # tex.set_color_by_tex_to_color_map({
        #     'a+b': RED})
        tex = MathTex("\\dfrac{\\sqrt{c}+b}{a+b}", color=BLACK, substrings_to_isolate=['a+b']).set_color_by_tex_to_color_map({'a+b': BLUE}).shift(UP * 0.5).scale(0.2)


        self.add(tex)

        tex = TNT().tx(s).shift(DOWN * 0.1)
        tex.set_color_by_string(string='a', color=RED)
        self.add(tex)

        return

        ## Main Box
        main_rect = swRoundedRectangle(height=2, width=2.2).shift(LEFT * 1.05)
        main_title = TNT().txt("Let z = 2 + 3i, solve ln(z)")
        main_rect.set_title(main_title)

        main_line1 = TNT().txt("Step 1: Convert to Polar").tx("z = \\sqrt{13} \\cdot e^{i \\cdot \\arctan(3/2)}")
        main_line2 = TNT().txt("Step 2: Use ln(z)").tx("\\ln(z) = \\ln(\\sqrt{13}) + i \\cdot \\arctan(3/2)")
        main_line3 = TNT().txt("Final Answer").tx("ln(z) = \\frac{1}{2}\\ln(13) + i \\cdot \\theta")

        main_content = VGroup(main_line1, main_line2, main_line3)
        main_rect.create_content(main_content, offset=0.075)

        ## Smaller Box
        smaller_rect = swRoundedRectangle(height=1, width=2).shift(RIGHT * 1.15)
        smaller_title = TNT().txt("Polar Form", color=PINK, weight="SEMIBOLD")
        smaller_rect.set_title(smaller_title, remove_line=True)

        smaller_line1 = TNT().tx("\\text{Norm} = \\sqrt{2^2 + 3^2} = \\sqrt{13}")
        smaller_line2 = TNT().tx("\\text{Arg} = \\arctan(3/2)")
        
        smaller_content = VGroup(smaller_line1, smaller_line2)
        smaller_rect.create_content(smaller_content, offset=0.075)

        ### Animations Part

        with self.voiceover(text="Let's solve for the logarithm of a complex number.") as tracker:
            self.play(Create(main_rect))

        with self.voiceover(text="First, we need to convert the complex number to its polar form.") as tracker:
            self.play(Create(smaller_rect))

        with self.voiceover(text="We calculate the norm using the square root of the sum of squares, two squared plus three squared.") as tracker:
            self.play(swWrite(smaller_line1))

        with self.voiceover(text="Next, find the argument using arctangent.") as tracker:
            self.play(swWrite(smaller_line2))

        with self.voiceover(text="Returning to the main problem, express z in polar form.") as tracker:
            self.play(swWrite(main_line1))

        with self.voiceover(text="Now, let's apply the properties of logarithms to express ln(z).") as tracker:
            self.play(swWrite(main_line2))

        with self.voiceover(text="Finally, this gives us the solution for the logarithm of the complex number.") as tracker:
            self.play(swWrite(main_line3))

        with self.voiceover(text="This is how you use polar form to compute the logarithm of a complex number.") as tracker:
            self.wait(1)

