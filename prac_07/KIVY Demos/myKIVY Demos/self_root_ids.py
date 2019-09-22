from kivy.app import App
from kivy.lang import Builder
import random

class IDDemo(App):
    def build(self):
        self.title = "Demoing the id attribute"
        self.root = Builder.load_file('self_root_ids.kv')
        return self.root

    def handle_pressed(self):
        if random.randint(1, 10) <= 5:
            self.root.ids.my_label.text = "ouch!!"
        else:
            self.root.ids.my_label.text = "stop that!!"

app = IDDemo()
app.run()
