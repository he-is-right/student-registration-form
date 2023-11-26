from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "base"
urlpatterns = [
    path("", views.HomePage, name="register"),
    path("completed", views.SuccessPage, name="success"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
