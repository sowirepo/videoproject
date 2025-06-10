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
        title = Text("""Significant figures""",
                     font='Quicksand',
                     color=PURPLE,
                     weight="SEMIBOLD",
                     t2c={'HIGHLIGHTED TEXT':PINK},
                     line_spacing=0.2).scale(0.25)
        title.move_to(ORIGIN)

        ## SCENE 1 mobjects ##
        # main box on the left (smaller)
        main_box = swRoundedRectangle(
            height=2, 
            width=2.2
        ).shift(LEFT * 1.05)

        main_title = TNT().txt("Significant figures", weight="SEMIBOLD", color=PINK)
        main_box.set_title(main_title)

        # content lines: 4 intros + 4 rules
        intro1a = TNT().txt("Precision of the tool")
        intro1b = TNT().txt("limits how many digits you can record.")
        # explain that you can’t know the final digit exactly
        intro2a = TNT().txt("The last digit cannot be measured exactly")
        # so you have to treat it as an estimate
        intro2b = TNT().txt("and must therefore be estimated.")

        rule1 = TNT().txt("count digits from left to right")
        rule2 = TNT().txt("non-zero digits are significant")
        rule3 = TNT().txt("zeros between digits are significant")
        rule4 = TNT().txt("leading zeros are not significant")
        rule5 = TNT().txt("trailing zeros in decimals are significant")

        # clear & recreate the content group
        main_box.create_content(
            VGroup(intro1a, intro1b, intro2a, intro2b,
                rule1, rule2, rule3, rule4, rule5),
            offset=0.05, align='left'
        )
        # shift every rule down a bit
        for rule in (rule1, rule2, rule3, rule4, rule5):
            rule.shift(DOWN * 0.1)

        # smaller box on the right for examples
        ex_box = swRoundedRectangle(
            height=1.2,
            width=2
        ).shift(RIGHT * 1.15)
        ex_title = TNT().txt("Examples", weight="SEMIBOLD", color=PINK)
        ex_box.set_title(ex_title)

        ex1 = TNT().tx("0.004560\\ \\mathrm{cm}")
        ex2 = TNT().tx("1.0320\\ \\mathrm{cm}")
        ex3 = TNT().tx("1500\\ \\mathrm{cm}")
        ex3sn = TNT().tx("1.500\\times 10^3 \\mathrm{cm}")

        ex_box.create_content(
            VGroup(ex1, ex2, ex3),
            offset=0.05, align='center'
        )

        ex3sn.move_to(ex3.get_center())

        ### ANIMATIONS ###

        ## Intro animations ##
        self.add(logo)
        self.wait(1)
        
        self.play(
            logo.animate.move_to(
                self.camera.frame.get_corner(DL)
                + 0.15 * UP 
                + 0.35 * RIGHT
            ).scale(0.009 / 0.03)
        )

        with self.voiceover(text="This video shows how to work with significant figures") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)
        
        ## SCENE 1 animations ##

        with self.voiceover(text="let’s begin with the theory for significant figures") as tracker:
            self.play(Create(main_box))

        with self.voiceover(text="When doing measurements, the precision of your tool limits how many digits you can record") as tracker:
            self.play(swWrite(intro1a))
            self.play(swWrite(intro1b))
        with self.voiceover(text="this means the last digit cannot be measured exactly and must therefore be estimated") as tracker:
            self.play(swWrite(intro2a))
            self.play(swWrite(intro2b))

        # then continue with the four rule voice-overs as before...
        with self.voiceover(text="now here are five core rules of counting significant figures") as tracker:
            pass

        with self.voiceover(text="rule one: in order to determine the number of significant digits in a value, start with the first measured value at the left and count the number of digits through the last digit written on the right.") as tracker:
            self.play(swWrite(rule1))

        with self.voiceover(text="rule two: every non-zero digit counts as significant.") as tracker:
            self.play(swWrite(rule2))

        with self.voiceover(text="rule three: any zero between significant digits also counts.") as tracker:
            self.play(swWrite(rule3))

        with self.voiceover(text="rule four: leading zeros do not count. they are mere placeholders to locate the decimal point.") as tracker:
            self.play(swWrite(rule4))

        with self.voiceover(text="rule five: trailing zeros in the decimal part are significant.") as tracker:
            self.play(swWrite(rule5))

        with self.voiceover(text="now let’s look at three measured values and count their significant figures.") as tracker:
            self.play(Create(ex_box))

        with self.voiceover(text="let's say we have measured zero point zero zero four five six zero centimeters. This number has four significant figures, since the first three zeroes only serve as placekeepers that locate the decimal point.") as tracker:
            self.play(swWrite(ex1))
        with self.voiceover(text="The measurement value one point zero three two zero centimeters ends with a zero. This zero is the result of the measurement which means this number has five significant figures.") as tracker:
            self.play(swWrite(ex2))
        with self.voiceover(text="Finally, we look at the measurement of fifteen hundred centimeters. without a decimal, this result is ambiguous. The zeroes may or may not be significant depending on style. They could be placeholders, or indicate known digits. This means that fifteenhundred could have two, three or four significant figures. To avoid this ambiguity, write it in scientific notation. For example, let's assume we actually measured fifteenhundred centimeters. This measurement has four significant figures.") as tracker:
            self.play(swWrite(ex3))

        with self.voiceover(text="To avoid ambiguity, this means we should write down the measurement as one point five zero zero times ten to the power of three.") as tracker:
            self.play(TransformMatchingShapes(ex3, ex3sn))

        ## Outro ##
        with self.voiceover(text="this concludes the examples. thanks for watching") as tracker:
            self.wait(1)
    
        self.wait(2)
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)
