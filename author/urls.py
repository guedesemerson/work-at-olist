from django.urls import path
from .views import AuthorViewSets

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
    path('', AuthorViewSets.as_view(list_actions), name="author_transactions"),
    path('<pk>', AuthorViewSets.as_view(single_actions), name='author_transaction'),
]