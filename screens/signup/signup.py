from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from firebase.firebase_auth import signin,login



class signup(Screen):
    Builder.load_file("C:/Users/agust/OneDrive/Documentos/olraNews/tutorial-env/screens/signup/signup.kv")


    def signupUser(self):
        username = self.ids.username_signin.text
        email = self.ids.email_signin.text
        password = self.ids.password_signin.text

        if signin(username,email,password):
            print("Se registro correctamente!")
            if login(email,password):
                self.manager.current = "home"
        
        else:
            print("No fue posible crear el usuario!")
            self.ids.labelErrorSignin.text = "Email or User already created!"