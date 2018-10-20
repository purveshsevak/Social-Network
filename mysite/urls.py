from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from mysite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('home/', include('home.urls', namespace='home'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
