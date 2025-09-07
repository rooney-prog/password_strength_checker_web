from flask import Flask, render_template, request
import os

app = Flask(__name__)


def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    return strength


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        password = request.form["password"]
        score = check_password_strength(password)
        if score <= 2:
            result = "Weak Password 🔴"
        elif score <= 4:
            result = "Moderate Password 🟡"
        else:
            result = "Strong Password 🟢"
    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environment.get("port", 5000))
    app.run(host="0.0.0.0", port=port)
