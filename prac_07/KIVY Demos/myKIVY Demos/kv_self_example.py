from kivy.app import App
from kivy.lang import Builder
class ButtonEventDemo(App):
    def build(self):
        self.title = "Button Event Demo"
        self.root = Builder.load_file('kv_self_example.kv')
        return self.root

    def press_button(self, button):
        print('app: ' + self)   # this is the app object
        print(str(button) + ' says "ouch!"')

ButtonEventDemo().run()
