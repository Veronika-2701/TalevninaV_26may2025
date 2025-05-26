SELECT products.product_name
FROM products
JOIN nutritional_information ON products.product_id = nutritional_information.product_id
WHERE nutritional_information.protein = (select max(protein) from nutritional_information)
