from manim import *
import re

### Colors stuff ####

GREEN = '#389B56'
ORANGE = '#F0A200'
RED = '#C74440'
BLUE = '#2D70B3'
BLUEISHGREY = '#E2E6F3'
PURPLE = '#594662'
PINK = '#BD567C'

# This is the right purple to use
swPURPLE = '#835ED8'

# This is the right gold color to use
swGOLD = '#cb8d29'

#######################



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
        self.title_underline = None

        super().__init__(
            corner_radius=final_config["corner_radius"],
            color=final_config["color"],
            fill_color=final_config["fill_color"],
            fill_opacity=final_config["fill_opacity"],
            height=final_config["height"],
            width=final_config["width"],
            stroke_width=0.2
        )

    def set_title(self, title, offset=0.05, remove_line=False):

        coords_upper_edge = self.get_edge_center(UP)

        title.move_to(coords_upper_edge).shift(DOWN * (SMALL_BUFF + offset))

        lower_edge_title = title.get_edge_center(DOWN)

        left_line = self.get_corner(UL) + RIGHT * SMALL_BUFF
        right_line = self.get_corner(UR) + LEFT * SMALL_BUFF

        title_underline = Line(left_line, right_line, color=GREY, stroke_width=0.2).shift(DOWN*( coords_upper_edge[1] - lower_edge_title[1] + offset ))
        


        self.add(title)
        if not remove_line:
            self.add(title_underline)
        self.title_underline = title_underline

        return self
    
    def create_content(self, group: VGroup, offset:float=0., align='center'):

        if self.title_underline is None:
            raise Exception("Title underline not set. Please set the title first using .set_title()")
        
        if align == 'center':
            middle_line = self.title_underline.get_center()

            for idx, mob in enumerate(group):
                mob.move_to(middle_line).shift(DOWN * (idx + 1) * (SMALL_BUFF + offset))
        
        elif align == 'left':
            middle_line = self.title_underline.get_center()

            for idx, mob in enumerate(group):
                mob.move_to(middle_line).shift(DOWN * (idx + 1) * (SMALL_BUFF + offset))

                left_factor = mob.get_edge_center(LEFT)[0] - self.title_underline.get_edge_center(LEFT)[0]

                mob.shift(LEFT * left_factor)
        else:
            raise Exception("Invalid alignment option. Use 'center' or 'left'.")

        return group

