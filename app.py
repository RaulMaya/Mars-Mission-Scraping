from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_mission_db")

@app.route("/")
def home():
    scrap_values = mongo.db.mars.find_one()
    return render_template("index.html", mars=scrap_values)

@app.route("/scrape")
def scrape():
    scrap_values= scrape_mars.scrape()
    mongo.db.mars.update({}, scrap_values, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
