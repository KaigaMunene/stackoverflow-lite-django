from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.questions.models import Question

from .models import Answer
from .serializers import AnswerSerializer


@api_view(["POST"])
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
    elif request.method == "GET":
        serializer = AnswerSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_answers(request):
    if request.method == "GET":
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_an_answer(request, question):
    question = get_object_or_404(Question, id=question)
    if request.method == "PUT":
        serializer = AnswerSerializer(
            data=request.data,
            context={"request": request, "question": question},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    if request.method == "DELETE":
        answer.delete()
        return Response(
            {"message": "The question was deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )
