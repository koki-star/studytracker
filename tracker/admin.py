from django.contrib import admin
from .models import Language, Topic, DailyProgress, Resource, Milestone, Goal

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty_level', 'date_started')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')

@admin.register(DailyProgress)
class DailyProgressAdmin(admin.ModelAdmin):
    list_display = ('date', 'language', 'topic', 'time_spent_minutes', 'confidence_level')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'resource_type')

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'is_completed', 'date_created')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_date', 'is_completed')
