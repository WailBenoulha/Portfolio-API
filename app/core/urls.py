from django.urls import path
from .views import (ProjectView,SkillView,ExperienceAdmin,
                    ExperienceView,EducationView,EducationAdmin)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('project/',ProjectView.as_view(),name='project'),
    path('skill/',SkillView.as_view(),name='skill'),
    path('exper/',ExperienceView.as_view(),name='Experience'),
    path('experadmin/',ExperienceAdmin.as_view(),name='Experience'),
    path('education/',EducationView.as_view(),name='Education'),
    path('educationadmin/',EducationAdmin.as_view(),name='Education')
]