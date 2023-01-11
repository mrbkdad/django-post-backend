from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializer import PostSerializer

class Posts(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serialzier = PostSerializer(posts,many=True)
        return Response(serialzier.data)
    
    def post(self,request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            saved_post = serializer.save()
            return Response(PostSerializer(saved_post).data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class PostDetail(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk = pk)
        except ObjectDoesNotExist:
            raise NotFound
    
    def get(self,request,pk):
        serializer = PostSerializer(self.get_object(pk))
        return Response(serializer.data)
    def put(self,request,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post,data=request.data,partial=True)
        if serializer.is_valid():
            updated_post = serializer.save()
            return Response(PostSerializer(updated_post).data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status.HTTP_204_NO_CONTENT)
