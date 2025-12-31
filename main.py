from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1) # Kırmızı karakter
            self.rect = Rectangle(pos=(100, 100), size=(100, 100))
        Window.bind(on_touch_down=self.jump)

    def jump(self, instance, touch):
        self.rect.pos = (self.rect.pos[0], self.rect.pos[1] + 50) # Zıplama

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    MyApp().run()
    
