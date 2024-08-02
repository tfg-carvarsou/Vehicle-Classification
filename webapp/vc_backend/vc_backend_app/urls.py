from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from vc_backend_app.views import VDImageCreateView, VDImageReadDeleteView

router = DefaultRouter()
router.register(r'snapzone', VDImageCreateView, basename='vdimage-create')
router.register(r'snapview', VDImageReadDeleteView, basename='vdimage-read-delete')

app_name = 'vc_backend_app'
urlpatterns = [
    path('detector/', include(router.urls)),
]

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)