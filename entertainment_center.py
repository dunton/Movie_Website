# import other files used in project
import media
import fresh_tomatoes

# build new instance ex_machina of Movie class
ex_machina = media.Movie("Ex Machina",
                         """Genius builds an AI and must subject her
                         to the Turing Test""",
                         "http://www.scifi-movies.com/images/contenu/data/0004530/affiche-ex-machina-2015-5.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=bggUmgeMCdc")

# build new instance pulp_fiction of Movie class
pulp_fiction = media.Movie("Pulp Fiction",
                           "Several everyday activities go way off the tracks",
                           "http://dgeiu3fz282x5.cloudfront.net/g/l/lgpp30791+movie-one-sheet-pulp-fiction-poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# build new instance inglourious_basterds of Movie class
inglourious_basterds = media.Movie("Inglorious Basterds",
                                   """Group of American soldiers try to
                                   kill Hitler""",
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Inglourious_Basterds_poster.jpg/220px-Inglourious_Basterds_poster.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=qRYDNWXuip8")  # NOQA

# build new instance wolf_of_wallstreet of Movie class
wolf_of_wallstreet = media.Movie("Wolf of Wall Street",
                                 "Man gets rich illegally and loses it all",
                                 "https://upload.wikimedia.org/wikipedia/en/thumb/1/1f/WallStreet2013poster.jpg/220px-WallStreet2013poster.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=iszwuX1AK6A")

# build new instance hitch of Movie class
hitch = media.Movie("Hitch",
                    "Man helps other men find their soulmates",
                    "https://upload.wikimedia.org/wikipedia/en/d/d4/Hitch_poster.JPG",  # NOQA
                    "https://www.youtube.com/watch?v=dMaq_pfxs-0")

# build new instance margin_call of Movie class
margin_call = media.Movie("Margin Call",
                          """Shows events inside investement bank during dawn
                          of financial crisis""",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/6/62/Margin_Call.jpg/220px-Margin_Call.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=Y2DqFRsPrns")

# make array of all instances of movies so they can be called all at once
movies = [ex_machina, pulp_fiction, inglourious_basterds, wolf_of_wallstreet,
          hitch, margin_call]

# run open_movies_page from fresh_tomatoes file taking movies as argument
fresh_tomatoes.open_movies_page(movies)

