from flask import Flask

app = Flask (__name__)

@app.route("/")
def home():
    print("Hello world ...")
    return("Hi there client!")

@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

if __name__ == "__main__":
    app.run(debug=True)