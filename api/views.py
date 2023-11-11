from django.shortcuts import render
from rest_framework import viewsets
from .models import companyapi,employee
from .serializers import CompanySerializers,employeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewset(viewsets.ModelViewSet):
    queryset = companyapi.objects.all()
    serializer_class = CompanySerializers
    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
        try:
            company=companyapi.objects.get(pk=pk)
            emps=employee.objects.filter(company=company)
            emps_serializer=employeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except:
            return Response({'message':'The company You Are Looking For DoesNot Exists!!'})

class  employeeviewset(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeSerializer