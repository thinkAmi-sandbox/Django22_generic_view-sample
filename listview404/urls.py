from django.urls import path

from listview404.views import NotFoundListView

app_name = 'listview404'

urlpatterns = [
    path('', NotFoundListView.as_view(), name='todo_list'),
]
