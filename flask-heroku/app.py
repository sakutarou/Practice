from flask import Flask
app =Flask(__name__)

@app.route("/")
def home():
    return main.html

@app.route("/test")
def test():
    return "Here's a test"

if __name__ == "__main__":
    app.run()