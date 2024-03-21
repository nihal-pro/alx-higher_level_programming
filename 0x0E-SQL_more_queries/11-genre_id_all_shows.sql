--  lists all shows contained in the database hbtn_0d_tvshows
-- cat 11-genre_id_all_shows.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT C.title, S.genre_id FROM tv_shows C
LEFT JOIN tv_show_genres S ON C.id = S.show_id
ORDER BY C.title, S.genre_id ASC;
