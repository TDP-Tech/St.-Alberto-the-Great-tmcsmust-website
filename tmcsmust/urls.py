"""tmcsmust URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'ST. ALBERTO THE GREAT TMCS-MUST'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Authenticate/', include('AuthenticationApp.urls')),
    path('Religion/', include('religionApp.urls')),
    path('malipo/', include('malipoApp.urls')),
    path('accounts/', include('accountApp.urls')),
    path('kwaya/', include('kwayaApp.urls')),
    path('Misa/Sadaka/', include('SadakaApp.urls')),
    path('materials/', include('MaterialsApp.urls')),
    path('Legio/', include('LegioApp.urls')),
    path('Karismatiki/', include('KarismatikiApp.urls')),
    path('MoyoMtakatifu/', include('MoyoMtakatifuWaYesuApp.urls')),
    path('Mipango/', include('MipangoNaFedhaApp.urls')),
    path('Leaders/', include('ClassLeadersApp.urls')),
    path('Chat/', include('ChatApp.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)