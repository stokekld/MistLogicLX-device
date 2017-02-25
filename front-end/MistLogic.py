from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', error={})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)