from flask import Flask, jsonify, request
import csv

all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
   

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
   
@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    

if __name__ == "__main__":
  app.run()
