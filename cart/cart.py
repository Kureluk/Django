CART_KEY = "product_cart_key"

def add_to_cart(session, id, quantity = 1):
    cart = session.get(CART_KEY, {})
    if id not in cart:
        cart[id] = quantity
    else:
        cart[id] += quantity
        
    
    session[CART_KEY] = cart

def get_cart(session):
    return session.get(CART_KEY, {})

def get_count(session):
    return len(get_cart(session).keys())

def remove_from_cart(session, id):
    cart = session.get(CART_KEY, {})
    str_id = str(id)  
    if str_id in cart:  
        del cart[str_id]  
    session[CART_KEY] = cart  


