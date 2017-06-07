from django.conf.urls import url, include
from django.urls import reverse
from polls.api import QuestionResource, ChoiceResource
from . import views
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(QuestionResource())
v1_api.register(ChoiceResource())

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex:/polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/api/5
    url(r'^api/', include(v1_api.urls))
]
