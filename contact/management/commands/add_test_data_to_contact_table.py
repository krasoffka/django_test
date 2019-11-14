import random

from django.core.management.base import BaseCommand
from faker import Faker

from contact.models import (
    Contact, Organisation, Department, Phone, Position, Subdivision
)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--row_num', type=int, required=True, default=None)

    def handle(self, *args, **options):
        row_num = options['row_num']
        fake = Faker('ru_RU')
        fake_orgs = create_fake_orgs()
        fake_deps = create_fake_deps()
        fake_pos = create_fake_pos(fake)
        fake_subdiv = create_fake_subdiv()
        for _ in range(row_num):
            contact = create_contact(
                fake, fake_orgs, fake_deps, fake_pos, fake_subdiv
            )
            create_phone(fake, contact)
        print(f'{row_num} contacts created')


def create_fake_subdiv():
    subdiv_names = ['Первое', 'Второе', 'Третье', 'Четвертое', 'Пятое']
    instances = []
    for name in subdiv_names:
        instances.append(Subdivision.objects.create(name=name))
    return instances


def create_phone(fake, contact):
    phone_names = ['Внутренний', 'Основной', 'Домашний', 'Рабочий', 'Факс',
                   'Запасной', 'Экстренный']
    for i in range(random.randint(1, 4)):
        Phone.objects.create(
            name=random.choice(phone_names),
            number=fake.msisdn(),
            contact=contact,
        )


def create_fake_pos(fake):
    instances = []
    for name in range(130):
        instances.append(Position.objects.create(name=fake.job()))
    return instances


def create_fake_orgs():
    organisations = ['Лукойл центр', 'Лукойл север', 'Лукойл юг',
                     'Лукойл запад', 'Лукойл восток', ]
    instances = []
    for name in organisations:
        instances.append(Organisation.objects.create(name=name))
    return instances


def create_fake_deps():
    departments = ['Технический', 'Инженерный', 'Кадровый', 'Добывающий',
                   'Специальный', 'Трудовой', 'Транспортный', 'Строительный',
                   'Нефтяной', 'Газовый', 'Водный', ]
    instances = []
    for name in departments:
        instances.append(Department.objects.create(name=name))
    return instances


def create_contact(fake, orgs, deps, pos, subdiv):
    instance = Contact(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        patronymic=fake.middle_name(),
        is_favorite=False,
        photo='https://via.placeholder.com/150',
        organisation=random.choice(orgs),
        department=random.choice(deps),
        position=random.choice(pos),
        subdivision=random.choice(subdiv),
        email=fake.email(),
        birthday=fake.date_between(start_date="-30y", end_date="today"),
        address=fake.address(),
        office=random.randint(1, 1000),
        building=random.randint(1, 1000),
    )
    instance.save()
    return instance
