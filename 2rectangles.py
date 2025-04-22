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

        ## DOUBLE swRoundedRectangle Example ##
        # Code for the double swROundedRectangle comes here
        
        rect = swRoundedRectangle(
            height=2,
            width=2.2,
        ).shift(LEFT * 1.05)
        rect_title = TNT().txt('Problem statement').tx('equation to solve in tex')
        rect.set_title(rect_title)

        line1 = TNT().txt('Derivation line 1').tx('some tex')
        line2 = TNT().tx('Derivation line 2, using theory box 1').tx('some tex')
        line3 = TNT().txt('Derivation line 3, using theory box 2').txt('some text')

        rect_content = VGroup(line1, line2, line3)
        rect.create_content(rect_content, offset=0.075)

        # first theory formula / additional information necessary for the solving of an equation or for clarity of an explaination
        formula_rect = swRoundedRectangle(
            height=0.8,
            width=2,
        ).shift(RIGHT * 1.15 +UP*0.5)
        formula_rect_title = TNT().txt('Formula title', weight="SEMIBOLD", color=PINK)
        formula_rect.set_title(formula_rect_title, remove_line=True)

        formula_line1 = TNT().tx('Formula in tex')
        formula_line2 = TNT().tx('another formula in tex')

        formula_rect_content = VGroup(formula_line1, formula_line2)
        formula_rect.create_content(formula_rect_content, offset=0.075)

        # potential second theory box
        second_formula_rect = swRoundedRectangle(
            height=0.8,
            width=2,
        ).shift(RIGHT * 1.15 + DOWN*0.5)
        second_formula_rect_title = TNT().txt('Some other formula', weight="SEMIBOLD", color=PINK)
        second_formula_rect.set_title(second_formula_rect_title, remove_line=True)

        second_formula_line1 = TNT().tx('another formula in tex')
        second_formula_line2 = TNT().tx('another formula in tex')

        second_formula_rect_content = VGroup(second_formula_line1, second_formula_line2)
        second_formula_rect.create_content(second_formula_rect_content, offset=0.075)


        ### ANIMATIONS ###

        ## The corresponding animations for the double roundedrectangles ##

        with self.voiceover(text="This voiceover presents the problem statement of the rectangle") as tracker:
            self.play(Create(rect))

        with self.voiceover(text="Explaining the first line of the derivation") as tracker:
            self.play(swWrite(line1))

        # if the second line of the derivation needs the first bit of theory, we present it such that the derivation can use it
        
        # start theory block 1
        with self.voiceover(text='Now we can look at this formula') as tracker:
            self.play(Create(formula_rect))
            
        with self.voiceover(text="Explaining the first line") as tracker:
            self.play(swWrite(formula_line1))

        with self.voiceover(text="Explaining the second line") as tracker:
            self.play(swWrite(formula_line2))
        # end theory block 1

        with self.voiceover(text="Explaining the second line of the derivation") as tracker:
            self.play(swWrite(line2))

        
        
        # if the third line of the derivation needs the second bit of theory, we present it such that the derivation can use it
        
        # start theory block 2
        with self.voiceover(text='Now we can look at this formula') as tracker:
            self.play(Create(second_formula_rect))
            
        with self.voiceover(text="Explaining the first line") as tracker:
            self.play(swWrite(second_formula_line1))

        with self.voiceover(text="Explaining the second line") as tracker:
            self.play(swWrite(second_formula_line2))
        # end theory block 2


        with self.voiceover(text="Explaining the third line of the derivation") as tracker:
            self.play(swWrite(line3))

