from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.factory import Factory

class HomeScreen(Screen):
    pass

class InputOne(Screen):
    pass


class MyBanner(MDApp):
    pass


# kv = Builder.load_file("main.kv")

class MainApp(MDApp):



    def build(self):
        self.root = Builder.load_file("main.kv")

    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name



if __name__ == "__main__":
    MainApp().run()