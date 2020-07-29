from django.urls import path
from myapp import views
app_name="myapp"
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('child/',views.child,name='child'),
    path('sm',views.sm,name='sm'),
    path('cm',views.cm,name='cm'),
]