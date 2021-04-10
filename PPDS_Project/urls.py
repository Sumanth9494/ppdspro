"""PPDS_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.views.static import serve
from PPDS import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ppdspro-preproduction.azurewebsites.net', views.home),
    path('ownerRegister/', views.url_path_link),
    path('ownerLogin/', views.url_path_link),
    path('userLogin/', views.url_path_link),
    path('userRegister/',views.url_path_link),
    path('authorityLogin/', views.url_path_link),
    path('ehcsLogin/', views.url_path_link),
    path('ownerHome/', views.ownerHome_view,name='odata'),
    path('ownerUPD/', views.ownerUPD_view),
    path('ownerVPD/', views.ownerVPD_view),
    path('ownerSAC/', views.ownerSAC_view),
    path('ownerVAC/', views.ownerVAC_view),
    path('ownerSacForm/', views.ownerSacForm),
    path('ownerActivate/<id>/', views.ownerActivate),
    path('ownerDeactivate/<id>/', views.ownerDeactivate),
    path('userActivate/<id>/', views.userActivate),
    path('userDeactivate/<id>/', views.userDeactivate),
    path('userHome/', views.userHome_view),
    path('userSearchPatient/', views.userSearchPatient_view),
    path('userSKR/', views.userSKR_view),
    path('userDwld/', views.userDownload_view),
    path('searchKey/', views.searchKey),
    path('viewFD/<id>/', views.viewFD),
    path('sendKeyRequest/<id>/<patient_name>/', views.sendKeyRequest),
    path('downloadFile/<patient_id>/', views.downloadFile),
    path('authorityHome/', views.authorityHome_view),
    path('authorityVO/', views.authorityVO_view),
    path('authorityVU/', views.authorityVU_view),
    path('authoritySK/', views.authoritySK_view),
    path('authorityAttacker/', views.authorityAttacker_view),
    path('generateKey/<id>', views.generateKey),
    path('ehcsHome/',views.ehcsHome_view),
    path('ehcsPatient/',views.ehcsPatient_view),
    path('ehcsSAC/',views.ehcsSAC_view),
    path('ehcsTransaction/',views.ehcsTransaction_view),
    path('ehcsSRK/',views.ehcsSKR_view),
    path('ehcsAttackers/',views.ehcsAttackers_view),
    path('ehcsDC/',views.ehcsDC_view),
    path('ehcsSRC/',views.ehcsSRC_view)

]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve,
            {'document_root':settings.MEDIA_ROOT}),
    ]


