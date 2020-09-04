import os
import time

from dotenv import load_dotenv
load_dotenv(verbose=True)

import bearer_agent

import httpx

bearer_agent.init(
  secret_key=os.environ.get("BEARER_SECRET_KEY"),
  environment=os.environ.get("APP_ENV")
)

# Postman-echo
print("-- Sending API calls to Postman-Echo --")
httpx.get("https://postman-echo.com/status/404",
              headers={"password": "h4x0r", "secret": "secret key"})

httpx.get("https://postman-echo.com/status/403",
              headers={"password": "h4x0r", "secret": "secret key"})


httpx.get("https://postman-echo.com/status/429",
              headers={"password": "h4x0r", "secret": "secret key"})

httpx.get("https://postman-echo.com/status/501?email=pii@example.com",
              headers={"password": "h4x0r", "secret": "secret key"})

httpx.get("https://postman-echo.com/status/200")

httpx.post("https://postman-echo.com/post",
              headers={"Content-Type": "application/json"},
              data={"foo": "Bar"})

# NASA API
print("-- Sending API calls to NASA API --")
httpx.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

# Star Wars API
print("-- Sending API calls to SWAPI --")
httpx.get("https://swapi.dev/api/people/1/")
httpx.get("https://swapi.dev/api/people/9/")
httpx.get("https://swapi.dev/api/starships/9/")

# Foo Bar -> Non Existing API
print("-- Sending API calls to non existing API --")
try:
  httpx.get("https://foo.bar/status/200")
except:
  print("")
