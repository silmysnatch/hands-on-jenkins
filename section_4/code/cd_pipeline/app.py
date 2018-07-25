from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "http://www.catgifpage.com/gifs/325.gif",
    "http://www.catgifpage.com/gifs/319.gif",
    "http://www.catgifpage.com/gifs/322.gif",
    "http://www.catgifpage.com/gifs/324.gif",
    "http://www.catgifpage.com/gifs/323.gif",
    "http://www.catgifpage.com/gifs/321.gif",
    "http://www.catgifpage.com/gifs/321.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
