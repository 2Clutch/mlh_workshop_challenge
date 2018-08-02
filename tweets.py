from flask import Flask
from search import tweets

app = Flask(__name__)


@app.route("/")
def index():
    for tweet in tweets:
        return tweet


if __name__ == "__main__":
    app.run()