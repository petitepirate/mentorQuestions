from flask import Flask, request, render_template, redirect, flash, session
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "adfasedira"

responses = []


@app.route('/')
def home_page():
    return render_template("home.html", survey=survey)


@app.route('/', methods=["POST"])
def start_survey():
    return redirect("/questions/0")


@app.route("/answer", methods=["POST"])
def handle_question():
    choice = request.form['answer']
    responses.append(choice)

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/questions/<int:qid>")
def show_question(qid):

    if (responses is None):
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")

    if (len(responses) != qid):
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]

    return render_template(
        "questions.html", question_num=qid, question=question, survey=survey)


@app.route("/complete")
def complete():

    return render_template("endsurvey.html")
