from flask import Flask, render_template, request
import statistics as stats

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        try:
            numbers = request.form["numbers"]
            numbers = [float(x) for x in numbers.split(",")]
            
            result["mean"] = round(stats.mean(numbers), 2)
            result["median"] = round(stats.median(numbers), 2)
            result["mode"] = stats.mode(numbers)
            result["variance"] = round(stats.variance(numbers), 2) if len(numbers) > 1 else "N/A"
            result["stdev"] = round(stats.stdev(numbers), 2) if len(numbers) > 1 else "N/A"
        except Exception as e:
            result["error"] = str(e)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
print()