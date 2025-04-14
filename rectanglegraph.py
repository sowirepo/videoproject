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
        title = Text("""[TITLE]""", font='Quicksand', color=PURPLE, weight="SEMIBOLD", 
                      line_spacing=0.2).scale(0.25)

        title.move_to(ORIGIN)

        ## swRoundedRectangle plus graph Example ##

        # Code for the swROundedRectangle comes here
        rect = swRoundedRectangle(
            height=2,
            width=2.2,
        ).shift(LEFT * 1.05)
        rect_title = TNT().txt('Problem statement').tx('equation to solve in tex')
        rect.set_title(rect_title)

        line1 = TNT().txt('Derivation line 1').tx('some tex')
        line2 = TNT().tx('Derivation line 2').tx('some tex')
        line3 = TNT().txt('Derivation line 3, could use graph').tx('some tex')
        line4 = TNT().tx('Derivation line 4, could use graph').txt('some tex')

        rect_content = VGroup(line1, line2, line3, line4)
        rect.create_content(rect_content, offset=0.075)

        ## graph code, choose one of the following ##
        graph_rect = swRoundedRectangle(
            height=2,
            width=2,
        ).shift(RIGHT * 1.15)

        graph_type = 1

        ## code for the graph, this example is a normal graph
        if graph_type == 0:
            pass
        ## normal graph end

        ## code for the graph, this example is a complex plane
        if graph_type == 1:
            userdefined_range = [-2, 5, 1] # a range where |min - max| should be approximately 7

            scale_factor_calc = -7/300 * (userdefined_range[1] - userdefined_range[0]) + 0.41 # bad interpolation to find the scale factor, keep range between like 6 and 9 

            graph = ComplexPlane(x_range=userdefined_range, y_range=userdefined_range,
                                axis_config=AXIS_CONFIG,
                                background_line_style=BACKGROUND_LINE_STYLE).add_coordinates(color=MAIN_AXIS_COLOR).scale(scale_factor_calc)
            graph.move_to(graph_rect.get_center())

        ## complex plane end

        ## code for the graph, this example is the polar plane
        if graph_type == 2:
            userdefined_angle = np.pi / 12

            azimuth = np.pi / userdefined_angle * 2 
            graph = PolarPlane(
                azimuth_units="PI radians",
                azimuth_step=azimuth, # the slices will be in steps of 2 * pi / azimuth_step, i.e. azimuth_step = 12 makes slices of pi/6 radians
                size=8,
                azimuth_label_font_size=33.6,
                # radius_config={"font_size": 33.6,
                #                "color": BLACK},
                radius_max=1.5,
                radius_step=0.5,
                background_line_style=BACKGROUND_LINE_STYLE,
                radius_config=AXIS_CONFIG
            ).add_coordinates().scale(0.21).move_to(graph_rect.get_center())
            graph[2:].set_color(DARK_GREY)

            # TODO this is sketchy
            # random labels that linger at the left and bottom of the axis
            graph[3][2][0].shift(UP * 9)
            graph[4][0][2][0].shift(UP * 9)

        ## polar plane end

        ## graph operations, like adding points or vectors

        vec = None

        ### INTRO ANIMATIONS ###
        self.add(logo)

        self.wait(1)

        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL) + 0.15*UP + 0.35*RIGHT).scale(0.009 / 0.03))

        with self.voiceover(text="Video title voiceover placeholder") as tracker:
            self.play(swWrite(title))

        self.play(FadeOut(title))
        self.wait(1)

        ## Scene Animations
        with self.voiceover(text="This voicover presents the problem statement from the rectangle") as tracker:
            self.play(Create(rect))

        with self.voiceover(text="This voicover explains the first line of the derivation") as tracker:
            self.play(swWrite(line1))

        with self.voiceover(text="This voicover explains the second line of the derivation") as tracker:
            self.play(swWrite(line2))

        with self.voiceover(text="This voicover presents the graph") as tracker:
            self.play(Create(graph_rect), Create(graph))

        with self.voiceover(text="This voicover explains the third line of the derivation") as tracker:
            self.play(swWrite(line3))

        with self.voiceover(text="This voicover explains the fourth line of the derivation") as tracker:
            self.play(swWrite(line4))


        return
        ## Outro ##
        with self.voiceover(text="This concludes the examples. Thanks for watching.") as tracker:
            self.wait(1)
    
        self.wait(2)

        # Fade out everything still on the screen
        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)