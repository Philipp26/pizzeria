from django.conf.urls import url

from . import views

urlpatterns = [
        #Home page
        url(r'^$', views.index, name='index'),
        #Output all items (pizza)
        url(r'^pizzas/$', views.pizzas, name='pizzas'),
        #Page with available toppings for pizza
        url(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
        ]
