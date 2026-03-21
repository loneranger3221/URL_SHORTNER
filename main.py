from fastapi import FastAPI, HTTPException
from datavalidate import URLData
import random , string
app = FastAPI()

@app.post("/shorten")
def shorten_url(url_data: URLData):
    
    characterset=string.ascii_letters + string.digits
    randomstr= ''.join(random.choice(characterset) for i in range(6))
    return {"short_url": "http://short.url/{randomstr}"} '''put the randomly generated string in the URL to create a unique shortened URL.'''

if __name__ == "__main__":
    app.run()
    