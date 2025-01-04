# WebHealth Project

A web-based health application built with Django and deployed on Railway platform.

## 🚀 Overview

WebHealth is a Django-based web application designed to provide health-related services and information. The project leverages the power of Django framework for backend operations and Railway for seamless deployment and hosting.

## ⚡ Features

- Django-powered backend
- Railway platform deployment
- Secure user authentication
- Responsive design
- Health information management

## 🛠️ Tech Stack

- **Backend Framework:** Django
- **Database:** PostgreSQL
- **Deployment Platform:** Railway
- **Version Control:** Git
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Django Authentication System

## 📋 Prerequisites

- Python 3.8+
- Django 4.0+
- Git
- PostgreSQL
- pip (Python package manager)

## 🚀 Local Development Setup

1. Clone the repository
```bash
git clone https://github.com/EmperorDa8/webhealth.git
cd webhealth
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

## 🌐 Deployment

This project is configured for deployment on Railway. Follow these steps to deploy:

1. Create a Railway account
2. Connect your GitHub repository
3. Configure environment variables in Railway dashboard
4. Deploy the application

## 📝 Environment Variables

Required environment variables:
- `SECRET_KEY`
- `DEBUG`
- `DATABASE_URL`
- `ALLOWED_HOSTS`

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- EmperorDa8

## 🙏 Acknowledgments

- Django Documentation
- Railway Platform
- Open Source Community