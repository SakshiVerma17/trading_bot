# Trading Bot – Binance Futures Testnet

## 📌 Overview

This is a CLI-based trading bot built in Python that simulates placing orders on Binance Futures Testnet (USDT-M).

The application supports:

- Market and Limit orders
- BUY and SELL sides
- CLI-based user input
- Logging of requests and responses
- Input validation and error handling

---

## ⚠️ Note

Due to limited accessibility and instability of Binance Futures Testnet API,  
a mock/simulated order execution layer is implemented.

The project structure is designed in a way that real Binance API integration can be easily added.

---



## 🛠️ Setup

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd trading_bot
```

### 2. Install Dependencies
```bash 
pip install -r requirements.txt
```

----

## ▶️ Usage

### ✅ Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
```
### ✅ Limit Order
```bash 
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 80000
```

----

### Project Structure 

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── bot.log
│
├── cli.py
├── requirements.txt
└── README.md

----

## Logging

- All logs (order requests, responses, and errors) are stored in:

```bash
logs/bot.log
```
