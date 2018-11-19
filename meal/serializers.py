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
    #count = MealsToOrder.objects.count
    #meals = MealSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'waiterid', 'tableid', 'isitopen', 'date', 'meals')


class MealsToOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealsToOrder
        fields = ('count', 'orderid', 'meals')


class CheckSerializer(serializers.ModelSerializer):
    totalsum = serializers.SerializerMethodField()
    #orderid= OrderSerializer(many=True)
    meals = serializers.SerializerMethodField()

    class Meta:
        model = Check
        fields = ('id','date','orderid','servicefee', 'totalsum', 'meals')

    def get_totalsum(self, obj):
        summ = 0
        meal_orders = MealsToOrder.objects.filter(orderid=obj.orderid)
        for meal_order in meal_orders:
            summ += meal_order.count * meal_order.meals.price
        return summ

    def get_meals(self, obj):
        meal_orders = MealsToOrder.objects.filter(orderid=obj.orderid)
        #return meal_orders.all().__str__()
        summ = []
        for meal_order in meal_orders:
            summ.append(meal_order.__str__())
        return summ





        # for i in func:
        #     summ += int(func.get('price__sum'))
        #     #print(i)
        #     return summ





