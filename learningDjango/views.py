from django.http import HttpResponse
from django.shortcuts import render

def signIn(request):
  return render(request, "sign_in.html")

def signUp(request):
  return render(request, "sign_up.html")
  
def successPage(request):
  return render(request, "success_page.html")
