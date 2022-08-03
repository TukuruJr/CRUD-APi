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


@api_view(['POST'])
def Post_Request(request):
    pass

