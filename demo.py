from flask import Flask,request
app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def save_file():
    data = request.files
    print("begin recv")
    file = data['filename']
    file.save(file.filename)
    print('done')
    return "success\n"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)