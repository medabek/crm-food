from django.contrib import admin
from django.urls import path
from .views import login, sample_api
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

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
    path('admin/', admin.site.urls),
    path('api/login', login),
    path('api/sampleapi', sample_api),
    path('users/', views.UserList.as_view()),
    path('roles/', views.RoleList.as_view()),
    re_path('roles/(?P<pk>[0-9]+)/$', views.RoleDetail.as_view()),
    re_path('users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)