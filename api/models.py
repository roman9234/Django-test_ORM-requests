from django.db import models


class BranchOffice(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)


class Department(models.Model):
    name = models.CharField(max_length=128)
    floor = models.IntegerField()
    branch_office = models.ForeignKey(BranchOffice, related_name="departments", on_delete=models.SET_NULL, null=True)


class Employee(models.Model):
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, null=True)
    birth_date = models.DateTimeField(null=True)
    email = models.EmailField(max_length=128, null=True)
    department = models.ForeignKey(Department, related_name="employees", on_delete=models.CASCADE, null=True)
