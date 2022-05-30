from rest_framework.serializers import ModelSerializer
from companies.models import Companies, TagLang


class CompanyBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'


class CompanyCreateModelSerializer(CompanyBaseModelSerializer):
    class Meta(CompanyBaseModelSerializer.Meta):
        fields = '__all__'


class CompanyDeleteModelSerializer(CompanyBaseModelSerializer):
    class Meta(CompanyBaseModelSerializer.Meta):
        fields = '__all__'


class TagLangBaseModelSerializer(ModelSerializer):
    class Meta:
        model = TagLang
        fields = (
            'tag_nation',
        )