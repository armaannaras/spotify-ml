# spotify-ml
Uses basic knn algorithm to build a spotify playlist. Accesses user playlists by calling to spotify api. Test set is formed from two existing playlists, one of songs I want the playlist to resemble, another of songs I don't want in it. Then accesses in-built spotify audio analysis features to use for learning. Aggregates songs from spotify featured playlists, and generates a new playlist of 100 songs.

# Conclusion
The playlist generated isn't perfect, but overall it's not too bad. Ultimately the playlist I generated wasn't very similar to my initial playlist but I did like the songs in the playlist, so in that way it was a success. I imagine that there's three main things that can be said to cause these issues. First is that spotify's inbuilt measures don't tell you much about the content of the music, as far as subject matter or choice or instrument, or other factors that determine genre. My interest was in creating a playlist of psychedelic rock music, but really I just ended up with a playlist of songs with loud instrumentals and fast tempo. That does describe the initial playlist I used, so in that way it was actually successful, but I didn't really end up with much psychedelic music. Secondly, I think my playlist of "bad" songs (songs I didn't want in my platlist) was perhaps not diverse enough. It was mostly built using songs/artists I actually like, just stuff I wouldnt want in a psychedlic rock playlist. The issue is that it was built using my rap playlist, in addition to some pop and rock albums I like. That's not a huge amount of musical diversity, in fact it doesn't even cover every genre of music I listen to. In addition, it's entirely possible that the songs I tested score similarly in spotify metrics to the psychedlic songs I used in my "good" playlist. It follows that if I like psychedelic music with a certain tempo/loudness/valence then I may also like rap or pop music with similar scores in those measures. In that case, I'm also not getting very much diversity as far as audio features. Third, I'm not sure how valuable knn is in this scenario. Music taste is very complex, and given how much goes in to determining whether songs are similar to one another (genre, types of instruments, use of instruments, audio features as spotify aggregates, lyrical content, emotional content, etc.) this kind of problem probably needs a more sophisticated algorithm.

On the bright side, I think this project helped me learn a bit about why I like certain songs, regardless of genre. Clearly I like songs that have a loud instrumentals and fast tempos, and that's why I ended up with a playlist of songs that has those attributes. As I learn more, I might try to refine and recreate this project with more advanced algorithms, and hopefully make a better playlist.
