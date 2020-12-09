from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('more/<int:sample_id>',views.more,name = "more"),
    path('turnon/',views.turnon,name = "turnon"),
    path('turnoff/',views.turnoff,name = "turnoff"),
]
