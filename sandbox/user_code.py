cart_total = 120.0
discount_applied = False

def apply_coupon(coupon_code):
    if coupon_code == "SAVE20":
        # Apply a 20% discount
        cart_total = cart_total * 0.80
        discount_applied = True
        print(f"Coupon applied! New total: ${cart_total:.2f}")
    else:
        print("Invalid coupon code.")

print(f"Initial Cart Total: ${cart_total:.2f}")

apply_coupon("SAVE20")

if discount_applied:
    print("You saved money today!")
else:
    print("No discounts were used.")