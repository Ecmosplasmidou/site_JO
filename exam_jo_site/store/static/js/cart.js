var cart = [];
    
document.querySelectorAll('.add-to-cart').forEach(item => {
  item.addEventListener('click', event => {
    event.preventDefault();
    
    var productId = event.target.dataset.productId;
    
    // Ajoutez le produit au panier (vous pouvez également vérifier si le produit est déjà dans le panier et augmenter la quantité)
    cart.push(productId);
    
    // Mettez à jour le SVG du panier
    document.getElementById('cart-count').textContent = cart.length;
  })
})