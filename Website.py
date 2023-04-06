from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mysecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        if "username" in session:
            return f"Welcome, {session['username']}!<br><a href='/logout'>Logout</a>"
        else:
            return redirect("/login")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password, password):
                session["username"] = username
                return redirect("/")
            else:
                return "Invalid username or password"

        return render_template("login.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            hashed_password = generate_password_hash(password, method="sha256")
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")

        return render_template("register.html")

    @app.route("/logout")
    def logout():
        session.pop("username", None)
        return redirect("/login")

    return app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

