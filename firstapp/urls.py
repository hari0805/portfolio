from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from firstapp.views import *

urlpatterns = [
    path('', Homeview.as_view(), name = 'homeview'),
    path('pdf', Download_Resume.as_view(), name = 'get_pdf'),

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
