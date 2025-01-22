-- Create the restaurants table
CREATE TABLE restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100),
    state CHAR(10),
    address1 VARCHAR(255),
    timezone VARCHAR(50)
);

-- Insert 50 restaurants into the table
INSERT INTO restaurants (id, name, city, state, address1, timezone) VALUES
(1, 'McDees', 'Houston', 'TX', '123 Cowboy Dr', 'Central Time'),
(2, 'Pizzas To Go', 'New York', 'NY', '456 Times Square', 'Eastern Time'),
(3, 'Burgerz', 'San Diego', 'CA', '789 Palm St', 'Pacific Time'),
(4, 'Sushi Delight', 'Los Angeles', 'CA', '101 Ocean Blvd', 'Pacific Time'),
(5, 'Taco Fiesta', 'Austin', 'TX', '202 River Walk', 'Central Time'),
(6, 'Pasta Palace', 'Chicago', 'IL', '303 Lake Shore Dr', 'Central Time'),
(7, 'BBQ Heaven', 'Dallas', 'TX', '404 Ranch Rd', 'Central Time'),
(8, 'Philly Subs', 'Philadelphia', 'PA', '505 Liberty Bell Ln', 'Eastern Time'),
(9, 'Steak Masters', 'Las Vegas', 'NV', '606 Vegas Strip', 'Pacific Time'),
(10, 'Coffee Haven', 'Seattle', 'WA', '707 Pike St', 'Pacific Time'),
(11, 'Wok This Way', 'San Francisco', 'CA', '808 Golden Gate Ave', 'Pacific Time'),
(12, 'Bistro 101', 'Miami', 'FL', '909 Ocean Dr', 'Eastern Time'),
(13, 'Grill House', 'Phoenix', 'AZ', '1010 Desert Rd', 'Mountain Time'),
(14, 'Bagel Bros', 'Boston', 'MA', '1111 Freedom St', 'Eastern Time'),
(15, 'Pizza Town', 'Portland', 'OR', '1212 Rose St', 'Pacific Time'),
(16, 'Seafood Sensation', 'Tampa', 'FL', '1313 Bayshore Blvd', 'Eastern Time'),
(17, 'Burger Shack', 'Orlando', 'FL', '1414 Theme Park Ln', 'Eastern Time'),
(18, 'Brewery & Co.', 'Denver', 'CO', '1515 Mile High Rd', 'Mountain Time'),
(19, 'Sandwich World', 'Columbus', 'OH', '1616 Buckeye Rd', 'Eastern Time'),
(20, 'Fried Chicken King', 'Atlanta', 'GA', '1717 Peachtree St', 'Eastern Time'),
(21, 'Curry House', 'Detroit', 'MI', '1818 Motor City Dr', 'Eastern Time'),
(22, 'Gourmet Greens', 'Sacramento', 'CA', '1919 Capitol Blvd', 'Pacific Time'),
(23, 'Pasta Works', 'Indianapolis', 'IN', '2020 Indy 500 Dr', 'Eastern Time'),
(24, 'Veggie Delights', 'Nashville', 'TN', '2121 Music Row', 'Central Time'),
(25, 'Steak Supreme', 'Fort Worth', 'TX', '2222 Stockyard Blvd', 'Central Time'),
(26, 'Noodle Nation', 'Las Vegas', 'NV', '2323 Casino St', 'Pacific Time'),
(27, 'Grill Spot', 'Baltimore', 'MD', '2424 Harbor Pl', 'Eastern Time'),
(28, 'Wing World', 'Charlotte', 'NC', '2525 Queen City Ave', 'Eastern Time'),
(29, 'Dim Sum Delight', 'San Jose', 'CA', '2626 Silicon Valley Rd', 'Pacific Time'),
(30, 'Taco Town', 'San Antonio', 'TX', '2727 Alamo Dr', 'Central Time'),
(31, 'Sushi Express', 'Honolulu', 'HI', '2828 Aloha St', 'Hawaii-Aleutian Time'),
(32, 'Greek Gyros', 'Salt Lake City', 'UT', '2929 Temple St', 'Mountain Time'),
(33, 'BBQ Bros', 'Memphis', 'TN', '3030 Beale St', 'Central Time'),
(34, 'Fish Fry', 'Jacksonville', 'FL', '3131 Riverwalk Dr', 'Eastern Time'),
(35, 'Southern Comfort', 'Birmingham', 'AL', '3232 Steel City Blvd', 'Central Time'),
(36, 'Pizzeria Roma', 'Buffalo', 'NY', '3333 Niagara St', 'Eastern Time'),
(37, 'Wraps & Rolls', 'Minneapolis', 'MN', '3434 Twin City Blvd', 'Central Time'),
(38, 'Bagel Barn', 'Albany', 'NY', '3535 Capitol Hill St', 'Eastern Time'),
(39, 'Cafe Paris', 'New Orleans', 'LA', '3636 Bourbon St', 'Central Time'),
(40, 'Crepe Corner', 'Raleigh', 'NC', '3737 Oak City Ave', 'Eastern Time'),
(41, 'Falafel House', 'Milwaukee', 'WI', '3838 Lakefront Blvd', 'Central Time'),
(42, 'Kabob King', 'Richmond', 'VA', '3939 Monument Ave', 'Eastern Time'),
(43, 'Burrito Bonanza', 'El Paso', 'TX', '4040 Border St', 'Mountain Time'),
(44, 'Pho Palace', 'San Bernardino', 'CA', '4141 Inland Empire Rd', 'Pacific Time'),
(45, 'Clam Shack', 'Providence', 'RI', '4242 Ocean Ave', 'Eastern Time'),
(46, 'Deli Delight', 'Hartford', 'CT', '4343 Capitol Dr', 'Eastern Time'),
(47, 'Tex Mex Grill', 'Lubbock', 'TX', '4444 Panhandle St', 'Central Time'),
(48, 'Fried Rice King', 'Fresno', 'CA', '4545 Farm Country Rd', 'Pacific Time'),
(49, 'Bistro Luxe', 'Scottsdale', 'AZ', '4646 Desert Ridge Ave', 'Mountain Time'),
(50, 'Steak Stop', 'Oklahoma City', 'OK', '4747 Thunder Rd', 'Central Time');

