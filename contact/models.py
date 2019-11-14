from django.db import models


class Organisation(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['id']


class Department(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['id']


class Subdivision(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['id']


class Position(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ['id']


class Contact(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128, null=True)
    is_favorite = models.BooleanField(default=False)
    photo = models.CharField(max_length=256, null=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True
    )
    subdivision = models.ForeignKey(
        Subdivision,
        on_delete=models.CASCADE,
        null=True
    )
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    email = models.EmailField(max_length=64, null=True)
    birthday = models.DateField(null=True)
    address = models.CharField(max_length=256, null=True)
    office = models.CharField(max_length=64, null=True)
    building = models.CharField(max_length=64, null=True)

    class Meta:
        ordering = ['id']


class Phone(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=64)
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        null=True,
        related_name='phones'
    )

    class Meta:
        ordering = ['id']
