-- Create the transactions table
CREATE TABLE transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    amount DECIMAL(10, 2),
    unix_timestamp BIGINT,
    description VARCHAR(255),
    location_id INT,
    FOREIGN KEY (location_id) REFERENCES restaurants(id)
);
