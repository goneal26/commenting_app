"""
URL configuration for commenting_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from commenting import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', views.commentpage, name='commentpage'), # comment posting/rendering url

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), 
        name='login'), # url for rendering the login page

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), 
        name='logout'),

    path('signup/', views.signup, name='signup'), 
    # didnt finish here but this url would've rendered the form for creating a new user

    path('', RedirectView.as_view(url='/login/')),
    # this would redirect the default path to the login page
]
