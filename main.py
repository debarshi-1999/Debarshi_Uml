from flask import Flask, render_template, request, send_file
import os
from io import BytesIO
# from pylint import pyreverse


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/upload", methods=['POST'])
def upload():
    temp = "test.py"
    file = request.files['path']
    with open(temp, 'wb') as f:
        f.write(BytesIO(file.read()).read())
        f.close()
    path = os.path.abspath(temp)
    os.system("pyreverse -o png " + path)
    output = "classes.png"
    return send_file(output, download_name="Uml_diagram", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
