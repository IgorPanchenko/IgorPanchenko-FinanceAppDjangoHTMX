from django.urls import path
from tracker import views


urlpatterns = [
    path("", views.index, name='index'),
    path("transactions/", views.transaction_list, name='transaction-list'),
    path("transactions/create/", views.create_transaction, name='create-transaction'),
    path("transactions/<int:pk>/update/", views.update_transaction, name='update-transaction'),
    path("transactions/<int:pk>/delete/", views.delete_transaction, name='delete-transaction'),
]
