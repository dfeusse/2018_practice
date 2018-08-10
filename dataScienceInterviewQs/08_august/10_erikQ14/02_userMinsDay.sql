SELECT user.user_id, date(user.timestamp, 'unixepoch'), sum(song.song_length)
FROM song_info as song
JOIN user_song_log as user
ON (song.song_id=user.song_id)
GROUP BY 1, 2