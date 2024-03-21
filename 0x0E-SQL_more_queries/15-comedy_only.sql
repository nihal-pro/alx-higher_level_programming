-- lists all Comedy shows in the database hbtn_0d_tvshows
-- cat 15-comedy_only.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT S.title AS title FROM tv_shows S
JOIN tv_show_genres SG ON S.id = SG.show_id
JOIN tv_genres G ON SG.genre_id = G.id
WHERE G.name = 'Comedy'
ORDER BY title ASC;
