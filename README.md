# 🎬 Movie Recommendation System

A content-based **Movie Recommendation System** built using **Python**, **Streamlit**, and **Machine Learning**.  
The system recommends movies based on textual similarity of genres, keywords, cast, crew, and overview.

---

## 🚀 Features

- 🔍 Content-based movie recommendations
- 🎞 Select movie from dropdown (no default selection)
- 🧠 Uses **cosine similarity** on movie metadata
- 🖼 Displays movie posters using **TMDB API**
- ✨ Clean and interactive Streamlit UI
- 🔐 Sensitive / large files excluded via `.gitignore`

---

## 🧠 How It Works

1. Movie metadata is processed and combined into a single **tags** column  
2. Text is vectorized using **CountVectorizer**
3. **Cosine similarity** is calculated between movies
4. Top similar movies are recommended when a movie is selected

---

## 🛠 Tech Stack

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **Streamlit**
- **NLTK**
- **TMDB API**
- **Pickle**

---

## 📂 Project Structure

movie-recommender-system/
│
├── app.py # Streamlit app
├── .gitignore # Ignored files (venv, pkl, cache)
├── README.md # Project documentation
│
└── (pkl files ignored) # Generated locally

---


API Configuration

This project uses The Movie Database (TMDB) API to fetch movie posters.
Created an account at https://www.themoviedb.org


🌱 Future Improvements
   Better recommendation accuracy (TF-IDF / embeddings)
   Add ratings and popularity filters
   User profiles & personalization
   Deploy on Streamlit Cloud
   Card-based UI with hover effects





