-- lists all shows contained in hbtn_0d_tvshows without a genre linked
-- cat 12-no_genre.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT C.title, S.genre_id FROM tv_shows C
LEFT JOIN tv_show_genres S ON C.id = S.show_id
WHERE S.genre_id IS NULL
ORDER BY C.title, S.genre_id ASC;
