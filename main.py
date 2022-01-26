from flask import Flask, render_template, request, send_file
import os
# from pylint import pyreverse


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/upload", methods=['POST'])
def upload():
    path = str(request.form.get('path'))
    os.system("pyreverse -o png " + path)
    output = "classes.png"
    return send_file(output, download_name="Uml_diagram", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
