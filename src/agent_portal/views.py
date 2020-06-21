from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import ListView, FormView, DetailView
from .models import CustomUser, Customer
from .forms import BatchCustomersDataForm, SingleCustomerDataForm, CustomerForm
from django.contrib.auth.forms import AuthenticationForm


class Homepage(View):
    '''
    Display Homepage and handle login
    '''

    def get(self, request):
        # Display Homepage on get request
        return render(request, 'homepage.html')

    def post(self, request):
        # Validate login credentials
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
        # Calling the base implementation first, then filtering with respect to agent
        return super().get_queryset().filter(agent=self.request.user.id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Adding a ModelForm to add a new customer
        context['form'] = SingleCustomerDataForm
        context['batchform'] = BatchCustomersDataForm
        return context


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'
    form_class = CustomerForm

    def get_form(self):
        form = self.form_class(instance=self.object)  # instantiate the form
        return form

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Adding a ModelForm to add a new customer
        context['form'] = self.get_form()
        return context


def add_a_customer(request):
    # Add a new customer by validating its data
    if request.method == 'POST':
        form = SingleCustomerDataForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'New customer is added successfully')
            return redirect('/dashboard')
        else:
            messages.info(
                request, 'ERROR occoured while validating the data. Please check data before entering')

    return redirect('/dashboard')


def add_batch_of_customers(request):
    # Add batch of customer via csv file
    if request.method == 'POST':
        form = BatchCustomersDataForm(
            request.POST, request.FILES)
        print('before checking the cond')
        if form.is_valid():
            form.process_data()
            messages.success(request, 'New customers are added successfully')
            return redirect('/dashboard')
        else:
            messages.info(
                request, 'ERROR occoured while loading data. Please check file before submitting')

    return redirect('/dashboard')


def update_customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        messages.success(request, 'Details updated successfully')
        return redirect(f'/customer_detail/{id}')

    else:
        messages.info(
            request, 'Error while validating the updated data, please check and try again')
        return redirect(f'/customer_detail/{id}')


def delete_customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()

    messages.success(request, 'Customer deleted successfully')
    return redirect('/dashboard')