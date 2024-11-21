from django.urls import path
from .views import ProjectView,SkillView

urlpatterns = [
    path('project/',ProjectView.as_view(),name='project'),
    path('skill/',SkillView.as_view(),name='skill')
]