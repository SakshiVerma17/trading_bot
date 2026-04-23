import argparse
import logging

from bot.logging_config import setup_logging
from bot.orders import place_order

def main():
    # 🔥 MUST be FIRST line
    setup_logging()

    logging.info("Bot started")

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float, default=None)

    args = parser.parse_args()

    # validation for LIMIT orders
    if args.type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")

    logging.info(f"Placing order: {args.symbol} {args.side} {args.type} {args.qty} {args.price}")

    result = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.qty,
        price=args.price
    )

    logging.info(f"Order response: {result}")
    logging.info(f"Order placed: {result}")

    print("\n📌 Order Summary:")
    print(result)

if __name__ == "__main__":
    main()