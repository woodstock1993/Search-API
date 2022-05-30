from .models import Companies, TagLang
from .serializers import CompanyBaseModelSerializer, TagLangBaseModelSerializer
from rest_framework import viewsets


class CompanyViewSet(viewsets.ModelViewSet):
    """
        작성자: 서재환
    """

    queryset = Companies.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CompanyBaseModelSerializer
        else:
            return CompanyBaseModelSerializer

    def create(self, request, *args, **kwargs):
        return super().create(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    """
        작성자: 서재환
    """

    queryset = TagLang.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TagLangBaseModelSerializer
        else:
            return TagLangBaseModelSerializer

    def create(self, request, *args, **kwargs):
        return super().create(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)