from django.db import models
from django.contrib.auth import get_user_model

# Create a Chapter model which takes two fields (name, and body).
# It has a one to many relationship with story (story -|--< chapters).
class Chapter(models.Model):
    """Chapter Model"""
    # define fields
    # name of the chapter
    name = models.CharField(max_length=100)
    # body of the chapter
    body = models.TextField(max_length=10000)

    # The chapter has a one to many relationship with the story and needs to refer
    # to it.
    story = models.ForeignKey(
        'Story',
        on_delete = models.CASCADE,
        related_name = 'chapters'
    )

    # return a string of the chapters model
    def __str__(self):
        return f"The chapter name is {self.name}. This is the body {self.body}"

    def as_dict(self):
        """Return a dictionary version of the chapter model"""
        return {
            'id': self.id,
            'name': self.name,
            'body': self.body
        }
