from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Language(models.Model):
    """Represents a programming language or skill being learned by a user."""
    DIFFICULTY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='languages', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='Beginner')
    date_started = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Topic(models.Model):
    """Specific topics or concepts within a language (e.g., 'Functions' in Python)."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.language.name})"

class DailyProgress(models.Model):
    """Daily study session logs with time tracking and confidence levels."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='daily_progress', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    what_i_learned = models.TextField()
    time_spent_minutes = models.PositiveIntegerField()
    confidence_level = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], default=3)

    class Meta:
        verbose_name_plural = "Daily Progress"

    def __str__(self):
        return f"{self.date} - {self.language.name}"

class Resource(models.Model):
    """Learning resources like tutorials, articles, and courses."""
    RESOURCE_TYPES = [
        ('Video', 'Video'),
        ('Article', 'Article'),
        ('Book', 'Book'),
        ('Course', 'Course'),
        ('Documentation', 'Documentation'),
        ('Other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    link = models.URLField()
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPES, default='Article')

    def __str__(self):
        return self.title

class Milestone(models.Model):
    """Significant achievements in learning a language."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='milestones', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='milestones')
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Goal(models.Model):
    """Learning goals with target dates and completion tracking."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals', null=True, blank=True)
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    target_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
