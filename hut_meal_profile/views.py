from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from hut_meal_profile.forms import LoginForm, UserAccountForm
from hut_meal_user.models import UserModel
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.



def login_page(request):
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
    context = {}
    return render(request, 'account.html', context)






User = get_user_model()
def register_page(request):
    if 'email' in request.POST:
        email = request.POST['email']
        first_name = request.POST['first_name']
        register_form = UserAccountForm(request.POST or None,initial={'email': email, 'first_name':first_name})
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
        password = register_form.cleaned_data['password']
        first_name = register_form.cleaned_data.get('first_name')
        last_name = register_form.cleaned_data.get('last_name')
        phone = register_form.cleaned_data.get('phone')
        address = register_form.cleaned_data.get('address')
        company = register_form.cleaned_data.get('company')
        user_obj = User.objects.filter(username=username).first()
        if user_obj is not None and user_obj.check_password(password):
            messages.info(request, 'The username or password is incorrect.')
            return redirect('/')
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)

            UserModel.objects.create(user_id=new_user.id, phone=phone, address=address, company=company)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")

    context["register_form"]= register_form
    return render(request, "register.html", context)




def log_out_page(request):
    logout(request)
    return redirect('/login-page')




