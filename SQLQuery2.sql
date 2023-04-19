

/*QUERY POR SUBCONSULTAS*/

SELECT Nombre 
FROM categoria
WHERE CodigoCategoria = 
	(SELECT CodigoCategoria
	FROM producto 
	WHERE CodigoProducto = (
		SELECT prod.CodigoProducto
		FROM 
			(SELECT TOP 1 *
			FROM venta 
			ORDER BY fecha ASC) AS prod
		)
	)
;


/* QUERY POR INNER JOINGS*/
SELECT TOP 1 c.Nombre
FROM categoria c
INNER JOIN producto p ON c.CodigoCategoria = p.CodigoCategoria
INNER JOIN venta v on p.CodigoProducto = v.CodigoProducto
ORDER BY v.Fecha DESC
