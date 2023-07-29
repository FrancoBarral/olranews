from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from firebase.firebase_auth import verify_token
from screens.home.home import home


class main(Screen):
    Builder.load_file("C:/Users/agust/OneDrive/Documentos/olraNews/tutorial-env/screens/main/main.kv")

    def on_pre_enter(self):
        if self.check_user_token():
            screen_manager = self.parent

            screen_manager.switch_to(home())


    def check_user_token(self):
        from plyer import storagepath
        import os

        path = os.path.join(storagepath.get_documents_dir(), "user_token.txt")
        if os.path.exists(path):
            with open(path, "r") as f:
                data = f.read().split(",")
                if len(data) == 2:
                    user_id, token = data[0], data[1]

                    # Verificar si el token es válido utilizando Firebase Auth
                    try:
                        user = verify_token(token)
                        return True
                    except Exception as e:
                        print("Error al verificar el token:", e)

        return False