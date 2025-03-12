from manim import *
from manim_extensions import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

GREEN = '#389B56'
ORANGE = '#F0A200'
RED = '#C74440'
BLUE = '#2D70B3'
BLUEISHGREY = '#E2E6F3'
PURPLE = '#594662'
PINK = '#BD567C'

PORPLE = '#835ED8'
GOLDY = '#f2a221' 
# GOLDY = '#e2a221' 
GOLDY = '#cb8d29'


class swRoundedRectangle(RoundedRectangle):
    FRAME_HEIGHT = 1
    FRAME_WIDTH = 2
    config = {
    "corner_radius": 0.2,
    "color": PURPLE,
    "fill_color": WHITE,
    "fill_opacity": 0.4,
    "height": FRAME_HEIGHT * 0.875,
    "width": FRAME_WIDTH * 0.45
    }

    def __init__(self, **kwargs):
        # Merge the default config with any overrides provided in kwargs
        final_config = {**self.config, **kwargs}
        
        super().__init__(
            corner_radius=final_config["corner_radius"],
            color=final_config["color"],
            fill_color=final_config["fill_color"],
            fill_opacity=final_config["fill_opacity"],
            height=final_config["height"],
            width=final_config["width"],
            stroke_width=0.2
        )
  
    
def PlaneLine(p2, plane, color=RED):
   return Line(plane.n2p(0), plane.n2p(p2), color=color, stroke_width=1)

def PlaneTriangleLines(p2, plane, color=RED, stroke_width=1):
    return VGroup(
        Line(plane.n2p(p2), plane.n2p(0), color=color, stroke_width=stroke_width),
        Line(plane.n2p(p2.real), plane.n2p(p2), color=color, stroke_width=stroke_width),
        Line(plane.n2p(0), plane.n2p(p2.real), color=color, stroke_width=stroke_width),
    )

class TextNTex(Mobject):
    def __init__(self):
        self.text = VGroup()

    def add_text(self, text, weight="NORMAL", color=BLACK):
        text_object = Text(text, font="Quicksand", weight=weight, color=color)
        self.text.add(text_object.scale(0.15))

        return self

    def add_tex(self, tex, color=BLACK):
        if 'dfrac' in tex or 'sqrt' in tex or 'arctan' in tex:
            tex_object = MathTex(tex, color=color)
        else:
            tex_object = MathTex(tex, color=color, substrings_to_isolate=['a ', 'b ', 'r ', '\\theta '])
        self.text.add(tex_object.scale(0.2))

        return self

    def create(self):
        obj = self.text.arrange(RIGHT, aligned_edge=UP, buff=0.06)
    
        # if no math symbol are used the mathtex object appears slightly to high, this corrects that
        for mob in obj:
            if type(mob) == MathTex:
                if mob.get_tex_string().isalnum():
                    mob.shift(DOWN * 0.0255)

                if 'dfrac' not in mob.get_tex_string() and 'sqrt' not in mob.get_tex_string():
                    mob.set_color_by_tex_to_color_map({'a ': BLUE, 'b ': GREEN, 'r ': GOLDY, '\\theta ': PORPLE})

        return obj    

