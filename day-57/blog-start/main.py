from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    print(blog_response.status_code)
    blog_data = blog_response.json()
    return render_template("index.html",all_posts = blog_data)

@app.route('/post/<id>')
def view_post(id):
    blog_response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    print(blog_response.status_code)
    blog_data = blog_response.json()
    blog_post = [post  for post in blog_data if int(id) == post['id']  ]
    return render_template('post.html',post_title=blog_post[0]['title'],post_body=blog_post[0]['body'])

if __name__ == "__main__":
    app.run(debug=True)
