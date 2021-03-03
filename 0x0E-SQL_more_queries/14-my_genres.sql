-- Lists all genres of a single show
SELECT tv_genres.name
FROM tv_show_genres LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = 8;
