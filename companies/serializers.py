from rest_framework.serializers import ModelSerializer
from companies.models import Companies


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'
