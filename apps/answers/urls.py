from django.urls import path

from . import views

urlpatterns = [
    path(
        "answer/post_and_get/<int:question>",
        views.post_answer,
        name="post_an_answer",
    ),
    path("answers/", views.get_all_answers, name="get_all_answers"),
    path(
        "answer/update/<int:question>",
        views.update_an_answer,
        name="update_answer",
    ),
    path("answer/delete/<int:id>", views.delete_answer, name="delete_answer"),
]
