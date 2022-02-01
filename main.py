from flask import Flask, render_template, request, send_file, send_from_directory
import os
from io import BytesIO
# from pdf2docx import parse
# from docx2pdf import convert
# from pylint import pyreverse


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/download_image")
def down():
#     return send_file(os.path.abspath('image1.jpg'), download_name="output.jpg", as_attachment=True)
    file_dir = os.path.dirname(os.path.abspath('image1.jpg'))
    par_dir = os.path.join(file_dir, os.pardir)
    output_dir = os.path.join(par_dir, 'images')
    return send_from_directory(output_dir, filename='image1.jpg', as_attachment=True)

@app.route("/converter")
def converter():
    return render_template("Dashboard.html")


@app.route("/upload_one", methods=['POST'])
def uploadone():
    # file = request.files['path']
    # split_tup = os.path.splitext(file.filename)
    # if split_tup[1] == '.py':
    #     temp = "test.py"
    #     with open(temp, 'wb') as f:
    #         f.write(BytesIO(file.read()).read())
    #         f.close()
    #     path = os.path.abspath(temp)
    #     os.system("pyreverse -o png " + path)
    #     output = "classes.png"
    #     os.remove(temp)
    #     return send_file(output, download_name="Uml_diagram.png", as_attachment=True)
    # elif split_tup[1] == '.java':
    #     temp = "test.java"
    #     with open(temp, 'wb') as f:
    #         f.write(BytesIO(file.read()).read())
    #         f.close()
    #     path = os.path.abspath(temp)
    #     os.system("pyreverse -o png " + path)
    #     output = "classes.png"
    #     os.remove(temp)
    #     return send_file(output, download_name="Uml_diagram.png", as_attachment=True)
    # else:
    #     print("error")
    files = request.files.getlist('path')
    temp = "temp.py"
    for f in files:
        print(f)
        with open(temp, 'ab') as file:
            file.write(BytesIO(f.read()).read())
            file.close()
    os.system("python injector.py")
    os.system("python sourceInject.py")
    os.system("python -m plantuml SD")
    os.remove(temp)
    return send_file(os.path.abspath('SD.png'), download_name="Sequence_diagram.png", as_attachment=True)


@app.route("/upload_mul", methods=['POST'])
def mul():
    files = request.files.getlist('mul')
    temp = "test.py"
    for f in files:
        print(f)
        with open(temp, 'ab') as file:
            file.write(BytesIO(f.read()).read())
            file.close()
    path = os.path.abspath(temp)
    os.system("pyreverse -o png " + path)
    #output = "classes.png"
    os.remove(temp)
    return send_file(os.path.abspath('classes.png'), download_name="Uml_diagram", as_attachment=True)


# @app.route("/upload", methods=['POST'])
# def upload():
#     option1 = str(request.form.get('op1'))
#     option2 = str(request.form.get('op2'))
#     file = request.files['file']
#     if (option1 == 'PDF') and (option2 == 'DOCX'):
#         filename = file.filename + "-converted.docx"
#         temp = 'test.pdf'
#         doc_file = 'test.docx'
#         with open(temp, 'wb') as f:
#             f.write(BytesIO(file.read()).read())
#             f.close()
#         parse(temp, doc_file, start=0, end=None)
#         os.remove(temp)
#         return send_file(doc_file, download_name=filename, as_attachment=True)
    # elif (option1 == 'DOCX') and (option2 == 'PDF'):
    #     filename = file.filename + "-converted.pdf"
    #     temp = 'test1.docx'
    #     pdf_file = 'test1.pdf'
    #     with open(temp, 'wb') as f:
    #         f.write(BytesIO(file.read()).read())
    #         f.close()
    #     convert('test1.docx')
    #     os.remove(temp)
    #     return send_file(pdf_file, download_name=filename, as_attachment=True)
    # else:
    #     return "<h1>Please select different file formats</h1>"


if __name__ == "__main__":
    app.run()
