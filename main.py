from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from fastapi.responses import RedirectResponse
import random
import string
from urlDB import SessionLocal, URL


app = FastAPI()

class URLData(BaseModel):
    '''Pydantic data and type validation'''
    url: HttpUrl

def generate_short_code(length=6):
    '''Generates a random string of specified length using letters and digits.'''
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.post("/shorten")
def shorten_url(url_data: URLData):
    
    db = SessionLocal() # Create a new database session
    
    
    randomstr = generate_short_code()
     # Ensure uniqueness using DB
    existing = db.query(URL).filter(URL.short_code == randomstr).first()
    while existing:
        randomstr = generate_short_code()
        existing = db.query(URL).filter(URL.short_code == randomstr).first()
    '''Handling collision of short URLs by generating a new random string until a unique one is found.'''
    '''Rather than storing the url as HttpUrl type we should store it as a string type in DB'''
    
    
    new_url = URL(short_code=randomstr, original_url=str(url_data.url)) # Create a new URL object with the generated short code and original URL
    db.add(new_url) # Add the new URL object to the database session
    db.commit() # Commit the transaction to save the new URL mapping in the database
    db.refresh(new_url) # Refresh the new URL object to get the updated data from the database (e.g., auto-generated ID)
    
    return {"short_url": f"http://short.url/{randomstr}"}


@app.get("/{short_code}")
def redirect_url(short_code: str):
    db=SessionLocal() # Create a new database session
    exists=db.query(URL).filter(URL.short_code == short_code).first() # Query the database to check if the short code exists
    if not exists:
        raise HTTPException(status_code=404, detail="Short URL not found") 
    # Handling the case where the short code is not found in the url_map, returning a 404 error.
    return RedirectResponse(url=exists.original_url) 
    '''Redirecting to the original URL associated with the short code. In a real application, this would involve sending an HTTP redirect response to the client using something like FastAPI's RedirectResponse.''' 
    
