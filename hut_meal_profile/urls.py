from django.urls import path

from .views import login_page, register_page, log_out_page, account_main_page

app_name = 'hut_meal_profile'

urlpatterns = [
    path('login-page', login_page, name='login_page'),
    path('account', account_main_page, name='account_main_page'),
    path('register-page', register_page, name='register_page'),
    path('log-out-age', log_out_page, name='log_out_page'),
]