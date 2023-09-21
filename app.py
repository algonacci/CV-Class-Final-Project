import os

from flask import Flask

from index import bp as index_bp
from orange_diseases import bp as orange_bp

app = Flask(__name__)


app.register_blueprint(index_bp)
app.register_blueprint(orange_bp)


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
