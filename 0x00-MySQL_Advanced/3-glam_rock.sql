-- Rank the bands with Glam rock as their main style by their longevity
-- Column names must be: band_name and lifespan (in years until 2022 - using 2022 instead of YEAR(CURDATE()))
-- Use attributes formed and split for computing the lifespan
SELECT
    band_name,
    (IFNULL(split, 2022) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
