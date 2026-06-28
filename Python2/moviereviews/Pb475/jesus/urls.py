from django.urls import path
from .import views

urlpatterns=[
    path('sign_up/',views.signup_view,name='signup_view'),
    path('login_vie/',views.login_view,name='login_view'),
    path('logout_view/',views.logout_view,name='logout_view')
]

# Browser URL → urls.py (path) → views.py (function) → template.html (page shown)
