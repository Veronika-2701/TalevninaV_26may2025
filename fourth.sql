SELECT products.category_id, SUM(nutritional_information.fat)
FROM products
JOIN nutritional_information ON  products.product_id = nutritional_information.product_id
WHERE nutritional_information.fat != 0
GROUP BY products.category_id