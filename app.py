from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta"

USER = "raul"
PASSWORD = "1234"

login_page = """
<h2>Login Pro 🔐</h2>
<form method="POST">
    Usuario: <input name="user"><br><br>
    Contraseña: <input name="password" type="password"><br><br>
    <button type="submit">Entrar</button>
</form>
"""

@app.route("/")
def home():
    return "<h1>Raúl Rodríguez es un joven de 15 años y tenista 🎾</h1><br><a href='/login'>Ir al login</a>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]

        if user == USER and password == PASSWORD:
            session["user"] = user
            return redirect(url_for("dashboard"))
        else:
            return "<h1>Error ❌ Usuario o contraseña incorrectos</h1>"

    return render_template_string(login_page)

@app.route("/dashboard")
def dashboard():
    user = session.get("user", "Invitado")
    return f"<h1>Bienvenido, {user} 🚀</h1>"

if __name__ == "__main__":
    app.run(debug=True)