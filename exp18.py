# 18. Create a shopping cart using a list. Perform add item, remove item, search item, display cart and count total items.

cart = []
cart.append("Pen")
cart.append("Book")
cart.remove("Pen")
print("Search:", "Book" in cart)
print("Cart:", cart)
print("Total items:", len(cart))