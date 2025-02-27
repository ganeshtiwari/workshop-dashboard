CREATE TABLE IF NOT EXISTS stock_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(100) NOT NULL, 
    trading_date DATE NOT NULL,
    open DECIMAL(10, 2),
    high DECIMAL(10, 2),
    low DECIMAL(10, 2),
    close DECIMAL(10, 2),
    adjusted_close DECIMAL(10, 2), 
    volume BIGINT, 
    dividend_amount DECIMAL(10, 2)
);
