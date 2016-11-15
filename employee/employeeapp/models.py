from django.db import models


class Departament(models.Model):
    """
    Defines a department int he company.
    Example: Accounting, HR, etc.
    """
    description = models.CharField(verbose_name='Descricao', max_length=50)

    def __str__(self):
        return self.description


class Employee(models.Model):
    """
    Defines a company employee
    """
    name = models.CharField(verbose_name='Nome', max_length=100)
    email = models.CharField(verbose_name='E-mail', max_length=100)
    departament = models.ForeignKey(Departament, verbose_name='Departamento', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
