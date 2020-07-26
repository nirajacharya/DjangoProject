from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    else:
        products = Product.get_all_products()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'index.html', context)


def validate_customer(customer):
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


def register_user(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('password')
    # sending entered data to sign up forms if error occured
    input_data = {'fname': fname, 'lname': lname, 'phone': phone, 'email': email}
    customer = Customer(first_name=fname, last_name=lname, phone=phone, email=email, password=password)
    # checking error if any
    error_message = validate_customer(customer)

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


def signup(request):
    if request.method == 'GET':
        print('get method')
        return render(request, 'signup.html')
    else:
        return register_user(request)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = "Password  Incorrect"
        else:
            error_message = "Email Or Password is Incorrect"

        return render(request, 'login.html', {'error': error_message})