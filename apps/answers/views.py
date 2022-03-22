from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.questions.models import Question

from .models import Answer
from .serializers import AnswerSerializer


@api_view(["POST"])
def post_answer(request):
    data = request.data
    question = get_object_or_404(Question, id=data.get("question_id"))
    serializer = AnswerSerializer(
        data=data,
        context={"request": request, "question": question},
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_answers(request):
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_answers_for_question(request, question_id):
    answers = Answer.objects.filter(question=question_id)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def update_and_delete_an_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.method == "GET":
        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = AnswerSerializer(
            instance=answer, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        if answer.user == request.user:
            answer.delete()
            return Response(
                {"message": "The question was deleted"},
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            {"message": "unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
        )
