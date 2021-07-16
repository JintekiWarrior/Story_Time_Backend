"""Chapter views"""
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from ..models.chapter import Chapter
from ..serializers import ChapterSerializer

# Chapter views
class Chapters(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ChapterSerializer
    """Chapter View for Create and Index"""

    def get(self, request):
        """Index request"""
        # filters the index so that only the owner be able to view their chapters.
        chapters = Chapter.objects.filter(owner=request.user.id)
        # Runs the serializer
        data = ChapterSerializer(chapters, many=True).data
        # return the data as an object
        return Response({ 'chapter': data })
    def post(self, request):
        """Create request"""
        # Add the user to the object
        request.data['chapter']['owner'] = request.user.id
        # Turn the data into object format
        chapter = ChapterSerializer(data=request.data['chapter'])
        # If the chapter is valid save it and send the response
        if chapter.is_valid():
            chapter.save()
            return Response({ 'chapter': chapter.data }, status=status.HTTP_201_CREATED)
        # If the data is invalid return error
        return Response(chapter.errors, status=status.HTTP_400_BAD_REQUEST)
