## Question
# Find the customers with the highest daily total order cost between 2019-02-01 and 2019-05-01. If a customer had more than one order on a certain day, sum the order costs on a daily basis. Output each customer's first name, total cost of their items, and the date. If multiple customers tie for the highest daily total on the same date, return all of them.
# customers -> (id, first_name, last_name, phone, city, address)
# orders -> (id, cust_id, order_date, order_details, total_order_cost)

## Solution
# libraries
import pyspark
from pyspark.sql import Window
from pyspark.sql.functions import col, dense_rank, sum, max

# filter
filtered_orders = orders.filter((col('order_date')>='2019-02-01') & (col('order_date')<='2019-05-01'))

# aggregate
cust_total = filtered_orders.groupBy('cust_id', 'order_date').agg(
    sum('total_order_cost').alias('total_spending'))

# rank
rank_spec = Window.partitionBy('order_date').orderBy(col('total_spending').desc())
ranked_cust = cust_total.withColumn('rnk', dense_rank().over(rank_spec))

# filter
result = ranked_cust.filter(col('rnk')<2)\
            .join(customers, customers['id']==ranked_cust['cust_id'])\
            .select('first_name', 'total_spending', 'order_date')
            
# result
result.toPandas() 