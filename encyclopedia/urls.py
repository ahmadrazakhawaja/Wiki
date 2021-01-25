from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<name>",views.title, name="title"),
    path("create_entry",views.create,name="create"),
    path("random_page",views.randomx,name="random"),
    path("search_page",views.search,name="search"),
    path("edit_page",views.edit,name="edit")
]
