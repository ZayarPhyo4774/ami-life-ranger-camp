from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('know-insurance/', views.know_insurance, name='know_insurance'),
    path('file-claim/', views.file_claim, name='file_claim'),
    path('get-quote/', views.get_quote, name='get_quote'),
    path('coverage-details/', views.coverage_details, name='coverage_details'),
    path('our-commitment/', views.ourCommitment, name='our_commitment'),
    path('policy-docs/', views.policydocs, name='policydocs'),
]
