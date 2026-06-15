# 🎬 AI Movie Recommendation System

A simple and interactive Movie Recommendation System developed in Python that suggests movies based on genre similarity using Machine Learning techniques.

## 📌 Project Overview

This project recommends movies to users based on their selected movie or preferred genre. It uses Content-Based Filtering with Count Vectorization and Cosine Similarity to identify movies with similar genres.

The application provides a clean menu-driven interface in the terminal and displays recommendations, top-rated movies, movie statistics, and available movies.

## 🚀 Features

✅ Recommend movies based on a selected movie

✅ Genre-based movie recommendations

✅ Top-rated movie list

✅ Available movie catalog

✅ Movie statistics dashboard

✅ Fuzzy search suggestions for misspelled movie names

✅ User-friendly terminal interface using Rich library

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-Learn
* Rich
* RapidFuzz


## 🧠 Machine Learning Concept Used

### Content-Based Filtering

The recommendation system analyzes movie genres and finds similarities between movies using:

* CountVectorizer
* Cosine Similarity

This allows the system to recommend movies with similar genre characteristics.


## 📂 Project Structure

Task4_Movie_Recommendation_System/
│
├── recommendation_system.py
├── movies.csv
├── requirements.txt
├── README.md
└── screenshots/
    ├── menu.png
    ├── recommendation.png
    └── top_rated.png


## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Task4_Movie_Recommendation_System.git
cd Task4_Movie_Recommendation_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python recommendation_system.py
```

---

## 📸 Screenshots

### Main Menu

(Add Screenshot Here)

### Movie Recommendations

(Add Screenshot Here)

### Top Rated Movies

(Add Screenshot Here)

## 📊 Sample Output

MENU
1. Recommend by Movie
2. Recommend by Genre
3. Top Rated Movies
4. Available Movies
5. Statistics
6. Exit


### Recommendation Example

Enter movie name: Avatar

Recommended Movies:
- Avengers Endgame
- The Martian
- Inception
- Mad Max Fury Road
- Interstellar


## 🎯 Future Improvements

* Graphical User Interface (GUI)
* Web-based deployment using Streamlit
* Larger movie dataset
* Movie poster integration
* User rating system
* Collaborative Filtering recommendations


## 👩‍💻 Author

**Shraddha Chauhan**

B.Tech Information Technology Student

Passionate about Artificial Intelligence, Machine Learning, and Software Development.

## ⭐ Acknowledgement

This project was developed as part of the **CodSoft Artificial Intelligence Internship Program**.
