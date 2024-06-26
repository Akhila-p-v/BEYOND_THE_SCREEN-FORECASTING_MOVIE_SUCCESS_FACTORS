import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('best_random_forest_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Background image from URL */
    .stApp {
        background-image: url("https://github.com/Akhila-p-v/BEYOND_THE_SCREEN-FORECASTING_MOVIE_SUCCESS_FACTORS/blob/main/bg3.jpg?raw=true");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Input fields styling */
    .stNumberInput input {
        background-color: beige;
        color: black;
        border-radius: 5px;
        border: 1px solid #8B4513; /* dark brown border */
        padding: 5px;
        font-size: 16px;
    }

    /* Labels styling */
    .stNumberInput label {
        color: black;
        font-size: 16px;
    }

    /* Title styling */
    .stMarkdown h1 {
        color: black;
        text-shadow: 1px 1px 2px white;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }

    /* Align text to the left */
    .stMarkdown p, .stNumberInput, .stTextInput, .stButton {
        text-align: left;
    }

    /* Align all tabs to the left */
    .stTabs [role="tablist"] {
        text-align: left;
    }

    /* + and - buttons styling */
    .stNumberInput button {
        background-color: #8B4513; /* dark brown */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 18px;
        padding: 3px;
        margin: 0 2px;
    }

    /* Predict button styling */
    .stButton button {
        background-color: #8B4513; /* dark brown */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 18px;
        padding: 10px 20px;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Predict button text color */
    .stButton button span {
        color: white;
    }

    /* Error message styling */
    .stAlert[data-baseweb="notification"] div[role="alert"] {
        background-color: rgba(0, 0, 0, 0.8);
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
    }

    /* Success message styling */
    .stAlert[data-baseweb="notification"] div[role="alertdialog"] {
        background-color: rgba(255, 215, 0, 0.8);
        color: black;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
    }

    /* Column styling */
    .stColumn {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 5px;
        padding: 15px;
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Movie Success Prediction")
st.write("Enter the details of the movie:")

col1, col2 = st.columns(2)

# Input fields for user to enter the movie details
with col1:
    num_critic_for_reviews = st.number_input("Number of Critic Reviews", min_value=2.0, max_value=813.0, value=138.0)
    duration = st.number_input("Duration (minutes)", min_value=37.0, max_value=330.0, value=106.0)
    director_facebook_likes = st.number_input("Director Facebook Likes", min_value=0.0, max_value=23000.0, value=63.0)
    actor_3_facebook_likes = st.number_input("Actor 3 Facebook Likes", min_value=0.0, max_value=23000.0, value=436.0)
    actor_1_facebook_likes = st.number_input("Actor 1 Facebook Likes", min_value=0.0, max_value=640000.0, value=1000.0)
    gross = st.number_input("Gross Revenue", min_value=162.0, max_value=760505800.0, value=30054710.5)
    num_voted_users = st.number_input("Number of Voted Users", min_value=91.0, max_value=1689764.0, value=53993.5)

with col2:
    facenumber_in_poster = st.number_input("Face Number in Poster", min_value=0.0, max_value=43.0, value=1.0)
    num_user_for_reviews = st.number_input("Number of User Reviews", min_value=4.0, max_value=5060.0, value=209.5)
    budget = st.number_input("Budget", min_value=218.0, max_value=12215500000.0, value=25000000.0)
    title_year = st.number_input("Title Year", min_value=1927.0, max_value=2016.0, value=2004.0)
    actor_2_facebook_likes = st.number_input("Actor 2 Facebook Likes", min_value=0.0, max_value=137000.0, value=683.0)
    movie_facebook_likes = st.number_input("Movie Facebook Likes", min_value=0.0, max_value=349000.0, value=225.5)

# Creating empty columns around the button for centering
col3, col4, col5 = st.columns([2, 1, 2])

with col4:
    submitted = st.button('Predict')

if submitted:
    user_features = np.array([
        num_critic_for_reviews, duration, director_facebook_likes,
        actor_3_facebook_likes, actor_1_facebook_likes, gross,
        num_voted_users, facenumber_in_poster, num_user_for_reviews, 
        budget, title_year, actor_2_facebook_likes, movie_facebook_likes,
    ]).reshape(1, -1)
    
    predicted_category = loaded_model.predict(user_features)[0]
    labels = ['Poor', 'Average', 'Good']
    
    # Convert predicted_category to integer or use directly if already numeric
    if isinstance(predicted_category, str):
        predicted_category = labels.index(predicted_category)
    predicted_label = labels[predicted_category]

    st.write(f"Predicted Category: {predicted_label}")

    # Styling the alert box
    if predicted_label == 'Poor':
        st.markdown(
            f'<div style="background-color: rgba(0, 0, 0, 0.8); color: white; border-radius: 5px; padding: 10px; font-size: 18px; font-weight: bold;">The movie is predicted not to be a success!</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div style="background-color: rgba(255, 215, 0, 0.8); color: black; border-radius: 5px; padding: 10px; font-size: 18px; font-weight: bold;">The movie is predicted to be a success!</div>',
            unsafe_allow_html=True
        )
