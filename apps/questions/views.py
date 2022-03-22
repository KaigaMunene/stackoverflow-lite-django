from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer


def question_post(request, post_id):
    question_object = Question.objects.get(id=post_id)
    question_object.views = question_object.views + 1
    question_object.save()
    return question_object


@api_view(["POST"])
def post_question(request):
    serializer = QuestionSerializer(
        data=request.data, context={"request": request}
    )
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
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = QuestionSerializer(
            instance=question, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        if question.user == request.user:
            question.delete()
            return Response(
                {"message": "The question was deleted"},
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            {"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
        )
