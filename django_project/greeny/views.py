from django.shortcuts import render, redirect
from django.http import HttpResponse
from secrets import token_hex
from os import environ
import json

def home(request):
    return render(request, 'greeny/home.html')

def about(request):
    return render(request, 'greeny/about.html', {"title":"Greeny - About Us"})

def privacy(request):
    return HttpResponse("<h1>Privacy</h1>")

def terms(request):
    return render(request, 'greeny/terms.html', {"title":"Greeny - Terms And Condition"})

def auth_func(request):
    request.session['state'] = token_hex(8)
    scopes = "+".join(environ.get('SCOPES').split(","))
    scopes = scopes.replace("'","")
    auth_uri = f"https://accounts.google.com/o/oauth2/v2/auth?state={request.session['state']}&response_type=code&client_id={environ.get('CLIENT_ID')}&redirect_uri={environ.get('DOMAIN')}/auth-resp&scope={scopes}&include_granted_scopes=true&prompt=select_account"
    print(auth_uri)
    return redirect(auth_uri)

def auth_resp(request):
    return HttpResponse("<h1>HI</h1>")
