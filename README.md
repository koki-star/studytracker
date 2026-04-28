# StudyTracker

![Django](https://img.shields.io/badge/Django-5.2.7-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A personal learning tracker I built with Django. You can log daily study sessions, set goals, track milestones, and organize resources by language — all tied to your own account.

**[Live Demo](https://studytracker-j38o.onrender.com/)**

## Features

- Daily progress logging with time tracking and confidence levels
- Goal setting with target dates and completion tracking
- Milestone tracking to mark achievements
- Resource library organized by language
- Topic organization within each language
- Dashboard with time visualization charts
- Dark mode support
- Per-user data isolation — accounts are fully separate

## Tech Stack

- Python 3.12 / Django 5.2.7
- Bootstrap 5.3 + custom glassmorphism design
- CSS scroll-driven animations with Intersection Observer fallback
- Chart.js for dashboard visualizations
- PostgreSQL (production) / SQLite (development)
- WhiteNoise for static files

## Local Setup

Clone the repo, copy `.env.example` to `.env`, install with `pip install -r requirements.txt`, then run `python3 manage.py migrate && python3 manage.py runserver`.

## Skills Demonstrated

- Full-stack Django development (models, views, forms, URLs)
- Custom middleware for security headers
- User authentication with per-user data access control
- Modern CSS (glassmorphism, scroll-timeline API, custom properties)
- JavaScript animations with graceful degradation
- Responsive mobile-first design
- Database design with Django ORM
- Production deployment and environment configuration

## License

MIT License

## Author

- GitHub: [@koki-star](https://github.com/koki-star)
- LinkedIn: [@kokob-haile](https://www.linkedin.com/in/kokob-haile)