# class CartesianToPolar(MovingCameraScene):
class Test(MovingCameraScene, VoiceoverScene):
    def construct(self):

        self.create_subcaption = False
        self.set_speech_service(
            OpenAIService(
                voice="alloy",
                model="tts-1-hd",
            )
        )

        self.next_section()
        ### SCENE CONFIG ###
        NOTHING = VGroup()
        # register_font('./Quicksand/Quicksand-VariableFont_wght.ttf')
        #################


        self.camera.background_color = BLUEISHGREY




        ### ADDING LOGO ###
        logo = ImageMobject('./Sowiso-logo-primary.png').scale(0.03)
        self.add(logo)

        self.wait(1)
        
        self.play(logo.animate.move_to(self.camera.frame.get_corner(DL)+0.15*UP + 0.35 * RIGHT).scale(0.009 / 0.03))
        ####################



        ### TITLE SCREEN ###
        title = Text("""Writing a complex number \n          in polar form""", font='Quicksand', color=PURPLE, weight="SEMIBOLD",
                        t2c={'cartesian coordinates':PINK, 'polar form':PINK},
                        line_spacing=0.2)

        title.scale(0.25).move_to(ORIGIN)

        with self.voiceover(text="This video shows how to write a complex number in polar form") as tracker:
            self.play(swWrite(title), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)
        self.play(FadeOut(title))
        ####################



        ### THEORY SECTION ###

        theory = Text('Theory', font="Quicksand", color=PINK, weight="SEMIBOLD")
        # top left corner
        theory.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.3 + DOWN * 0.15)
        # self.play(Create(theory))

        text_rect = swRoundedRectangle(width=2.7, height=2)
        self.play(swWrite(theory), Create(text_rect))
        # self.wait(1)
        
        polar_form = Text('Polar form', font="Quicksand", color=PINK, weight="SEMIBOLD")
        # top left corner of text_rect
        polar_form.scale(0.15).move_to(text_rect.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.1)


        # disregard this line
        longlineoftext = TextNTex().add_text('the position vector of').add_tex('z').add_text('makes with the positive x axis').create()
        ul = Underline(longlineoftext, color=BLACK, stroke_width=0.07).shift(UP * 0.95)
        self.play(swWrite(polar_form), Create(ul))
        # self.play(Create(ul))

        text = Text('Cartesian form ', font="Quicksand", color=BLACK, weight="NORMAL")
        # cart = ColorFormula().add('a', BLUE).add('+').add('b', GREEN).add('i').get()
        cart = MathTex('z=a + b\\cdot\\mathrm{i}', color=BLACK, substrings_to_isolate=['a ', 'b']).set_color_by_tex_to_color_map({'a ': BLUE, 'b': GREEN})

        text.scale(0.15).shift(UP * 0.8).shift(LEFT * 0.3)
        cart.scale(0.2).next_to(text, RIGHT * 0.5)

        group_text_cart = VGroup(text, cart)
        group_text_cart.shift(DOWN * 0.1)

        with self.voiceover(text="We have seen the cartesian form, which is 'a' + b times i.") as tracker:
            self.play(swWrite(group_text_cart), run_time=tracker.duration) 
            self.wait(1)
            # self.play(Create(cart), run_time=tracker.duration)

        # self.play(Create(text))
        # self.play(Create(cart))



        text2 = Text('We can also write   by using ', font="Quicksand", color=BLACK, weight="NORMAL")
        var1 = MathTex('r', color=GOLDY)
        text2_next = Text('and', font="Quicksand", color=BLACK, weight="NORMAL")
        var2 = MathTex('\\theta', color=PORPLE)
        z = MathTex('z', color=BLACK)
        # VO: explain r and theta, r >0 norm of z and theta is angle it makes with POS REAL AXIS not x axis

        # polar = MathTex('z=r e^{i\\varphi}', color=BLACK, substrings_to_isolate=['r ', '\\varphi']).set_color_by_tex_to_color_map({'r ': GOLD, '\\varphi': PURPLE})
        # text2.scale(0.15).shift(UP * 0.5).shift(LEFT * 0.3)
        # polar.scale(0.2).next_to(text2, RIGHT * 0.5)

        line = VGroup(text2, var1, text2_next, var2)
        
        # scale the Textobjects by 0.15 and the MathTex objects by 0.2
        line.scale(0.2)
        line[0].scale(0.15/0.2)
        line[2].scale(0.15/0.2)

        line.arrange(direction=RIGHT, aligned_edge=DOWN, buff=0.05)
        line[1:].shift(UP * 0.02)

        line.shift(UP * 0.5)
        z.scale(0.2)
        z.move_to(line[0].get_center() + RIGHT * 0.215)


        line_good = TNT().add_text('We can also write ').add_tex('z', BLACK).add_text(' by using ').add_tex('r', GOLDY).add_text(' and ').add_tex('\\theta', PORPLE).create()
        line_good.move_to(line.get_center())
        line_good[0].shift(UP*0.005)


        with self.voiceover(text="We can also write this complex number, using r and theta.") as tracker:
            self.play(swWrite(line_good), run_time=tracker.duration)
        # self.play(Create(line), Create(z))

        with self.voiceover(text="r is the norm of z and is always greater than zero. Theta is the angle that the position vector of z makes with the positive real axis") as tracker:
            self.play(Create(NOTHING), run_time=tracker.duration)
            self.wait(1)

        # VO: do this
        ### THIS MUST BE WELL EXPLAINED WITH AUDIO ###

        # r_explained = TextNTex().add_text('The number').add_tex('r',color=GOLD).add_tex('>0').add_text('denotes the norm of ').add_tex('z').create()
        # r_explained.shift(UP * 0.2)

        # self.play(Create(r_explained))
        # self.wait(1)

        # theta_explained = TextNTex().add_text('and the number').add_tex('\\theta',color=PORPLE).add_text('denotes the angle that').create()
        # theta_explained_sequel = TextNTex().add_text('the position vector of').add_tex('z').add_text('makes with the positive x axis').create()
        # theta_explained.shift(DOWN * 0.2)
        # theta_explained_sequel.shift(DOWN * 0.4)
        # ul_theta_explained_sequel = Underline(theta_explained_sequel, color=BLACK, stroke_width=0.07).shift(UP * 0.05)
        # theta_explained_full = VGroup(theta_explained, theta_explained_sequel, ul_theta_explained_sequel)

        # theta_explained_full.shift(UP*0.2)

        # self.play(Create(theta_explained))
        # self.play(Create(theta_explained_sequel), Create(ul_theta_explained_sequel))

        ###############################################


        to_switch = TextNTex().add_text('To switch from cartesian form to polar form, we can use').create()
        to_switch.shift(UP * 0.3)


        formulas = TextNTex().add_tex('a =r \\cdot\\cos(\\theta )').add_text('and').add_tex('b =r \\cdot\\sin(\\theta )').create()
        formulas.shift(UP * 0.1)

        with self.voiceover(text="To switch from cartesian form to polar form, we can use the following formulas") as tracker:

            self.play(swWrite(to_switch), run_time = tracker.duration / 3)
            self.play(swWrite(formulas), run_time=tracker.duration / 3)
            self.wait(tracker.duration / 3)



        ul_theory1 = ul.copy().shift(DOWN * 0.8)
        self.play(Create(ul_theory1))

        # using_the_formulas = Text('Using the formulas gives the ', font="Quicksand", color=BLACK, weight="NORMAL")
        using_the_formulas = TextNTex().add_text('Using the formulas gives the ').add_text('polar form', 'SEMIBOLD').create()
        using_the_formulas.move_to(text_rect.get_center() + DOWN * 0.12)

        with self.voiceover(text="Using the formulas gives us the polar form.") as tracker:
            self.play(swWrite(using_the_formulas), run_time=tracker.duration * 0.9)

        cartesian = MathTex('z = a + b\\cdot \\mathrm{i}', color=BLACK, substrings_to_isolate=['a ', 'b']).set_color_by_tex_to_color_map({'a ': BLUE, 'b': GREEN})
        cartesian.scale(0.2).move_to(text_rect.get_center() + DOWN * 0.3)

        self.play(swWrite(cartesian))

        polar1 = TextNTex().add_tex('z = r \\cdot \\cos(\\theta ) + r \\cdot \\sin(\\theta )\\cdot \\mathrm{i}').create()
        polar1.move_to(cartesian.get_center())

        polar2 = TextNTex().add_tex('z = r \\cdot (\\cos(\\theta ) + \\sin(\\theta )\\cdot \\mathrm{i})').create()
        polar2.move_to(cartesian.get_center())


        # VO: explain the formulas
        with self.voiceover(text="Plugging in the formula for 'a' and for 'b' gives z is equal to r times the cosine of theta plus r times the sine of theta multiplied by i.") as tracker:
            self.play(TransformMatchingShapes(cartesian, polar1), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)
        
        with self.voiceover(text="By factoring out the 'r', this can be simplified to r times the cosine of theta plus the sine of theta multiplied by i.") as tracker:
            self.play(TransformMatchingShapes(polar1, polar2), run_time = tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)
    
        the_formulas_imply = Text('The formulas imply that', font="Quicksand", color=BLACK, weight="NORMAL").scale(0.15)
        norm = MathTex('r = ||z|| = \\sqrt{a^2+b^2}>0', color=BLACK, substrings_to_isolate=['r ']).set_color_by_tex_to_color_map({'r ': GOLDY}).scale(0.2)
        norm[1][9].set_color(BLUE)
        norm[1][12].set_color(GREEN)

        the_formulas_imply.shift(DOWN * 0.6)
        norm.shift(DOWN * 0.75)

        with self.voiceover(text="The formulas imply that 'r', which is the norm of z, is equal to the square root of 'a' squared plus 'b' squared, which is always greater than zero") as tracker:
            self.play(swWrite(the_formulas_imply), run_time=tracker.duration * 0.3)
            self.play(swWrite(norm), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)
    
        polar_form_group = VGroup(
            text_rect, text, cart, z, to_switch, formulas, polar_form, ul, the_formulas_imply, norm, ul_theory1, polar2, using_the_formulas, line_good
        )

        self.play(polar_form_group.animate.shift(LEFT * 1.1).scale(0.75))

        ######################

        
        ## second part of the theory ##

        theory2_rect = swRoundedRectangle(width=2.1, height=2.3)
        theory2_rect.move_to(RIGHT * 1.1)

        self.play(Create(theory2_rect))

        calculating_variables = Text('Angle Formulas', font="Quicksand", color=PINK, weight="SEMIBOLD")
        calculating_variables.scale(0.15).move_to(theory2_rect.get_corner(UL) + RIGHT * 0.5 + DOWN * 0.1)
        line_segment = Line(theory2_rect.get_corner(UL) + RIGHT * 0.1 + DOWN * 0.1, theory2_rect.get_corner(UR) + LEFT * 0.1 + DOWN * 0.1, color=BLACK, stroke_width=0.1)
        line_segment.shift(DOWN * 0.07)

        with self.voiceover(text="For theta, there are different formulas based on the values of 'a' and 'b'.") as tracker:
            self.play(swWrite(calculating_variables), Create(line_segment), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)



        # VO: explain for any integer k

        # 0
        exception_0 = TextNTex().add_text('If ').add_tex('a > 0,').add_text('then').create().scale(0.9)
        exception_0_rule = TextNTex().add_tex('\\theta= \\arctan\\left(\\dfrac{b}{a}\\right) + 2 \\cdot k \\cdot \\pi').create().scale(0.9)
        exception_0_rule[0][0][0].set_color(PORPLE)
        exception_0_rule[0][0][9].set_color(GREEN)
        exception_0_rule[0][0][11].set_color(BLUE)

        exception_0.move_to(theory2_rect.get_center() + UP * 0.87 + LEFT * 0.6)
        exception_0_rule.move_to(theory2_rect.get_center() + UP * 0.7)
        with self.voiceover(text="If a is greater than zero, theta is equal to the arctangent of b over a + 2 times 'k' times pi. Here, 'k' can be any integer.") as tracker:
            self.play(swWrite(exception_0), run_time = tracker.duration * 0.3)
            self.play(swWrite(exception_0_rule), run_time = tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)

        self.wait(0.5)

        spacing = 0.4
        # 1
        exception_1 = TextNTex().add_text('If ').add_tex('a < 0').add_text(' and ').add_tex('b \\geq 0,').create().scale(0.9)
        exception_1_rule = TextNTex().add_tex('\\theta= \\arctan\\left(\\dfrac{b}{a}\\right) + \\pi + 2 \\cdot k \\cdot \\pi').create().scale(0.9)
        exception_1_rule[0][0][0].set_color(PORPLE)
        exception_1_rule[0][0][9].set_color(GREEN)
        exception_1_rule[0][0][11].set_color(BLUE)

        exception_1.move_to(exception_0.get_center() + DOWN * spacing + RIGHT * 0.11)
        exception_1_rule.move_to(exception_0_rule.get_center() + DOWN * 1.05 * spacing + RIGHT * 0.1)

        with self.voiceover(text="However, If a is less than zero and b is greater than or equal to zero, we have to add pi to the arctangent of b over a") as tracker:
            self.play(swWrite(exception_1), run_time=tracker.duration * 0.3)
            self.play(swWrite(exception_1_rule), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)

        # 2
        exception_2 = TextNTex().add_text('If ').add_tex('a < 0').add_text(' and ').add_tex('b < 0,').create().scale(0.9)
        exception_2_rule = TextNTex().add_tex('\\theta= \\arctan\\left(\\dfrac{b}{a}\\right) - \\pi + 2 \\cdot k \\cdot \\pi').create().scale(0.9)
        exception_2_rule[0][0][0].set_color(PORPLE)
        exception_2_rule[0][0][9].set_color(GREEN)
        exception_2_rule[0][0][11].set_color(BLUE)

        exception_2.move_to(exception_1.get_center() + DOWN * spacing)
        exception_2_rule.move_to(exception_1_rule.get_center() + DOWN * spacing)

        with self.voiceover(text="If a is less than zero and b is less than zero, we have to subtract pi from the arctangent of b over a") as tracker:
            self.play(swWrite(exception_2), run_time=tracker.duration * 0.3)
            self.play(swWrite(exception_2_rule), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)

        self.wait(0.5)

        # 3
        exception_3 = TextNTex().add_text('If ').add_tex('a = 0').add_text(' and ').add_tex('b > 0,').create().scale(0.9)
        exception_3_rule = TextNTex().add_tex('\\theta= \\dfrac{\\pi}{2} + 2 \\cdot k \\cdot \\pi').create().scale(0.9)
        exception_3_rule[0][0][0].set_color(PORPLE)

        exception_3.move_to(exception_2.get_center() + DOWN * spacing)
        exception_3_rule.move_to(exception_2_rule.get_center() + DOWN * spacing)

        with self.voiceover(text="If a is equal to zero and b is greater than zero, theta is equal to pi over 2 plus 2 times 'k' times pi") as tracker:
            self.play(swWrite(exception_3), run_time = tracker.duration * 0.3)
            self.play(swWrite(exception_3_rule), run_time = tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)

        self.wait(0.5)

        # 4
        exception_4 = TextNTex().add_text('If ').add_tex('a = 0').add_text(' and ').add_tex('b < 0,').create().scale(0.9)
        exception_4_rule = TextNTex().add_tex('\\theta= -\\dfrac{\\pi}{2} + 2 \\cdot k \\cdot \\pi').create().scale(0.9)
        exception_4_rule[0][0][0].set_color(PORPLE)

        exception_4.move_to(exception_3.get_center() + DOWN * spacing)
        exception_4_rule.move_to(exception_3_rule.get_center() + DOWN * spacing)

        with self.voiceover(text="And finally, if a is equal to zero and b is less than zero, theta is equal to negative pi over 2 plus 2 times 'k' times pi") as tracker:
            self.play(swWrite(exception_4), run_time=tracker.duration * 0.3)
            self.play(swWrite(exception_4_rule), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)


        all_mobs = Group(*self.mobjects)

        all_except = Group()

        for mob in all_mobs:
            if type(mob) == ImageMobject:
                continue
            if type(mob) == VGroup:
                for m in mob:
                    if type(m) == swRoundedRectangle:
                        continue
                    all_except.add(m)
                continue

            all_except.add(mob)



        self.play(FadeOut(all_except, theory2_rect))
        self.wait(2)

    
        ######################

        ### SECTION 2 -- EXAMPLE 1 ###
        self.next_section()

        ex_rect = swRoundedRectangle(width=1.8, height=2)
        ex_rect.move_to(LEFT * 1.3 + RIGHT * 0.1)
        
        self.play(Transform(text_rect, ex_rect))

        example = Text('Example 1', font="Quicksand", color=PINK, weight="SEMIBOLD")
        # top left corner
        example.scale(0.15).move_to(self.camera.frame.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.15)

        with self.voiceover(text="Let's look at an example") as tracker:    
            self.play(swWrite(example), run_time=tracker.duration)
        #######################
    
        ### PLANE CONFIG ###
        MAIN_AXIS_COLOR = DARK_GREY
        AUX_AXIS_COLOR = GREY
        AXIS_WIDTH = 1.5
        AUX_AXIS_WIDTH = 0.5

        AXIS_CONFIG = {
            "stroke_color": MAIN_AXIS_COLOR,
            "stroke_width": AXIS_WIDTH,
            "include_numbers": True,
            "include_tip": True,
            "tip_width": 0.1,
            "tip_height": 0.1,
            "tip_shape": StealthTip,
        }

        BACKGROUND_LINE_STYLE = {
           "stroke_color": AUX_AXIS_COLOR,
           "stroke_width": AUX_AXIS_WIDTH,
            "stroke_opacity": 0.5,
        }
        ####################

        range_ = [-2, 5, 1]
        # apply n2p operation etc to this plane
        plane = ComplexPlane(x_range=range_, y_range=range_,
                             axis_config=AXIS_CONFIG,
                             background_line_style=BACKGROUND_LINE_STYLE).add_coordinates(color=MAIN_AXIS_COLOR)
        # plane.color = GREY

        # draw this plane, workaround to remove the i from the y axis labels
        plane_to_draw = NumberPlane(x_range=range_, y_range=range_,
                                    axis_config=AXIS_CONFIG,
                                    background_line_style=BACKGROUND_LINE_STYLE).add_coordinates(color=MAIN_AXIS_COLOR)


        planeRect = swRoundedRectangle(width=2.4, height=2)
        planeRect.move_to((1,0,0))
        
        plane_scaling_factor = 0.25
        plane.scale(plane_scaling_factor).move_to(planeRect.get_center())
        plane_to_draw.scale(plane_scaling_factor).move_to(planeRect.get_center())

        label_Y = MathTex(r'\mathrm{Im}', color=BLACK).scale(0.2).move_to(plane.y_axis.get_top() + LEFT * 0.15 + DOWN * 0.05)
        label_X = MathTex(r'\mathrm{Re}', color=BLACK).scale(0.2).move_to(plane.x_axis.get_right() + DOWN * 0.07 + LEFT * 0.12)
        plane_to_draw.add(label_X, label_Y)

        # workaround to remove the i from the y axis labels
        self.play(FadeIn(planeRect), Create(plane_to_draw))#, Create(plane)) 


        text1 = Text('Write ', font="Quicksand", color=BLACK, weight="SEMIBOLD")
        tex1 = MathTex('z = 2\\cdot\\sqrt{3} + 2 \\cdot \\mathrm{i}', color=BLACK)
        text2 = Text('in polar form', font="Quicksand", color=BLACK, weight="SEMIBOLD")

        tex1[0][2:7].set_color(BLUE)
        tex1[0][8].set_color(GREEN)

        text_line = VGroup(text1, tex1, text2).arrange(direction=RIGHT, buff=0.8)
        text_line.scale(0.15)
        text_line[1].scale(0.2/0.15)
        tex1.shift(UP * 0.02)
        # move to up left corner
        text_line.shift(UP * 0.9 + LEFT * 1.2)

        ul = Underline(text_line, color=BLACK, stroke_width=0.05).scale(1.1).shift(UP * 0.09)

        with self.voiceover(text="We want to write 2 times the square root of 3 plus 2 times i in polar form") as tracker:
            self.play(swWrite(text_line), Create(ul), run_time = tracker.duration * 0.9)
            self.wait(tracker.duration * 0.1)

        self.wait(1)

        p2 = 2*np.sqrt(3)+2j
        # lines = PlaneTriangleLines(3+2j, plane, color=RED)
        line = PlaneLine(p2, plane, color=GOLD)
        line.add_tip(tip_length=0.1,tip_width=0.05)

        hdash = DashedLine(plane.n2p(p2.imag * 1j), plane.n2p(p2), color=GREY, stroke_width=1)
        vdash = DashedLine(plane.n2p(p2.real), plane.n2p(p2), color=GREY, stroke_width=1)

        y_axis_dot = Dot(plane.n2p(p2.imag * 1j), color=GREEN, radius=0.02)
        label = Tex('b', color=GREEN, font_size=10).next_to(y_axis_dot, LEFT, buff=0.05)

        x_axis_dot = Dot(plane.n2p(p2.real), color=BLUE, radius=0.02)
        label2 = Tex('a', color=BLUE, font_size=10).next_to(x_axis_dot, DOWN, buff=0.05)

        point = Dot(plane.n2p(p2), color=GREY_D, radius=0.02)
        
        # label_point = MathTex('z = 3 + 2\\cdot\\mathrm{i}', color=BLACK, substrings_to_isolate=['3', '2'], font_size=10).set_color_by_tex_to_color_map({'3': BLUE, '2': GREEN}).next_to(point, UR, buff=0.0)
        label_point = tex1.copy().next_to(point, UR, buff=0.0)
        label_point.scale(0.8).shift(LEFT * 0.05)

        with self.voiceover(text="We can represent this complex number as a point in the complex plane") as tracker:
            self.play(Create(line), FadeIn(point), swWrite(label_point))
        
        self.play(Create(hdash), Create(vdash), Create(y_axis_dot), Create(x_axis_dot), swWrite(label), swWrite(label2))
        self.wait(2)




        calculating = Text('Calculating the norm', font="Quicksand", color=BLACK, weight="NORMAL")
        calculating.scale(0.15)
        calculating.shift(UP * 0.66 + LEFT * 1.5)
        
        with self.voiceover(text="First, we calculate the norm of 'z'.") as tracker: 
            self.play(swWrite(calculating), run_time=tracker.duration)

        ###### no cam yet ###
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.75).move_to(plane.get_center()))

        dot1 = Dot(plane.n2p(0), color=BLACK, radius=0.02)
        dot2 = Dot(plane.n2p(p2), color=BLACK, radius=0.02)
        rg = MathTex('r', color=GOLD).scale(0.2).move_to(line.get_center()).shift(UP * 0.05)

        self.play(Create(dot1))
        
        with self.voiceover(text="The norm 'r' is the length of the position vector of 'z'") as tracker:
            self.play(swWrite(rg, GOLDY), run_time=tracker.duration * 0.2)
            self.play(Transform(dot1, dot2), run_time=tracker.duration * 0.8)

        self.play(Restore(self.camera.frame), FadeOut(dot1))
        ####################

        tex_r =     MathTex(r"&= \sqrt{a ^ 2 + b^2}", color=BLACK)
        tex_r[0][3].set_color(BLUE)
        tex_r[0][6].set_color(GREEN)
        tex_step1 = MathTex(r"&= \sqrt{(2\cdot\sqrt{3})^2 + 2^2}", color=BLACK).next_to(tex_r, DOWN, aligned_edge=LEFT)
        tex_step1[0][4:9].set_color(BLUE)
        tex_step1[0][12].set_color(GREEN)
        tex_step2 = MathTex(r"&= \sqrt{12+4}", color=BLACK).next_to(tex_step1, DOWN, aligned_edge=LEFT)
        tex_step3 = MathTex(r"&= \sqrt{16}", color=BLACK).next_to(tex_step2, DOWN, aligned_edge=LEFT)
        tex_step4 = MathTex(r"&= 4", color=BLACK).next_to(tex_step3, DOWN, aligned_edge=LEFT)
        
        r = MathTex('r', color=GOLD).next_to(tex_r, LEFT, buff=0.2).shift(DOWN * 0.05)

        group = VGroup(tex_r, tex_step1, tex_step2, tex_step3, tex_step4, r)
        group.scale(0.2)
        group.move_to(ex_rect.get_center() + UP * 0.2)


        with self.voiceover(text="Using the pythagorean theorem, we can see that r is equal to the square root of 'a' squared plus b squared. After substituting our values for 'a' and 'b', we can see that this expression simplifies to the square root of 16, which is 4") as tracker:
            self.play(swWrite(r, GOLDY))
            self.play(swWrite(tex_r))
            self.wait(1)  
            self.play(swWrite(tex_step1))
            self.wait(1)  
            self.play(swWrite(tex_step2))
            self.wait(1)
            self.play(swWrite(tex_step3))
            self.wait(1)
            self.play(swWrite(tex_step4))

        # play fadeout on tex_r and tex_step1 and animate tex_step4 moving up
        self.play(FadeOut(tex_r), FadeOut(tex_step1), FadeOut(tex_step2), FadeOut(tex_step3))
        self.play(tex_step4.animate.shift(UP * 0.67))

        self.play(r.animate.shift(RIGHT * 0.05), tex_step4.animate.shift(RIGHT * 0.05))

        ul2 = ul.copy().shift(DOWN * 0.42)
        self.play(Create(ul2))






        ### EXPLAINING THETA ###

        calculating_angle = Text('Calculating the angle', font="Quicksand", color=BLACK, weight="NORMAL")
        calculating_angle.scale(0.15)
        calculating_angle.move_to(calculating.get_center() + DOWN * 0.4)

        with self.voiceover(text="Next, we calculate the angle theta.") as tracker:
            self.play(swWrite(calculating_angle), run_time=tracker.duration*0.3)
            self.wait(tracker.duration*0.7)

        ## SETUP CAM THETA
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.75).move_to(plane.get_center()))

        def func_circle(x):
            return np.sqrt(np.abs(0.7**2 - x**2))

        circ_plot = plane.plot(func_circle, color=PORPLE, stroke_width=0.7, x_range=[0.7, 0.6063, -0.01])

        theta_camzoom = MathTex(r'\theta', color=PORPLE).scale(0.2).move_to(circ_plot.get_center() + RIGHT * 0.07 + UP * 0.03)

        with self.voiceover(text="We can represent the angle theta as the angle that the position vector of z makes with the positive real axis. We draw that angle here.") as tracker:
            self.play(Create(circ_plot), run_time = tracker.duration * 0.3)
            self.play(swWrite(theta_camzoom, PORPLE), run_time = tracker.duration * 0.2)
            self.wait(tracker.duration * 0.5)

        self.play(Restore(self.camera.frame))
        ####################

        thetal1 = MathTex('&= \\arctan\\left(\\frac{b}{a}\\right)', color=BLACK)
        thetal1[0][10].set_color(BLUE)
        thetal1[0][8].set_color(GREEN)

        thetal2 = MathTex('&= \\arctan\\left(\\frac{2}{2\\cdot\\sqrt{3}}\\right)', color=BLACK).next_to(thetal1, DOWN, aligned_edge=LEFT)
        thetal2[0][10:15].set_color(BLUE)
        thetal2[0][8].set_color(GREEN)

        thetal3 = MathTex('&= \\dfrac{\\pi}{6}', color=BLACK).next_to(thetal2, DOWN, aligned_edge=LEFT)

        theta = MathTex('\\theta', color=PORPLE).next_to(thetal1, LEFT, buff=0.2).shift(DOWN * 0.05)

        group = VGroup(thetal1, thetal2, thetal3, theta)

        group.scale(0.2)
        group.move_to(ex_rect.get_center() + DOWN * 0.2)

        with self.voiceover(text="Since 'a' is greater than zero, we can calculate theta by taking the arctangent of b over a. This simplifies to pi over 6") as tracker:
            self.play(swWrite(theta, PORPLE))
            self.play(swWrite(thetal1))
            self.wait(2)
            self.play(swWrite(thetal2))
            self.wait(2)
            self.play(swWrite(thetal3))
            self.wait(1)


        self.play(FadeOut(thetal1), FadeOut(thetal2))
        self.play(thetal3.animate.move_to(thetal3.get_center() + UP * 0.535))

        ul3 = ul2.copy().shift(DOWN * 0.5)
        self.play(Create(ul3))



        ## conclusion of example 1 ##

        text = Text('The polar form is', font="Quicksand", color=BLACK, weight="NORMAL")
        text.scale(0.15)
        text.shift(LEFT * 1.6 + DOWN * 0.4)



        polar = MathTex('z = r \\cdot (\\cos(\\theta) + \\sin(\\theta) \\cdot \\mathrm{i})', color=BLACK, substrings_to_isolate=['r ', '\\theta']).set_color_by_tex_to_color_map({'r ': GOLD, '\\theta': PORPLE})
        polar.scale(0.2)
        polar.shift(DOWN * 0.6)
        polar.shift(LEFT * 1.3)

        with self.voiceover(text="We can now write down the polar form, by substituting our values for 'r' and 'theta'") as tracker:
            self.play(swWrite(text), run_time=tracker.duration * 0.3)
            self.play(swWrite(polar), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.4)


        polar2 = MathTex('z = 4 \\cdot (\\cos(\\dfrac{\\pi}{6}) + \\sin(\\dfrac{\\pi}{6}) \\cdot \\mathrm{i})', color=BLACK)
        polar2[0][2].set_color(GOLD)
        polar2[0][9:12].set_color(PORPLE)
        polar2[0][18:21].set_color(PORPLE)

        polar2.scale(0.2)
        polar2.move_to(polar.get_center())

        self.wait(1)

        with self.voiceover(text="This gives us the polar form, 'z' is equal to four times the cosine of pi over 6 plus sine of pi over 6 multiplied by 'i'") as tracker:
            self.play(TransformMatchingShapes(polar, polar2))

        self.wait(1)





        to_fadeout = VGroup(
            calculating, calculating_angle, text, polar2, ul, ul2, ul3, r, tex_step4, theta, thetal3, circ_plot, text_line, plane_to_draw, line, hdash, vdash, label, label2, y_axis_dot, x_axis_dot, point, label_point, theta_camzoom, rg, label_X, label_Y
        ) 

        with self.voiceover(text="Now let's take a look at another example") as tracker:
            self.play(FadeOut(to_fadeout), FadeOut(example))



        self.wait(0.5)


        #########################
        ## SECTION 3 EXAMPLE 2 ##
        self.next_section()


        example_2 = Text('Example 2', font="Quicksand", color=PINK, weight="SEMIBOLD")
        example_2.scale(0.15).move_to(example.get_center())
        self.play(Create(example_2))


        ex2_range = [-5, 2, 1]
        ex2_plane = ComplexPlane(x_range=ex2_range, y_range=ex2_range,
                             axis_config=AXIS_CONFIG,
                             background_line_style=BACKGROUND_LINE_STYLE).add_coordinates(color=MAIN_AXIS_COLOR)
        ex2_plane_to_draw = NumberPlane(x_range=ex2_range, y_range=ex2_range,
                                    axis_config=AXIS_CONFIG,
                                    background_line_style=BACKGROUND_LINE_STYLE).add_coordinates(color=MAIN_AXIS_COLOR)
        
        plane = ex2_plane
        plane_to_draw = ex2_plane_to_draw

        plane_scaling_factor = 0.24
        ex2_plane.scale(plane_scaling_factor).move_to(planeRect.get_center())
        ex2_plane_to_draw.scale(plane_scaling_factor).move_to(planeRect.get_center())

        label_X.shift(UP * 0.55 + RIGHT * 0.05)
        label_Y.shift(RIGHT * 0.5)
        self.play(Create(ex2_plane_to_draw), swWrite(label_X), swWrite(label_Y))



        ### example explaining time ###
        ## this is all copy pasted from example 1

        text1 = Text('Write ', font="Quicksand", color=BLACK, weight="SEMIBOLD")
        tex1 = MathTex('z = -\\dfrac{5}{2} - \\dfrac{5 \\cdot \\sqrt{3}}{2} \\cdot \\mathrm{i}', color=BLACK)
        text2 = Text('in polar form', font="Quicksand", color=BLACK, weight="SEMIBOLD")

        tex1[0][2:6].set_color(BLUE)
        tex1[0][6:6+8].set_color(GREEN)

        text_line = VGroup(text1, tex1, text2).arrange(direction=RIGHT, buff=1.2)
        text_line.scale(0.13)
        text_line[1].scale(0.2/0.15)
        tex1.shift(UP * 0.02)
        # move to up left corner
        text_line.shift(UP * 0.85 + LEFT * 1.2)

        ul = Underline(text_line, color=BLACK, stroke_width=0.05).scale(1.1).shift(UP * 0.08)

        with self.voiceover(text="We want to write -5 over 2 minus 5 times the square root of 3 over 2 multiplied by 'i' in polar form") as tracker:
            self.play(swWrite(text_line), Create(ul), run_time = tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)


        p2 = -5/2 - 0.5 * (5*np.sqrt(3)) * 1j
        # lines = PlaneTriangleLines(3+2j, plane, color=RED)
        line = PlaneLine(p2, plane, color=GOLD)
        line.add_tip(tip_length=0.1,tip_width=0.05)

        hdash = DashedLine(plane.n2p(p2.imag * 1j), plane.n2p(p2), color=GREY, stroke_width=1)
        vdash = DashedLine(plane.n2p(p2.real), plane.n2p(p2), color=GREY, stroke_width=1)

        y_axis_dot = Dot(plane.n2p(p2.imag * 1j), color=GREEN, radius=0.02)
        label = Tex('b', color=GREEN, font_size=10).next_to(y_axis_dot, RIGHT, buff=0.05)
        label.shift(DOWN * 0.05 + LEFT * 0.02)

        x_axis_dot = Dot(plane.n2p(p2.real), color=BLUE, radius=0.02)
        label2 = Tex('a', color=BLUE, font_size=10).next_to(x_axis_dot, UP, buff=0.05)

        point = Dot(plane.n2p(p2), color=GREY_D, radius=0.02)
        
        # label_point = MathTex('z = 3 + 2\\cdot\\mathrm{i}', color=BLACK, substrings_to_isolate=['3', '2'], font_size=10).set_color_by_tex_to_color_map({'3': BLUE, '2': GREEN}).next_to(point, UR, buff=0.0)
        label_point = tex1.copy().next_to(point, DL, buff=0)
        label_point.scale(0.8).shift(RIGHT * 0.35)

        self.wait(1)

        with self.voiceover(text="We can once again represent this complex number as a point in the complex plane") as tracker:
            self.play(Create(line), FadeIn(point), swWrite(label_point))
            
            self.play(Create(hdash), Create(vdash), Create(y_axis_dot), Create(x_axis_dot), swWrite(label), swWrite(label2))
            self.wait(2)

    

        calculating = Text('Calculating the norm', font="Quicksand", color=BLACK, weight="NORMAL").scale(0.8)
        calculating.scale(0.15)
        calculating.shift(UP * 0.6 + LEFT * 1.6)

        with self.voiceover(text="First, we calculate the norm of 'z'.") as tracker:
            self.play(swWrite(calculating), run_time=tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        ###### no cam yet ###
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.75).move_to(plane.get_center()))

        dot1 = Dot(plane.n2p(0), color=BLACK, radius=0.02)
        dot2 = Dot(plane.n2p(p2), color=BLACK, radius=0.02)
        rg = MathTex('r', color=GOLD).scale(0.2).move_to(line.get_center()).shift(UP * 0.1)

        self.play(Create(dot1))

        with self.voiceover(text="The norm 'r' is the length of the position vector of 'z'") as tracker:
            self.play(swWrite(rg, GOLDY), run_time=tracker.duration * 0.2)
            self.play(Transform(dot1, dot2), run_time=tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)

        self.play(Restore(self.camera.frame), FadeOut(dot1))
        ####################


        tex_r =     MathTex(r"&= \sqrt{a ^ 2 + b^2}", color=BLACK)
        tex_r[0][3].set_color(BLUE)
        tex_r[0][6].set_color(GREEN)
        tex_step1 = MathTex(r"&= \sqrt{\left(-\dfrac{5}{2}\right)^2 + \left(-\dfrac{5\cdot \sqrt{3}}{2}\right)^2}", color=BLACK).next_to(tex_r, DOWN, aligned_edge=LEFT)
        tex_step1[0][7:11].set_color(BLUE)
        tex_step1[0][15:15+8].set_color(GREEN)
        tex_step2 = MathTex(r"&= \sqrt{\dfrac{25}{4}+\dfrac{75}{4}}", color=BLACK).next_to(tex_step1, DOWN, aligned_edge=LEFT)
        tex_step3 = MathTex(r"&= \sqrt{25}", color=BLACK).next_to(tex_step2, DOWN, aligned_edge=LEFT)
        tex_step4 = MathTex(r"&= 5", color=BLACK).next_to(tex_step3, DOWN, aligned_edge=LEFT)
        
        r = MathTex('r', color=GOLD).next_to(tex_r, LEFT, buff=0.2).shift(DOWN * 0.05)

        group = VGroup(tex_r, tex_step1, tex_step2, tex_step3, tex_step4, r)
        group.scale(0.2)
        group.move_to(ex_rect.get_center())

        with self.voiceover(text="r is equal to the square root of 'a' squared plus 'b' squared. If we substitute our values for 'a' and 'b', we can calculate that this equation simplifies to 5.") as tracker:
            self.play(swWrite(r, GOLDY))
            self.play(swWrite(tex_r))
            self.wait(1)  
            self.play(swWrite(tex_step1))
            self.wait(1)  
            self.play(swWrite(tex_step2))
            self.wait(1)
            self.play(swWrite(tex_step3))
            self.wait(1)
            self.play(swWrite(tex_step4))


        # play fadeout on tex_r and tex_step1 and animate tex_step4 moving up
        self.play(FadeOut(tex_r), FadeOut(tex_step1), FadeOut(tex_step2), FadeOut(tex_step3))
        self.play(tex_step4.animate.shift(UP * 0.99))

        ul2 = ul.copy().shift(DOWN * 0.42)
        self.play(Create(ul2))



        ### EXPLAINING THETA ###

        # calculating_angle = Text('Calculating the angle', font="Quicksand", color=BLACK, weight="NORMAL")
        calculating_angle = TextNTex().add_text('Calculating the angle, with').add_tex('a<0').add_text('and ').add_tex('b<0').create().scale(0.8)
        # calculating_angle.scale(0.15)
        calculating_angle[1][0][0].set_color(BLUE)
        calculating_angle[3][0][0].set_color(GREEN)

        calculating_angle.move_to(calculating.get_center() + DOWN * 0.4 + RIGHT * 0.4)

        with self.voiceover(text="Next, we calculate the angle theta, where a and b are less than zero") as tracker:
            self.play(swWrite(calculating_angle), run_time = tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)


        ## SETUP CAM THETA
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.75).move_to(plane.get_center()))

        def func_circle(x):
            return -np.sqrt(np.abs(0.8**2 - x**2))

        circ_plot = plane.plot(func_circle, color=PORPLE, stroke_width=0.7, x_range=[0.8, -0.4059, -0.01])

        theta_camzoom = MathTex(r'\theta', color=PORPLE).scale(0.2).move_to(circ_plot.get_center() + RIGHT * 0.07 + DOWN * 0.1)

        with self.voiceover(text="We can represent the angle theta as the angle that the position vector of z makes with the positive real axis. Since both a and b are less than zero, we draw the angle clockwise. ") as tracker:
            self.play(Create(circ_plot), run_time = tracker.duration * 0.3)
            self.play(swWrite(theta_camzoom, PORPLE))
            self.wait(tracker.duration * 0.7)

        self.wait(2)

        self.play(Restore(self.camera.frame))

        # a = -\\dfrac{5}{2}
        # b = -\\dfrac{5\\cdot \\sqrt{3}}{2}

        thetal1 = MathTex('&= \\arctan\\left(\\frac{b}{a}\\right) - \\pi', color=BLACK)
        thetal1[0][10].set_color(BLUE)
        thetal1[0][8].set_color(GREEN)

        thetal2 = MathTex('&= \\arctan\\left(\\frac{-\\dfrac{5\\cdot \\sqrt{3}}{2}}{-\\dfrac{5}{2}}\\right) - \\pi', color=BLACK).next_to(thetal1, DOWN, aligned_edge=LEFT)
        thetal2[0][20:20+4].set_color(BLUE)
        thetal2[0][11:11+8].set_color(GREEN)

        thetal3 = MathTex('&= \\arctan(\\sqrt{3}) - \\pi', color=BLACK).next_to(thetal2, DOWN, aligned_edge=LEFT).shift(RIGHT * 0.01)

        theta = MathTex('\\theta', color=PORPLE).next_to(thetal1, LEFT, buff=0.2).shift(DOWN * 0.05)

        group = VGroup(thetal1, thetal2, thetal3, theta)

        group.scale(0.2)
        group.move_to(ex_rect.get_center() + DOWN * 0.4)

        with self.voiceover(text="Since both a and b are less than zero, we can calculate theta by taking the arctangent of b over a and subtracting pi") as tracker:
            self.play(swWrite(theta, PORPLE))
            self.play(swWrite(thetal1), run_time = tracker.duration * 0.3)
            self.wait(tracker.duration * 0.7)

        self.wait(1)

        with self.voiceover(text="We can fill in our values for 'a' and 'b'.") as tracker:
            self.play(swWrite(thetal2))
            self.wait(1)


        altthetal2 = MathTex('&= \\arctan\\left(\\dfrac{5 \\cdot 2 \\cdot \\sqrt{3}}{2 \\cdot 5}\\right) - \\pi', color=BLACK).move_to(thetal2.get_center()).scale(0.2)

        self.wait(2)
        with self.voiceover(text="We can simplify the fraction like this") as tracker:
            self.play(TransformMatchingShapes(thetal2, altthetal2))
            self.play(altthetal2.animate.shift(UP*0.05))
            # self.wait(tracker.duration * 0.5)

        thetal3.shift(UP * 0.05)

        self.play(swWrite(thetal3))
        self.wait(1)

        altthetal3 = MathTex('&= \\dfrac{\\pi}{3} -\\pi', color=BLACK).move_to(thetal3.get_center() + LEFT * 0.2).scale(0.2)

        with self.voiceover(text="This simplifies to pi over 3 minus pi") as tracker:
            self.play(TransformMatchingShapes(thetal3, altthetal3), run_time = tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)

        altthetal4 = MathTex('&= -\\dfrac{2\\cdot\\pi}{3}', color=BLACK).move_to(altthetal3.get_center()).scale(0.2)


        with self.voiceover(text="And this is equal to minus 2 pi over 3") as tracker:
            self.play(TransformMatchingShapes(altthetal3, altthetal4), run_time = tracker.duration * 0.5)
            self.wait(tracker.duration * 0.5)

        self.play(FadeOut(thetal1), FadeOut(altthetal2))


        self.play(altthetal4.animate.shift(UP * 0.7))

        ul3 = ul2.copy().shift(DOWN * 0.5)
        self.play(Create(ul3))


        new_group = VGroup(theta, altthetal4)
        self.play(new_group.animate.shift(UP * 0.1 + LEFT * 0.05))


        ## conclusion of example 2 ##

        text = Text('The polar form is', font="Quicksand", color=BLACK, weight="NORMAL")
        text.scale(0.15)
        text.shift(LEFT * 1.6 + DOWN * 0.4)

        with self.voiceover(text="We can now write down the polar form, by substituting our values for 'r' and 'theta'") as tracker:
            self.play(swWrite(text))


        polar = MathTex('z = r \\cdot (\\cos(\\theta) + \\sin(\\theta) \\cdot \\mathrm{i})', color=BLACK, substrings_to_isolate=['r ', '\\theta']).set_color_by_tex_to_color_map({'r ': GOLD, '\\theta': PORPLE})
        polar.scale(0.2)
        polar.shift(DOWN * 0.6)
        polar.shift(LEFT * 1.3)

        self.play(swWrite(polar))


        polar2 = MathTex('z = 5 \\cdot (\\cos(-\\dfrac{2\\cdot\\pi}{3}) + \\sin(-\\dfrac{2\\cdot\\pi}{3}) \\cdot \\mathrm{i})', color=BLACK)
        polar2[0][2].set_color(GOLD)
        polar2[0][9:9+6].set_color(PORPLE)
        polar2[0][18+3:21+6].set_color(PORPLE)

        polar2.scale(0.2)
        polar2.move_to(polar.get_center() + RIGHT * 0.1)

        self.wait(2)

        with self.voiceover(text="This gives us the polar form, 'z' is equal to five times the cosine of minus 2 pi over 3 plus sine of minus 2 pi over 3 multiplied by 'i'") as tracker:
            self.play(TransformMatchingShapes(polar, polar2))

        self.wait(1)

        # to_fadeout = VGroup(
        #     calculating, calculating_angle, text, polar2, ul, ul2, ul3, r, tex_step4, theta, thetal3, circ_plot, text_line, plane_to_draw, line, hdash, vdash, label, label2, y_axis_dot, x_axis_dot, point, label_point, theta_camzoom, rg, label_X, label_Y
        # ) 
        # self.play(FadeOut(to_fadeout), Uncreate(example))

        with self.voiceover(text="This concludes the examples. Thanks for watching") as tracker:

            self.wait(tracker.duration)
    
        # fade out everything still on the screen
        self.wait(2)

        fadeout_all = Group(*self.mobjects)
        self.play(FadeOut(fadeout_all))
        self.wait(1)


class Test1(Scene):
    def construct(self):
        self.camera.background_color = BLUEISHGREY
        self.wait(1)

        line = TextNTex(

        ).add_text('This is a'
                   ).add_tex('\\dfrac{a}{b}'
                             ).add_text(' test because i want to show that '
                                        ).add_tex('\\sqrt{3}').create()
        self.play(Create(line))
        self.wait(1)
