FROM python:3.12
LABEL authors="Konrad Kihan"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "zti/manage.py", "runserver", "0.0.0.0:8000"]