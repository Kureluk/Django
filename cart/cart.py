PRODUCT_KEY = "product_cart_key"


def addProduct(session, id, quantity = 1):

    cart = session.get(PRODUCT_KEY, {})

    if id not in cart:
        cart[id] = quantity
    else:
        cart[id] += quantity
    
    session[PRODUCT_KEY] = cart

def getProduct(session):
    return session.get(PRODUCT_KEY, {})