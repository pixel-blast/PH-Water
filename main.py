from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    ph_input = ""

    if request.method == "POST":
        ph_input = request.form.get("ph")
        try:
            ph_value = float(ph_input)
            if ph_value < 7 and ph_value > 0:
                result = "Acidic"
            elif ph_value == 7:
                result = "Neutral"
            elif ph_value <= 14 and ph_value > 7:
                result = "Basic(Alkaline)"
            elif ph_value == 0:
                result = 'Concentrated Acid'
            elif ph_value == 15:
                result = 'Concentrated Base'
            else:
                result = "Invalid pH"
        except ValueError:
            result = "Please enter a number"

    return render_template("index.html", result=result, ph_input=ph_input)

if __name__ == "__main__":
    app.run(debug=True)
