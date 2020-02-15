from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
# @TODO: Initialize your Flask app here
# YOUR CODE GOES HERE

app = Flask(__name__)
justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]


@app.route("/")
def home():
    return ("Welcome to Justice League API"
            "<BR/>Returns Json<BR/>"
            "<a href=/api/v1.0/justice-league>/api/v1.0/justice-league</a>")



@app.route("/api/v1.0/justice-league")
def jsonified():
    return jsonify(justice_league_members)


if __name__ == "__main__":
    app.run(debug=True, port=5000)



