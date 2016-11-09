from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeesSerializer


class EmployeesList(APIView):
    """
    Returns all employees in the database
    """
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeesSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeesDetails(APIView):
    """
    Read, Update and Delete an Employee
    """

    def get_object(self, pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employees = self.get_object(pk)
        serializer = EmployeesSerializer(employees)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employees = self.get_object(pk)
        serializer = EmployeesSerializer(employees, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employees = self.get_object(pk)
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)