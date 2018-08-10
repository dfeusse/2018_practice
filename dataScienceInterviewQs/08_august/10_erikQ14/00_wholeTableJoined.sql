SELECT song.song_id, song.artist_id, song.song_length, user.user_id, user.timestamp, user.song_id, user.artist_id
FROM song_info as song
JOIN user_song_log as user
ON (song.song_id=user.song_id)