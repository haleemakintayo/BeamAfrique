# BeamAfrique
 


---

```markdown
# BeamAfrique

BeamAfrique is a full-stack application that combines a Django REST Framework backend with a React frontend. It enables content uploads (for home ads, news, TV, events, magazine content), user authentication with JWT, and visitor analytics. Additionally, it features a contact form that sends emails via Gmail.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
  - [Backend (Django)](#backend-django)
  - [Frontend (React)](#frontend-react)
- [Configuration](#configuration)
  - [Email Settings (Gmail)](#email-settings-gmail)
  - [JWT Authentication](#jwt-authentication)
- [Running the Application](#running-the-application)
- [Analytics](#analytics)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- **Content Management:** Upload various types of content (videos, news, TV, events, magazines) with file uploads.
- **User Authentication:** Signup and login with JWT-based authentication.
- **Contact Form:** Send emails directly to your designated email using Gmail’s SMTP.
- **Analytics:** Track visitor statistics (daily, weekly, monthly) and per-post analytics.
- **Dashboard:** Manage posts (delete content) and view analytics in a unified admin dashboard.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework, SimpleJWT
- **Frontend:** React, Axios, Tailwind CSS, React Router
- **Analytics:** Custom Django models & middleware or Google Analytics (optional)
- **Email:** Gmail SMTP (or console backend for development)

## Setup

### Backend (Django)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/beamafrique.git
   cd beamafrique/backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
      # On Windows: 
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```



5. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional, for Django admin):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Serve Media Files (development only):**

   In your project’s main `urls.py`, include:

   ```python
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns = [
       # ... your URL patterns ...
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

### Frontend (React)

1. **Navigate to the frontend directory:**

   ```bash
   cd ../frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Configure API endpoints (if necessary):**

   Update the API URL in your axios calls if needed. You might consider adding a proxy in `package.json`:
   ```json
   "proxy": "http://127.0.0.1:8000"
   ```

4. **Run the development server:**

   ```bash
   npm start
   ```

## Configuration

### Email Settings (Gmail)

1. **Enable 2FA on your Gmail account.**
2. **Generate an App Password:**
   - Go to [Google Account](https://myaccount.google.com/).
   - Navigate to **Security > App passwords**.
   - Create a new app password for “Mail” (e.g., for your Django app).
   - Copy the 16-digit app password and add it to your `.env` file as `EMAIL_HOST_PASSWORD`.
3. **.env Example:**

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   DEFAULT_FROM_EMAIL=your_email@gmail.com
   CONTACT_EMAIL=recipient@example.com
   ```

### JWT Authentication

1. **Install SimpleJWT:**

   ```bash
   pip install djangorestframework-simplejwt
   ```

2. **Update your Django REST Framework settings in `settings.py`:**

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }
   ```

3. **Include token endpoints in your URL configuration:**

   ```python
   from django.urls import path
   from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

   urlpatterns = [
       # ... other endpoints ...
       path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   ]
   ```

## Running the Application

1. **Start Django Server:**  
   In the backend directory:
   ```bash
   python manage.py runserver
   ```



3. **Access the App:**  
.  
   API endpoints are available at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

## Analytics

For basic user analytics, we track visits using a custom model:




## API Endpoints

- **Content Upload:**  
  - `GET /api/upload/?section=<section>` – Retrieve content uploads filtered by section.
  - `POST /api/upload/` – Upload generic content.
  - `DELETE /api/upload/<id>/` – Delete a specific content upload.

- **Magazine Content:**  
  - `POST /api/magazine/` – Upload magazine content.
  - `GET /api/magazines/` – Retrieve magazine content.
  - `DELETE /api/magazine/<id>/` – Delete a specific magazine entry.

- **User Authentication:**  
  - `POST /api/signup/` – User registration.
  - `POST /api/token/` – User login (JWT).
  - `POST /api/token/refresh/` – Refresh JWT token.

- **Contact Form:**  
  - `POST /api/send-email/` – Send an email from the contact form.

- **Analytics:**  
  - `GET /api/app-analytics/` – Retrieve visit statistics (daily, weekly, monthly).

## License

[MIT License](LICENSE)
```

---


