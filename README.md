# Movie Recommender System

A content-based movie recommendation system built using **Python**, **Machine Learning**, and **Streamlit**. The system suggests movies similar to a user's choice based on metadata such as genres, keywords, cast, and crew.

## Live Demo
The application features a sleek web interface where you can select a movie and instantly receive 5 recommendations with posters fetched via **The Movie Database (TMDB) API**.

## Features

- **Content-Based Filtering**: Recommends movies based on similarity in tags (genres, overview, cast, director).
- **Interactive UI**: Built with Streamlit for a smooth user experience.
- **Real-time Posters**: Dynamically fetches movie posters using the TMDB API.
- **Natural Language Processing**: Uses `CountVectorizer` and Stemming to process movie metadata into searchable tags.

## Machine Learning Workflow

1. **Data Collection**: Used the [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
2. **Data Preprocessing**:
   - Merged `movies` and `credits` datasets.
   - Cleaned and extracted relevant fields (Genres, Keywords, Top 3 Cast, Director).
   - Combined all features into a single `tags` column.
   - Applied **Porter Stemming** to normalize words.
3. **Vectorization**: Converted text tags into 5000-dimensional vectors using `CountVectorizer` (Bag of Words).
4. **Similarity Calculation**: Used **Cosine Similarity** to measure the distance between movie vectors.
5. **Model Persistence**: Saved the processed data and similarity matrix using `pickle` for fast loading in the web app.

## Tech Stack

- **Language**: Python 3.x
- **Libraries**: Pandas, NumPy, Scikit-Learn, NLTK, Requests
- **Frontend**: Streamlit
- **API**: TMDB API

## Project Structure

```text
.
├── app.py                  # Streamlit web application
├── movie-recommendation.ipynb # Data preprocessing & model building
├── movies.pkl              # Pickled movie data (DataFrame)
├── similarity.pkl          # Pickled cosine similarity matrix
├── tmdb_5000_movies.csv    # Raw movie dataset
└── tmdb_5000_credits.csv   # Raw credits dataset
```

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yovyshh/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit pandas requests scikit-learn
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## License
This project is open-source. Feel free to use and improve it!

---
*Developed by Vaishnav T. Prakash*
