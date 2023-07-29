from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from screens.loginup.loginup import loginup
from screens.signup.signup import signup
from screens.main.main import main
from screens.home.home import home



class MainApp(MDApp):
    def build(self):
        Window.size = (414,600)

        screenManage = ScreenManager()

        
        screenManage.add_widget(main(name="main"))
        screenManage.add_widget(loginup(name="loginup"))
        screenManage.add_widget(signup(name="signup"))
        screenManage.add_widget(home(name="home"))


        return screenManage



MainApp().run()