from rest_framework import serializers
from .models import companyapi , employee

class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = companyapi
        fields = "__all__"


class employeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = "__all__"