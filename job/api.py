from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import filters

from .serializer import JobSerializer
from .models import Job

#data---->jesson
#@api_view(['GET'])
#def job_list_api(request):
   # jobs=Job.objects.all()
    #data=JobSerializer(jobs,many=True).data
    #return Response({'Jobs':data})

#@api_view(['GET'])
#def job_detail_api(request,id):
 #   job=Job.objects.get(id=id)
  #  data=JobSerializer(job).data
   # return Response({'Job':data})



class JobListApi(generics.ListCreateAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilters]
    filterset_fields = ['title', 'job_type','vacancy']
    search_fields = ['title', 'description']
    ordering_fields = ['salary_start', 'salary_end','experince']





class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Job.objects.all()
    serializer_class=JobSerializer