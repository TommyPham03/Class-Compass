from flask import Flask, render_template
from Course import create, match_course, Course, Subject

# Add your code to create the "CS_CRS" object here
dr_lst = ["course_database/CS.txt", "course_database/MATH.txt"]
subjects = create(dr_lst)
CS_CRS = match_course("CS2334", subjects)

def create_thang_app():
    app = Flask(__name__)

    @app.route("/thang", methods=["GET", "POST"])
    def index_t():
        course = CS_CRS
        return render_template("thang.html", course=CS_CRS)

    return app

if __name__ == "__main__":
    app = create_thang_app()
    app.run(debug=True, port=5001)
