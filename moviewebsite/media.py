import webbrowser #for opening webpages

class Movie():
    def __init__(self, t, p, s, v, r):
        self.title = t
        self.poster_image_url = p
        self.storyline = s
        self.trailer_youtube_url = v
        self.ranking = r

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
