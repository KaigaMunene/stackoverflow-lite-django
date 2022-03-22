from django.urls import include, path

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("qs/", include("apps.questions.urls")),
    path("ans/", include("apps.answers.urls")),
]
