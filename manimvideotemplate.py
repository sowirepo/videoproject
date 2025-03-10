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
        title = Text(""" TITLE HERE """, font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'quotient':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)

        ## Logo
        logo = ImageMobject('./Sowiso-logo-primary.png')
        logo.move_to(self.camera.frame.get_corner(DL)).shift(0.15*UP + 0.35*RIGHT)
        logo.scale(0.009)

        ### ANIMATIONS ###
        self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        self.add(logo)