from .models import Employees
from .serializers import EmployeesSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response


class EmployeesList(APIView):
    """
    Returns all employees in the database
    """
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)


class EmployeesDetails(APIView):
    """
    Return single employee
    """
    def get_object(self, pk):
        try:
            return Employees.object.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeesSerializer(employee)
        return Response(serializer.data)