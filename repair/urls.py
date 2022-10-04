from argparse import Namespace
from django.urls import path
from repair.views import *
# from repair.views import CreateRepairView




app_name = 'repair'
urlpatterns = [
    path('', RepairListView.as_view(),name='index'),
    path('detailRepair/<slug:slug>/', RepairDetailView.as_view(), name='repair-detail'),
    path('create', RepairCreateView.as_view(),name='repair-create'),
    path('recieveRepair/<slug:slug>', RepairRecieveUpdateView.as_view(),name='repair_recieve'),
    path('descRepair/<slug:slug>', RepairDescUpdateView.as_view(),name='repair_desc'),
    path('reviewRepair/<slug:slug>/', RepairReviewUpdateView.as_view(), name='repair-review'),
    path('workRepair/<slug:slug>/', RepairWorkUpdateView.as_view(), name='repair-work'),
    path('allRepair/', RepairMeListView.as_view(), name='repair-me'),
    path('staffRepair/', RepairStaffListView.as_view(), name='repair-staff'),
    path('myRepair/', RepairMyListView.as_view(), name='repair-my'),
    path('knowledgeRepair/', RepairKnowledgeistView.as_view(), name='repair-knowledge'),
    path('forwardRepair/<slug:slug>/', RepairForwardUpdateView.as_view(), name='repair-forward'),
  




    
]