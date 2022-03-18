from multiprocessing import context

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer


@api_view(["POST"])
def post_question(request):
    serializer = QuestionSerializer(data=request.data, context=request.user)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def question_view(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "GET":
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = QuestionSerializer(instance=question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        question.delete()
        return Response({"message": "The question was deleted"})
