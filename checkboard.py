from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def checkboard():
    return render_template('index.html', x = 8, y = 8, color1 = "green", color2 = "pink")
    
@app.route("/<int:y>")
def checkboard_y(y):
    return render_template('index.html', x = 8, y = int(y), color1 = "green", color2 = "pink")

@app.route("/<int:x>/<int:y>")
def checkboard_xy(x, y):
    return render_template('index.html', x = int(x), y = int(y), color1 = "green", color2 = "pink")

@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def checkboard_xy_color(x, y, color1, color2):
    return render_template('index.html', x = int(x), y = int(y), color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug=True)