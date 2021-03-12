from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class APIPost(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIPostDetail(APIView):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, id):
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid() and post.author == request.user:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
    def patch(self, request, id):
        post = Post.objects.get(pk=id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid() and post.author == request.user:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, id):
        post = Post.objects.get(pk=id)
        if request.user == post.author:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class APIComment(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICommentDetal(APIView):
    def get(self, request, id):
        comment = Comment.objects.get(pk=id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def put(self, request, id):
        comment = Comment.objects.get(pk=id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid() and comment.author == request.user:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
    def patch(self, request, id):
        comment = Comment.objects.get(pk=id)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid() and comment.author == request.user:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, id):
        comment = Comment.objects.get(pk=id)
        if request.user == comment.author:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class APIFollow(APIView):
    def get(self, request):
        Follows = Follow.objects.all()
        serializer = FollowSerializer(Follows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIGroup(APIView):
    def get(self, request):
        Groups = Group.objects.all()
        serializer = GroupSerializer(Groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
