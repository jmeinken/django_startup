from django.urls import path, include

from . import views


urlpatterns = [
    # path('js/graph_functions.js', views.js_graph_functions, name='js_graph_functions'),
    # path('myview2/<int:code>', views.myview2, name='myview2'),
    path("", views.home, name="home"),
]
