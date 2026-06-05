# Recommendation System
# CodSoft AI Internship - Task 4

movies = {
    "action": [
        "Avengers: Endgame",
        "The Dark Knight",
        "Mad Max: Fury Road",
        "John Wick",
        "Mission Impossible"
    ],

    "comedy": [
        "3 Idiots",
        "Golmaal",
        "Dhamaal",
        "Hera Pheri",
        "Welcome"
    ],

    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Gravity",
        "Avatar"
    ],

    "horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle",
        "The Nun",
        "It"
    ],

    "romance": [
        "Titanic",
        "The Notebook",
        "Aashiqui 2",
        "Veer-Zaara",
        "Jab We Met"
    ]
}

print("=" * 50)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable Genres:")
for genre in movies:
    print("-", genre)

user_choice = input("\nEnter your favorite genre: ").lower()

if user_choice in movies:

    print("\nRecommended Movies:\n")

    for i, movie in enumerate(movies[user_choice], start=1):
        print(f"{i}. {movie}")

else:
    print("\nSorry! Genre not found.")