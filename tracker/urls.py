from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),

    # Language URLs
    path('languages/', views.language_list, name='language_list'),
    path('languages/create/', views.language_create, name='language_create'),
    path('languages/<int:pk>/', views.language_detail, name='language_detail'),
    path('languages/<int:pk>/update/', views.language_update, name='language_update'),
    path('languages/<int:pk>/delete/', views.language_delete, name='language_delete'),

    # Topic URLs
    path('topics/', views.topic_list, name='topic_list'),
    path('topics/create/', views.topic_create, name='topic_create'),
    path('topics/<int:pk>/update/', views.topic_update, name='topic_update'),
    path('topics/<int:pk>/delete/', views.topic_delete, name='topic_delete'),

    # Progress
    path('progress/', views.progress_list, name='progress_list'),
    path('progress/create/', views.progress_create, name='progress_create'),
    path('progress/<int:pk>/update/', views.progress_update, name='progress_update'),
    path('progress/<int:pk>/delete/', views.progress_delete, name='progress_delete'),

    # Goal URLs
    path('goals/', views.goal_list, name='goal_list'),
    path('goals/create/', views.goal_create, name='goal_create'),
    path('goals/<int:pk>/update/', views.goal_update, name='goal_update'),
    path('goals/<int:pk>/delete/', views.goal_delete, name='goal_delete'),

    # Milestone URLs
    path('milestones/', views.milestone_list, name='milestone_list'),
    path('milestones/create/', views.milestone_create, name='milestone_create'),
    path('milestones/<int:pk>/update/', views.milestone_update, name='milestone_update'),
    path('milestones/<int:pk>/delete/', views.milestone_delete, name='milestone_delete'),

    # Resource URLs
    path('resources/', views.resource_list, name='resource_list'),
    path('resources/create/', views.resource_create, name='resource_create'),
    path('resources/<int:pk>/update/', views.resource_update, name='resource_update'),
    path('resources/<int:pk>/delete/', views.resource_delete, name='resource_delete'),
]
