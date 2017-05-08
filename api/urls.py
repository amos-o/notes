from django.conf.urls import url, include

from api.views import RegisterView, NoteCreateView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^notes/$', NoteCreateView.as_view(), name='notes')
    # url(r'', name='detail')
]
