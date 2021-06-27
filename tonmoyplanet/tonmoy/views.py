from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Home,About,Profile,Category,Portfolio,Workprocess,Education,Contact

def index(request):
    
    home=Home.objects.latest('updated')
    #about
    about=About.objects.latest('updated')
    profiles=Profile.objects.filter(about=about)
    #education
    education=Education.objects.latest('updated')
    categories=Category.objects.all()
    #portfolio
    portfolios=Portfolio.objects.all()
    #contact
    contact=Contact.objects.latest('updated')

    workprocess=Workprocess.objects.latest('updated')

    diction={'title':'welcome to tonmoyPlanet','home':home,'about':about,'profiles':profiles,'categories':categories,'portfolios':portfolios,'workprocess':workprocess,'education':education,'contact':contact }
    return render (request,'tonmoy/index.html',context=diction)