-- Add random leading and trailing spaces to texts and randomizing the case of the first letter
UPDATE restaurants
SET
    name = CONCAT(
        REPEAT(' ', FLOOR(RANDOM() * 2)::int),
        CASE WHEN RANDOM() < 0.5 THEN LOWER(SUBSTRING(name, 1, 1)) ELSE UPPER(SUBSTRING(name, 1, 1)) END,
        SUBSTRING(name, 2),
        REPEAT(' ', FLOOR(RANDOM() * 2)::int)
    ),
    city = CONCAT(
        REPEAT(' ', FLOOR(RANDOM() * 2)::int),
        CASE WHEN RANDOM() < 0.5 THEN LOWER(SUBSTRING(city, 1, 1)) ELSE UPPER(SUBSTRING(city, 1, 1)) END,
        SUBSTRING(city, 2),
        REPEAT(' ', FLOOR(RANDOM() * 2)::int)
    ),
    state = CONCAT(
        REPEAT(' ', FLOOR(RANDOM() * 2)::int),
        CASE WHEN RANDOM() < 0.5 THEN LOWER(SUBSTRING(state, 1, 1)) ELSE UPPER(SUBSTRING(state, 1, 1)) END,
        SUBSTRING(state, 2),
        REPEAT(' ', FLOOR(RANDOM() * 2)::int)
    ),
    address1 = CONCAT(
        REPEAT(' ', FLOOR(RANDOM() * 2)::int),
        CASE WHEN RANDOM() < 0.5 THEN LOWER(SUBSTRING(address1, 1, 1)) ELSE UPPER(SUBSTRING(address1, 1, 1)) END,
        SUBSTRING(address1, 2),
        REPEAT(' ', FLOOR(RANDOM() * 2)::int)
    );