class TNT(VMobject):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.objs = VGroup()
        self.aligned_chars = []
        self.add(self.objs)

    def txt(self, text, weight="NORMAL", color=BLACK):
        text_object = Text(text, font="Quicksand", weight=weight, color=color)
        self.objs.add(text_object.scale(0.15))
        self.aligned_chars.append(None)

        return self.create()

    def tx(self, tex, color=BLACK, aligned_char='='):
        tex_object = MathTex(tex, color=color)
        self.objs.add(tex_object.scale(0.2))

        if '=' not in tex:
            possible_chars = ['>', '<', '\\geq', '\\leq', '(', ')']
            for char in possible_chars:
                if char in tex:
                    aligned_char = char
                    break

        self.aligned_chars.append(aligned_char)

        return self.create()

    def create(self):
        objs = self.objs.arrange(RIGHT, aligned_edge=UP, buff=0.06)

        FirstObject = self.objs[0]

        if type(FirstObject) == Text:
            center = FirstObject.get_center_of_mass()
            proposed_height = center[1]

        if type(FirstObject) == MathTex:
            proposed_height = FirstObject[0].get_center()[1]

        for i, mob in enumerate(objs[1:]):

            if type(mob) == MathTex:
                char_tex_string = self.parse_latex_characters(mob.get_tex_string())

                if len(char_tex_string) > len(mob[0]):
                    print(f"Warning: parsed tex string is longer than the actual tex string, {char_tex_string}")

                char_to_find = self.aligned_chars[i+1]
                assert char_to_find is not None

                index_of_equals = char_tex_string.find(char_to_find)
                # todo, check behaviour if char_to_find is -1 so the last index, -1 is returned at .find if no match is found

                if index_of_equals == -1:
                    index_of_equals = 0

                center_mob = mob[0][index_of_equals].get_center()
                
                mob.shift(UP * (proposed_height - center_mob[1]))

            if type(mob) == Text:
                center_mob = mob.get_center_of_mass()
                mob.shift(UP * (proposed_height - center_mob[1]))

        return self
    
    def parse_latex_characters(self, tex_string):
        # remove ^ and _
        tex_string = re.sub(r'\^', '', tex_string)
        tex_string = re.sub(r'\_', '', tex_string)

        # turn dfrac into frac
        tex_string = re.sub(r'dfrac', 'frac', tex_string)

        # parse fracs
        tex_string = self.replace_dfrac(tex_string)

        # remove curly braces
        tex_string = re.sub(r'{', '', tex_string)
        tex_string = re.sub(r'}', '', tex_string)

        # remove \\ and \, and \; and \! and \quad and \qquad
        tex_string = re.sub(r'\\,', '', tex_string)
        tex_string = re.sub(r'\\;', '', tex_string)
        tex_string = re.sub(r'\\!', '', tex_string)
        tex_string = re.sub(r'\\quad', '', tex_string)
        tex_string = re.sub(r'\\qquad', '', tex_string)
        tex_string = re.sub(r' ', '', tex_string)

        #remove \text \textbf \textit \texttt
        tex_string = re.sub(r'\\textbf', '', tex_string)
        tex_string = re.sub(r'\\textit', '', tex_string)
        tex_string = re.sub(r'\\texttt', '', tex_string)
        tex_string = re.sub(r'\\text', '', tex_string)

        # remove \left and \right
        tex_string = re.sub(r'\\left', '', tex_string)
        tex_string = re.sub(r'\\right', '', tex_string)

        one_length_symbols = ['dfrac', 'frac', 'theta', 'overline', 'underline', 'bar', 'hat', 'tilde', 'vec', 'dot', 'cdot', 'vdash', 'dashv', 'overset', 'underset', 'to', 'rightarrow', 'leftarrow', 'leftrightarrow', 'Rightarrow', 'Leftarrow', 'Leftrightarrow', 'leq', 'geq', 'varphi', 'pi', 'wedge', 'vee']
        two_length_symbols = ['sqrt']

        # replace each one length symbol with a single character
        for symbol in one_length_symbols:
            tex_string = re.sub(r'\\' + symbol, f'{symbol[0]}', tex_string)
        
        # replace each two length symbol with a single character
        for symbol in two_length_symbols:
            tex_string = re.sub(r'\\' + symbol, f'{symbol[0]}{symbol[0]}', tex_string)

        # remove all other backslashes
        tex_string = re.sub(r'\\', '', tex_string)

        # remove mathrm
        tex_string = re.sub(r'mathrm', '', tex_string)

        return tex_string
    
    def set_color_by_string(self, string: str, color):
        for mob in self.objs:
            if type(mob) == MathTex:
                char_tex_string = self.parse_latex_characters(mob.get_tex_string())
                parsed_string = self.parse_latex_characters(string)


                start = 0
                indices_of_strings = []

                while start < len(char_tex_string):
                    index = char_tex_string.find(parsed_string, start)
                    if index == -1:
                        break
                    indices_of_strings.append(index)
                    start = index + 1

                # print('Index of equals: ', indices_of_strings)

                if indices_of_strings != -1:
                    for index in indices_of_strings:
                        mob[0][index:index+len(parsed_string)].set_color(color)

    def find_matching_brace(self, s, start_index):
        """Find the index of the matching closing brace for the brace at start_index."""
        depth = 0
        for index, char in enumerate(s[start_index:], start=start_index):
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0:
                    return index
        return -1


    def replace_dfrac(self, expression: str):

        start = 0
        indices_of_fracs = []

        while start < len(expression):
            index = expression.find('frac', start)
            if index == -1:
                break
            indices_of_fracs.append(index)
            start = index + 1

        indices_of_braces = [i + 4 for i in indices_of_fracs]

        back_braces = []
        for index in indices_of_braces:
            brace_index = self.find_matching_brace(expression, index)
            back_braces.append(brace_index)
            assert expression[brace_index:brace_index+2] == '}{'

        expression_list = [char for char in expression]

        for idx, brace_index in enumerate(back_braces):
            # at index 'brace_index' + idx + 1, insert a '`'

            # this character is used to indicate that there is a fraction and should never be used in a mathematical expression
            expression_list.insert(brace_index + idx + 1, '`')

        parsed_ = ''.join(expression_list)

        return re.sub(r'frac', '', parsed_)

class swWrite(Write):

    def __init__(self, mobject: Mobject, color=BLUEISHGREY, **kwargs):
        super().__init__(mobject, **kwargs)

        self.lag_ratio = 99999999
        self.stroke_color = color
        self.stroke_width = 1