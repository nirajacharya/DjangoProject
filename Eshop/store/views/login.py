from django.shortcuts import render, redirect,HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    return_url=None
    def get(self, request):
        Login.return_url=request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('homepage')
            else:
                error_message = "Password  Incorrect"
        else:
            error_message = "Email Or Password is Incorrect"

        return render(request, 'login.html', {'error': error_message})

class Logout(View):
    def get(self,request):
        request.session.clear()
        return redirect('loginpage')
