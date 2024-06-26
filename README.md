# BEYOND THE SCREEN-FORECASTING MOVIE SUCCESS FACTORS

# Introduction

Exploring the IMDb 5000 movies dataset, we aim to decode the elements of cinematic success. Our analysis spans directors, actors, genres, and budgets to predict a film's IMDb category and success. Using advanced machine learning, we identify key factors influencing movie performance. After evaluating various models, we find the Random Forest algorithm to be the most accurate, achieving an impressive accuracy of 0.8094, even with minimal hyperparameter tuning.

To share our insights, we've developed a user-friendly Streamlit web app. This tool allows users to input key movie features and receive predictions on the IMDb score category—Poor, Average, or Good. Our goal is to empower filmmakers and industry professionals with actionable predictions to navigate the evolving film landscape confidently.

# Problem Statement

Our main goal is to develop robust models capable of predicting two key aspects of a movie's performance: its IMDb category and whether it succeeds or not. We'll analyze the dataset extensively using machine learning techniques to uncover the factors influencing a movie's categorization and success. These insights will be invaluable for filmmakers, producers, and the movie industry's advancement overall.

# Dataset Profiling

The dataset used for this project is sourced from the Kaggle repository, intended for Machine Learning Model development.

This dataset provides comprehensive information about movies, capturing various factors that influence a film's commercial success, including directors, actors, critic reviews, and audience reactions. IMDb scores are a key metric for gauging a movie's success. We utilized the IMDb 5000 movie dataset, which contains detailed data for 5043 movies across 28 different attributes. The attributes included are listed below:

1.	Color: Indicates if the movie is black-and-white or colored.
2.	Director name: Name of the movie director.
3.	num_critic_for_reviews: Number of critics who reviewed the movie.
4.	Duration: Duration of the movie in minutes.
5.	director_facebook_likes: Number of likes for the director on Facebook.
6.	actor_3_facebook_likes: Number of likes for the third lead actor on Facebook.
7.	actor2_name: Name of the second lead actor.
8.	actor_1_facebook_likes: Number of likes for the lead actor on Facebook.
9.	Gross: Gross earnings of the movie in dollars.
10.	Genres: Film categorization, such as 'Animation', 'Comedy', 'Romance', 'Horror', 'Sci-Fi', 'Action', 'Family'.
11.	actor_1_name: Name of the lead actor.
12.	Movie title: Title of the movie.
13.	num_voted_users: Number of people who voted for the movie.
14.	cast_total_facebook_likes: Total number of Facebook likes for the movie's cast.
15.	actor_3_name: Name of the third lead actor.
16.	facenumber_in_poster: Number of actors featured in the movie poster.
17.	Plot keywords: Keywords describing the movie plot.
18.	movie_imdb_link: IMDb link of the movie.
19.	num_user_for_reviews: Number of users who reviewed the movie.
20.	Language: Language in which the movie is made.
21.	Country: Country where the movie was produced.
22.	Content rating: Content rating of the movie.
23.	Budget: Budget of the movie in dollars.
24.	Title year: Year in which the movie was released.
25.	actor_2_facebook_likes: Number of Facebook likes for the second lead actor.
26.	imdb_score: IMDb score of the movie.
27.	Aspect ratio: Aspect ratio in which the movie was made.
28.	movie_facebook_likes: Total number of Facebook likes for the movie


# Streamlit Application

Deploying a machine learning model in Streamlit is a straightforward process. Streamlit is a Python library that allows you to create interactive web applications for data science and machine learning projects. A Streamlit web application was developed to host the trained machine learning model. The application provides users with a user-friendly interface to input movie features and receive predictions for IMDb score categories. The design emphasizes simplicity and interactivity.

•	Begin by installing Streamlit using pip.

•	Imported the necessary libraries such as pandas, NumPy, scikit-learn and pickle along with Streamlit.

•	Defined the layout of the application.

•	Added widgets for user input. Users can input 13 features related to movies like duration,director_facebook_likes,actor_3_facebook_likes,actor_1_facebook_likes,gross,num_voted_users,facenumber_in_poster,num_user_for_reviews,budget,title_year,actor_2_facebook_likes and  movie_facebook_likes.

•	Loaded the pre-trained Random Forest model into memory.

•	Performed predictions based on user input.

•	Presented the prediction to the user.

•	Once the app runned locally, deployed it to Streamlit Sharing.



**Hosted Website:** 

# Screenshots

![Average Prediction](https://github.com/Akhila-p-v/BEYOND_THE_SCREEN-FORECASTING_MOVIE_SUCCESS_FACTORS/blob/main/average.png)
*Average:* The movie is predicted to be a success.

![Good Prediction](https://github.com/Akhila-p-v/BEYOND_THE_SCREEN-FORECASTING_MOVIE_SUCCESS_FACTORS/blob/main/good.png)
*Good:* The movie is predicted to be a success.

![Poor Prediction](https://github.com/Akhila-p-v/BEYOND_THE_SCREEN-FORECASTING_MOVIE_SUCCESS_FACTORS/blob/main/poor.png)
*Poor:* The movie is predicted not to be a success.


