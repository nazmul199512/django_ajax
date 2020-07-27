from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [

    path('', TaskList.as_view(), name='task-list'),
    path('<str:id>/completed/', TaskComplete.as_view(), name='task-complete'),
    path('<str:id>/delete/', TaskDelete.as_view(), name='task-delete')

]
