from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from vc_backend_app.views import VDImageListCreateView, VDImageRetrieveDeleteView
from vc_backend_app.views import VCImageListCreateView, VCImageRetrieveDeleteView

vdrouter = DefaultRouter()
vdrouter.register(r'snapzone', VDImageListCreateView, basename='vdimage-list-create')
vdrouter.register(r'snapview', VDImageRetrieveDeleteView, basename='vdimage-retrieve-delete')
vcrouter = DefaultRouter()
vcrouter.register(r'snapzone', VCImageListCreateView, basename='vcimage-list-create')
vcrouter.register(r'snapview', VCImageRetrieveDeleteView, basename='vcimage-retrieve-delete')

app_name = 'vc_backend_app'
urlpatterns = [
    path('detector/', include(vdrouter.urls)),
    path('classifier/', include(vcrouter.urls)),
]

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)