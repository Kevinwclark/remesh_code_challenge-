"""remesh_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from conversations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='homepage'),
    path('new-conversation/', views.new_conversation_view, name='conversation'),
    path('current-conversations/', views.current_conversations_view, name='current-conversation'),
    path('conversation-detail/<int:conversation_id>/', views.conversation_detail_view, name='convo-detail'),
    path('search-conversations', views.Search.as_view(), name='search'),
    path('', include('thoughts.urls')),
    path('', include('message.urls')),
]
