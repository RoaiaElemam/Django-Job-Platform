from .views import job_list,job_detail
from django.urls import path
from .api import JobListApi,JobDetailApi

urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail),


    path('api/list',JobListApi.as_view()),
    path('api/list/<int:pk>',JobDetailApi.as_view()),

]