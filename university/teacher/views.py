from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from faker import Faker

from .models import Teacher


def index(request):
    return render(request, "teacher/index.html")


def teachers(request):
    teachers_list = list(Teacher.objects.values())
    return render(request, "teacher/teachers.html", {"teachers_list": teachers_list})


def generate_teachers(request):
    try:
        count = request.GET["count"]
    except MultiValueDictKeyError:
        return HttpResponse('Query parameter "count" did not find! Try again')
    if not (count.isdigit() and 0 < int(request.GET["count"]) <= 100):
        return HttpResponse(f"Count {count} is not valid! Try again")
    try:
        count = int(count)
    except ValueError:
        return HttpResponse(f"Count {count} is not an integer! Try again")

    fake = Faker()
    teachers_list = []
    for _ in range(count):
        teachers_list.append(
            Teacher(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birthday=fake.date_of_birth(),
            )
        )
    teachers = Teacher.objects.bulk_create(teachers_list)
    return HttpResponse(f"Generate {count} fake teachers: <p>{teachers}</p>")
