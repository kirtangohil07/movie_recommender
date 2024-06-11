import streamlit as st
import joblib
import pandas as pd
import pickle

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load the movies data
with open('movie_dict.pkl', 'rb') as file:
    movies_dict = pickle.load(file)
movies = pd.DataFrame(movies_dict)

# Load the similarity data using joblib
similarity = joblib.load('similarity.pkl')

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for i in range(5):
        with columns[i]:
            st.text(recommended_movie_names[i])
