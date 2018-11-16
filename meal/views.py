from django.db.models import Sum
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from meal.models import MealCategory, Department, ServicePercentage, Status, Table, Meal, Check, Order, MealsToOrder
from meal.serializers import DepartmentSerializer, MealCategorySerializer, StatusSerializer, TableSerializer, \
    ServicePercentageSerializer, MealSerializer, CheckSerializer, OrderSerializer, MealsToOrderSerializer
from rest_framework import generics

#
#
# def home(request):
#     course = Course.objects.all()
#     return render(request, 'home.html', {'course': course})


# class MealCategoryList(generics.ListCreateAPIView):
#     queryset = MealCategory.objects.all()
#     serializer_class = MealCategorySerializer
#     # def get_queryset(self):
#     #     return MealCategory.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     # def post(self, request):
#     #     Course.objects.create(
#     #         name=request.POST.get('name'),
#     #         description=request.POST.get('description'),
#     #         logo = request.POST.get('logo'))
#
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     # def patch(self, request, *args, **kwargs):
#     #     return self.update(request, *args, **kwargs)


class MealCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.filter(mealcategory_id=1)
    serializer_class = MealCategorySerializer


class MealCategoryView(generics.ListCreateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer


class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealCategory.objects.filter(department_id=1),
    serializer_class = DepartmentSerializer


class StatusView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TableView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ServicePercentageView(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


class MealView(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealList(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def get_queryset(self):
        return Meal.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def post(self, request):
    #     Course.objects.create(
    #         name=request.POST.get('name'),
    #         description=request.POST.get('description'),
    #         logo = request.POST.get('logo'))

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)


class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class CheckView(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer

    # def get_queryset(self):
    #     return Check.objects.annotate(
    #         totalsum=Sum('price')
    #     )


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class MealsToOrderView(generics.ListCreateAPIView):
    queryset = MealsToOrder.objects.all()
    serializer_class = MealsToOrderSerializer