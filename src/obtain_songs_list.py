def obtain_songs_list(root):
    songs = []
    namespace = {'ns': 'http://xspf.org/ns/0/'}
    for track in root.findall(".//ns:trackList/ns:track", namespace):
        title = track.find("ns:title", namespace).text
        location = track.find("ns:location", namespace).text
        songs.append({"title": title, "location": location})
    return songs

#(for better comprension of how it works and how is the use of the variable "namespace").
###Is equivalent to
#-->
#def obtain_songs_list(root):
#    songs = []
#    for track in root.findall(".//{http://xspf.org/ns/0/}trackList/{http://xspf.org/ns/0/}track"):
#        title = track.find("{http://xspf.org/ns/0/}title").text
#        location = track.find("{http://xspf.org/ns/0/}location").text
#        songs.append({"title": title, "location": location})
#    return songs
