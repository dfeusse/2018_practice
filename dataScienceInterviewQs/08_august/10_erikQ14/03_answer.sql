SELECT avg(average) /60 / 60 FROM
(
SELECT user.user_id as user, sum(song.song_length)/count(date(user.timestamp, 'unixepoch')) as average
FROM song_info as song
JOIN user_song_log as user
ON (song.song_id=user.song_id)
GROUP BY 1
ORDER BY 1
)