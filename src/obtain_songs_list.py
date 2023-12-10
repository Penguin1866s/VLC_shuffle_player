def obtain_songs_list(root):
    songs = []
    namespace = {'ns': 'http://xspf.org/ns/0/'}
    for track in root.findall(".//ns:trackList/ns:track", namespace):
        title = track.find("ns:title", namespace).text
        location = track.find("ns:location", namespace).text
        songs.append({"title": title, "location": location})
    return songs
