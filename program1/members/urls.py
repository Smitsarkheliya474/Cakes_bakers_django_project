from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/contact/', views.contact, name='contact'),
    path('index/registers/', views.registers, name='registers'),
    path('index/login/', views.login, name='login'),
    path('index/login/datainsert/', views.datainsert, name='datainsert'),
    path('index/login/checkdata/', views.checkdata, name='checkdata'),
    path('index/login/registers/', views.registers, name='registers'),
    path('index/login/registers/datainsert', views.datainsert, name='datainsert'),
    path('admin_index/', views.admin_index, name='admin_index'),
    path('admin_index/admin_form/', views.admin_form, name='admin_form'),
    path('admin_index/admin_login/', views.admin_login, name='admin_login'),
    path('admin_index/admin_table', views.admin_table, name='admin_table'),
    path('admin_index/admin_form/add_data/', views.add_data, name='add_data'),
    path('admin_index/admin_login/admin_checkdata/', views.admin_checkdata, name='admin_checkdata'),
    path('admin_index/delete/<int:id>', views.delete, name='delete'),
    path('admin_index/update/<int:id>', views.update , name='update'),
    path('admin_index/update/updatedata/<int:id>', views.updatedata , name='updatedata'),
    path('admin_index/user_data/', views.user_data, name='user_data'),
]