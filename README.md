# 📚 StudyTracker

A modern, full-stack web application for tracking your learning journey. Built with Django and Bootstrap 5, featuring a beautiful UI with dark mode support, responsive design, and comprehensive learning management tools.

![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **📊 Progress Tracking** - Log daily study sessions with time tracking and confidence levels
- **🎯 Goal Management** - Set and track learning objectives with deadlines
- **🏆 Milestones** - Celebrate achievements and mark important learning checkpoints
- **📚 Resource Library** - Organize learning materials, articles, and links
- **💡 Topic Organization** - Structure your learning by language/subject and subtopics
- **🌗 Dark Mode** - Beautiful dark and light themes with smooth transitions
- **📱 Fully Responsive** - Optimized for desktop, tablet, and mobile devices
- **📈 Data Visualization** - Interactive charts powered by Chart.js
- **🔒 User Authentication** - Secure login system with user-specific data isolation

## 🚀 Live Demo

[View Live Demo](#) _(Coming soon)_

## 📸 Screenshots

### Dashboard
_Beautiful overview with progress charts and quick stats_

### Dark Mode
_Seamless dark theme throughout the app_

## 🛠️ Tech Stack

- **Backend:** Python 3.12, Django 5.2.7
- **Frontend:** HTML5, CSS3, JavaScript
- **UI Framework:** Bootstrap 5.3
- **Icons:** Bootstrap Icons
- **Charts:** Chart.js
- **Database:** SQLite (development), PostgreSQL (production-ready)
- **Authentication:** Django's built-in auth system

## ⚡ Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/koki-star/studytracker.git
   cd studytracker
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and set your SECRET_KEY
   ```

5. **Run migrations**
   ```bash
   python3 manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python3 manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python3 manage.py runserver
   ```

8. **Open your browser** and navigate to `http://127.0.0.1:8000`

## 📖 Usage

1. **Sign Up** - Create your account on the landing page
2. **Add Languages** - Define what you're learning (e.g., "Python", "JavaScript")
3. **Create Topics** - Break down your learning into specific topics
4. **Log Progress** - Record your daily study sessions
5. **Set Goals** - Define what you want to achieve with deadlines
6. **Track Milestones** - Mark important achievements
7. **Save Resources** - Keep all your learning materials organized

## 📁 Project Structure

```
studytracker/
├── learning_tracker/          # Main Django project
│   ├── settings.py           # Project settings
│   ├── urls.py               # Root URL configuration
│   ├── static/               # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── style.css    # Custom styles
│   │   └── js/
│   │       ├── main.js      # Animations and interactions
│   │       └── theme-toggle.js  # Dark mode functionality
│   └── templates/            # Base templates
│       ├── base.html
│       ├── landing.html
│       └── about.html
├── tracker/                   # Main app
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── forms.py              # Form definitions
│   ├── urls.py               # App URL routing
│   ├── migrations/           # Database migrations
│   └── templates/            # App templates
│       └── tracker/
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management script
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🔧 Environment Variables

Create a `.env` file in the project root:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

**Generate a new SECRET_KEY:**
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 🎯 Key Features Explained

### User Authentication
- Custom user registration with secure password handling
- Django's built-in authentication system
- User-specific data isolation - each user only sees their own data
- Protected views with `@login_required` decorator

### Progress Tracking
- Daily log entries with date tracking
- Time tracking in minutes
- Confidence level assessment (1-5 scale)
- Notes and learnings for each session
- Linked to specific topics and languages

### Data Visualization
- Interactive charts showing time spent per language
- Progress tracking over time
- Visual representation of learning patterns
- Theme-aware chart colors

### Modern UI/UX
- Glassmorphism effects on navigation
- Smooth animations and transitions
- Scroll-triggered fade-in effects
- 3D tilt effect on cards
- Gradient text and backgrounds
- Responsive navigation with mobile menu

## 🧪 Testing

```bash
# Run Django's built-in tests
python3 manage.py test

# Check for potential issues
python3 manage.py check

# Check deployment readiness
python3 manage.py check --deploy
```

## 🚀 Deployment

This application is ready to deploy on:
- Railway
- Heroku
- DigitalOcean App Platform
- AWS Elastic Beanstalk
- Any Django-compatible platform

**Deployment checklist:**
- [ ] Generate a new `SECRET_KEY` for production
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Configure `CSRF_TRUSTED_ORIGINS` with your domain
- [ ] Run `python manage.py migrate`
- [ ] Run `python manage.py collectstatic`
- [ ] Create a superuser with `python manage.py createsuperuser`
- [ ] Use a production database (PostgreSQL recommended)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🌟 Skills Demonstrated

This project showcases:
- ✅ Full-stack web development with Django
- ✅ Modern, responsive UI design with Bootstrap
- ✅ Database design and Django ORM usage
- ✅ User authentication and authorization
- ✅ Form validation and CSRF protection
- ✅ Data visualization with Chart.js
- ✅ RESTful URL patterns
- ✅ Theme system with dark mode
- ✅ Security best practices
- ✅ Clean code organization
- ✅ Git workflow and version control

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Kokob Haile**

- LinkedIn: [@kokob-haile](https://www.linkedin.com/in/kokob-haile)
- GitHub: [@koki-star](https://github.com/koki-star)

## 💡 About

Built as a portfolio project to demonstrate modern web development skills and best practices. StudyTracker showcases end-to-end application development, from database design to user authentication to responsive UI implementation.

---

**⭐ If you found this project helpful, please give it a star!**

_Built with ❤️ for learners everywhere_
