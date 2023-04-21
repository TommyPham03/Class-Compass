from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, session, url_for
from Course import create, match_course, Course, Subject

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
            #return f"Welcome, {session['username']}!<br><a href='/logout'>Logout</a>"
            return redirect("/schedule")
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
                session["user_id"] = user.id
                return redirect("/schedule")
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

    @app.route("/logout", methods=["POST"])
    def logout():
        session.clear()
        return redirect("/login")

    @app.route("/schedule")
    def schedule():
        return render_template("schedule.html")
    @app.route("/enter_classes", methods=["GET", "POST"])
    def enter_classes():
        if request.method == "POST":
            class_name = request.form["classname"]
            professor = request.form["professor"]
            semester = request.form["semester"]
            hours = request.form["hours"]

            if "user_id" not in session:
                return "User ID not found in the session. Please log in again."

            new_course = Course(name=class_name, professor=professor, semester=semester, hours=hours,
                                user_id=session["user_id"])
            db.session.add(new_course)
            db.session.commit()
            return redirect("/schedule")
        else:
            return render_template("enter_classes.html")

    @app.route("/view_classes")
    def view_classes():
            if "username" in session:
                user = User.query.filter_by(username=session["username"]).first()
                courses = Course.query.filter_by(user_id=user.id).all()
                return render_template("view_classes.html", courses=courses)
            else:
                return redirect("/login")

    @app.route('/recommend_courses/<int:max_hours>')
    def recommend_courses_route(max_hours):
        if "username" not in session:
            return redirect("/login")

        user_id = session["user_id"]
        completed_courses = Course.query.filter_by(user_id=user_id).all()
        completed_course_codes = [course.name for course in completed_courses]

        target_semester = "FALL"  # You can change this to any other semester as needed.

        recommended_courses = recommend_courses(completed_courses, target_semester, max_hours)
        return render_template('recommend_courses.html', courses=recommended_courses)

    @app.route('/hours', methods=['GET', 'POST'])
    def hours_route():
        if "username" not in session:
            return redirect("/login")

        if request.method == "POST":
            hours = int(request.form["hours"])
            return redirect(url_for('recommend_courses_route', max_hours=hours))

        return render_template('hours.html')

    return app

    # Uses from the Course.py imports
    dr_lst = ["course_database/CS.txt", "course_database/MATH.txt"]
    subjects = create(dr_lst)
    CS_CRS = match_course("CS2334", subjects)

    @app.route("/thang")
    def index():
        course = CS_CRS
        return render_template("thang.html", course = CS_CRS)

def recommend_courses(completed_courses, semester, max_hours=None):
    completed_course_codes = {course.name for course in completed_courses}

    courses = {
        "FALL": {
            "freshman": ["MATH1914", "CS1321", "CS1323", "CS1324", "ENGL1113", "ENGR1411", "UCOL1523", "Open Electives"],
            "sophomore": ["MATH2934", "CS2813/MATH2513", "CS2413", "ENGR2002", "Approved Elective Social Science"],
            "junior": ["CS3203", "CS3113", "CS3823", "3000+ level MATH", "Approved Electives Artistic Forms"],
            "senior": ["CS4000+ Elective", "CS4413", "CS4173", "CS4513", "CS4000+ Elective OR MATH4073/MATH4673/MATH4313"]
        },
        "SPRING": {
            "freshman": ["MATH2924", "CS2334", "ENGL/EXPO1213", "NATURAL SCIENCE with Lab"],
            "sophomore": ["OPEN ELECTIVES", "CS2614", "CS3323", "Natural Science (Core i)/PHYS2514"],
            "junior": ["CS4000+ Elective", "MATH3333", "MATH4753/ISE3293/MATH4743", "PSC1113", "Approved Elective Western Culture"],
            "senior": ["CS4000+ Elective", "CS4473", "CS4273", "HIST1483/HIST1493", "Approved Elective World Culture"]
        },
        "SUMMER": {},
        "JANUARY INTERSESSION": {},
        "MAY INTERSESSION": {},
    }

    semester_courses = courses.get(semester.upper())

    available_courses = []
    for year_courses in semester_courses.values():
        for course in year_courses:
            if course not in completed_course_codes:
                course_hours = int(course.split()[-1]) if course.split()[
                    -1].isdigit() else 3  # assuming default 3 hours
                available_courses.append((course, course_hours))

    available_courses.sort(key=lambda x: x[1], reverse=True)

    recommended_courses = []
    total_hours = 0
    for course, hours in available_courses:
        if total_hours + hours <= max_hours:
            recommended_courses.append(course)
            total_hours += hours

    return recommended_courses




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    courses = db.relationship("Course", backref="user", lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    professor = db.Column(db.String(50), nullable=True)
    semester = db.Column(db.String(50), nullable=True)
    hours = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

if __name__ == "__main__":
    app = create_app()
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    app.run(debug=True)


