# Vercel Python serverless entrypoint.
#
# Vercel har request "api/" ke andar kisi file ko WSGI/ASGI handler
# expect karke bhejta hai. Humara poora Flask app main.py (repo root) me
# hai — us logic ko yahan duplicate nahi kiya, sirf import karke expose
# kiya hai, taaki main.py hi single source of truth rahe (Render/Docker
# deploy ke liye bhi wahi file use hoti hai, bina kisi change ke).
from main import flask_app as app
