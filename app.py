<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Art Store — Главная</title>
<link rel="stylesheet" href="static/css/style.css">
</head>
<body>

<header>
    <h1>Art Store</h1>
    <div class="cart-info">
        Корзина: <span id="cart-count">0</span> шт.
        <a href="cart.html">Перейти в корзину</a>
    </div>
</header>

<main>
    <section class="paintings">
        <h2>Картины</h2>
        <div class="grid">
            <div class="card" data-id="1" data-price="1000000">
                <img src="static/images/monalisa.jpg" alt="Мона Лиза">
                <h3>Мона Лиза</h3>
                <p>Леонардо да Винчи</p>
                <p>$1 000 000</p>
                <button onclick="addToCart(1, 1000000)">Добавить в корзину</button>
            </div>
            <div class="card" data-id="2" data-price="1000">
                <img src="static/images/mountain.jpg" alt="Горы">
                <h3>Горы</h3>
                <p>Неизвестный</p>
                <p>$1 000</p>
                <button onclick="addToCart(2, 1000)">Добавить в корзину</button>
            </div>
            <div class="card" data-id="3" data-price="1000">
                <img src="static/images/river.jpg" alt="Река">
                <h3>Река</h3>
                <p>Неизвестный</p>
                <p>$1 000</p>
                <button onclick="addToCart(3, 1000)">Добавить в корзину</button>
            </div>
            <div class="card" data-id="4" data-price="1000">
                <img src="static/images/sunset.jpg" alt="Закат">
                <h3>Закат</h3>
                <p>Неизвестный</p>
                <p>$1 000</p>
                <button onclick="addToCart(4, 1000)">Добавить в корзину</button>
            </div>
        </div>
    </section>
</main>

<script>
// Работа с корзиной через localStorage
function getCart() {
    return JSON.parse(localStorage.getItem('cart') || '{}');
}

function setCart(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
}

function addToCart(id, price) {
    let cart = getCart();
    cart[id] = (cart[id] || 0) + 1;
    setCart(cart);
    alert("Товар добавлен в корзину!");
}

function updateCartCount() {
    let cart = getCart();
    let total = Object.values(cart).reduce((a,b) => a+b, 0);
    document.getElementById('cart-count').textContent = total;
}

// Обновляем счетчик при загрузке страницы
updateCartCount();
</script>

</body>
</html>