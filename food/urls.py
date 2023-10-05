from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    path('', view=views.hello_world , name='index'),
    path('items/', view=views.items , name='items'),
    path('<int:item_id>/',view=views.details,name='details'),
]