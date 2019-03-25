from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from task.views import TaskView, TaskCreateView, TaskUpdateView

urlpatterns = [
    url('^$', login_required(TaskView.as_view())),
    url('^create/$', login_required(TaskCreateView.as_view())),
    url('^update/(?P<task_id>[-a-fA-F0-9]{36})$',
        login_required(TaskUpdateView.as_view())),
    url('^(?P<task_id>[-a-fA-F0-9]{36})/$', login_required(TaskView.as_view())),
]
