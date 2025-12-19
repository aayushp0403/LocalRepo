import requests
from django.shortcuts import render

HANDLE = "guzudon2code"   # 🔴 change this to your Codeforces handle

def welcome(request):
    return render(request, "welcome.html")

def codeforces_stats(request):
    # Fetch user info
    user_url = f"https://codeforces.com/api/user.info?handles={HANDLE}"
    rating_url = f"https://codeforces.com/api/user.rating?handle={HANDLE}"

    user_data = requests.get(user_url).json()
    rating_data = requests.get(rating_url).json()

    user = user_data["result"][0]

    ratings = []
    contests = []

    best_contest = None
    max_change = -10**9

    for r in rating_data["result"]:
        ratings.append(r["newRating"])
        contests.append(r["contestName"])

        change = r["newRating"] - r["oldRating"]
        if change > max_change:
            max_change = change
            best_contest = r["contestName"]

    context = {
        "handle": HANDLE,
        "name": user.get("firstName", "User"),
        "rating": user.get("rating", "N/A"),
        "rank": user.get("rank", "N/A"),
        "max_rating": user.get("maxRating", "N/A"),
        "ratings": ratings,
        "contests": contests,
        "best_contest": best_contest,
    }

    return render(request, "codeforces.html", context)
