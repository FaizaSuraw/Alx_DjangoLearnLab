# 📚 Advanced Features and Security — Django Project

This project demonstrates advanced Django features and security best practices. It is part of the **ALX Software Engineering Program**, focusing on securing Django web applications against common web vulnerabilities like XSS, CSRF, SQL Injection, and insecure cookies or connections.

---

---

## ✅ Features Implemented

### 1. **Permission-Based Views**
- Views are protected using `@permission_required` decorators to enforce access control.
- Example permissions: `can_view`, `can_create`.

### 2. **Security Best Practices**
#### 🔐 `settings.py` Security Configuration:
- `DEBUG = False` for production.
- `SECURE_SSL_REDIRECT = True`
- `SECURE_HSTS_SECONDS = 31536000`
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
- `SECURE_HSTS_PRELOAD = True`
- `X_FRAME_OPTIONS = "DENY"`
- `SECURE_CONTENT_TYPE_NOSNIFF = True`
- `SECURE_BROWSER_XSS_FILTER = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`

#### 🧠 Secure Coding Practices:
- Django ORM is used to prevent raw SQL injections.
- User inputs are sanitized using Django `ModelForms`.

### 3. **CSRF Protection**
- All HTML forms use `{% csrf_token %}` to protect against Cross-Site Request Forgery.

### 4. **Content Security Policy (CSP)**
- Middleware added via `django-csp`:
```python
'django.middleware.security.SecurityMiddleware',
'csp.middleware.CSPMiddleware',

'''settings.py
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
CSP_SCRIPT_SRC = ("'self'",)

'''to run the project
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
