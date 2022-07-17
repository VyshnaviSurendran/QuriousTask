"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from TestApp import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('addmanager',views.addManager,name='addManager'),
    path('viewmanager',views.viewManager,name='viewManager'),
    path('editmanager/<int:id>',views.editManager,name='editManager'),
    path('updatemanager/<int:id>',views.updateManager,name='updateManager'),
    path('addcoordinator',views.addCoordinator,name='addCoordinator'),
    path('viewcoordinator',views.viewCoordinator,name='viewCoordinator'),
    path('editcoordinator/<int:id>',views.editCoordinator,name='editCoordinator'),
    path('updatecoordinator/<int:id>',views.updateCoordinator,name='updateCoordinator'),
    path('addinspector',views.addInspector,name='addInspector'),
    path('viewinspector',views.viewInspector,name='viewInspector'),
    path('editinspector/<int:id>',views.editInspector,name='editInspector'),
    path('updateinspector/<int:id>',views.updateInspector,name='updateInspector'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('adminhome',views.adminHome,name='adminHome'),
    path('coordinatorhome',views.coordinatorHome,name='coordinatorHome'),
    path('coordinatoraddinspector',views.coordinatorAddInspector,name='coordinatorAddInspector'),
    path('coordinatorviewinspector',views.coordinatorViewInspector,name='coordinatorViewInspector'),
    path('coordinatoreditinspector/<int:id>',views.coordinatorEditInspector,name='coordinatorEditInspector'),
    path('coordinatorupdateinspector/<int:id>',views.coordinatorUpdateInspector,name='coordinatorUpdateInspector'),
    path('viewclientmaster',views.viewClient,name='viewClient'),
    path('jobmaster',views.jobSchedule,name='jobSchedule'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)