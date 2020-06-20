from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import ListView, FormView, DetailView
from .models import CustomUser, Customer
from .forms import BatchdataForm


class Homepage(View):
    '''
    Display Homepage and handle the login
    '''

    def get(self, request):
        return render(request, 'homepage.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, f"You are signed in as {username}")
            return redirect("/dashboard")
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect('/')


class Dashboard(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'dashboard.html'

    def get_queryset(self):
        # Calling the base implementation first, then filtering with agent
        return super().get_queryset().filter(agent=self.request.user.id)


class CustomerDetailView(DetailView):
    model = Customer
    template_name = '/customer_detail.html'


def add_a_customer(request):

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        contact = request.POST['contact']

        agent = CustomUser.objects.get(id=request.user.id)
        Customer.objects.create(agent=agent, name=name,
                                age=age, gender=gender, contact=contact)
        return redirect('/dashboard')

    return redirect('/dashboard')


class BatchdataView(FormView):
    template_name = 'batchprocessing.html'
    form_class = BatchdataForm
    success_url = '/batch_customer_data'

    def form_valid(self, form):
        form.process_data()
        return super().form_valid(form)
