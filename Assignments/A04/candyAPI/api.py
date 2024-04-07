# Libraries for FastAPI
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from mongoManager import MongoManager

# Builtin libraries


"""
           _____ _____   _____ _   _ ______ ____
     /\   |  __ \_   _| |_   _| \ | |  ____/ __ \
    /  \  | |__) || |     | | |  \| | |__ | |  | |
   / /\ \ |  ___/ | |     | | | . ` |  __|| |  | |
  / ____ \| |    _| |_   _| |_| |\  | |   | |__| |
 /_/    \_\_|   |_____| |_____|_| \_|_|    \____/

The `description` is the information that gets displayed when the api is accessed from a browser and loads the base route.
Also the instance of `app` below description has info that gets displayed as well when the base route is accessed.
"""

description = """🤡
(This description is totally satirical and does not represent the views of any real person alive or deceased. 
And even though the topic is totally macabre, I would love to make anyone who abuses children very much deceased.
However, the shock factor of my stupid candy store keeps you listening to my lectures. If anyone is truly offended
please publicly or privately message me and I will take it down idbediately.)🤡


## Description:
Sweet Nostalgia Candies brings you a delightful journey through time with its extensive collection of 
candies. From the vibrant, trendy flavors of today to the cherished, classic treats of yesteryear, 
our store is a haven for candy lovers of all ages (but mostly kids). Step into a world where every shelf and corner 
is adorned with jars and boxes filled with colors and tastes that evoke memories and create new ones. 
Whether you're seeking a rare, retro candy from your childhood or the latest sugary creation, Sweet 
Nostalgia Candies is your destination. Indulge in our handpicked selection and experience a sweet 
escape into the world of confectionery wonders! And don't worry! We will watch your kids!! (😉)

#### Contact Information:

- **Address:** 101 Candy Lane, Alcatraz Federal Penitentiary, San Francisco, CA 94123.
- **Phone:** (123) 968-7378 [or (123 you-perv)]
- **Email:** perv@kidsinvans.com
- **Website:** www.kidsinvans.fun

"""
# Needed for CORS
# origins = ["*"]


