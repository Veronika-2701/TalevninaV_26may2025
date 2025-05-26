SELECT products.product_id, products.product_name, products.price 
FROM products
JOIN nutritional_information ON products.product_id = nutritional_information.product_id
WHERE nutritional_information.fiber > 5
