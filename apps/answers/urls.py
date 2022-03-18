from django.urls import path

from . import views

urlpatterns = [
    path("answer/<int:question>", views.post_answer, name="post_an_answer")
]
