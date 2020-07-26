from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class SignUp(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # sending entered data to sign up forms if error occured
        input_data = {'fname': fname, 'lname': lname, 'phone': phone, 'email': email}
        customer = Customer(first_name=fname, last_name=lname, phone=phone, email=email, password=password)
        # checking error if any
        error_message = self.validate_customer(customer)

        if not error_message:
            # saving user to database and creating hash password
            customer.password = make_password(customer.password)
            customer.register_new_user()
            return redirect('homepage')
        else:
            context = {
                'error': error_message,
                'input_data': input_data
            }
            return render(request, 'signup.html', context)

    def validate_customer(self, customer):
        # validating form
        error_message = None
        if not customer.first_name:
            error_message = "Firstname is required"
        elif len(customer.first_name) < 4:
            error_message = "Firstname must be more than 4 char long"
        elif not customer.last_name:
            error_message = "Lastname is required"
        elif len(customer.last_name) < 3:
            error_message = " Lastname must be more than 3 char long"
        elif not customer.phone:
            error_message = "Phone  is required"
        elif len(customer.phone) < 10:
            error_message = "Phone must be more than 10 char long"
        elif not customer.email:
            error_message = "Email  is required"
        elif not customer.password:
            error_message = "Password  is required"
        elif len(customer.password) < 4:
            error_message = "Password must be more than 4 char long"
        elif customer.user_exist():
            error_message = "Email Address Already Registered"

        return error_message
