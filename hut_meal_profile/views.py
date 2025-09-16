from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from hut_meal_profile.forms import LoginForm, UserAccountForm
from hut_meal_user.models import UserModel
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.



def login_page(request):
    print(request.user.is_authenticated)
    print(request.user)
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Login successfully completed.')
            return redirect("/")
        else:
            messages.info(request, 'The username or password is incorrect.')

    context = {
        "login_form": login_form
    }

    return render(request, "login.html", context)






@login_required(login_url='/login')
def account_main_page(request):
    print(1111)
    context = {}
    return render(request, 'account.html', context)






User = get_user_model()
def register_page(request):
    context = {}


    if request.user.is_authenticated :
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if user is None:
            raise Http404()
        register_form = UserAccountForm(request.POST or None,
                                    initial={'first_name': user.first_name, 'last_name': user.last_name,
                                             'phone': user.usermodel.phone, 'username': user.username,
                                             'email': user.email, 'address': user.usermodel.address,
                                             'company': user.usermodel.company})
        context['user']= user
    else:
        register_form = UserAccountForm(request.POST or None)


    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        phone = register_form.cleaned_data.get('phone')
        password = register_form.cleaned_data['password']
        address = register_form.cleaned_data.get('address')
        company = register_form.cleaned_data.get('company')
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is not None and user_obj.check_password(password):
            messages.info(request, 'The username or password is incorrect.')
            return redirect('/')

        else:
            new_user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)

            UserModel.objects.create(user_id=new_user.id)
            new_user.usermodel.phone = phone
            new_user.usermodel.address = address
            new_user.usermodel.company = company
            new_user.save()
            new_user.usermodel.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")

    context["register_form"]= register_form



    return render(request, "register.html", context)




def log_out_page(request):
    logout(request)
    return redirect('/login-page')




