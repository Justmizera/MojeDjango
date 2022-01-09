from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if request.method == "POST": #to oznacza że zrób coś jeśli user wejdzie i coś zrobi na stronie a nie tylko ją wyświetli
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
            
        else:
            messages.success(request, ("Błędna nazwa użytkownika lub login, spróbuj ponownie."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, ("Zostałeś wylogowany."))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST) #jeśli user wypełni formularz to wrzucamy go tutaj- to jest ten formularz klasyczny rozszerzony o dodatkowe pola w pliku forms.py
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password) #tym robimy autentykację użytkownika
            login(request, user)
            #tym od razu logujemy użytkownika, który się zarejestrował
            messages.success(request, ("Zostałeś zarejestrowany prawidłowo"))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form':form,})
     
