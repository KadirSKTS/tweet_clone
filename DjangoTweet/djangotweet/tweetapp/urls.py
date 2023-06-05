from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path("", views.listtweet, name='listtweet'), # atılsamancioglu.com/tweetapp/
    path("addtweet/", views.addtweet, name='addtweet'),  # atılsamancioglu.com/tweetapp/addtweet/
    path('addtweetbyform', views.addtweetbyform, name='addtweetbyform'),
    path('signup/', views.SingUpView.as_view(), name='signup'),
    path('deletetweet/<int:id>', views.deletetweet, name='deletetweet')
]
