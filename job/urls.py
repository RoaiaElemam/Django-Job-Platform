from .views import job_list,job_detail
from django.urls import path
from .api import job_list_api,job_detail_api,JobListApi

urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail),


    path('api/list',JobListApi.as_view()),
    path('api/list/<int:id>',job_detail_api),

]