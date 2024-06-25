# Gunakan image Python versi terbaru sebagai base image
FROM python:3.11.2-slim

# Set working directory di dalam container
WORKDIR /app

# Copy file requirements.txt dan install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy seluruh proyek Flask ke dalam container
COPY . .

# Expose port yang digunakan oleh aplikasi Flask
EXPOSE 5000

# Set environment variable untuk Flask
ENV FLASK_APP app.py

# Command untuk menjalankan aplikasi Flask saat container dijalankan
CMD ["flask", "run", "--host=0.0.0.0"]
