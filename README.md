# spotify-ml
Uses basic knn algorithm to build a spotify playlist. Accesses user playlists by calling to spotify api. Test set is formed from two existing playlists, one of songs I want the playlist to resemble, another of songs I don't want in it. Then accesses in-built spotify audio analysis features to use for learning. Aggregates songs from spotify featured playlists, and generates a new playlist of 100 songs.

Also, as a warning, it takes a very long time for the playlist to actually be generated, as it has to make individual calls to spotify's API in order to fetch audio features for every song

# Conclusion
The playlist generated isn't perfect, but overall it's not too bad. Ultimately the playlist I generated wasn't very similar to my initial playlist but I did like the songs in the playlist, so in that way it was a success. I think part of the issue was that I wanted a psychedelic music playlist, but there's more to a psych song (or a song of any genre) than just what's captured by spotify audio features. Another issue is that I ended up with a lot of instrumental songs. This isn't necessarily a problem, but I personally don't like instrumental songs, so it may have been a good idea to try and cut them out. Overall though I'm not particularly unhappy. I ended up finding some songs I like through my playlist too.

On the bright side, I think this project helped me learn a bit about why I like certain songs, regardless of genre. Clearly I like songs that have a loud instrumentals and fast tempos, and that's why I ended up with a playlist of songs that has those attributes. As I learn more, I might try to refine and recreate this project with more advanced algorithms, and hopefully make a better playlist.
