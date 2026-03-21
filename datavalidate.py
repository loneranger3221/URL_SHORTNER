from pydantic import BaseModel, HttpUrl

class URLData(BaseModel):
    
    '''Pydantic's HttpUrl data validation ensures that an input string is a syntactically valid HTTP or HTTPS URL. It checks for the presence of a valid scheme (http or https), a valid host, and optionally a port, path, query parameters, and fragments. '''
    
    url: HttpUrl
