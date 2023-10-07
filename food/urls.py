from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    path('', view=views.IndexClassView.as_view() , name='index'),
    path('items/', view=views.items, name='items'),
    #for a particular food items
    path('<int:pk>/', view=views.FoodDetail.as_view(), name='details'),
    #Add
    path('add/', view=views.CreateItem.as_view(), name='create_item'),
    # UPDATE
    path('update/<int:item_id>/',view=views.update_item, name='update_item'),
    # delete
    path('delete/<int:id>/',view=views.delete_item, name='delete_item'),
]