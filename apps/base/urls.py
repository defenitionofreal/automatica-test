from django.urls import path
from .api import (store_list,
                  visit_create)

app_name = 'base'

urlpatterns = [
    path('store/list/', store_list.StoreListAPIView.as_view()),
    path('visit/create/', visit_create.VisitCreateAPIView.as_view())
]
