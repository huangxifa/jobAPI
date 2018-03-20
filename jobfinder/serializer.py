from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from jobfinder.models import JobList


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobList
        fields = '__all__'



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000