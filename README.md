To run
```
pip install virtualenv
virtualenv venv -p $(which python3)
source venv/bin/activate
make install
# Run tests
make test # tests do not pass yet
# start server
make start
open http://localhost:8000/
```

## Progress
- I was practicing TDD here, so I spent much more time setting up a testing environment than writing code, but my plan would be:
    - Upload the csv to a temp table using `\copy`
    - Update customers from temp table where `customer.id` is in the temp table, possibly using the django orm, but the resulting sql would look like
```
UPDATE customer
SET first_name=subquery.first_name,
    last_name=subquery.last_name,
    address=subquery.address,
    zip_code=subquery.zip_code,
    state=subquery.state
FROM (SELECT customer_id, first_name, last_name, ... FROM temp_table) AS subquery
WHERE customer.id=subquery.customer_id;
```
    - Create customers from temp table where customer id is not
```
INSERT INTO customer (
    SELECT customer_id, first_name, last_name, ...
    FROM temp_table
    WHERE custome_id NOT IN ( SELECT id FROM customer)
);
```
-
    - Repeat for Products
    - Repeat for Purchases using timestamp as the id for lack of a better identifier
- The reason for the temp table instead of is that looping through rows in the csv and creating Customers, Products and Purchases individually:
    - I could reduce the number of queries to ~7, increasing speed
    - This should result give me data locality and increase speed

##Further Optimizations
###Normalization of the database
- I'm assuming that there are 3 types of objects
    - Customers
    - Products
    - Purchases
- If a customer can purchase a product multiple times, a purchase must be defined by the time it occurred

###Authentication and authorization capabilities
- Django can handle this.  Any kind of single sign on seems unlikely if this provider can't integrate with an API endpoint or in some automated way 
###Support for files larger than 3MB (upload progress indicator, etc)
- This job could be handed off to a celery task that could be polled for progress
###Irregularity detection and alerting (for instance, if a purchase is canceled that has not been previously seen as new)
- There could be a series of heuristic checks, such as cancelations of purchases that had not yet occurred
- There could be anomaly detection done on number of new customers or new products 
###Detecting and handling updating addresses for customers
- We may want to store previous addresses for a customer, and therefore addresses might need to be stored in their own table with a foreign key to user