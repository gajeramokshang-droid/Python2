from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]

# અહીં name 'signup_view' છે.

# Templates માં {% url 'signup' %} લખ્યું હશે.

# Django એ 'signup' શોધે છે, પણ urls.py માં 'signup_view' છે → NoReverseMatch error.