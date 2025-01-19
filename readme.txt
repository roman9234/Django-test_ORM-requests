Нужен ipython !

Запуск консоли
python manage.py shell

Импортирование моделей
from api.models import BranchOffice, Department, Employee
from random import randint, choice
from datetime import datetime

---- Заполнение данными ----

---- Филиалы

names = ["Филиал на Тверской","Филиал на Большой Ордынке","Филиал в Санкт-Петербурге"]
addresses = ["Москва, Тверская улица, 22","Москва, улица Большая Ордынка, 38с1","Санкт-Петербург, Чкаловский проспект, 23"]
for i in range(len(names)):
    branch = BranchOffice(name=names[i],address=addresses[i])
    branch.save()

for branch in BranchOffice.objects.all():
    print(branch.pk)



---- Отделы

types = ["продаж", "связей с общественностью", "маркетинга", "администрации", "кадров", "бухгалтерии", "безопасности", "логистики", "контроля качества"]
for branch_pk in range(1,3+1):
    q = randint(2,5)
    for i in range(q):
        branch = BranchOffice.objects.get(pk=branch_pk)
        floor = randint(2,30)
        name = f"Отдел {choice(types)} на этаже {floor}, {branch.name}"
        department = Department(name=name, floor=floor,branch_office=branch)
        department.save()

for department in Department.objects.all():
    print(department.pk, department.name)

---- Сотрудники

types = [
"Уборщик",
"штатный сотрудник",
"штатный сотрудник",
"штатный сотрудник",
"штатный сотрудник",
"штатный сотрудник",
"сотрудник на испытательном сроке",
"сотрудник на испытательном сроке",
"менеджер"
]

first_names = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Margaret",
    "Matthew", "Lisa", "Anthony", "Betty", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Dorothy", "Paul", "Kimberly", "Andrew", "Emily", "Joshua", "Donna",
    "Kenneth", "Michelle", "Kevin", "Carol", "Brian", "Amanda", "George", "Melissa",
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
]

mails = ["mail","gmail","outlook","yahoo"]
coms = ["ru","com","su"]

for department in Department.objects.all():
    q = randint(1,30)
    for i in range(q):
        f_name = choice(first_names)
        l_name = choice(last_names)
        employee = Employee(
            name = f"{f_name} {l_name}",
            position = choice(types),
            phone_number = f"8(9{randint(10,99)}){randint(100,999)}-{randint(10,99)}-{randint(10,99)}",
            birth_date = datetime(randint(1985,2005), 10, 25, 15, 30),
            email = f"{f_name.lower()}_{l_name.lower()}@{choice(mails)}.{choice(coms)}",
            department = department
        )
        employee.save()

for employee in Employee.objects.all():
    print(employee.name, employee.position, employee.phone_number, employee.email, employee.department.name)


Удаление email
employee = Employee.objects.get(pk=200)
employee.email = None
employee.save()
employee = Employee.objects.get(pk=220)
employee.email = None
employee.save()
employee = Employee.objects.get(pk=230)
employee.email = None
employee.save()

print(Employee.objects.get(pk=200).email)

---- Запросы
1 с должностью “Менеджер”
for employee in Employee.objects.filter(position="менеджер"):
    print(employee.name, employee.position, employee.phone_number, employee.email, employee.department.name)


2 работающих на четвертых этажах
for employee in Employee.objects.filter(department__floor=4):
    print(employee.name, employee.position, employee.phone_number, employee.email, employee.department.name)


3 ID двух отделов, и получи список всех сотрудников, работающих в этих двух филиалах, с помощью Q
for branch in BranchOffice.objects.all()[:2]:
    print(branch.pk)

for employee in Employee.objects.filter(
    Q(department__branch_office__pk=1) |
    Q(department__branch_office__pk=2)
    ):
    print(employee.name, employee.position, employee.phone_number, employee.email, employee.department.name)

Запросы прогугленные (на самом деле всё это тоже было в уроке)
1
for employee in Employee.objects.filter(
    department__branch_office__pk__in= list(
        BranchOffice.objects.values_list("pk",flat=True)[:2]
        )
    ):
    print(employee.name, employee.position, employee.phone_number, employee.email, employee.department.name)

2
for employee in Employee.objects.filter(email__isnull=True):
    print(employee.name, employee.position, employee.phone_number, employee.email, employee.department.name)

3
for employee in Employee.objects.filter(birth_date__year=1990):
    print(employee.name, employee.position, employee.phone_number, employee.email, employee.department.name)


---- Удаление ----
Department.objects.all().delete()
Employee.objects.all().delete()
























