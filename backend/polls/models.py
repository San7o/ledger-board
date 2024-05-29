"""Models for Polls app."""
from django.db import models

# Create your models here.


class Question(models.Model):

    """Question model for Polls app."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        """Return the question text."""
        return self.question_text


class Choice(models.Model):

    """Choice model for Polls app."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Return the choice text."""
        return self.choice_text
