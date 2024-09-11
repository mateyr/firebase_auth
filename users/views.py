from django.shortcuts import render
import os
import pyrebase

config = {
    "apiKey": "AIzaSyDODdAaKjeUDaLsfm-t-nFLBFFEPYjo44Y",
    "authDomain": "autentificacion-de-animales.firebaseapp.com",
    "databaseURL": "https://autentificacion-de-animales.firebaseio.com",
    "projectId": "autentificacion-de-animales",
    "storageBucket": "autentificacion-de-animales.appspot.com",
    "messagingSenderId": "135378187853",
    "appId": "1:135378187853:web:955a63790002c3fb4a4e04",
    "measurementId": "G-L13XR3G9LB",
}

# Initialising database,auth and firebase for further use
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
# database = firebase.database()


def signIn(request):
    return render(request, "Login.html")


def home(request):
    return render(request, "Home.html")


def postsignIn(request):

    email = request.POST.get("email")
    pasw = request.POST.get("pass")
    try:
        # if there is no error then signin the user with given email and password
        user = auth.sign_in_with_email_and_password(email, pasw)
    except:
        message = "Invalid Credentials!!Please ChecK your Data"
        return render(request, "Login.html", {"message": message})
    session_id = user["idToken"]
    request.session["uid"] = str(session_id)
    return render(request, "Home.html", {"email": email})


# def logout(request):
#     try:
#         del request.session["uid"]
#     except:
#         pass
#     return render(request, "Login.html")


def signUp(request):
    return render(request, "Registration.html")


def postsignUp(request):
    email = request.POST.get("email")
    passs = request.POST.get("pass")
    name = request.POST.get("name")
    try:
        # creating a user with the given email and password
        user = auth.create_user_with_email_and_password(email, passs)
        uid = user["localId"]
        idtoken = request.session["uid"]
        # print(uid)
    except Exception as e:
        print(f"Exception: {e}")
        return render(request, "Registration.html")
    return render(request, "Home.html")
