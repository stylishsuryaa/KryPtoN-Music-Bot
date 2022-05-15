HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = environ["SUDO_CHAT_ID"]
    SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = "7086582"
    API_HASH = "5f87de0805ef1e47680954eb70aa43bd"
    SUDO_CHAT_ID = "1921122662"


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
