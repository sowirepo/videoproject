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

        with self.voiceover(text="this is the letter phy. Phy equals the angle. This is Phy."):
            self.play(Create(VGroup()))