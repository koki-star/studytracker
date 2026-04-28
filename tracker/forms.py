from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Language, Topic, DailyProgress, Resource, Milestone, Goal

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ("username", "email") # UserCreationForm automatically adds password fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "User Name"
        self.fields['email'].label = "Email Address"
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @ . + - _ only.'
        if 'password1' in self.fields:
            self.fields['password1'].label = "Password"
        if 'password2' in self.fields:
            self.fields['password2'].label = "Confirm Password"

    def clean_email(self):
        """Ensure email is unique across all users."""
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user with this email address already exists.")
        return email.lower()  # Normalize email to lowercase

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'description', 'difficulty_level', 'date_started']
        widgets = {
            'date_started': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class TopicForm(forms.ModelForm):
    new_language = forms.CharField(required=False, label="Or add new language", widget=forms.TextInput(attrs={'placeholder': 'Type new language name'}))

    class Meta:
        model = Topic
        fields = ['language', 'name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['language'].required = False

        # SECURITY FIX: Only show languages belonging to this user
        if user:
            self.fields['language'].queryset = Language.objects.filter(user=user)

    def clean(self):
        cleaned_data = super().clean()
        language = cleaned_data.get('language')
        new_language = cleaned_data.get('new_language')

        if not language and not new_language:
            raise forms.ValidationError("Please select a language or add a new one.")

        # SECURITY FIX: Validate that selected language belongs to user
        if language and self.user and language.user != self.user:
            raise forms.ValidationError("You don't have permission to use this language.")

        if new_language:
            # SECURITY FIX: Create language for this specific user only
            language, created = Language.objects.get_or_create(
                name=new_language,
                user=self.user
            )
            cleaned_data['language'] = language
            self.instance.language = language

        return cleaned_data

class DailyProgressForm(forms.ModelForm):
    new_language = forms.CharField(required=False, label="Or add new language", widget=forms.TextInput(attrs={'placeholder': 'Type new language name'}))

    class Meta:
        model = DailyProgress
        fields = ['language', 'topic', 'date', 'what_i_learned', 'time_spent_minutes', 'confidence_level']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'what_i_learned': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['language'].required = False

        # SECURITY FIX: Only show languages and topics belonging to this user
        if user:
            self.fields['language'].queryset = Language.objects.filter(user=user)
            self.fields['topic'].queryset = Topic.objects.filter(user=user)

    def clean(self):
        cleaned_data = super().clean()
        language = cleaned_data.get('language')
        new_language = cleaned_data.get('new_language')
        topic = cleaned_data.get('topic')

        if not language and not new_language:
            raise forms.ValidationError("Please select a language or add a new one.")

        # SECURITY FIX: Validate that selected language belongs to user
        if language and self.user and language.user != self.user:
            raise forms.ValidationError("You don't have permission to use this language.")

        # SECURITY FIX: Validate that selected topic belongs to user
        if topic and self.user and topic.user != self.user:
            raise forms.ValidationError("You don't have permission to use this topic.")

        if new_language:
            # SECURITY FIX: Create language for this specific user only
            language, created = Language.objects.get_or_create(
                name=new_language,
                user=self.user
            )
            cleaned_data['language'] = language
            self.instance.language = language

        return cleaned_data

class ResourceForm(forms.ModelForm):
    new_language = forms.CharField(required=False, label="Or add new language", widget=forms.TextInput(attrs={'placeholder': 'Type new language name'}))

    class Meta:
        model = Resource
        fields = ['language', 'title', 'link', 'resource_type']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['language'].required = False

        # SECURITY FIX: Only show languages belonging to this user
        if user:
            self.fields['language'].queryset = Language.objects.filter(user=user)

    def clean(self):
        cleaned_data = super().clean()
        language = cleaned_data.get('language')
        new_language = cleaned_data.get('new_language')
        link = cleaned_data.get('link')

        if not language and not new_language:
            raise forms.ValidationError("Please select a language or add a new one.")

        # SECURITY FIX: Validate that selected language belongs to user
        if language and self.user and language.user != self.user:
            raise forms.ValidationError("You don't have permission to use this language.")

        # SECURITY FIX: Only allow http:// and https:// URL schemes
        if link:
            link_lower = link.lower().strip()
            if not link_lower.startswith(('http://', 'https://')):
                raise forms.ValidationError("Invalid URL scheme. Only http:// and https:// URLs are allowed.")

        if new_language:
            # SECURITY FIX: Create language for this specific user only
            language, created = Language.objects.get_or_create(
                name=new_language,
                user=self.user
            )
            cleaned_data['language'] = language
            self.instance.language = language

        return cleaned_data

class MilestoneForm(forms.ModelForm):
    new_language = forms.CharField(required=False, label="Or add new language", widget=forms.TextInput(attrs={'placeholder': 'Type new language name'}))

    class Meta:
        model = Milestone
        fields = ['language', 'title', 'details', 'is_completed']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['language'].required = False

        # SECURITY FIX: Only show languages belonging to this user
        if user:
            self.fields['language'].queryset = Language.objects.filter(user=user)

    def clean(self):
        cleaned_data = super().clean()
        language = cleaned_data.get('language')
        new_language = cleaned_data.get('new_language')

        if not language and not new_language:
            raise forms.ValidationError("Please select a language or add a new one.")

        # SECURITY FIX: Validate that selected language belongs to user
        if language and self.user and language.user != self.user:
            raise forms.ValidationError("You don't have permission to use this language.")

        if new_language:
            # SECURITY FIX: Create language for this specific user only
            language, created = Language.objects.get_or_create(
                name=new_language,
                user=self.user
            )
            cleaned_data['language'] = language
            self.instance.language = language

        return cleaned_data

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'details', 'target_date', 'is_completed']
        widgets = {
            'target_date': forms.DateInput(attrs={'type': 'date'}),
            'details': forms.Textarea(attrs={'rows': 3}),
        }
