-- Lists genres and number of TV shows that match
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP By tv_genres.id
ORDER BY number_of_shows DESC;
