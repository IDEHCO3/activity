
from django.conf.urls import include, url
from activityResource import views

urlpatterns = [
    url(r'^activities/', views.ActivityList.as_view(), name='list'),
    url(r'^activities/(?P<pk>\d+)/', views.ActivityDetail.as_view(), name='detail'),
]