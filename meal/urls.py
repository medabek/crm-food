from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from meal import views

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('department', views.DepartmentView)
# router.register('table', views.TableView)
# router.register('mealcategory', views.MealCategoryView)
# router.register('status', views.StatusView)
# router.register('servicePercentage', views.ServicePercentageView)
urlpatterns = [
    path('departments/', views.DepartmentView.as_view()),
    re_path('departments/(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view()),
    re_path('category/(?P<pk>[0-9]+)/$', views.MealCategoryDetail.as_view()),
    path('category/', views.MealCategoryView.as_view()),
    path('meals/', views.MealList.as_view()),
    re_path('meals/(?P<pk>[0-9]+)/$', views.MealDetail.as_view()),
    path('checks/', views.CheckView.as_view()),
    path('orders/', views.OrderView.as_view()),
    path('tables/', views.TableView.as_view()),
    path('status/', views.StatusView.as_view()),
    path('toorder/', views.MealsToOrderView.as_view()),
    path('fee/', views.ServicePercentageView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)