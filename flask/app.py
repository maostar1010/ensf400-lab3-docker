from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://picsum.photos/seed/2/200/300",
    "https://picsum.photos/seed/3/200/300",
    "https://picsum.photos/seed/4/200/300",
    "https://picsum.photos/seed/5/200/300",
    "https://picsum.photos/seed/6/200/300",
    "https://picsum.photos/seed/7/200/300",
    "https://picsum.photos/seed/8/200/300",
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
