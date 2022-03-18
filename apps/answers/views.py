from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.questions.models import Question

from .models import Answer
from .serializers import AnswerSerializer


@api_view(["POST", "GET"])
def post_answer(request, question):
    question = get_object_or_404(Question, id=question)
    if request.method == "POST":
        serializer = AnswerSerializer(
            data=request.data,
            context={"request": request, "question": question},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
