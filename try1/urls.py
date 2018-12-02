"""try1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from try1 import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^welcome_(?P<username>\D+)$', views.base, name='base'),
    url(r'^about', views.about, name='about'),
    url(r'^(?P<username>\D+)/about', views.about2, name='about2'),
    url(r'^church/', include('church.urls', namespace='church')),
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^password_reset', auth_views.PasswordResetView.as_view(template_name="reset.html"), name='password_reset'),
    url(r'^password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="resetdone.html"), name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>\S+)/(?P<token>\S+)/', auth_views.PasswordResetConfirmView.as_view(template_name="resetconfrim.html"), name='password_reset_confirm'),
    url(r'^password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="resetcomplete.html"), name='password_reset_complete'),
    url(r'^(?P<username>\D+)/contacts', views.contacts, name='contacts'),
    url(r'^2contacts', views.contacts2, name='contacts2'),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
