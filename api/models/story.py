from django.db import models
from django.contrib.auth import get_user_model

# Create a Story model which takes a field called title, and an owner
# relationship.
class Story(models.Model):
    # define fields
    # title field which will be the title of the story.
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # the owner field which refers to the user. The method `get_user_model`
    # refernces the user model as a lazy reference or import won't work here. The
    # on_delete will make sure that if the data in the field is deleted so will
    # the user reference.
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = 'stories'
    )

    # return story title as a string.
    def __str__(self):
        return f"The story title is {self.title}"

    def as_dict(self):
        """Returns a dictionary version of the story model"""
        return {
          'id': self.id,
          'title': self.title
        }
