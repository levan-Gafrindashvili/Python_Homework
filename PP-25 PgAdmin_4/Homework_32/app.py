from flask import Flask, render_template
from models import movies

app = Flask(__name__)


@app.route('/')
def index():
    total_movies = len(movies)
    avg_duration = sum(movie['duration'] for movie in movies) / total_movies
    return render_template("index.html", movies=movies, total=total_movies, average_duration=avg_duration)

if __name__ == "__main__":
    app.run(debug=True)