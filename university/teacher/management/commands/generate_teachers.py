from django.core.management.base import BaseCommand
from faker import Faker

from teacher.models import Teacher


class Command(BaseCommand):
    help = "Generate fake teachers. Default count = 100"

    def add_arguments(self, parser):
        parser.add_argument("count", nargs="?", type=int, default=100)

    def handle(self, *args, **options):
        fake = Faker()
        teachers_list = []
        for _ in range(options["count"]):
            teachers_list.append(
                Teacher(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    birthday=fake.date_of_birth(),
                )
            )
        teachers = Teacher.objects.bulk_create(teachers_list)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {len(teachers)} teachers")
        )
