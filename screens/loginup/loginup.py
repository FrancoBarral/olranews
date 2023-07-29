from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from firebase.firebase_auth import login


class loginup(Screen):

    Builder.load_file("C:/Users/agust/OneDrive/Documentos/olraNews/tutorial-env/screens/loginup/loginup.kv")

    def accessApp(self):
        email = self.ids.email_login.text
        password = self.ids.password_login.text

        if login(email,password):
            self.manager.current = "home"
            print("Podes ingresar correctamente!")
        else:
            self.ids.email_login.text = ""
            self.ids.password_login.text = ""
            self.ids.labelErrorPassord.text = "Email or Password incorrect!"
            print("No existe el usuario")