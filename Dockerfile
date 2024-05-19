FROM python:3.12
LABEL authors="Konrad Kihan"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
RUN mkdir -p zti/media/car_images
CMD ["python", "zti/manage.py", "makemigrations"]
CMD ["python", "zti/manage.py", "migrate"]
CMD ["python", "zti/manage.py", "runserver", "0.0.0.0:8000"]