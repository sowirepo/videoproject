from manim import *
from manim_extensions import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

class Test(MovingCameraScene, VoiceoverScene):

    def construct(self):
        # Setup scene
        self.create_subcaption = False
        self.camera.background_color = BLUEISHGREY
        self.set_speech_service(OpenAIService(
            voice="alloy",
            model="gpt-4o-mini-tts",
        ))

        # Mobjects
        logo = ImageMobject('./Sowiso-logo-primary.png').scale(0.03)

        title = Text("Complex Logarithm Examples", font='Quicksand', color=PURPLE, weight="SEMIBOLD", line_spacing=0.2).scale(0.25).move_to(ORIGIN)

        example1_rect = swRoundedRectangle(height=2.1, width=2.5).shift(LEFT * 1.1)
        example2_rect = swRoundedRectangle(height=2.1, width=2.5).shift(LEFT * 1.1)
        properties_rect = swRoundedRectangle(height=1.5, width=2.5).shift(RIGHT * 1.1)

        # Example 1 Mobjects
        example1_title = TNT().txt("Example 1: Calculate ").tx('ln(z_1) where z_1=e^{\\theta \\cdot \\mathrm{i}}')
        example1_step1 = TNT().txt("Given ").tx('z_1=e^{\\theta \\cdot \\mathrm{i}}').txt(" with ").tx('-\\pi < \\theta \\leq \\pi')
        example1_step2 = TNT().txt('ln(z_1)').txt(' = \\ln( |z_1|\\cdot e^{\\mathrm{i} \\theta} )')
        example1_step3 = TNT().txt(' = \\ln( |z_1| ) + \\ln\\left( e^{\\mathrm{i} \\theta} \\right)')
        example1_step4 = TNT().txt(' = 0 + \\mathrm{i} \\theta')  # ln(|z|) = ln(1) = 0
        
        # Example 2 Mobjects
        example2_title = TNT().txt("Example 2: Calculate ").tx('ln(z_2) where ').tx('z_2 = e^{(\\theta + 2\\cdot\\pi)\\cdot \\mathrm{i}}')
        example2_step1 = TNT().txt("Given ").tx('z_2=e^{(\\theta + 2\\cdot\\pi)\\cdot \\mathrm{i}}').txt(" with ").tx('\\theta > \\pi')
        example2_step2 = TNT().txt('ln(z_2)').txt(' = \\ln( |z_2|\\cdot e^{\\mathrm{i} (\\theta + 2\\cdot\\pi)} )')
        example2_step3 = TNT().txt(' = \\ln( |z_2| ) + \\ln\\left( e^{\\mathrm{i} (\\theta + 2\\cdot\\pi)} \\right)')
        example2_step4 = TNT().txt(' =  2\\cdot\\pi\\cdot\\mathrm{i} + \\mathrm{i} \\theta')
        
        # Properties Mobjects
        properties_title = TNT().txt("Computational Properties", weight="SEMIBOLD")
        properties1 = TNT().tx('\\ln(z_1 \\cdot z_2) = \\ln(z_1) + \\ln(z_2)')
        properties2 = TNT().tx('\\ln(z^n) = n \\ln(z)')
        properties3 = TNT().tx('e^{\\ln(z)} = \\ln(e^z) = z')

        example1_rect.set_title(example1_title)
        example2_rect.set_title(example2_title)
        properties_rect.set_title(properties_title)

        example1_group = example1_rect.create_content(VGroup(example1_step1, example1_step2, example1_step3, example1_step4))
        example2_group = example2_rect.create_content(VGroup(example2_step1, example2_step2, example2_step3, example2_step4))
        properties_group = properties_rect.create_content(VGroup(properties1, properties2, properties3))

        # Animations
        self.add(logo)
        self.wait(1)
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL) + 0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))
        
        with self.voiceover(text="In this video, we will explore the complex logarithm through two examples, and conclude with key computational properties."):
            self.play(swWrite(title))

        self.play(FadeOut(title))

        # Example 1
        with self.voiceover(text="Our first example is to calculate the natural logarithm of a complex number, z one, in polar-exponential form, with argument theta in the principal value range."):
            self.play(Create(example1_rect))
        
        with self.voiceover(text="Given z one equals e to the theta times i, where theta is in the range minus pi to pi."):
            self.play(swWrite(example1_step1))

        with self.voiceover(text="Taking the natural logarithm gives us the logarithm of the magnitude times the exponential term."):
            self.play(swWrite(example1_step2))
        
        with self.voiceover(text="We can split this into two separate logarithms."):
            self.play(swWrite(example1_step3))

        with self.voiceover(text="Since the magnitude of z one is 1, its logarithm is zero, leaving us with i times theta."):
            self.play(swWrite(example1_step4))

        self.play(FadeOut(example1_group))

        # Example 2
        with self.voiceover(text="Next, we consider a complex number, z two, in polar-exponential form with argument outside the principal value range."):
            self.play(Create(example2_rect))

        with self.voiceover(text="Given z two equals e to the power of theta plus two pi times i, where theta is greater than pi."):
            self.play(swWrite(example2_step1))

        with self.voiceover(text="Taking the natural logarithm, we again consider both the magnitude and exponential term."):
            self.play(swWrite(example2_step2))
        
        with self.voiceover(text="Splitting into two separate logarithms gives us the following expression."):
            self.play(swWrite(example2_step3))

        with self.voiceover(text="This evaluates to two pi i plus i times theta."):
            self.play(swWrite(example2_step4))

        self.play(example2_rect.animate.shift(LEFT * 1.1), FadeOut(example2_group))

        # Properties
        with self.voiceover(text="Finally, let's discuss the following important computational properties of complex logarithms."):
            self.play(Create(properties_rect))

        with self.voiceover(text="The logarithm of a product is the sum of the logarithms."):
            self.play(swWrite(properties1))

        with self.voiceover(text="The logarithm of a power is the power times the logarithm."):
            self.play(swWrite(properties2))

        with self.voiceover(text="Exponential and logarithm functions are inverses of each other, so the exponential of a logarithm returns z."):
            self.play(swWrite(properties3))

        with self.voiceover(text="This concludes the examples and properties for the complex logarithm. Thanks for watching."):
            self.wait()

        # Fade out
        all_fadeout = Group(*self.mobjects)
        self.play(FadeOut(all_fadeout))
        self.wait(1)