"""whereWeStoppin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import roomsession.views
from roomsession.views import landing_page, room_creation, preferences_selection, results_page

urlpatterns = [
    path('', landing_page, name='home'),
    path('admin/', admin.site.urls),
    path("create_room", roomsession.views.create_room, name="create_room"),
    path("join_room", roomsession.views.join_room, name="join_room"),
    path("rooms/<room_id>", roomsession.views.access_room, name="access_room"),
    path("rooms/<room_id>/results", roomsession.views.access_room_results)
]
