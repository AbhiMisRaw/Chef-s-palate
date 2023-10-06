from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    path('', view=views.hello_world , name='index'),
    path('items/', view=views.items, name='items'),
    path('<int:item_id>/', view=views.details, name='details'),
    #Add
    path('add/', view=views.create_item, name='create_item'),
    # UPDATE
    path('update/<int:item_id>/',view=views.update_item, name='update_item'),
    # delete
    path('delete/<int:id>/',view=views.delete_item, name='delete_item'),
]