from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from ..models.story import Story
from ..serializers import StorySerializer

# Story views
class Stories(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = StorySerializer
    """Story View"""
    def get(self, request):
        """Index request"""
        # converts the request into an object and filters the objects so that
        # the owner will only be able to view their object.
        stories = Story.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = StorySerializer(stories, many=True).data
        # return the data as an object
        return Response({ 'story': data })

    # create a new story object
    def post(self, request):
        """Create request"""
        print('give me data ', request.data)
        # Add the user to the object
        request.data['story']['owner'] = request.user.id
        # Turn the data into object format
        story = StorySerializer(data=request.data['story'])
        # If the story has a valid serializer save the data and send the response
        if story.is_valid():
            story.save()
            return Response({ 'story': story.data }, status=status.HTTP_201_CREATED)
        # If the data is invalid throw an error
        return Response(story.errors, status=status.HTTP_400_BAD_REQUEST)

class StoryDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    # shows a single story related to the owner
    def get(self, request, pk):
        """Show request"""
        # locate the right story in the url using its key in the url
        story = get_object_or_404(Story, pk=pk)

        if not request.user.id == story.owner.id:
            raise PermissionDenied('Not your story')
        # Serialize the story and return the response
        data = StorySerializer(story).data
        return Response({ 'story': data })

    # delete a story
    def delete(self, request, pk):
        """Delete request"""
        # Locate the story to delete
        story = get_object_or_404(Story, pk=pk)
        # Check that the owner is the one deleting the story and throw error
        # if not
        if not request.user.id == story.owner.id:
            raise PermissionDenied("You can't delete someone else's story")
        # delete the story and return the response
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # locate story and return an object presentation of the story
        story = get_object_or_404(Story, pk=pk)
        # Check for authentication and stop the function and throw an error if not.
        if not request.user.id == story.owner.id:
            raise PermissionDenied("Can't update anothers story")
        # Ensure the owners field matches the current id
        request.data['story']['owner'] = request.user.id
        # validate with serializer
        data = StorySerializer(story, data=request.data['story'], partial=True)
        if data.is_valid():
            # if data is valid save and send the response
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If not send an error
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
