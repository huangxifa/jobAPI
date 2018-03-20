from rest_framework import generics

from jobfinder.models import JobList
from jobfinder.serializer import JobSerializer, LargeResultsSetPagination


class Jobdetail(generics.ListAPIView, generics.RetrieveAPIView):
    queryset = JobList.objects.all()
    serializer_class = JobSerializer
    pagination_class = LargeResultsSetPagination
    filter_fields = '__all__'