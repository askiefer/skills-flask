from flask import Flask, render_template, flash, request, redirect

app = Flask(__name__)

app.secret_key = 'something_difficult_to_guess'


@app.route("/")
def index_page():
    """Show an index page."""

    #return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    
    return render_template("base.html")

@app.route("/application-form")
def show_form():
	"""Shows application form."""

	return render_template("application-form.html")
	

@app.route("/application", methods=["POST"])
def submission_response():
	"""Gets application info and returns a confirmation statement."""

	first_name = request.form.get("firstname")
	last_name = request.form.get("lastname")
	job_type = request.form.get("job-input")
	exp_salary = request.form.get("salary")

	if first_name == "" or last_name == "" or job_type == "" or exp_salary == "":
		flash("Please fill in all the required forms.")
		return redirect("application-form")
	
	return render_template("application-response.html", firstname=first_name, 
		lastname=last_name, jobtype=job_type, salary=exp_salary)

if __name__ == "__main__":
    app.run(debug=True)
