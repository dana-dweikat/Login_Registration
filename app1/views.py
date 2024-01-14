from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

import bcrypt

def index(request):
    return render(request, "index.html") 


def success(request):
    first_name = request.session.get('first_name')

    if first_name:
        return render(request, 'welcome.html')
    else:
        messages.error(request, 'User should Login.')
        return redirect('app1:index')
        

def register(request):
    if request.method == "POST":
        
        errors = Users.objects.validate(request.POST)
        
        # There is some errors
        if len(errors) > 0:
            for error in errors.values():
                messages.error(request, error)
            return redirect('app1:index')
        
        first_name_form = request.POST['first_name']
        last_name_form = request.POST['last_name']
        email_form = request.POST['email']
        password_form = request.POST['password1']
        confirm_password_form = request.POST['password2']
        
        if password_form == confirm_password_form:
            hash_password = bcrypt.hashpw(password_form.encode(), bcrypt.gensalt()).decode()
            
            new_user =Users.objects.create(
                first_name=first_name_form,
                last_name = last_name_form,
                email=email_form,
                password=hash_password)
            
            context = {
                'type': 'registered'    
            }
            
            request.session['first_name'] = new_user.first_name
            return render(request, 'welcome.html', context)

        # if password didn't match
        else:
            messages.error(request, 'Password not match.')
            return redirect('app1:index')



def login(request):
    if request.method == "POST":
        email_form = request.POST['email']
        password_form = request.POST['password1']
        
        users = Users.objects.filter(email=email_form)
        
        if len(users) == 0:
            messages.error(request, "Email doesn't exist.")
            return render(request, 'index.html')
        
        if bcrypt.checkpw(password_form.encode(), users.first().password.encode()):
            request.session['first_name'] = users.first().first_name
            context = {
                'type': 'Logged In'
            }
            return render(request, 'welcome.html', context)
        # if password is wrong
        else:
            messages.error(request, 'Password not correct.')
            return redirect('app1:index')



def logout(request):
    request.session.flush()
    return redirect('app1:index')