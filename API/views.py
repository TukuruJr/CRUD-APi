from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view  # for decorating function based views
from rest_framework.response import Response
from API.models import Post
from API.serializers import PostSerializer


# Create your views here.

# for a get request
@api_view(['GET'])
def Get_Request(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Detailed_Request(request, key):  # pass the id as parameter
    post = Post.objects.get(id=key)  # get only post with the given id
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Create(request):  #
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def Delete(request, key):  # pass the id as parameter
    post = Post.objects.get(id=key)  # get only post with the given id
    post.delete()
