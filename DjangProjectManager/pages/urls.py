from django.urls import path

from .views import deleteTodo

app_name = "Todo"
urlpatterns = [
    path('<int:todo_id>', deleteTodo, name='todo' )
]