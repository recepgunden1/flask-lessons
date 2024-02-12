from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def definition():
    response = make_response("<html><body><h1>ilk Flask denemesi</h1></body></html>")
    response.set_cookie('name', 'Ahmet')
    return response

if __name__ == "__main__":
    app.run(debug=True)
