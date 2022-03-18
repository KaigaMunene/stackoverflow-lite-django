from django.urls import include, path

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("questions/", include("apps.questions.urls")),
]
