from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token

from api.views import RegisterView, NoteCreateView, NoteDetailView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^notes/$', NoteCreateView.as_view(), name='notes'),
    url(r'^notes/(?P<pk>[0-9]+)$', NoteDetailView.as_view(), name='detail'),
    url(r'^token/', obtain_jwt_token),
]
