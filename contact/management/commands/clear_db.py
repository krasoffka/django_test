from django.core.management.base import BaseCommand

from contact.models import (
    Contact, Organisation, Department, Phone, Position, Subdivision
)


class Command(BaseCommand):

    def handle(self, *args, **options):  # TODO ONLI FOR DEV
        for model in [
            Contact, Organisation, Department, Phone, Position, Subdivision
        ]:
            model.objects.all().delete()
