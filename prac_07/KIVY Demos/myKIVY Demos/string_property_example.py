from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

class MVCDemo(App):
    message = StringProperty()

    def build(self):
        self.title = "Simple MVC Demo"
        self.root = Builder.load_file('string_property_example.kv')
        return self.root

    def handle_press(self):
        self.message = self.root.ids.user_input.text

MVCDemo().run()
