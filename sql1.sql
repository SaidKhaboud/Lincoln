SELECT
    T.date AS date,
    SUM(T.prod_price * T.prod_qty) AS chiffre_affaires
FROM
    TRANSACTIONS T
INNER JOIN
    PRODUCT_NOMENCLATURE P
ON
    T.prod_id = P.product_id
WHERE
    T.date >= '2019-01-01' AND T.date <= '2019-12-31'
GROUP BY
    T.date
ORDER BY
    T.date;
