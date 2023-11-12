from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import JobSerializer
from .models import Job

#data---->jesson
@api_view(['GET'])
def job_list_api(request):
    jobs=Job.objects.all()
    data=JobSerializer(jobs,many=True).data
    return Response({'Jobs':data})

@api_view(['GET'])
def job_detail_api(request,id):
    job=Job.objects.get(id=id)
    data=JobSerializer(job).data
    return Response({'Job':data})
