import kivy

kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.logger import Logger
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.accordion import Accordion, AccordionItem
from home_core.models import Category, Device
from .light_widget import LightWidget

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class HomeMainApp(App):

    def build(self):
        for device in Device.objects.order_by('pin'):
            GPIO.setup(device.pin, GPIO.OUT)
          
        screen = Accordion()
        for category in Category.objects.order_by('order'):
            item = AccordionItem(title=category.label)
            screen.add_widget(item)
            item.add_widget( self.buildCategory(category))
        return screen

    def buildCategory(self, category):
        container = StackLayout()

        for device in category.devices:
            state = 'down' if device.is_on else 'normal'
            GPIO.output(device.pin, device.is_on)

            def callback(widget):
                device = widget.device
                is_on = not device.is_on
                Device.objects(id=widget.device.id).update(is_on=is_on)
                device.is_on = is_on
                Logger.info("Application: Seting pin %d to %s" % (device.pin, is_on))
                GPIO.output(device.pin, is_on)


            button = ToggleButton(text=device.label,
                                width=80,
                                size_hint=(None, 0.15),
                                state=state,
                                on_press=callback
            )

            button.device = device
            container.add_widget( button)
            Logger.info("Application: Adding device %s on" % device.label)

            #container.add_widget( LightWidget())

        return container

def startup():
    HomeMainApp().run()
