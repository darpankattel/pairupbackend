from django.urls import path
from .views import ProjectList, MembershipList
# appended with /api/project/ in the url

urlpatterns = [
    path('projects/', ProjectList.as_view(), name="project-list"),
    path('memberships/', MembershipList.as_view(), name="membership-list"),
]
