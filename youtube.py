import fresh_tomatoes
import media
from apiclient.discovery import build

# insert here your Google Dev API key
API_KEY = "AIzaSyD4ar-efhC78OeptkkE3Ci2tEjgvr8cEVo"
list_id = "PLX9_I-EOJPdFuOjcI2zkmTck55homHEBE"

def youtube_list_movies(listid):
    if API_KEY:
        youtube = build("youtube", "v3", developerKey=API_KEY)
        response = youtube.playlistItems().list(playlistId=listid,part="id,snippet",maxResults="48").execute()
        l = []
        for item in response["items"]:
            title = item["snippet"]["title"]
            title = cap(title, 24)
            desc = item["snippet"]["description"].encode('utf-8')
            desc = cap(desc, 80)
            img = item["snippet"]["thumbnails"]["high"]["url"]
            video = "https://www.youtube.com/watch?v="+item["snippet"]["resourceId"]["videoId"]
            l.append(media.Movie(title,desc,img,video))
        return l
    else:
        road_show = media.Movie("Road Show",
                                "Rich playboy Drogo Gaines is in imminent danger of marrying a gold digger, and escapes by feigning insanity ",
                                "https://i.ytimg.com/vi/jqHfzCb8b10/hqdefault.jpg",
                                "https://www.youtube.com/watch?v=jqHfzCb8b10")
        clipped_wings = media.Movie("Clipped Wings",
                                 "Mickey Lofton, young half-brother of famed war-aviator Jerry, fails in his attempt to enter the Canadian Air Corps",
                                 "https://i.ytimg.com/vi/NbVx6_buRLw/hqdefault.jpg",
                                 "https://www.youtube.com/watch?v=NbVx6_buRLw")
        sunny = media.Movie(     "Sunny",
                                 "The beautiful Anna Neagle stars as a circus performer who falls in love with a rich car dealer's son",
                                 "https://i.ytimg.com/vi/-RUYUuKh1ew/hqdefault.jpg",
                                 "https://www.youtube.com/watch?v=-RUYUuKh1ew")
        cross_streets = media.Movie("Cross Streets",
                                "A man falls in love with a young woman, only to discover that she's the daughter of an ex-girlfriend ",
                                "https://i.ytimg.com/vi/ZZIg09vJpV0/hqdefault.jpg",
                                "https://www.youtube.com/watch?v=D-Qs0rSJyQs")
        ten_nights = media.Movie("Ten Nights in a Barroom",
                                 "A man's heavy drinking drives away his family and threatens to destroy his relationship with his little daughter",
                                 "https://i.ytimg.com/vi/yiv8aYfbSKA/hqdefault.jpg",
                                 "https://www.youtube.com/watch?v=yiv8aYfbSKA")
        old_fashioned_girl = media.Movie("An Old Fashioned Girl",
                                 "The story revolves around Polly Milton a country girl who visits a wealthy friend in the city",
                                 "https://i.ytimg.com/vi/0CN3wNgf_EI/hqdefault.jpg",
                                 "https://www.youtube.com/watch?v=0CN3wNgf_EI")
        l = [road_show,clipped_wings,sunny,cross_streets,ten_nights,old_fashioned_girl]
        return l

def cap(s, l):
    return s if len(s)<=l else s[0:l-3]+'...'

list = youtube_list_movies(list_id)
fresh_tomatoes.open_movies_page(list)
