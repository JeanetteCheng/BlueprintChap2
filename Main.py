from kivy.app import App
from kivy.base import EventLoop
from kivy.config import Config
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton



class CanvasWidget(Widget):
    line_width= 2
    def on_touch_down(self, touch):
        for widget in self.children:
            widget.on_touch_down(touch)

        with self.canvas:
            touch.ud['current_line'] =Line(points= (touch.x, touch.y), width=2)

        if Widget.on_touch_down(self, touch):
            return

    def on_touch_move(self, touch):
        if 'current_line' in touch.ud: #ud= user data
            touch.ud ['current_line'].points += (touch.x, touch.y)

    def set_color(self, new_color):
        self.canvas.add(Color(*new_color))

    def set_line_width(self, line_width='Normal'):
        self.line_width = {'Thin': 2, 'Normal': 3, 'Thick': 5}[line_width]

    def clear_canvas(self):
        saved = self.children[:]
        #the [:] operation is an array copy (create a new array with these same element.

        self.canvas.clear()
        self.canvas.children = [widget.canvas for widget in self.children]


class PaintApp(App):
    def build(self):
        EventLoop.ensure_window()
        if EventLoop.ensure_window.__class__.__name__.endswith('Pygame'):
            try:
                from pygame import mouse

                a, b = pygame_compile_cursor()
                mouse.set_cursor((24, 24), (9, 9), a, b)
            except:
                pass

        self.canvas_widget = CanvasWidget()
        self.canvas_widget.set_color(get_color_from_hex ('#000000'))

        return self.canvas_widget


class RadioButton(ToggleButton):
    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)

class LineWidthButton(Widget):
    line_width = 2

    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud['current_line'] = Line(
                points= (touch.x, touch.y), width=self.line_width)





if __name__ == '__main__':
 # ??
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')  #16:9

    Config.set('graphics', 'resizable', '0')

    Config.set('input', 'mouse', 'mouse,deisable_multitouch')


    from kivy.core.window import Window
    Window.clearcolor = get_color_from_hex ('#FFFFFF')

    PaintApp() .run()


