# myapp/api.py
from tastypie.resources import ModelResource
from tastypie import fields
from polls.models import Question, Choice


class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'
        fields = ['question_text', 'pub_date']


class ChoiceResource(ModelResource):
    question = fields.ForeignKey(QuestionResource, 'question')

    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'
        fields = ['choice_text', 'votes']

