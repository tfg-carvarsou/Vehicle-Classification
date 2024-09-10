from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from vc_backend_app.views import VDImageListCreateView, VDImageRetrieveDeleteView
from vc_backend_app.views import VCImageListCreateView, VCImageRetrieveDeleteView 
from vc_backend_app.admin import AdminVDImageDeleteAllView, AdminVCImageDeleteAllView, AdminImageDeleteAllView

vd_router = DefaultRouter()
vd_router.register(r'snapzone', VDImageListCreateView, basename='vdimage-list-create')
vd_router.register(r'snapview', VDImageRetrieveDeleteView, basename='vdimage-retrieve-delete')
vd_router.register(r'', AdminVDImageDeleteAllView, basename='admin-vdimage-delete-all')
vc_router = DefaultRouter()
vc_router.register(r'snapzone', VCImageListCreateView, basename='vcimage-list-create')
vc_router.register(r'snapview', VCImageRetrieveDeleteView, basename='vcimage-retrieve-delete')
vc_router.register(r'', AdminVCImageDeleteAllView, basename='admin-vcimage-delete-all')
root_router = DefaultRouter()
root_router.register(r'', AdminImageDeleteAllView, basename='admin-image-delete-all')

app_name = 'vc_backend_app'
urlpatterns = [
    path('detector/', include(vd_router.urls)),
    path('classifier/', include(vc_router.urls)),
    path('root/', include(root_router.urls)),
]

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)