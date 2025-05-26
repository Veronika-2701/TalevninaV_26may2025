SELECT categories.category_name, ROUND(AVG(products.price)::numeric, 2)
FROM products
JOIN categories ON  products.category_id = categories.category_id
GROUP BY categories.category_name