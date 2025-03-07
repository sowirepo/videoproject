from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService


### Colors stuff ####

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

#######################



### Directions ####

UPS = UP * 0.01
DOWNS = DOWN * 0.01
LEFTS = LEFT * 0.01
RIGHTS = RIGHT * 0.01

###################



### Config for plane ####

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

###################


# sw rectangle with smooth corners
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
  
    
# adds a line in a complex plane from 0 to p2, p2 is a complex number
def PlaneLine(p2, plane, color=RED):
   return Line(plane.n2p(0), plane.n2p(p2), color=color, stroke_width=1)

# draws a right triangle in a complex plane with hypotenuse 0->p2, p2 is a complex number
def PlaneTriangleLines(p2, plane, color=RED, stroke_width=1):
    return VGroup(
        Line(plane.n2p(p2), plane.n2p(0), color=color, stroke_width=stroke_width),
        Line(plane.n2p(p2.real), plane.n2p(p2), color=color, stroke_width=stroke_width),
        Line(plane.n2p(0), plane.n2p(p2.real), color=color, stroke_width=stroke_width),
    )

# Text and MathTex on the same line, aligned :)
class TNT(Mobject):

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
        objs = self.text.arrange(RIGHT, aligned_edge=UP, buff=0.06)
    
        for mob in objs:
            if type(mob) == MathTex:

                if 'dfrac' not in mob.get_tex_string() and 'sqrt' not in mob.get_tex_string():
                    mob.set_color_by_tex_to_color_map({'a ': BLUE, 'b ': GREEN, 'r ': GOLDY, '\\theta ': PORPLE})

        prevObj_y = None
        for mob in objs:

            if prevObj_y is None:
                prevObj_y = mob.get_center_of_mass()

            else:
                mob.shift(UP * (prevObj_y[1] - mob.get_center_of_mass()[1]))

        return objs
    
    def txt(self, text, weight="NORMAL", color=BLACK):
        self.add_text(text, weight, color)
        return self
    
    def t(self, text, weight="NORMAL", color=BLACK):
        self.add_text(text, weight, color)
        return self
    
    def tx(self, tex, color=BLACK):
        self.add_tex(tex, color)
        return self

# normal complex plane has 'i' in the vertical axis, this one removes that by
# implementing ComplexPlane only functions on the NumberPlane Object
class swComplexPlane(NumberPlane):


    def __init__(self, x_range, y_range=-1, **kwargs):

        if y_range == -1:
            y_range = x_range

        super().__init__(x_range=x_range, y_range=y_range, axis_config=AXIS_CONFIG, background_line_style=BACKGROUND_LINE_STYLE, **kwargs)

        self.add_coordinates(color=MAIN_AXIS_COLOR)

        label_Y = MathTex(r'\mathrm{Im}', color=BLACK).scale(0.5).move_to(self.y_axis.get_top() + LEFT * 0.5 + DOWN * 0.1)
        label_X = MathTex(r'\mathrm{Re}', color=BLACK).scale(0.5).move_to(self.x_axis.get_right() + DOWN * 0.07 + LEFT * 0.12)
        self.add(label_X, label_Y)

        self.compplane = ComplexPlane(x_range=x_range, y_range=y_range, axis_config=AXIS_CONFIG, background_line_style=BACKGROUND_LINE_STYLE, **kwargs)
        self.add(self.compplane)

    def update_(self):
        self.compplane.move_to(self.get_center())
        return self

    def n2p(self, number):


        self.compplane.move_to(self.get_center())
        self.remove(self.compplane)

        return self.compplane.n2p(number)


class swWrite(Write):

    def __init__(self, mobject, color=BLACK, **kwargs):
        super().__init__(mobject, **kwargs)

        self.lag_ratio = 9999999
        self.stroke_color = color
        self.stroke_width = 1


