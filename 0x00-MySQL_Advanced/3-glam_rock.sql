-- Comment: Create a table with glam rock bands
SELECT band_name,
  IF(split IS NOT NULL, split - formed, 2022 - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name DESC;
