from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from faker import Faker

from .models import Teacher


def index(request):
    return HttpResponse("There is a teacher page!")


def teachers(request):
    return HttpResponse("There is a teacher's list")


def generate_teachers(request):
    try:
        if request.GET["count"].isdigit() and 0 < int(request.GET["count"]) <= 100:
            count = int(request.GET["count"])
        else:
            count = request.GET["count"]
            return HttpResponse(f"Count {count} is not valid! Try again")
    except MultiValueDictKeyError:
        count = 100

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




