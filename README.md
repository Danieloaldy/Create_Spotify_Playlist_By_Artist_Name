# Create_Spotify_Playlist_By_Artist_Name



# English

You Must Have python And spotipy downloaded

to install python
https://www.python.org/

to install spotipy (after python)
1. open cmd
2. type "pip install spotipy"


HOW TO GET CLIENT ID AND CLIENT SECRET
1. You need to have a spotify account to use this code.
2. Go to https://developer.spotify.com/ 
3. Login and go to the dashboard and create app
4. You can fill the app name anything that you want
5. For the "Redirect URI" Column you need to enter that as "https://example.com/"
6. Checklist the "Web API"
7. Checklist the Terms and Services and save
8. Then go To Settings, Copy The "Client ID and Client Secret" and paste it on the code, (Line 9 & Line 10)
9. For the username, go to "https://www.spotify.com/account/profile/" and copy the your username id (Line 13)
10. The first run, there will a popup on a browser to authorize, click agree and copy the website link then paste it on the terminal


After you input the artist name, the code will search the artist and take top 50 of the artist. then it will added to the new playlist, if the same title have been added, the same title will be skipped, thats why you often found it didnt take 50

the base market is set to "ID" Indonesia, You can change it to your country (Line 23)






# Indonesia

Pastikan python dan spotipy sudah di download

cara install python
https://www.python.org/

cara install spotipy (setelah python)
1. buka cmd
2. type "pip install spotipy"

Cara mendapatkan Client ID dan Client Secret
1. Kamu harus memiliki akun spotify untuk menggunakan kode ini.
2. Pergi ke https://developer.spotify.com/
3. Login lalu tekan profile, pergi ke halaman dashboard lalu tekan
4. Kamu bisa mengisi, App name, App Description bebas
5. Untuk "Redirect URI" kamu harus memasukkan ini "https://example.com/"
6. Centang bagian "Web API"
7. Centang Terms and Services lalu save
8. Pergi ke settings, copy "Client ID and Client Secret" dan paste di Code, (Line 9 & Line 10)
9. Untuk username, pergi ke "https://www.spotify.com/account/profile/" dan copy username id lalu paste ke code (Line 13)
10. Saat pertama kali di run, akan ada browser untuk mengizinkan api tersebut, tekan agree dan copy link website saat ini, lalu paste di terminal


Setelah memasukkan nama artis, program akan mencari top 50 dari artis tersebut. lalu akan menambahkan ke playlist terbaru, jika ada lagu dengan judul yang sama, itu akan di skip. itulah biasanya, playlist tidak selalu berisi 50 lagu

marketnya di set "ID" Indonesia, jika ingin menggantinya ada di (Line 23)



