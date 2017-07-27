# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .forms import RegForm, SigninForm
from models import User, Message, Comment

# Create your views here.
def index(request):
    return render(request, 'dashboardApp/index.html')

def signin(request):
    form=SigninForm()
    context={
        'form':form
    }
    return render(request, 'dashboardApp/signin.html', context)

def login(request):
    bound_form=SigninForm(request.POST)
    # print request.POST['email']
    user = User.objects.filter(email=request.POST['email'])
    if len(user)==1:
        request.session['user']=request.POST['email']

        currentUser = User.objects.get(email=request.session['user'])
        users = User.objects.all()
        context={
            'currentUser':currentUser,
            'users':users
        }

        return render(request, 'dashboardApp/dashboard.html', context)
    else:
        context={
            'form':bound_form,
            'error':"Email or Password were incorrect."
        }
        return render(request, 'dashboardApp/signin.html', context)
def signup(request):
    form=RegForm()
    context={
        'form':form
    }
    return render(request, 'dashboardApp/signup.html', context)



def register(request):
    bound_form=RegForm(request.POST)
    if bound_form.is_valid():
        alluser=User.objects.all()
        if len(alluser)==0:
            user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], level="admin", description="")

            request.session['user']=request.POST['email']

            currentUser = User.objects.get(email=request.session['user'])
            users = User.objects.all()
            context={
                'currentUser':currentUser,
                'users':users
            }

            return render(request, 'dashboardApp/dashboard.html', context)
        else:
            checkExists=User.objects.filter(email=request.POST['email'])
            if len(checkExists)>0:
                print "error"
                return render(request, 'dashboardApp/signup.html')
            else:
                user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], level="normal", description="")
                request.session['user']=request.POST['email']

                currentUser = User.objects.get(email=request.session['user'])
                users = User.objects.all()
                context={
                    'currentUser':currentUser,
                    'users':users
                }

                return render(request, 'dashboardApp/dashboard.html', context)
    else:
        context={
            'form':bound_form
        }
        return render(request, 'dashboardApp/signup.html', context)

def add(request):
    bound_form=RegForm(request.POST)
    if bound_form.is_valid():
        checkExists=User.objects.filter(email=request.POST['email'])
        if len(checkExists)>0:
            print "error"
            return render(request, 'dashboardApp/addUser.html')
        else:
            user=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], level="normal", description="")

            currentUser = User.objects.get(email=request.session['user'])
            users = User.objects.all()
            context={
                'currentUser':currentUser,
                'users':users
            }

            return render(request, 'dashboardApp/dashboard.html', context)
    else:
        context={
            'form':bound_form
        }
        return render(request, 'dashboardApp/addUser.html', context)


def dashboard(request):
    sessUser= request.session['user']
    print sessUser
    currentUser = User.objects.get(email=sessUser)
    users = User.objects.all()
    context={
        'currentUser':currentUser,
        'users':users
    }
    return render(request, 'dashboardApp/dashboard.html', context)

def addUser(request):
    return render(request, 'dashboardApp/addUser.html')

def edit(request):
    return render(request, 'dashboardApp/edit.html')

def delete(request, id):
    sessUser= request.session['user']
    currentUser = User.objects.get(email=sessUser)
    User.objects.get(id=id).delete()
    users = User.objects.all()
    context={
        'currentUser':currentUser,
        'users':users
    }
    return render(request, 'dashboardApp/dashboard.html', context)

def adminEdit(request, id):
    user=User.objects.get(id=id)
    context={
        'user':user
    }
    return render(request, 'dashboardApp/admin_edit.html', context)

def save(request):
    return render(request, 'dashboardApp/profile.html')

def logoff(request):
    request.session['user']=None
    return render(request, 'dashboardApp/index.html')
