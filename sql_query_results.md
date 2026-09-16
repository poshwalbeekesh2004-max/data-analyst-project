# Week 2: SQL for Data Analysis - Query Results

**Dataset:** sales.db (SQL_Sales.csv)
**Table:** sales (200 rows)

---

## 1. Category-wise Total Revenue

```
category     total_revenue
-----------  -------------
Clothing     484259
Electronics  549302
Furniture    714399
Grocery      672147
```

---

## 2. Region-wise Average Order Value

```
region  avg_order_value
------  ----------------
East    12142.1568627451
North   9820.975
South   12252.2878787879
West    13938.7674418605
```

---

## 3. Category-wise Order Count

```
category     order_count
-----------  -----------
Clothing     40
Electronics  52
Furniture    59
Grocery      49
```

---

## 4. Category-wise Total Revenue (Sorted, Highest to Lowest)

```
category     total_revenue
-----------  -------------
Furniture    714399
Grocery      672147
Electronics  549302
Clothing     484259
```

**Insight:** Furniture generates the highest revenue, followed by Grocery, Electronics, and Clothing.

---

## 5. CASE Statement - Order Value Categorization (High/Medium/Low)

```sql
SELECT customer_name, total_price,
CASE
    WHEN total_price >= 20000 THEN 'High'
    WHEN total_price >= 10000 THEN 'Medium'
    ELSE 'Low'
END AS order_category
FROM sales
LIMIT 10;
```

```
customer_name     total_price  order_category
----------------  -----------  --------------
Caleb Davis       2394         High
Misty Herrera     13581        Medium
Rick Soto         5230         High
Sean Haas         2920         High
Ann Hall          1096         Medium
Michelle White    5458         High
Breanna Gonzalez  26136        High
Angela Rivera     20797        High
Emily Anderson    7010         High
Laura Anderson    4454         High
```

---

## 6. Subquery - Customers Above Average Order Value

```sql
SELECT customer_name, total_price
FROM sales
WHERE total_price > (SELECT AVG(total_price) FROM sales)
LIMIT 10;
```

```
customer_name     total_price
----------------  -----------
Caleb Davis       2394
Misty Herrera     13581
Rick Soto         5230
Sean Haas         2920
Michelle White    5458
Breanna Gonzalez  26136
Angela Rivera     20797
Emily Anderson    7010
Laura Anderson    4454
Ryan Smith        9834
```

---

## 7. Top 5 Customers by Total Amount Spent

```
customer_name     total_spent
----------------  -----------
Lynn Garrison     47940
Debbie Turner     44990
Megan Charles     44620
Michelle Beltran  42471
Rick Sanford      41211
```

---

## 8. Overall Average Order Value

```
average_order_value
-------------------
12100.535
```

---

## Summary of Key Insights

- **Highest revenue category:** Furniture (₹714,399)
- **Lowest revenue category:** Clothing (₹484,259)
- **Most orders placed in:** Furniture (59 orders)
- **Highest avg order value by region:** West (₹13,938.77)
- **Lowest avg order value by region:** North (₹9,820.98)
- **Top customer by spend:** Lynn Garrison (₹47,940)
- **Overall average order value:** ₹12,100.54
