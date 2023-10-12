from flask import Flask, render_template,request
import requests

app = Flask(__name__, static_folder="static")

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/4c425f61384429c24825"
    blog_response = requests.get(blog_url)
    if blog_response.status_code == 200:
        blog_data = blog_response.json()   
    return render_template("index.html",all_posts=blog_data)

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/post/<post_id>')
def view_post(post_id):
    blog_url = "https://api.npoint.io/4c425f61384429c24825"
    blog_response = requests.get(blog_url)
    if blog_response.status_code == 200:
        post = [blog_data for blog_data in blog_response.json() if blog_data["id"] == int(post_id)]
    return render_template("post.html",selected=post)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'GET':
       return render_template("contact.html")
    elif request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        message=request.form['message']
        return render_template("success.html")
    return render_template("contact.html")

  



if __name__ == "__main__":
    app.run(debug=True)