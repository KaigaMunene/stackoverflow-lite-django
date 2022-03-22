from django.urls import path

from . import views

urlpatterns = [
    path(
        "answer/",
        views.post_answer,
        name="post_an_answer",
    ),
    path(
        "answers/", views.get_all_answers, name="get_all_answers_to_a_question"
    ),
    path(
        "answers/question/<int:question_id>",
        views.get_all_answers_for_question,
        name="get_all_answers_for_question",
    ),
    path(
        "answer/<int:answer_id>",
        views.update_and_delete_an_answer,
        name="update_answer",
    ),
]
