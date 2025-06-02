FROM python:3.12.7

WORKDIR /app
COPY . /app

# Install all dependencies
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate


EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=OJProject.settings

ENV PYTHONUNBUFFERED=1

# Run migrations and then the dev server at container startup
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
