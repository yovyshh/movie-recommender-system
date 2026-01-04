import streamlit as st
import pickle
import requests

# =======================
# LOAD DATA
# =======================
movies = pickle.load(open("movies.pkl", "rb"))        # DataFrame
similarity = pickle.load(open("similarity.pkl", "rb"))

API_KEY = "25e228835ed7419122b38b1e1dce889b"

# =======================
# FUNCTIONS
# =======================
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()

    if data.get('poster_path'):
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# =======================
# STREAMLIT UI
# =======================
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values,
    index=None,
    placeholder="Select a movie"

)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    st.subheader("Recommended Movies")

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            if posters[i]:
                st.image(posters[i])
            st.caption(names[i])
