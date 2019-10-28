from django.views.generic import ListView
from listview404.models import Todo


class NotFoundListView(ListView):
    allow_empty = False  # データがない場合は、HTTP404
    model = Todo
