Final Project: Otomatisasi CI/CD untuk Pengembangan Aplikasi Website Perpustakaan Sederhana
Kelompok SatSet
Wahib Muhibi Nur (05211940000059)
Achmad Hussein Azzaydi (5026211134)
Algracevian Andrea Gibran Syahrial (05211940000056)
Deskripsi Proyek
Proyek ini bertujuan untuk mengotomatisasi proses Continuous Integration (CI) dan Continuous Deployment (CD) untuk sebuah aplikasi web perpustakaan sederhana. Proyek mencakup pengembangan aplikasi, kontainerisasi dengan Docker, dan otomatisasi pipeline menggunakan GitHub Actions.

Lingkup Proyek
Pipeline CI/CD: Mencakup versi kontrol, pengujian otomatis, kontainerisasi, deployment, monitoring, dan keamanan.
Deploy ke Cloud: Aplikasi web di-deploy ke AWS menggunakan Docker.
Pengembangan Lokal: Pengembangan dan pengujian aplikasi secara lokal menggunakan Docker.
Tahap Proyek
Tahap 1: Perencanaan Proyek dan Pengaturan Awal
Definisi Lingkup dan Tujuan: Deploy aplikasi web ke Cloud dan otomatisasi prosesnya dengan GitHub Actions.
Rencana Proyek dan Timeline: Menggunakan Trello untuk manajemen proyek dan Figma untuk desain awal.
Trello Board
Figma Design
Sistem Versi Kontrol: Membuat repository GitHub dan mengundang kolaborator.
Repository GitHub
Konfigurasi Alat CI/CD: Menggunakan GitHub Actions dan Docker.
Tahap 2: Integrasi Berkelanjutan dan Pengembangan Awal
Strategi Branching: Menggunakan branch main untuk produksi dan dev untuk pengembangan.
Pengembangan Aplikasi: Menggunakan Flask, Python, dan Docker.
Struktur Proyek:
lua
Copy code
/perpussatset
|-- app.py
|-- requirements.txt
|-- Dockerfile
|-- templates/
|-- static/
Dockerfile:
Dockerfile
Copy code
FROM python:3.11.2-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP app.py
CMD ["flask", "run", "--host=0.0.0.0"]
docker-compose.yml:
yaml
Copy code
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      FLASK_APP: app.py
      FLASK_ENV: development
    volumes:
      - .:/app
Tahap 3: Deployment Berkelanjutan dan Otomatisasi Infrastruktur
Uji Coba Deploy Manual: Melakukan deploy manual ke AWS untuk memahami prosesnya.
Pengembangan Skrip Otomatisasi: Menggunakan GitHub Actions untuk otomatisasi build, test, dan deploy.
Implementasi CD: Mengotomatiskan proses deployment ke AWS ECS menggunakan GitHub Actions.
Tahap 4: Monitoring, Keamanan, dan Presentasi Akhir
Monitoring: Menggunakan Prometheus dan Grafana untuk monitoring aplikasi.
Keamanan: Menyertakan pemindaian keamanan OWASP ZAP dalam workflow GitHub Actions.
Dokumentasi dan Presentasi: Menyusun dokumentasi proyek dan menyiapkan presentasi akhir.
Hasil Proyek
Repository VCS GitHub: Link Repository
Workflow GitHub Actions: Konfigurasi CI/CD untuk build, test, dan deploy.
Aplikasi yang Berjalan: Link Aplikasi
Langkah-langkah untuk Menjalankan Proyek
Clone Repository:

sh
Copy code
git clone https://github.com/wahibmuhibi/perpussatset
cd perpussatset
Setup Virtual Environment:

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Jalankan Aplikasi Secara Lokal:

sh
Copy code
docker-compose up
Akses Aplikasi di Browser:

http://localhost:5000
Jalankan Unit Testing:

sh
Copy code
pytest
Dokumentasi Tambahan
Presentasi Akhir: Link Presentasi
Dokumentasi Lengkap: Link Dokumentasi
Tim Pengembang
Wahib Muhibi Nur: wahib@example.com
Achmad Hussein Azzaydi: hussein@example.com
Algracevian Andrea Gibran Syahrial: algracevian@example.com
