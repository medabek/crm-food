from django.db.models import Sum, F
from rest_framework import serializers
from meal.models import MealCategory, Department, ServicePercentage, Status, Table, Meal, Order, MealsToOrder, Check


class DepartmentSerializer(serializers.ModelSerializer):
    #name = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'name')


class TableSerializer(serializers.ModelSerializer):
    #name = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = ('id', 'name')


class StatusSerializer(serializers.ModelSerializer):
    #service_name = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = ('id','name')


class ServicePercentageSerializer(serializers.ModelSerializer):
    #percentage = serializers.SerializerMethodField()

    class Meta:
        model = ServicePercentage
        fields = ('id','percentage')


class MealCategorySerializer(serializers.ModelSerializer):
    #name = serializers.SerializerMethodField()
    #department_id = serializers.Id(read_only=True, source='department.id')

    class Meta:
        model = MealCategory
        fields = ('id', 'name', 'department_id')


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ('id', 'name', 'mealcategory_id', 'price', 'description')


class OrderSerializer(serializers.ModelSerializer):
    count = MealsToOrder.objects.count
    mealsid = MealSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'waiterid', 'tableid', 'isitopen', 'date', 'mealsid')


class MealsToOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealsToOrder
        fields = ('count', 'orderid', 'meals')


class CheckSerializer(serializers.ModelSerializer):
    totalsum = serializers.SerializerMethodField()

    class Meta:
        model = Check
        fields = ('id','date','orderid','servicefee', 'totalsum')

    def get_totalsum(self, obj):
        count = MealsToOrder.objects.count
        #price = obj.orderid.mealsid.all().get_attribute('price')
        func = obj.orderid.mealsid.all().aggregate(Sum('price'))
        #print(int(func.get('price__sum')))
        return int(func.get('price__sum'))




        # for i in func:
        #     summ += int(func.get('price__sum'))
        #     #print(i)
        #     return summ





