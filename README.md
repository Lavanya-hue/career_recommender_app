# career_recommender_app

# 🎯 Career Recommender App

A full-stack web application built using **React** for the frontend and **Flask** for the backend that recommends career paths based on user-entered interests.

---

## 🔍 Overview

This application helps students and job seekers discover career options that align with their personal interests. Users simply enter a sentence describing their passions (e.g., "I love teaching and yoga"), and the app returns a curated list of potential career paths.

---

## 🛠️ Tech Stack

| Frontend         | Backend         | Styling        |
|------------------|------------------|----------------|
| React (Vite/CRA) | Flask (Python)   | CSS            |
| Axios (API calls)| Flask-CORS       | Flexbox/Grid   |

---

## 🚀 Features

- ✅ User-friendly interface to input career interests
- ✅ Backend API powered by Flask
- ✅ Intelligent keyword-based career mapping
- ✅ Dynamic results display using React state
- ✅ Error handling, loading indicators, and reset button
- ✅ Clean and minimal styling

---

## 🧠 How It Works

1. User types their interests into a text box.
2. React frontend sends the data to the Flask backend via a POST request.
3. Flask processes the input, checks for matching keywords, and returns a list of suggested careers.
4. React displays the results as career suggestion cards.

---

## 📦 Folder Structure

career-recommender-app/
│
├── client/ # React frontend
│ ├── App.js
│ ├── App.css
│ └── ...
│
├── server/ # Flask backend
│ └── app.py
│
├── README.md
└── requirements.txt
