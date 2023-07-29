import pyrebase
from firebase_admin import auth as authFirebase
import firebase_admin
from firebase_admin import credentials

# Ruta al archivo JSON de configuración de Firebase
cred = credentials.Certificate("C:/Users/agust/OneDrive/Documentos/olraNews/tutorial-env/firebase/olranews-firebase-adminsdk-fvyjr-568e8e8055.json")
firebase_admin.initialize_app(cred)

firebaseConfig = {
    "apiKey": "AIzaSyB7icVOYRbE4J0pRSHQiMzNrjAvPV1kGSs",
  "authDomain": "olranews.firebaseapp.com",
  "projectId": "olranews",
  "storageBucket": "olranews.appspot.com",
  "messagingSenderId": "664655658645",
  "appId": "1:664655658645:web:c1dca1ec4470b46f7fe59c",
  "measurementId": "G-H27GD4Q2YF",
  "databaseURL": "https://olranews-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def login(email,password):
    print("Log in...")
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        store_user_token(login['localId'], login['idToken'])
        print(f"localid: {login['localId']}")
        print("############################")
        print(f"idToken: {login['idToken']}")
        print("Successfuly")
        return 1
    except:
        print("Invalid email or password")
        return 0
        

def signin(username,email,password):

    print("Sing in...")

    try:
        user = authFirebase.create_user(display_name=username,email=email,password=password)

        return 1
    except:
        print("Email already exist")
        return 0
    return

def store_user_token(user_id, token):
    from plyer import storagepath
    import os

    path = os.path.join(storagepath.get_documents_dir(),"user_token.txt")
    print(path)
    with open(path, "w") as f:
        f.write(f"{user_id},{token}") 

def verify_token(token):
    return authFirebase.verify_id_token(token)