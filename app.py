from flask import Flask, render_template, request

app = Flask(__name__)

dresses = [
{"name":"Summer Floral Dress","price":1200},
{"name":"Casual T-Shirt Dress","price":900},
{"name":"Elegant Evening Gown","price":3500},
{"name":"Denim Jacket","price":1800},
{"name":"Men's Formal Shirt","price":1500},
{"name":"Women's Kurti","price":1100},
{"name":"Designer Saree","price":4500},
{"name":"Leather Jacket","price":5200},
{"name":"Hoodie","price":1400},
{"name":"Jeans","price":1700}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dresses")
def dress_page():
    return render_template("dresses.html", dresses=dresses)

@app.route("/checkout", methods=["POST"])
def checkout():

    items=[]
    total=0

    for dress in dresses:

        qty=request.form.get(dress["name"])

        if qty and int(qty)>0:

            qty=int(qty)

            price=dress["price"]*qty

            items.append({
                "name":dress["name"],
                "qty":qty,
                "price":price
            })

            total+=price

    return render_template("checkout.html", items=items, total=total)

@app.route("/payment", methods=["POST"])
def payment():

    total=request.form["total"]

    return render_template("payment.html", total=total)

@app.route("/order")
def order():
    return render_template("order.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
