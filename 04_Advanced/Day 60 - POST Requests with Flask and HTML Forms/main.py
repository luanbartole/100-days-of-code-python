from flask import Flask, render_template, request
import requests
import smtplib
import os

BOT_EMAIL = os.environ.get("PYTHON_EMAIL")
BOT_EMAIL_PASSWORD = os.environ.get("PYTHON_EMAIL_PASSWORD")
user_email = os.environ.get("USER_EMAIL")
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(BOT_EMAIL, BOT_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=BOT_EMAIL,
                to_addrs=user_email,
                msg=f"Subject: Blog Contact Form - {data['username']} \n\nMessage: {data['message']} \n\n"
                    f"Email: {data['email']} \nPhone Number: {data['phone']}"
            )
        print(data["username"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")


@app.route("/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
