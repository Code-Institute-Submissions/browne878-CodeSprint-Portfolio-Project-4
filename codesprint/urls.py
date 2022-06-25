"""codesprint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from planner import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects', views.projects, name='projects'),
    path('sprints/<str:project>', views.sprints, name='sprints'),
    path('cases/<str:sprint>', views.cases, name='cases'),
    path('accounts/', include('allauth.urls')),
    path('new-profile', views.new_profile, name='profile'),
    path('create-profile', views.create_profile, name='create-profle'),
    path('new-company', views.new_company, name='company'),
    path('create-company', views.create_company, name='create-company'),
    path('new-project', views.new_project, name='new-project'),
    path('new-sprint/<str:project>', views.new_sprint, name='new-sprint'),
    path('new-case/<str:sprint>', views.new_case, name='new-case'),
    path('edit-case/<str:sprint>/<case>', views.edit_case, name='edit-case'),
    path(
        'delete-case/<str:sprint>/<case>',
        views.delete_case,
        name='delete-case'
        )
]
