from django.urls import path
from animal import views

urlpatterns = [
    path('page_a/',views.page_a),
    path('page_b/',views.page_b),
    path('page_c/',views.page_c),

    path('create/',views.create),

    path('',views.index),
    path('edit/<animal_id>',views.edit),
    path('delete/<animal_id>',views.delete),
]
