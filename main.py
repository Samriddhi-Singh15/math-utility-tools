from flask import Flask, jsonify, render_template, request
from math_utility import Fraction
from math_utility import Line, Point, Polynomial


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/fraction/add", methods=["POST"])
def add_fractions():
            data = request.get_json()
            f1 = Fraction(data["num1"], data["den1"])
            f2 = Fraction(data["num2"], data["den2"])
            result = f1 + f2
            return jsonify({"result": str(result)})

@app.route("/fraction/subtract", methods=["POST"])
def subtract_fractions():
            data = request.get_json()
            f1 = Fraction(data["num1"], data["den1"], show_menu=False)
            f2 = Fraction(data["num2"], data["den2"], show_menu=False)
            result = f1 - f2
            return jsonify({"result": str(result)})
    
@app.route("/fraction/multiply", methods=["POST"])
def multiply_fraction():
    data = request.get_json()
    f1 = Fraction(data["num1"], data["den1"], show_menu=False)
    f2 = Fraction(data["num2"], data["den2"], show_menu=False)
    result = f1 * f2
    return jsonify({"result": str(result)})

@app.route("/fraction/divide", methods=["POST"])
def divide_fraction():
    data = request.get_json()
    f1 = Fraction(data["num1"], data["den1"], show_menu=False)
    f2 = Fraction(data["num2"], data["den2"], show_menu=False)
    result = f1 / f2
    return jsonify({"result": str(result)})

@app.route("/coordinate/distance", methods=["POST"])
def point_distance():
    data = request.get_json()
    p1 = Point(data["x1"], data["y1"])
    p2 = Point(data["x2"], data["y2"])
    result = p1.euclidean_dist(p2)
    return jsonify({"result": result})


@app.route("/coordinate/origin", methods=["POST"])
def distance_from_origin():
    data = request.get_json()
    p = Point(data["x"], data["y"])
    result = p.dist_from_origin()
    return jsonify({"result": result})


@app.route("/coordinate/midpoint", methods=["POST"])
def midpoint():
    data = request.get_json()
    p1 = Point(data["x1"], data["y1"])
    p2 = Point(data["x2"], data["y2"])
    mid = p1.mid_point_2_point(p2)
    return jsonify({"result": f"({mid[0]}, {mid[1]})"})


@app.route("/coordinate/slope", methods=["POST"])
def slope():
    data = request.get_json()
    p1 = Point(data["x1"], data["y1"])
    p2 = Point(data["x2"], data["y2"])
    result = p1.slope_bw_2_points(p2)
    return jsonify({"result": result})


@app.route("/coordinate/quadrant", methods=["POST"])
def quadrant():
    data = request.get_json()

    p = Point(data["x"], data["y"])
    result = p.quadrant_finder()
    return jsonify({"result": result})

@app.route("/line/slope", methods=["POST"])
def line_slope():
    data = request.get_json()
    line = Line(data["A"], data["B"], data["C"])
    result = line.slope_line()
    return jsonify({"result": result})


@app.route("/line/yintercept", methods=["POST"])
def y_intercept():
    data = request.get_json()
    line = Line(data["A"], data["B"], data["C"])
    result = line.y_intercept()
    return jsonify({"result": result})


@app.route("/line/pointon", methods=["POST"])
def point_on_line():
    data = request.get_json()
    line = Line(data["A"], data["B"], data["C"])
    p = Point(data["x"], data["y"])
    result = line.point_on_line(p)
    return jsonify({"result": "Yes" if result else "No"})


@app.route("/line/shortestdist", methods=["POST"])
def shortest_dist():
    data = request.get_json()
    line = Line(data["A"], data["B"], data["C"])
    p = Point(data["x"], data["y"])
    result = line.shortest_dist(p)
    return jsonify({"result": result})


@app.route("/polynomial/add", methods=["POST"])
def poly_add():
    data = request.get_json()
    p1 = Polynomial(data["poly1"], show_menu=False)
    p2 = Polynomial(data["poly2"], show_menu=False)
    result = str(p1 + p2)
    return jsonify({"result": result})


@app.route("/polynomial/subtract", methods=["POST"])
def poly_subtract():
    data = request.get_json()
    p1 = Polynomial(data["poly1"], show_menu=False)
    p2 = Polynomial(data["poly2"], show_menu=False)
    result = str(p1 - p2)
    return jsonify({"result": result})


@app.route("/polynomial/multiply", methods=["POST"])
def poly_multiply():
    data = request.get_json()
    p1 = Polynomial(data["poly1"], show_menu=False)
    p2 = Polynomial(data["poly2"], show_menu=False)
    result = str(p1 * p2)
    return jsonify({"result": result})


@app.route("/polynomial/divide", methods=["POST"])
def poly_divide():
    data = request.get_json()
    p1 = Polynomial(data["poly1"], show_menu=False)
    p2 = Polynomial(data["poly2"], show_menu=False)
    result = str(p1 / p2)
    return jsonify({"result": result})
if __name__ == "__main__":
    app.run(debug=True)