import media #the other file with the other code in it
import fresh_tomatoes

game1 = media.Movie("Watch Dogs 2", "https://upload.wikimedia.org/wikipedia/en/b/b0/Watch_Dogs_2.jpg", "We aren't just script kiddies anymore.", "https://www.youtube.com/watch?v=7hamZRt3gFE", "Score: 5/5")
game2 = media.Movie("Fallout 4", "https://upload.wikimedia.org/wikipedia/en/7/70/Fallout_4_cover_art.jpg", "War never changes.", "https://www.youtube.com/watch?v=GE2BkLqMef4", "Score: 4/5")
game3 = media.Movie("Nuclear Throne", "https://i.redditmedia.com/adaKdAfojxg_eiG44o7UWTLB-esLpqunypWtaXVpoPI.jpg?w=320&s=7eb565ec376dfbe9093d67bb8630d67a", "Twelve Heirs to the throne.", "https://www.youtube.com/watch?v=7LSs1bj41P4", "Score: 3/5")

movies = [game1, game2, game3]

fresh_tomatoes.open_movies_page(movies)
