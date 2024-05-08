from django.urls import path, include

# appended with /api/ in the url

urlpatterns = [
    path('account/', include('account.urls')),
    path('project/', include('project.urls')),
    path('post/', include('post.urls')),
    path('chat/', include('chat.urls')),
]
