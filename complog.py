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
        
        ## Logo
        logo = ImageMobject('./Sowiso-logo-primary.png').scale(0.03)

        ## Title
        title = Text("""The complex logarithm""", font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'logarithm':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)


        ### ANIMATIONS ###
        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))
        self.play(swWrite(title))

        return
    
        self.play(FadeOut(title))
        self.wait(1)


        # with self.voiceover(text="This concludes the examples. Thanks for watching") as tracker:
        #     self.wait(tracker.duration)
    
        # fade out everything still on the screen
        self.wait(2)

        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)