HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["7086582"])
    API_HASH = environ["5f87de0805ef1e47680954eb70aa43bd"]
    SUDO_CHAT_ID = environ["1921122662"]
    SESSION_STRING = environ["BQBVHdU_QgTUYhsch_Dh2Pw8M-9w6cmqgtt9IuLSVUWVKQ4_M8U311Pn8yVAPsQb6FX8TwsGpKwmgy8vQ6gQuoY9nDWlVz8zTewbgzJfxLkqySJRpets9KYvel9ECrevxQUFtLUPMpayt3RSLufN9xILNLuU0PuS0N8iogyKT5fpAYNesQqS2z_owzIowol6AddhbOxf3kyCTEEw4OQAjcRweLymiJy-QLsvyZK1TNu0JpxL1GLWW1DsRSig1P1ozpcbFE5fBtBE5CNks-zd9TzWnwTrxF1PmsOSqJeu0GyxZyOjMuGgvADELx0qozRj0AwGg0e2VMiWSZOzm3yGNb9pcoIBZgA"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = "7086582"
    API_HASH = "5f87de0805ef1e47680954eb70aa43bd"
    SUDO_CHAT_ID = "1921122662"


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
