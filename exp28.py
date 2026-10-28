def invoice(price, quantity):
    total = price * quantity
    discount = total * 0.10
    gst = (total - discount) * 0.18
    return total - discount + gst

print(invoice(1000, 2))