
import json


def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str) -> None:
    with open('orders_1.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders_1.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4)