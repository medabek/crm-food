from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from user.models import User


class Department(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'names'

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'names'

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    name = models.CharField(max_length=250)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name_plural = 'names'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'names'

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    percentage = models.FloatField()


class Meal(models.Model):
    name = models.CharField(max_length=250)
    mealcategory_id = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name='meals')
    price = models.IntegerField()
    description = models.TextField(max_length=1500)

    class Meta:
        verbose_name_plural = 'names'

    def __str__(self):
        return self.name


class Order(models.Model):
    waiterid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    tableid = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')
    tablename = models.CharField(max_length=250, default='table1')
    isitopen = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='orders')
    date = models.CharField(max_length=300)
    mealsid = models.ManyToManyField(Meal, through='MealsToOrder', related_name='orders')


    def __str__(self):
        return "Order #" + str(self.pk) + "," + self.tableid.name + \
               ", Waiter: " + self.waiterid.name + ", " \
                "Meals: " + str(self.mealsid.name)


class MealsToOrder(models.Model):
    count = models.IntegerField(default=0)
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='mealstoorders')
    meals = models.ForeignKey(Meal, on_delete=models.CASCADE, null=False, related_name='mealstoorders')

    def __str__(self):
        return "Waiter: " + self.orderid.waiterid.name + ", Meal: " + self.meals.name


class Check(models.Model):
    orderid = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='checks')
    date = models.CharField(max_length=300)
    servicefee = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE, related_name='checks')
    totalsum = models.IntegerField(default=0)
    #meals = models.ManyToManyField(Meal)

    def __str__(self):
        return "Check #" + str(self.pk)

    # def get_totalsum(self):
    #     return self.meals.aggregate(Sum('price'))['totalsum']

