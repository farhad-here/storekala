from django.urls import path
from .views import signup_view, login_view, logout_view, customer_panel, payment_view

urlpatterns = [
       path('signup/', signup_view, name='signup'),
       path('login/', login_view, name='login'),
       path('logout/', logout_view, name='logout'),
       path('panel/', customer_panel, name='customer_panel'),
       path('payment/', payment_view,    name='payment'),
]