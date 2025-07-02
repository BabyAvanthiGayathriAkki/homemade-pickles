// script.js

// Add to cart function
function addToCart(name, price) {
  // Get cart from localStorage or create new
  let cart = JSON.parse(localStorage.getItem('cart')) || [];

  // Add the item
  cart.push({ name: name, price: price });

  // Save it back
  localStorage.setItem('cart', JSON.stringify(cart));

  // Optionally redirect to cart page
  window.location.href = "/cart";
}

// Load cart items on cart page
function loadCart() {
    let cart = JSON.parse(sessionStorage.getItem('cart')) || [];
    let cartItems = document.getElementById('cart-items');
    let total = 0;

    if (cart.length === 0) {
        cartItems.innerHTML = "<p>Your cart is empty.</p>";
    } else {
        cart.forEach((item, index) => {
            let itemElement = document.createElement('div');
            itemElement.innerHTML = `<p>${item.name} - ₹${item.price}</p>`;
            cartItems.appendChild(itemElement);
            total += parseFloat(item.price);
        });
    }

    let totalElement = document.getElementById('cart-total');
    if (totalElement) {
        totalElement.innerText = "Total: ₹" + total;
    }
}

// Clear cart after checkout
function clearCart() {
    sessionStorage.removeItem('cart');
}function addToCart(name, price) {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  cart.push({ name: name, price: price });
  localStorage.setItem('cart', JSON.stringify(cart));
  window.location.href = '/cart'; // redirect to cart page
}

