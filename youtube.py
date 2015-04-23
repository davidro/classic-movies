import fresh_tomatoes
import media
# Google APIs Client Library for Python you havto to install in order to run the script: pip install --upgrade google-api-python-client
from apiclient.discovery import build

# insert here your Google Dev API key
API_KEY =""
# youtube playlist id, change it to display movies of a custom list on youtube
list_id = "PLX9_I-EOJPdFuOjcI2zkmTck55homHEBE"

# function that you pass an youtube playlist id and returns a list containing instances of movies from media module
def youtube_list_movies(listid):

    # this part gets executed if you provide an API_KEY
    if API_KEY:
        # make a request to youtube API with youtube playlist id as an parameter
        youtube = build("youtube", "v3", developerKey=API_KEY)
        response = youtube.playlistItems().list(playlistId=listid,part="id,snippet",maxResults="48").execute()

        # initialize an empty list
        list_of_movies = []

        # itterate trough the response object and extract title, desc, img and video properties for each item
        for item in response["items"]:
            title = item["snippet"]["title"]
            # shorten title to 24 characters with cap function
            title = cap(title, 24)
            desc = item["snippet"]["description"].encode('utf-8')
            # shorten description to 80 characters with cap function
            desc = cap(desc, 80)
            img = item["snippet"]["thumbnails"]["high"]["url"]
            video = "https://www.youtube.com/watch?v="+item["snippet"]["resourceId"]["videoId"]
            # append each item properties in a list
            list_of_movies.append(media.Movie(title,desc,img,video))
        return list_of_movies

    # if API_KEY is not provided this part gets executed, where each instance of a Movie class is created by passing in the Title, Description, Picture and URL to video parameters
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

        list_of_movies = [road_show,clipped_wings,sunny,cross_streets,ten_nights,old_fashioned_girl]
        return list_of_movies

# function to shorten the string length: s - is string, l - is numeric value of characters to preserve in string
def cap(string_to_shorten, length):
    return string_to_shorten if len(string_to_shorten)<=length else string_to_shorten[0:length-3]+'...'


# finally call the youtube_list_movies function and pass its results to the fresh_tomatoes function
movies_list = youtube_list_movies(list_id)
# generates the html file with list of movies and opens it in browser
fresh_tomatoes.open_movies_page(movies_list)
