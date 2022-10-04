from argparse import Namespace
from django.urls import path
from emp.views import *
from django.conf import settings
from django.conf.urls.static import static




app_name = 'emp'
urlpatterns = [
    path('', EmpIndexView.as_view(),name='index'),
    path('empUpdate/<slug:pk>', EmpUpdateView.as_view(),name='emp-update'),
   



    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)