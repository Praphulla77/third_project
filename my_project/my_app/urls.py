from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('add',views.add,name='add'),

    path('view',views.view,name='view'),

    path('delete/<int>id',views.delete,name='delete'),
    
]
