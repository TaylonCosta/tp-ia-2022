import smtplib

from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import *

from monografia.forms import UserCreateForm


from email.message import EmailMessage

def Index(request):

    template_name = 'monografia/index.html'
    context = {}

    return render(request, template_name, context)

def CreateAccount(request):

    context = {}
    template_name = 'registration/cadastro_user.html'

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            try:
                NovoUser = None
                NovoUser = User()
                NovoUser.username = username
                NovoUser.set_password(password)
                NovoUser.email = email
                NovoUser.first_name = first_name
                NovoUser.last_name = last_name
                NovoUser.save()

                sender = f'taylon@minasvale.com'
                receiver = f'' + NovoUser.email + ''
                password = input(str("senha do server: "))
                msg = f'Conta criada no sistema de monografia com sucesso!'

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, receiver, msg)
                server.quit()


            except Exception as e:
                print(e)
        return redirect('login')

    else:
        form = UserCreateForm()

        context = {
            'form' : form
        }

    return render(request, template_name, context)