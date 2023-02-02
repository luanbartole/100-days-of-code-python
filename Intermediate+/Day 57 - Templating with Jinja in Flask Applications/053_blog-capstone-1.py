from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

# Get the posts from the json/API
response = requests.get(blog_url)
all_posts = response.json()
# all_posts = [post for post in posts_data]
number_of_posts = len(all_posts)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts, total_posts=number_of_posts)


@app.route('/post/<post_index>')
def get_post(post_index):
    id = int(post_index)-1
    return render_template("post.html", post=all_posts[id])


if __name__ == "__main__":
    app.run(debug=True)
