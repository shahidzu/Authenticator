from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# In a real-world scenario, use a proper database for user management
users = {
    "john_doe": {"username": "john_doe", "password": "password123"},
    "jane_smith": {"username": "jane_smith", "password": "qwerty456"},
}

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = users.get(username)

    if user and user["password"] == password:
        return redirect(url_for("dashboard", username=username))
    else:
        return render_template("login.html", error="Invalid credentials")

@app.route("/dashboard/<username>")
def dashboard(username):
    user = users.get(username)

    if user:
        return f"Welcome, {user['username']}! This is your dashboard."
    else:
        return "User not found."

if __name__ == "__main__":
    app.run(debug=True)