# This is the `app` instance which passes in a series of keyword arguments
# configuring this instance of the api. The URL's are obviously fake.
app = FastAPI(
    title="KidsInVans.Fun🤡",
    description=description,
    version="0.0.1",
    terms_of_service="http://www.kidsinvans.fun/worldleterms/",
    contact={
        "name": "KidsInVans.Fun",
        "url": "http://www.kidsinvans.fun/worldle/contact/",
        "email": "perv@www.kidsinvans.fun",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

# Needed for CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

"""
  _      ____   _____          _         _____ _                _____ _____ ______  _____
 | |    / __ \ / ____|   /\   | |       / ____| |        /\    / ____/ ____|  ____|/ ____|
 | |   | |  | | |       /  \  | |      | |    | |       /  \  | (___| (___ | |__  | (___
 | |   | |  | | |      / /\ \ | |      | |    | |      / /\ \  \___ \\___ \|  __|  \___ \
 | |___| |__| | |____ / ____ \| |____  | |____| |____ / ____ \ ____) |___) | |____ ____) |
 |______\____/ \_____/_/    \_\______|  \_____|______/_/    \_\_____/_____/|______|_____/

This is where you will add code to load all the countries and not just countries. Below is a single
instance of the class `CountryReader` that loads countries. There are 6 other continents to load or
maybe you create your own country file, which would be great. But try to implement a class that 
organizes your ability to access a countries polygon data.
"""

"""
  _      ____   _____          _        __  __ ______ _______ _    _  ____  _____   _____
 | |    / __ \ / ____|   /\   | |      |  \/  |  ____|__   __| |  | |/ __ \|  __ \ / ____|
 | |   | |  | | |       /  \  | |      | \  / | |__     | |  | |__| | |  | | |  | | (___
 | |   | |  | | |      / /\ \ | |      | |\/| |  __|    | |  |  __  | |  | | |  | |\___ \
 | |___| |__| | |____ / ____ \| |____  | |  | | |____   | |  | |  | | |__| | |__| |____) |
 |______\____/ \_____/_/    \_\______| |_|  |_|______|  |_|  |_|  |_|\____/|_____/|_____/

This is where methods you write to help with any routes written below should go. Unless you have 
a module written that you include with statements above.  
"""


"""
  _____   ____  _    _ _______ ______  _____
 |  __ \ / __ \| |  | |__   __|  ____|/ ____|
 | |__) | |  | | |  | |  | |  | |__  | (___
 |  _  /| |  | | |  | |  | |  |  __|  \___ \
 | | \ \| |__| | |__| |  | |  | |____ ____) |
 |_|  \_\\____/ \____/   |_|  |______|_____/

 This is where your routes will be defined. Routes are just python functions that retrieve, save, 
 delete, and update data. How you make that happen is up to you.
"""

db = MongoManager(db="candy_store")


@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")


@app.get("/candies")
def list_all_candies():
    """
    Retrieve a list of all candies available in the store.
    """
    db.setCollection("candies")
    result = db.get(filter={"_id": 0})
    return result


@app.get("/categories")
def list_all_categories():
    """
    Retrieve a list of all candy categories available in the store.
    """
    db.setCollection("categories")
    results = db.get(filter={"_id": 0})
    return results


@app.get("/candies/category/{category}")
def candies_by_category(category: str):
    """
    Search for candies based on a query string (e.g., name, category, flavor).
    """
    db.setCollection("candies")
    result = db.get(
        query={"category": category},
        filter={"_id": 0, "name": 1, "price": 1, "category": 1},
    )
    return result


@app.get("/candies/desc/{desc}")
def candies_by_description(desc: str):
    """
    Search for candies based on a description keyword string (e.g., name, category, flavor).
    """
    db.setCollection("candies")
    regex_query = {"desc": {"$regex": desc, "$options": "i"}}
    results = db.get(
        query=regex_query,
        sort_criteria=[("name", 1)],
    )
    return results


@app.get("/candies/name/{name}")
def candies_by_name(name: str):
    """
    Search for candies based on a name keyword string (e.g., name, category, flavor).
    """
    db.setCollection("candies")
    regex_query = {"name": {"$regex": name, "$options": "i"}}
    results = db.get(
        query=regex_query,
        sort_criteria=[("name", 1)],
    )
    return results


@app.get("/candies/id/{id}")
def get_candy_by_id(id: str):
    """
    Get detailed information about a specific candy.
    """
    db.setCollection("candies")
    result = db.get(
        query={"id": id}, filter={"_id": 0, "name": 1, "price": 1, "category": 1}
    )
    return result


@app.get("/candies/price/{price1}-{price2}")
def get_candy_by_price_range(price1: float, price2: float):
    """
    Get candies within a specified price range.
    """
    price_range_query = {"price": {"$gte": price1, "$lte": price2}}
    db.setCollection("candies")
    rangeQuery = db.get(
        query=price_range_query,
        filter={"_id": 0, "price": 1, "category_id": 1, "name": 1},
        sort_criteria={"price": -1},
    )
    return rangeQuery


@app.post("/candies")
def add_new_candy(document):
    """
    Add a new candy to the store's inventory.
    """
    db.setCollection("candies")
    result = db.post(document)
    return result


@app.put("/candies/{candy_id}/{update_type}/{update_data}")
def update_candy_info(candy_id: int, update_type: str, update_data: str):
    """
    Update information about an existing candy.
    """
    db.setCollection("candies")
    result = db.put2("_id", candy_id, update_type, update_data)
    return result


@app.delete("/candies/{candy_id}")
def delete_candy(candy_id: int):
    """
    Remove a candy from the store's inventory.
    """
    db.setCollection("candies")
    result = db.delete(candy_id)
    return result


@app.get("/categories")
def list_categories():
    """
    Get a list of candy categories (e.g., chocolates, gudbies, hard candies).
    """
    db.setCollection("categories")
    result = db.get(filter={"_id": 0})
    return result


if __name__ == "__main__":
    uvicorn.run(
        app="api:app", host="mater.systems", port=8084, log_level="debug", reload=True
    )
