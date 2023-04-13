CREATE DATABASE banking_data;
USE banking_data;
CREATE TABLE banking_customer_churn  (customer_id        int,
									  credit_score       int, 
									  country            varchar(50), 
									  gender             varchar(50), 
									  age                int, 
									  tenure             int,
									  balance            float, 
									  products_number    int, 
									  credit_card        int, 
									  active_member      int,
									  estimated_salary   float, 
									  churn	             int
								     );
                                       
SELECT *  FROM banking_customer_churn;
