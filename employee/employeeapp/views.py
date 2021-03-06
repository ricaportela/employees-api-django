from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response


class EmployeeList(APIView):
    """
    Returns all Employee in the database
    """

    def get(self, request):
        """
        Get Employee
        """
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post Employee
        """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)

class EmployeeDetails(APIView):
    """
    Return single employee
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=204)
