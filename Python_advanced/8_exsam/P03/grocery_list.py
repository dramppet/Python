def shop_from_grocery_list(a,product_list,*args):
    budget = int(a)

    by_product = []
    all_p = product_list

    product_by = False

    for product_name, price in args:
        if product_by:
            break
        for _ in product_list:
            if product_name in by_product:
                continue
            if product_name in product_list and budget - price > 0:
                budget = budget - price
                by_product.append(product_name)
                break
            if budget < price:
                product_by = True
                break

    for a in by_product:
        for b in all_p:
            if a == b:
                all_p.remove(a)
                break

    if len(all_p) > 0:
        return f"You did not buy all the products. Missing products: {', '.join(all_p)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
#
#
#
# # print(shop_from_grocery_list(
# #     100,
# #     ["tomato", "cola"],
# #     ("cola", 5.8),
# #     ("tomato", 10.0),
# #     ("tomato", 20.45),
# # ))
#
# # print(shop_from_grocery_list(
# #     100,
# #     ["tomato", "cola", "chips", "meat"],
# #     ("cola", 5.8),
# #     ("tomato", 10.0),
# #     ("meat", 22),
# # ))
#
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
#

def a (*args):
    print(type(args))

