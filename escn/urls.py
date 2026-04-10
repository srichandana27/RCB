from django.urls import path
from . import  views
urlpatterns = [
    path('',views.index,name="home"),
    path('register',views.register,name="register"),
    path('pin generation',views.pin_gen,name="pin"),
    path('validate',views.validate,name="validate"),
    path("balance",views.check_balance,name="bal"),
    path('deposit',views.deposit,name="deposit"),
    path('with',views.withdraw,name="withdraw"),
    path('transfer',views.acc_transfer,name="transfer"),
]