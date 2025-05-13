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
        main_line6.shift(DOWN * 0.35)

        # discriminant theory box on the right
        disc_box = swRoundedRectangle(height=0.8, width=1.8).shift(RIGHT * 1.15 + UP * 0.5)
        disc_title = TNT().txt("Discriminant", weight="SEMIBOLD", color=PINK)
        disc_box.set_title(disc_title)
        disc_line1 = TNT().tx("D=b^2-4\\cdot a\\cdot c")
        disc_box.create_content(VGroup(disc_line1), offset=0.075)

        ## SCENE 2 mobjects ##
        # second problem box centered
        box2 = swRoundedRectangle(height=2, width=3.4)

        # title: problem statement
        title2 = TNT()\
            .txt("Given ")\
            .tx("z = 1")\
            .txt(" is a root of")\
            .tx("f(z),")\
            .txt(" factorize ")\
            .tx("f(z) = z^3 - 3\\cdot z^2 + 7\\cdot z - 5")
        box2.set_title(title2)

        # content lines: use fundamental theorem, factor, discriminant, sqrt, quadratic formula
        line1_2 = TNT().txt("We know that ").tx("f(z) = (z-1)(z-w_2)(z-w_3)")
        line2_2 = TNT().txt("We factor out the known root to get")
        line3_2 = TNT().tx("f(z) = (z - 1)\\cdot (z^2 - 2\\cdot z + 5)")
        line4_2 = TNT().tx("D = (-2)^2 - 4\\cdot 1\\cdot 5 = -16")
        line5_2 = TNT().tx("\\sqrt{D} = \\sqrt{-16} = 4\\cdot \\mathrm{i}")
        line6_2 = TNT().tx("w_2 = \\dfrac{2 + 4\\cdot \\mathrm{i}}{2} = 1 + 2\\cdot \\mathrm{i}")
        line7_2 = TNT().tx("w_3 = \\dfrac{2 - 4\\cdot \\mathrm{i}}{2} = 1 - 2\\cdot \\mathrm{i}")
        line8_2 = TNT().tx("f(z)=(z-1)(z-(1 + 2\\cdot \\mathrm{i}))(z-(1 - 2\\cdot \\mathrm{i}))")

        # include all lines in the content group
        content2 = VGroup(
            line1_2,
            line2_2,
            line3_2,
            line4_2,
            line5_2,
            line6_2,
            line7_2,
            line8_2
        )
        box2.create_content(content2, offset=0.075)

        line6_2.shift(DOWN * 0.1)
        VGroup(line7_2, line8_2).shift(DOWN * 0.2)

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
        with self.voiceover(text='in this video we explore how to solve a quadratic equation with complex roots, and connect it to the fundamental theorem of algebra.'): 
            self.play(swWrite(title))
        
        self.play(FadeOut(title))
        self.wait(1)

        ## SCENE 1 ##
        with self.voiceover(text='First we will solve the following problem: find the roots of "z" squared plus four times "z" plus 13.'):
            self.play(Create(main_box))

        with self.voiceover(text='first we recall the definition of the discriminant.'):
            self.play(Create(disc_box))

        with self.voiceover(text='the discriminant "D" is equal to "b" squared minus four times "a" times "c".'):
            self.play(swWrite(disc_line1))

        with self.voiceover(text='now substitute "a" equals one, "b" equals four, "c" equals thirteen into this formula'):
            self.play(swWrite(main_line1))

        with self.voiceover(text='we get that "D" is sixteen minus fifty two equals minus thirty six, so "D" is negative.'):
            self.play(swWrite(main_line2))

        with self.voiceover(text="because we are dealing with complex numbers now, the square root of the discriminant is always well-defined. a discriminant of less than zero means there are two complex roots. this means that a quadratic complex polynomial with complex coefficients always has two roots."):
            pass

        with self.voiceover(text='to proceed we take the square root of "D". here "D" is negative, so the result involves the imaginary unit. we get that the square root of minus thirty six is six times "i".'):
            self.play(swWrite(main_line3))

        with self.voiceover(text='next we apply the quadratic formula: "z" one and "z" two equal minus "b" plus or minus the square root of "D" over two times "a".'):
            self.play(swWrite(main_line4))

        with self.voiceover(text='for the first root we compute minus four plus six times "i" over two, which simplifies to negative two plus three times "i".'):
            self.play(swWrite(main_line5))

        with self.voiceover(text='for the second root we compute minus four minus six times "i" over two, giving negative two minus three times "i". these are the two roots of the equation'):
            self.play(swWrite(main_line6))

        ## SCENE 2 ##
        # fade out everything except the logo
        to_fade = [m for m in self.mobjects if m is not logo]
        self.play(FadeOut(Group(*to_fade)))
        self.wait(1)

        with self.voiceover(text='now given that "z" equals one is a root of the cubic polynomial, we have to factorise it accordingly.'):
            self.play(Create(box2))

        with self.voiceover(text='by the fundamental theorem of algebra, a cubic equation has three roots and we can rewrite the formula as z minus 1 times z minus w2 times z minus w3, where w2 and w3 are the remaining roots.'):
            self.play(swWrite(line1_2))

        with self.voiceover(text='We can factor out the known root to end up with a quadratic equation.'):
            self.play(swWrite(line2_2))

        with self.voiceover(text='factoring out z minus 1 gives f of "z" is equal to z minus 1 times z squared minus 2 times z plus 5.'):
            self.play(swWrite(line3_2))

        with self.voiceover(text='To solve for the quadratic part, we once again compute the discriminant: negative two squared minus four times one times five equals minus sixteen.'):
            self.play(swWrite(line4_2))

        with self.voiceover(text='taking the square root of minus sixteen yields four times "i".'):
            self.play(swWrite(line5_2))

        with self.voiceover(text='the first remaining root w two is two plus four "i" over two, which simplifies to one plus two "i".'):
            self.play(swWrite(line6_2))

        with self.voiceover(text='the second remaining root w three is two minus four "i" over two, simplifying to one minus two "i".'):
            self.play(swWrite(line7_2))

        with self.voiceover(text='finally, we write the fully factored form f of z equals z minus one times z minus one plus two "i" times z minus one minus two "i".'):
            self.play(swWrite(line8_2))

        ## Outro ##
        with self.voiceover(text='this concludes the examples. thanks for watching.'):
            self.wait(1)

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)
