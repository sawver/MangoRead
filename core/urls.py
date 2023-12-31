"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from MangoRead.views import MangaCardsAPIViewSet, AddReviewView
from users.views import UserRegistrationViewSet, UserAuthenticationViewSet, UserLogoutAPIViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/mangacards/', MangaCardsAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/mangacards/<int:id>/', MangaCardsAPIViewSet.as_view({
        'get': 'retrieve', 'post': 'update', 'delete': 'destroy'
    })),
    path('api/v1/registration/', UserRegistrationViewSet.as_view({'get': 'list', 'post': 'post'})),
    path('api/v1/authentication/', UserAuthenticationViewSet.as_view({'get': 'list', 'post': 'post'})),
    path('api/v1/add-review/', AddReviewView.as_view()),
    path('api/v1/logout/', UserLogoutAPIViewSet.as_view({'get': 'list'}))
]
