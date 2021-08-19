import re
from functools import reduce
from time import sleep

from Core.Console.Colors import Colors 
from Core.Console.Effects import Effects

class TextContext:
    def __init__(
        self,
        tag = None,
        foreground = Colors.FOREGROUND_NONE,
        background = Colors.BACKGROUND_NONE,
        effect = Effects.NONE
    ):
        self.tag = tag
        self.foreground = foreground
        self.background = background
        self.effect = effect

    def __or__(self, other):
        if self.foreground == Colors.FOREGROUND_NONE:
            self.foreground = other.foreground
        if self.background == Colors.BACKGROUND_NONE:
            self.background = other.foreground
        if self.effect == Effects.NONE:
            self.effect = other.effect
        return self


class Text:
    TAGS = {
        '<>'        :   TextContext('<>', Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.NONE),
        'b'         :   TextContext('b', Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.BOLD),
        't'         :   TextContext('t', Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.THIN),
        'i'         :   TextContext('i', Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.ITALIC),
        'u'         :   TextContext('u', Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.UNDERLINE),
        'blink'     :   TextContext('blink', Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.BLINK),
        'blinkf'    :   TextContext('blinkf', Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.BLINK_FAST),
        's'         :   TextContext('s', Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.SWAP),

        'black'     :   TextContext('black', Colors.FOREGROUND_BLACK, Colors.BACKGROUND_NONE, Effects.NONE),
        'red'       :   TextContext('red', Colors.FOREGROUND_RED, Colors.BACKGROUND_NONE, Effects.NONE),
        'green'     :   TextContext('green', Colors.FOREGROUND_GREEN, Colors.BACKGROUND_NONE, Effects.NONE),
        'yellow'    :   TextContext('yellow', Colors.FOREGROUND_YELLOW, Colors.BACKGROUND_NONE, Effects.NONE),
        'blue'      :   TextContext('blue', Colors.FOREGROUND_BLUE, Colors.BACKGROUND_NONE, Effects.NONE),
        'purple'    :   TextContext('purple', Colors.FOREGROUND_PURPLE, Colors.BACKGROUND_NONE, Effects.NONE),
        'cian'      :   TextContext('cian', Colors.FOREGROUND_CIAN, Colors.BACKGROUND_NONE, Effects.NONE),
        'white'     :   TextContext('white', Colors.FOREGROUND_WHITE, Colors.BACKGROUND_NONE, Effects.NONE),
    
        'bgblack'   :   TextContext('bgblack', Colors.FOREGROUND_NONE, Colors.BACKGROUND_BLACK, Effects.NONE),
        'bgred'     :   TextContext('bgred', Colors.FOREGROUND_NONE, Colors.BACKGROUND_RED, Effects.NONE),
        'bggreen'   :   TextContext('bggreen', Colors.FOREGROUND_NONE, Colors.BACKGROUND_GREEN, Effects.NONE),
        'bgyellow'  :   TextContext('bgyellow', Colors.FOREGROUND_NONE, Colors.BACKGROUND_YELLOW, Effects.NONE),
        'bgblue'    :   TextContext('bgblue', Colors.FOREGROUND_NONE, Colors.BACKGROUND_BLUE, Effects.NONE),
        'bgpurple'  :   TextContext('bgpurple', Colors.FOREGROUND_NONE, Colors.BACKGROUND_PURPLE, Effects.NONE),
        'bgcian'    :   TextContext('bgcian', Colors.FOREGROUND_NONE, Colors.BACKGROUND_CIAN, Effects.NONE),
        'bgwhite'   :   TextContext('bgwhite', Colors.FOREGROUND_NONE, Colors.BACKGROUND_WHITE, Effects.NONE)
    }
    TAGS_REG = rf"{reduce(lambda prev, cur: f'{prev}|<{cur}>|</{cur}>', TAGS)}" 

    def __init__(self, text : str) -> None:
        self.ascii = str()
        ctxs = [TextContext(Colors.FOREGROUND_NONE, Colors.BACKGROUND_NONE, Effects.DEFAULT )]

        tag = re.search(Text.TAGS_REG, text)
        if not tag:
            self.ascii = text
        while tag:  
            ctx = TextContext()
            value = tag.group(0)
            if value[1] != '/':
                if value[1:-1:] not in Text.TAGS.keys(): raise Exception(f"Undefined tag: {value}")
                base_ctx = Text.TAGS[value[1:-1:]]
                ctx = TextContext(base_ctx.tag, base_ctx.foreground, base_ctx.background, base_ctx.effect)
                ctxs.append(ctx | ctxs[-1])
                self.ascii += text[:tag.start():]
                self.ascii += ctx.foreground + ctx.background + ctx.effect
                text = text[tag.start() + len(value)::]
            else:
                if value[2:-1:] not in Text.TAGS.keys(): raise Exception(f"Undefined tag: {value}")
                if value[2:-1:] != ctxs[-1].tag: raise Exception(f"Found alone close tag: {value}")
                ctxs.pop(-1)
                ctx = ctxs[-1]
                self.ascii += text[:tag.start():]
                self.ascii += ctx.foreground + ctx.background + ctx.effect
                text = text[tag.start() + len(value)::]
            tag = re.search(Text.TAGS_REG, text)
        ctx = ctxs[-1]
        self.ascii += ctx.foreground + ctx.background + ctx.effect
        self.ascii += text

    def __str__(self) -> str:
        return self.ascii
