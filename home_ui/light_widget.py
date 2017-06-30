from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line

class LightWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]



    """
    def _a_init__(device):
        ToggleButton.__init__(text=device.label)

    def on_touch_down(self, touch):
        print 'hey'
        for device in category.devices:
            state = 'down' if device.is_on else 'normal'
            container.add_widget(
                ToggleButton(text=device.label,
                             width=80,
                             size_hint=(None, 0.15),
                             state=state,
                             on_press=callback
                )
            )
"""
