# 🔗 URL Shortener with Analytics

A backend system built using **FastAPI** and **SQLAlchemy** that converts long URLs into short, unique links with persistent storage and click analytics.

---

## 🚀 Features

* 🔗 Generate short URLs from long URLs
* 💾 Persistent storage using SQLite
* 🔁 Collision handling for unique short codes
* ↪️ HTTP redirect to original URL
* 📊 Click tracking (analytics)
* 📈 Endpoint to retrieve usage statistics

---

## 🧠 System Design Overview

* FastAPI handles API requests and routing
* SQLAlchemy ORM manages database interactions
* SQLite used for lightweight persistent storage
* Unique short codes generated using random alphanumeric strings
* Click count incremented on every redirect

---

## 🛠 Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Language:** Python

---

## 📡 API Endpoints

### 1. Shorten URL

**POST** `/shorten`

**Request Body:**

```json
{
  "url": "https://example.com"
}
```

**Response:**

```json
{
  "short_url": "http://short.url/abc123"
}
```

---

### 2. Redirect to Original URL

**GET** `/{short_code}`

➡️ Redirects to the original URL and increments click count.

---

### 3. Get Analytics

**GET** `/stats/{short_code}`

**Response:**

```json
{
  "short_code": "abc123",
  "original_url": "https://example.com",
  "clicks": 5
}
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd url-shortener
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

---

## 📌 Notes

* The SQLite database file (`*.db`) is ignored via `.gitignore`
* Database tables are automatically created on startup
* Redirect endpoint should be tested via browser (Swagger may not handle redirects properly)

---

## 🔮 Future Improvements

* ⚡ Redis caching for faster lookups
* ⏳ Link expiration support
* ✏️ Custom short URLs
* 🌐 Deployment on cloud (AWS/GCP)
* 🔐 Authentication & rate limiting

---

## 👨‍💻 Author

**Sayak Mitra**

* GitHub: https://github.com/loneranger3221
* LinkedIn: https://linkedin.com/in/sayak-mitra12

---

## ⭐ If you found this useful, consider giving it a star!
