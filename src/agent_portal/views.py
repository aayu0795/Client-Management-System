from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth



class Homepage(View):

    def get(self, request):
        return render(request, 'homepage.html')


    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/dashboard")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/')

