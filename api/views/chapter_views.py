"""Chapter views"""
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from ..models.chapter import Chapter
from ..serializers import ChapterSerializer, ChapterStorySerializer

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
        data = ChapterStorySerializer(chapters, many=True).data
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

class ChapterDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    # show a single chapter
    def get(self, request, pk):
        """Show request"""
        # locate the chapter id in the url
        chapter = get_object_or_404(Chapter, pk=pk)

        if not request.user.id == chapter.owner.id:
            raise PermissionDenied('Not your chapter')
        # Serialize the story and return the response
        data = ChapterStorySerializer(chapter).data
        return Response({ 'chapter': data })

    # delete a chapter
    def delete(self, request, pk):
        """Delete request"""
        # Locate the chapter to delete
        chapter = get_object_or_404(Chapter, pk=pk)

        if not request.user.id == chapter.owner.id:
            raise PermissionDenied('Not your chapter to delete')
        # Serialize the chapter and return the response
        chapter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Update a chapter
    def partial_update(self, request, pk):
        """Update Request"""
        # locate a chapter and return an object presentation of the chapter
        chapter = get_object_or_404(Chapter, pk=pk)
        # Check for authentication before allowing an update
        if not request.user.id == chapter.owner.id:
            raise PermissionDenied("Can't update anothers story")
        # Ensure the owners field matches the current id
        request.data['chapter']['owner'] = request.user.id
        # validate with serializer
        data = ChapterSerializer(chapter, data=request.data['chapter'], partial=True)
        # if data is valid save and return the response, otherwise throw an error
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If not send an error
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
