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
        main_box_title = TNT().txt("You’re driving on the highway with 100 km/h, what is that in m/s?")
        main_box.set_title(main_box_title)
        
        # step-by-step unit conversion
        line1 = TNT().tx("100 \\cdot 1000 \\dfrac{m}{h}")
        line2 = TNT().tx("100 \\cdot 1000 \\cdot \\dfrac{1}{3600} \\dfrac{m}{s}")
        line3 = TNT().tx("\\dfrac{100000}{3600} \\dfrac{m}{s} = \\dfrac{250}{9} \\dfrac{m}{s} \\approx 27.78 \\dfrac{m}{s}")
        
        rect_content = VGroup(line1, line2, line3)
        main_box.create_content(rect_content, offset=0.175)

        ## SCENE 2 mobjects ##
        acc_box = swRoundedRectangle(height=2, width=3.4)
        acc_box_title = (
            TNT()
            .txt("a cheetah can accelerate with approximately")
            .tx("10.5 \\dfrac{m}{s^2},")
            .txt("what is that in")
            .tx("\\dfrac{km}{h^2}")
            .txt("?")
        )
        acc_box.set_title(acc_box_title)
        
        # drop acc_line1
        acc_line2 = TNT().tx("10.5 \\cdot \\dfrac{1}{1000} \\dfrac{km}{s^2}")
        acc_line3 = TNT().tx("10.5\\cdot \\dfrac{1}{1000} \\cdot 3600^2 \\dfrac{km}{h^2}")
        acc_line4 = TNT().tx("= 136080 \\dfrac{km}{h^2}?", aligned_char="?")
        
        acc_content = VGroup(acc_line2, acc_line3, acc_line4)
        acc_box.create_content(acc_content, offset=0.15)


        ### ANIMATIONS ###

        ## Intro animations ##
        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))

        with self.voiceover(text="Video title voiceover placeholder") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        ## SCENE 1 animations ##
        with self.voiceover(text="now we show the question box asking to convert 100 kilometers per hour to meters per second") as tracker:
            self.play(Create(main_box))
        
        with self.voiceover(text="first we convert kilometers into meters: we multiply one hundred by one thousand, yielding 100 \\cdot 1000 \\dfrac{m}{h}") as tracker:
            self.play(swWrite(line1))
        
        with self.voiceover(text="next we change hours into seconds: one hour equals three thousand six hundred seconds, so we multiply by \\dfrac{1}{3600}, giving 100 \\cdot 1000 \\cdot \\dfrac{1}{3600} \\dfrac{m}{s}") as tracker:
            self.play(swWrite(line2))
        
        with self.voiceover(text="finally we simplify the fraction \\dfrac{100000}{3600} \\dfrac{m}{s} to \\dfrac{250}{9} \\dfrac{m}{s} and approximate to 27.78 \\dfrac{m}{s}") as tracker:
            self.play(swWrite(line3))

        # fade out everything except logo before scene 2
        scene1_objs = [m for m in self.mobjects if m is not logo]
        fadeout_scene1 = Group(*scene1_objs)
        self.play(FadeOut(fadeout_scene1))

        ## SCENE 2 animations ##
        with self.voiceover(text="now we show the question box asking to convert a cheetah’s acceleration from meters per second squared to kilometers per hour squared") as tracker: 
            self.play(Create(acc_box))
        
        with self.voiceover(text="first we convert meters to kilometers by multiplying by \\dfrac{1}{1000}, giving 10.5 \\cdot \\dfrac{1}{1000} \\dfrac{km}{s^2}") as tracker:
            self.play(swWrite(acc_line2))
        
        with self.voiceover(text="then we convert seconds squared to hours squared by multiplying by 3600 squared, giving \\dfrac{10.5}{1000} \\cdot 3600^2 \\dfrac{km}{h^2}") as tracker:
            self.play(swWrite(acc_line3))
        
        with self.voiceover(text="finally simplifying yields 136080 \\dfrac{km}{h^2}") as tracker:
            self.play(swWrite(acc_line4))

        ## Outro ##
        with self.voiceover(text="This concludes the examples. Thanks for watching") as tracker:
            self.wait(1)
    
        # time to let everthing sink in
        self.wait(2)

        # fade out everything still on the screen
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1) # make sure everything is gone before the video ends