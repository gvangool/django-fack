from __future__ import absolute_import

try:
    from django.conf.urls.defaults import *
except ImportError:
    from django.conf.urls import url

    try:
        from django.conf.urls import patterns
    except ImportError:
        patterns = None
from . import views

urls = [
    url(regex=r"^$", view=views.TopicList.as_view(), name="faq_topic_list"),
    url(regex=r"^submit/$", view=views.SubmitFAQ.as_view(), name="faq_submit"),
    url(
        regex=r"^submit/thanks/$",
        view=views.SubmitFAQThanks.as_view(),
        name="faq_submit_thanks",
    ),
    url(
        regex=r"^(?P<slug>[\w-]+)/$",
        view=views.TopicDetail.as_view(),
        name="faq_topic_detail",
    ),
    url(
        regex=r"^(?P<topic_slug>[\w-]+)/(?P<slug>[\w-]+)/$",
        view=views.QuestionDetail.as_view(),
        name="faq_question_detail",
    ),
]

if patterns is None:
    urlpatterns = urls
else:
    urlpatterns = patterns("", *urls)
