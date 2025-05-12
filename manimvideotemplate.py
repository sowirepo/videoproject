from manim import *
from manim_extensions import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

class MainScene(MovingCameraScene, VoiceoverScene):

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
        title = Text(""" TITLE HERE """, font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'HIGHLIGHTED TEXT':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)


        ## SCENE 1 mobjects ##



        ### ANIMATIONS ###
        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))

        with self.voiceover(text="Video title voiceover placeholder") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        ## SCENE 1 animations ##



        ## Outro ##
        with self.voiceover(text="This concludes the examples. Thanks for watching") as tracker:
            self.wait(1)
    
        self.wait(2)

        # fade out everything still on the screen
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)