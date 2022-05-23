from .models import Companies
from rest_framework.viewsets import ModelViewSet
from .serializers import CompanyModelSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanyModelSerializer


# post_list = CompanyViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# post_detail = CompanyViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })