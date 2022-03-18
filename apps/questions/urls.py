from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_question, name="post_question"),
    path("questions", views.get_all_questions, name="get_all_questions"),
    path("question/<int:id>", views.question_view, name="question_view"),
]
