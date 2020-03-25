from django.urls import path
from .views import BookViewSets

list_actions = {
    'get': 'list',
    'post': 'create'
}

single_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = [
    path('', BookViewSets.as_view(list_actions), name="book_transactions"),
    path('<pk>', BookViewSets.as_view(single_actions), name='book_transaction'),
]