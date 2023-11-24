from functools import wraps
from flask import Flask, render_template, redirect, url_for, flash,request,abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm,RegisterForm,CommentForm,LoginForm
from libgravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


##CONFIGURE TABLES

class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    is_active = db.Column(db.Boolean, default=True) 
    posts = db.relationship('BlogPost', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)

    def __init__(self,name, email,password):
        self.name = name
        self.email = email
        self.password = password

    def get_id(self):
        return str(self.id)



class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(user_id)


def adminonly(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if current_user.get_id() == 1:  # Replace with your authentication logic
            flash('Please log in to access this page.', 'warning')
            abort(403)
        return view_func(*args, **kwargs)
    return wrapper


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register',methods=['GET','POSt'])
def register():
    register_form = RegisterForm()
    if request.method == 'POST':
        email = register_form.email.data
        password = register_form.password.data
        name = register_form.name.data
        hashed_password=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(name=name,email=email,password=hashed_password)
        if db.session.query(User).filter(User.email==new_user.email).first():
            flash('User already exist.. Please Login')
            return redirect(url_for('login'))
        else:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration Successful')
            user=db.session.query(User).filter(User.email==new_user.email).first()
            login_user(user)
            flash('Logged in Successfully')
            return redirect(url_for('get_all_posts'))
    return render_template("register.html",form=register_form)


@app.route('/login',methods=['GET','POSt'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        email = login_form.email.data
        password = login_form.password.data
        user = db.session.query(User).filter(User.email==email).first()
        if user == None:
            flash('User does not exist')   
            return redirect(url_for('login')) 
        elif load_user(user.id):
            if check_password_hash(str(user.password),str(password)):
                login_user(user)
                flash('Logged in Successfully')
                return redirect(url_for('get_all_posts'))
        else:
            flash('invalid credentials')
    return render_template("login.html",form=login_form)


@app.route('/logout',methods=['GET','POSt'])
@login_required
def logout():
    logout_user()
    flash('Logged Out Successfully')
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>",methods=['GET','POSt'])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    comments = Comment.query.all()
    comment_form = CommentForm()
    g = Gravatar('someemail@gmail.com')
    gravatar_url=g.get_image()
    
    if request.method == 'POST':
        comment_text = comment_form.body.data
        new_comment = Comment(text=comment_text,user_id=current_user.get_id(),post_id=requested_post.id)
        if current_user.get_id() == None:
            flash("Create an Account or Login")
            return redirect(url_for('login'))
        else:
            db.session.add(new_comment)
            db.session.commit()
    return render_template("post.html", post=requested_post,form=comment_form,all_comments=comments,g_url=gravatar_url)


@app.route("/about",methods=['GET','POSt'])
def about():
    return render_template("about.html")


@app.route("/contact",methods=['GET','POSt'])
def contact():
    return render_template("contact.html")


@app.route("/new-post",methods=['GET','POSt'])
@login_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=str(form.img_url.data),
            author=str(current_user.get_id()),
            user_id=current_user.get_id(),
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>",methods=['GET','POSt'])
@adminonly
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form,is_edit=True)


@app.route("/delete/<int:post_id>",methods=['GET','POSt'])
@adminonly
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
