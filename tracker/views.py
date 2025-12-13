from django.shortcuts import render, get_object_or_404, redirect
from .models import Language, Topic, DailyProgress, Resource, Milestone, Goal
from .forms import LanguageForm, TopicForm, DailyProgressForm, ResourceForm, MilestoneForm, GoalForm, CustomUserCreationForm
from django.db.models import Sum, Count
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import json


# Public pages
def landing(request):
    """Landing page for new visitors."""
    return render(request, 'landing.html')


def about(request):
    """About page with app information."""
    return render(request, 'about.html')


# Authentication
def signup(request):
    """User registration - creates account and logs in automatically."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# Dashboard
@login_required
def dashboard(request):
    """Main dashboard showing user's learning progress and statistics."""
    languages = Language.objects.filter(user=request.user)
    total_languages = languages.count()
    total_progress_entries = DailyProgress.objects.filter(user=request.user).count()
    upcoming_goals = Goal.objects.filter(user=request.user, is_completed=False).order_by('target_date')[:5]
    recent_milestones = Milestone.objects.filter(user=request.user, is_completed=True).order_by('-date_created')[:5]

    # Chart data
    progress_data = []
    labels = []
    for lang in languages:
        total_time = DailyProgress.objects.filter(user=request.user, language=lang).aggregate(Sum('time_spent_minutes'))['time_spent_minutes__sum'] or 0
        progress_data.append(total_time)
        labels.append(lang.name)

    context = {
        'total_languages': total_languages,
        'total_progress_entries': total_progress_entries,
        'upcoming_goals': upcoming_goals,
        'recent_milestones': recent_milestones,
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(progress_data),
    }
    return render(request, 'dashboard.html', context)


# Language management
@login_required
def language_list(request):
    languages = Language.objects.filter(user=request.user)
    return render(request, 'tracker/languages_list.html', {'languages': languages})

@login_required
def language_detail(request, pk):
    language = get_object_or_404(Language, pk=pk, user=request.user)
    return render(request, 'tracker/languages_detail.html', {'language': language})

@login_required
def language_create(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save(commit=False)
            language.user = request.user
            language.save()
            return redirect('language_list')
    else:
        form = LanguageForm()
    return render(request, 'tracker/languages_form.html', {'form': form})

@login_required
def language_update(request, pk):
    language = get_object_or_404(Language, pk=pk, user=request.user)
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('language_list')
    else:
        form = LanguageForm(instance=language)
    return render(request, 'tracker/languages_form.html', {'form': form})

@login_required
def language_delete(request, pk):
    language = get_object_or_404(Language, pk=pk, user=request.user)
    if request.method == 'POST':
        language.delete()
        return redirect('language_list')
    return render(request, 'tracker/languages_confirm_delete.html', {'language': language})

# Topics
@login_required
def topic_list(request):
    topics = Topic.objects.filter(user=request.user)
    return render(request, 'tracker/topics_list.html', {'topics': topics})

@login_required
def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect('topic_list')
    else:
        form = TopicForm()
    return render(request, 'tracker/topics_form.html', {'form': form})

@login_required
def topic_update(request, pk):
    topic = get_object_or_404(Topic, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topic_list')
    else:
        form = TopicForm(instance=topic)
    return render(request, 'tracker/topics_form.html', {'form': form})

@login_required
def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk, user=request.user)
    if request.method == 'POST':
        topic.delete()
        return redirect('topic_list')
    return render(request, 'tracker/topics_confirm_delete.html', {'topic': topic})

# Daily progress tracking
@login_required
def progress_list(request):
    progress_entries = DailyProgress.objects.filter(user=request.user).order_by('-date')
    return render(request, 'tracker/progress_list.html', {'progress_entries': progress_entries})

@login_required
def progress_create(request):
    if request.method == 'POST':
        form = DailyProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user
            progress.save()
            return redirect('progress_list')
    else:
        form = DailyProgressForm()
    return render(request, 'tracker/progress_form.html', {'form': form})

@login_required
def progress_update(request, pk):
    progress = get_object_or_404(DailyProgress, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DailyProgressForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            return redirect('progress_list')
    else:
        form = DailyProgressForm(instance=progress)
    return render(request, 'tracker/progress_form.html', {'form': form})

@login_required
def progress_delete(request, pk):
    progress = get_object_or_404(DailyProgress, pk=pk, user=request.user)
    if request.method == 'POST':
        progress.delete()
        return redirect('progress_list')
    return render(request, 'tracker/progress_confirm_delete.html', {'progress': progress})

# Goals
@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'tracker/goals_list.html', {'goals': goals})

@login_required
def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'tracker/goals_form.html', {'form': form})

@login_required
def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'tracker/goals_form.html', {'form': form})

@login_required
def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('goal_list')
    return render(request, 'tracker/goals_confirm_delete.html', {'goal': goal})

# Milestones
@login_required
def milestone_list(request):
    milestones = Milestone.objects.filter(user=request.user)
    return render(request, 'tracker/milestones_list.html', {'milestones': milestones})

@login_required
def milestone_create(request):
    if request.method == 'POST':
        form = MilestoneForm(request.POST)
        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.user = request.user
            milestone.save()
            return redirect('milestone_list')
    else:
        form = MilestoneForm()
    return render(request, 'tracker/milestones_form.html', {'form': form})

@login_required
def milestone_update(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MilestoneForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect('milestone_list')
    else:
        form = MilestoneForm(instance=milestone)
    return render(request, 'tracker/milestones_form.html', {'form': form})

@login_required
def milestone_delete(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk, user=request.user)
    if request.method == 'POST':
        milestone.delete()
        return redirect('milestone_list')
    return render(request, 'tracker/milestones_confirm_delete.html', {'milestone': milestone})

# Learning resources
@login_required
def resource_list(request):
    resources = Resource.objects.filter(user=request.user)
    return render(request, 'tracker/resources_list.html', {'resources': resources})

@login_required
def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.user = request.user
            resource.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'tracker/resources_form.html', {'form': form})

@login_required
def resource_update(request, pk):
    resource = get_object_or_404(Resource, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'tracker/resources_form.html', {'form': form})

@login_required
def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk, user=request.user)
    if request.method == 'POST':
        resource.delete()
        return redirect('resource_list')
    return render(request, 'tracker/resources_confirm_delete.html', {'resource': resource})
