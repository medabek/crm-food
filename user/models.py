from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'roles'

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    login = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    email = models.EmailField(max_length=400)
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='roles')
    dateofadd = models.CharField(max_length=200)
    phone = models.CharField(max_length=150)
    class Meta:
        verbose_name_plural = 'users'

    def __str__(self):
        return self.name



# class Contact(models.Model):
#     contact_choice=(
#         (1, "PHONE"),
#         (2, "FACEBOOK"),
#         (3, "EMAIL"),
#     )
#
#     contact_choice = models.IntegerField(choices=contact_choice, default=1)
#     value = models.CharField(max_length=200)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='contacts')





