from django.shortcuts import render
from mainapp.models import UserInfo
from rest_framework import viewsets
from api.serializers import UserInfoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserInfoList(ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def get_queryset(self,**kwargs):
        queryset = UserInfo.objects.all()
        return super().get_queryset()

# @api_view(['GET'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = UserInfo.objects.all()
#         serializer = UserInfoSerializer(snippets, many=True)
#         return Response(serializer.data)
