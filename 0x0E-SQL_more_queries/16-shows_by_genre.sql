-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- cat 16-shows_by_genre.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT S.title AS title, G.name AS name
FROM tv_shows S
LEFT JOIN tv_show_genres SG ON S.id = SG.show_id
LEFT JOIN tv_genres G ON SG.genre_id = G.id
ORDER BY title, name ASC;
