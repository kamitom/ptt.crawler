FROM python:3.8.0-alpine3.10

LABEL AUTHOR = "TOM" \
  EMAIL = "TOM@TEST.COM"

COPY . /app

WORKDIR /app

# COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install Flask
# RUN pip install Faker
# RUN pip install beautifulsoup4

EXPOSE 5000/tcp

CMD ["python", "app.py"]
