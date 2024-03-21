-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- cat 14-my_genres.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT G.name AS name FROM tv_shows S
LEFT JOIN tv_show_genres SG ON S.id = SG.show_id
LEFT JOIN tv_genres G ON SG.genre_id = G.id
WHERE S.title = 'Dexter'
ORDER BY name ASC;
