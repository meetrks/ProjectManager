from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from project.views import ProjectView, ProjectCreateView, ProjectUpdateView

urlpatterns = [
    url('^$', login_required(ProjectView.as_view())),
    url('^project/$', login_required(ProjectView.as_view())),
    url('^project/create/$', login_required(ProjectCreateView.as_view())),
    url('^project/update/(?P<project_id>[-a-fA-F0-9]{36})/$', login_required(ProjectUpdateView.as_view())),
    url('^project/(?P<project_id>[-a-fA-F0-9]{36})/$', login_required(ProjectView.as_view())),
    url('^project/(?P<project_id>[-a-fA-F0-9]{36})/task/', include('task.urls')),
]
