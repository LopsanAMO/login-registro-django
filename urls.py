from django.conf.urls import include, url
from django.contrib import admin
from .views import Registrar, Login, Index
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registrar/', Registrar.as_view(), name='registrar'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^index/', Index.as_view(), name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
