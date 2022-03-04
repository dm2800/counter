from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security 

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0 
    session['count'] += 1
    return render_template("index.html")

@app.route('/incrementbytwo')
def increment_bytwo():
    if "count" not in session:
        session['count'] = 0 
    session['count'] += 2
    return render_template("index.html")


@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

    # @app.route('/incrementbyuser', methods=['POST'])
# def increment_byuser(user_increment):
#     if "count" not in session:
#         session['count'] = 0 
#     session['count'] += {{int(request.form[user_increment])}}
#     return render_template("index.html", user_increment)




if __name__ == "__main__":
    app.run(debug=True)
