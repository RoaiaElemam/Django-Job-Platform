from .views import job_list,job_detail
from django.urls import path


urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_detail)

]