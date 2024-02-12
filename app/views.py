from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def definition():
    return "<html><body><h1>ilk Flask denemesi</h1></body></html>"

if __name__ == "__main__":
    app.run(debug=True)
