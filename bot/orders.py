import logging
import random

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        order = {
            "orderId": random.randint(100000, 999999),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity,
            "avgPrice": price if price else "market_price"
        }

        logging.info(f"Order response: {order}")

        return order

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        raise