from django.db import models
from cms.models import CMSPlugin
from polls.models import Question


class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.question_text
