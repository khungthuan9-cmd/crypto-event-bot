# Crypto Event Trading Bot & API Integration

A lightweight, modular personal framework designed for testing REST and WebSocket API integrations, fetching historical market data, and running local event-driven strategy backtests on cryptocurrency exchanges.

## Project Overview

This repository serves as a personal sandbox environment for developing and evaluating quantitative trading scripts. It establishes secure connection protocols, handles real-time ticker data parsing, and implements basic risk-management wrappers for event contract trading.

## Core Features

- **API Connectivity & Authentication:** 
  - Automated HMAC-SHA256 signature generation for secure private endpoints.
  - Public REST API health checks and latency monitoring.
- **Data Pipeline:** 
  - Real-time data ingestion framework for order book updates and trade history.
  - JSON response parsing and local structural logging.
- **Strategy & Backtest Sandbox:** 
  - Modular template for running simulation-based event contract trading strategies.
  - Configurable threshold triggers and automated error-handling routines.

## Project Structure

```text
crypto-event-bot/
│
├── config/              # API keys configuration template & environment variables
├── src/                 # Core source code
│   ├── api_client.py    # Request handler & signature generator
│   ├── strategy.py      # Event trading logic template
│   └── logger.py        # Log management and error tracking
│
├── main.py              # Entry point for running connection and test scripts
├── requirements.txt     # Dependency list (requests, websocket-client, pandas)
└── README.md            # Project documentation
