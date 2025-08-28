from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Каталог картин (цены в долларах)
paintings = [
    {"id": 1, "name": "Мона Лиза", "artist": "Леонардо да Винчи", "price": 1000000, "img": "/static/images/monalisa.jpg"},
    {"id": 2, "name": "Горы", "artist": "Неизвестный", "price": 1000, "img": "/static/images/mountain.jpg"},
    {"id": 3, "name": "Река", "artist": "Неизвестный", "price": 1000, "img": "/static/images/river.jpg"},
    {"id": 4, "name": "Закат", "artist": "Неизвестный", "price": 1000, "img": "/static/images/sunset.jpg"},
]

# Корзина в памяти (структура: {painting_id: qty})
cart = {}

def get_cart_items():
    items = []
    total = 0
    for painting_id, qty in cart.items():
        painting = next((p for p in paintings if p["id"] == painting_id), None)
        if painting:
            subtotal = painting["price"] * qty
            items.append({"painting": painting, "qty": qty, "subtotal": subtotal})
            total += subtotal
    return items, total

@app.context_processor
def inject_cart_count():
    # Чтобы cart_count был доступен во всех шаблонах
    return dict(cart_count=sum(cart.values()))

@app.route("/")
def index():
    return render_template("index.html", paintings=paintings)

@app.route("/painting/<int:painting_id>")
def painting_detail(painting_id):
    painting = next((p for p in paintings if p["id"] == painting_id), None)
    if painting:
        return render_template("painting_detail.html", painting=painting)
    return "Картина не найдена", 404

@app.route("/cart")
def cart_view():
    items, total = get_cart_items()
    return render_template("cart.html", items=items, total=total)

@app.route("/cart/add/<int:painting_id>", methods=["POST"])
def cart_add(painting_id):
    cart[painting_id] = cart.get(painting_id, 0) + 1
    return redirect(url_for("cart_view"))

@app.route("/cart/increase/<int:painting_id>")
def cart_increase(painting_id):
    if painting_id in cart:
        cart[painting_id] += 1
    return redirect(url_for("cart_view"))

@app.route("/cart/decrease/<int:painting_id>")
def cart_decrease(painting_id):
    if painting_id in cart:
        cart[painting_id] -= 1
        if cart[painting_id] <= 0:
            cart.pop(painting_id)
    return redirect(url_for("cart_view"))

@app.route("/cart/remove/<int:painting_id>")
def cart_remove(painting_id):
    cart.pop(painting_id, None)
    return redirect(url_for("cart_view"))

@app.route("/cart/clear")
def cart_clear():
    cart.clear()
    return redirect(url_for("cart_view"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    items, total = get_cart_items()
    if not items:
        flash("Ваша корзина пуста!", "error")
        return redirect(url_for("cart_view"))

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        address = request.form.get("address")

        if name and email and address:
            cart.clear()
            flash(f"Спасибо за заказ, {name}! Сумма: ${total}", "success")
            return redirect(url_for("index"))
        else:
            flash("Пожалуйста, заполните все поля", "error")

    return render_template("checkout.html", items=items, total=total)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        if name and email and message:
            flash("Сообщение отправлено!", "success")
            return redirect(url_for("contact"))
        else:
            flash("Пожалуйста, заполните все поля", "error")
    return render_template("contact.html")

@app.route("/shop/paintings")
def shop_paintings():
    return render_template("shop/paintings.html")

@app.route("/shop/sculptures")
def shop_sculptures():
    return render_template("shop/sculptures.html")

@app.route("/shop/rareties")
def shop_rareties():
    return render_template("shop/rareties.html")

@app.route("/shop/coins")
def shop_coins():
    return render_template("shop/coins.html")

if __name__ == "__main__":
    app.run(debug=True)