"""
Vulnerable Web Authentication Endpoint - Dictionary & Brute-Force Target
Author: Jaser Halabi
Purpose: Demonstrates the security risks of unthrottled authentication forms 
         susceptible to automated online dictionary attacks using THC-Hydra.
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials for testing demonstration
USERNAME = "admin"
PASSWORD = "12345678"

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure Login</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .login-box { border: 1px solid #333; padding: 20px; width: 300px; }
        input { margin-bottom: 10px; width: 90%; padding: 5px; }
        .error { color: red; font-weight: bold; }
        .success { color: green; font-weight: bold; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Login Panel</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Login">
        </form>
        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        user = request.form.get("username", "")
        pwd = request.form.get("password", "")

        if user == USERNAME and pwd == PASSWORD:
            return """
            <h1 style="color: green; font-family: Arial, sans-serif;">Access Granted</h1>
            <p>Welcome back, Administrator.</p>
            """
        else:
            error = "Invalid credentials"

    return render_template_string(HTML_TEMPLATE, error=error)


if __name__ == "__main__":
    print("[*] Starting vulnerable authentication service on http://127.0.0.1:5000")
    print(f"[*] Target username: {USERNAME}")
    app.run(host="127.0.0.1", port=5000, debug=False)
