from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/welcome")
def login_page():
    return render_template("login_page.html")

@app.route("/details", methods=["GET","POST"])
def details():
    if request.method=="POST":
        name=request.form.get("name")
        contact=request.form.get("contact")
        password=request.form.get("password")
    if len(contact)==10:
        return render_template("login_page.html",nm=name,contact=contact,pswd=password)
    else:
        return render_template("error.html")

if __name__=="__main__":
    app.run(debug=True)