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

        ## Logo and Title ##
        logo = ImageMobject('../Sowiso-logo-primary.png').scale(0.03)
        title = Text(
            """     Complex quadratic formula and \nthe fundamental theorem of algebra """,
            font='Quicksand',
            color=PURPLE,
            weight="SEMIBOLD",
            t2c={
                'fundamental theorem of algebra': PINK,
                'quadratic formula': PINK
            },
            line_spacing=0.2
        ).scale(0.25).move_to(ORIGIN)

        ## SCENE 1 mobjects ##
        # main problem box (larger)
        main_box = swRoundedRectangle(height=2, width=2.2).shift(LEFT * 1)
        main_box_title = TNT().txt("Calculate the roots of").tx("z^2+4\\cdot z+13")
        main_box.set_title(main_box_title)

        # main content lines
        main_line1 = TNT().tx("D=4^2-4\\cdot 1\\cdot 13")
        main_line2 = TNT().tx("=16-52=-36")
        main_line3 = TNT().tx("\\sqrt{D}=\\sqrt{-36}=6\\cdot\\mathrm{i}")
        main_line4 = TNT().tx("z_{1,2}=\\dfrac{-b\\pm\\sqrt{D}}{2\\cdot a}")
        main_line5 = TNT().tx("z_{1}=\\dfrac{-4+6\\cdot\\mathrm{i}}{2}=-2+3\\cdot\\mathrm{i}")
        main_line6 = TNT().tx("z_{2}=\\dfrac{-4-6\\cdot\\mathrm{i}}{2}=-2-3\\cdot\\mathrm{i}")

        main_content = VGroup(
            main_line1,
            main_line2,
            main_line3,
            main_line4,
            main_line5,
            main_line6
        )
        main_box.create_content(main_content, offset=0.075)

        # adjust deeper lines down for spacing
        main_line4.shift(DOWN * 0.15)
        main_line5.shift(DOWN * 0.25)
        main_line6.shift(DOWN * 0.25)

        # discriminant theory box on the right
        disc_box = swRoundedRectangle(height=0.8, width=1.8).shift(RIGHT * 1.15 + UP * 0.5)
        disc_title = TNT().txt("discriminant", weight="SEMIBOLD", color=PINK)
        disc_box.set_title(disc_title)
        disc_line1 = TNT().tx("D=b^2-4\\cdot a\\cdot c")
        disc_box.create_content(VGroup(disc_line1), offset=0.075)

        ### ANIMATIONS ###

        ## Intro ##
        self.add(logo)
        self.wait(1)
        self.play(
            logo.animate.move_to(
                self.camera.frame.get_corner(DL)
                + 0.15 * UP
                + 0.35 * RIGHT
            ).scale(0.009 / 0.03)
        )
        with self.voiceover(text="welcome. in this video we explore how to solve a quadratic equation with complex roots, and connect it to the fundamental theorem of algebra."): 
            self.play(swWrite(title))
        
        self.play(FadeOut(title))
        self.wait(1)

        ## SCENE 1 ##
        with self.voiceover(text="here is our problem: find the roots of z squared plus four z plus thirteen."):
            self.play(Create(main_box))

        with self.voiceover(text="first we recall the discriminant definition in a quick reminder box on the right."):
            self.play(Create(disc_box))
            self.play(swWrite(disc_line1))

        with self.voiceover(text="now substitute a equals one, b equals four, c equals thirteen into D equals b squared minus four a c."):
            self.play(swWrite(main_line1))
            self.play(swWrite(main_line2))

        with self.voiceover(text="to proceed we take the square root of D. here D is negative, so the result involves the imaginary unit. sqrt of minus thirty six is six i."):
            self.play(swWrite(main_line3))

        with self.voiceover(text="next we apply the quadratic formula: z one and z two equal minus b plus or minus square root of D over two a."):
            self.play(swWrite(main_line4))

        with self.voiceover(text="for the first root we compute minus four plus six i over two, which simplifies to negative two plus three i."):
            self.play(swWrite(main_line5))

        with self.voiceover(text="for the second root we compute minus four minus six i over two, giving negative two minus three i."):
            self.play(swWrite(main_line6))

        ## Outro ##
        with self.voiceover(text="and there we have the two complex roots. thank you for watching!"):
            self.wait(1)

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
