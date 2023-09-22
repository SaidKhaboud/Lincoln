SELECT
    T.client_id AS client_id,
    SUM(CASE WHEN P.product_type = 'MEUBLE' THEN T.prod_price * T.prod_qty ELSE 0 END) AS ventes_meuble,
    SUM(CASE WHEN P.product_type = 'DECO' THEN T.prod_price * T.prod_qty ELSE 0 END) AS ventes_deco
FROM
    TRANSACTIONS T
INNER JOIN
    PRODUCT_NOMENCLATURE P
ON
    T.prod_id = P.product_id
WHERE
    T.date >= '2020-01-01' AND T.date <= '2020-12-31'
GROUP BY
    T.client_id;
