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
        
        ## Logo
        logo = ImageMobject('../Sowiso-logo-primary.png').scale(0.03)

        ## Title
        title = Text("""Converting units""", font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'HIGHLIGHTED TEXT':PINK},
                        line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)


        ## SCENE 1 mobjects ##
        # main box with question title
        main_box = swRoundedRectangle(height=2, width=3.4)
        main_box_title = TNT().txt("You’re driving on the highway with").tx("100 \\dfrac{\\text{km}}{\\text{h}},").txt("what is that in").tx("\\dfrac{\\text{m}}{\\text{s}}?", aligned_char='?')
        main_box.set_title(main_box_title)
        
        # step-by-step unit conversion
        line1 = TNT().tx("100 \\cdot \\dfrac{1000\\;\\text{m}}{\\text{h}}")
        line2 = TNT().tx("=100 \\cdot 1000 \\cdot \\dfrac{1\\;\\text{m}}{3600 \\;\\text{s}}")
        # keeping units as separate fractions after each numeric fraction
        line3 = TNT().tx("=\\dfrac{100000}{3600} \\dfrac{\\text{m}}{\\text{s}} = \\dfrac{250}{9} \\dfrac{\\text{m}}{\\text{s}} \\approx 27.78 \\dfrac{\\text{m}}{\\text{s}}")  

        
        rect_content = VGroup(line1, line2, line3)
        main_box.create_content(rect_content, offset=0.175)

        ## SCENE 2 mobjects ##
        acc_box = swRoundedRectangle(height=2, width=3.6)
        acc_box_title = (
            TNT()
            .txt("A cheetah can accelerate with approximately")
            .tx("10.5 \\dfrac{\\text{m}}{\\text{s}^2},")
            .txt("what is that in")
            .tx("\\dfrac{\\text{km}}{\\text{h}^2}?", aligned_char='?')
        )
        acc_box.set_title(acc_box_title)
        
        # drop acc_line1
        acc_line2 = TNT().tx("10.5 \\cdot \\dfrac{\\frac{1}{1000}\\;\\text{km}}{\\text{s}^2}")
        acc_line3 = TNT().tx("10.5 \\cdot \\dfrac{1}{1000} \\cdot \\dfrac{\\text{km}}{\\frac{1}{3600^2}\\text{h}^2}")
        acc_line4 = TNT().tx("\\dfrac{10.5\\cdot 12960000}{1000 }\\dfrac{\\text{km}}{\\text{h}^2} = 136080\\dfrac{\\text{km}}{\\text{h}^2}")
        
        acc_content = VGroup(acc_line2, acc_line3, acc_line4)
        acc_box.create_content(acc_content, offset=0.15)


        ### ANIMATIONS ###

        ## Intro animations ##
        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))

        with self.voiceover(text="This video shows how to convert units") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        ## SCENE 1 animations ##
        # scene 1 animations
        with self.voiceover(text="here is our first question, converting one hundred kilometers per hour into meters per second") as tracker:
            self.play(Create(main_box))
        with self.voiceover(text="first we change kilometers to meters by multiplying one hundred by one thousand, giving one hundred thousand meters per hour") as tracker:
            self.play(swWrite(line1))
        with self.voiceover(text="next we convert hours to seconds, knowing one hour is three thousand six hundred seconds, so we divide by three thousand six hundred to get meters per second") as tracker:
            self.play(swWrite(line2))
        with self.voiceover(text="finally we simplify one hundred thousand over three thousand six hundred to two hundred fifty over nine, which is approximately twenty seven point seven eight meters per second") as tracker:
            self.play(swWrite(line3))

        # fade out scene 1 except logo
        scene1_objs = [m for m in self.mobjects if m is not logo]
        fadeout_scene1 = Group(*scene1_objs)
        self.play(FadeOut(fadeout_scene1))

        # scene 2 animations
        with self.voiceover(text="now our second question: convert a cheetah’s acceleration of ten point five meters per second squared into kilometers per hour squared") as tracker:
            self.play(Create(acc_box))
        with self.voiceover(text="first we change meters into kilometers by multiplying by one over one thousand, giving ten point five times one over one thousand kilometers per second squared") as tracker:
            self.play(swWrite(acc_line2))
        with self.voiceover(text="next we convert seconds squared to hours squared by multiplying by three thousand six hundred squared, so we multiply our previous result by three thousand six hundred squared to get kilometers per hour squared") as tracker:
            self.play(swWrite(acc_line3))
        with self.voiceover(text="finally we multiply and simplify to obtain one hundred thirty six thousand eighty kilometers per hour squared") as tracker:
            self.play(swWrite(acc_line4))

        # outro
        with self.voiceover(text="that concludes our unit conversion examples, thanks for watching") as tracker:
            self.wait(1)

        # hold for a moment then fade out everything
        self.wait(2)
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1) #make sure everything is gone before the video ends