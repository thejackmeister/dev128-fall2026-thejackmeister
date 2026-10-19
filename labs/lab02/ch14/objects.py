from dataclasses import dataclass

#use decorator to begin coding the attributes for our Movie class
@dataclass
class Movie:
    name: str =""
    year: int = 0

    #define our getter method for name and year of an object in our Moive class
    def getStr(self):
        return f"{self.name} ({self.year})"