from fastapi import FastAPI, Query, Path, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
import uvicorn
from pymongo import MongoClient

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
please publicly or privately message me and I will take it down immediately.)🤡


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
client = MongoClient("mongodb://localhost:27017/")
db = client["candy_store"]
collection = db["candies"]

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


@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")


@app.get("/candies")
def list_all_candies():
    return list(collection.find({}, {"_id": 0}))


# get list of candy categories
@app.get("/candies/categories")
def list_all_candy_categories():
    return list(collection.distinct("category"))


# get candies in a specific category
@app.get("/candies/{category}")
def list_candies_in_category(category: str):
    return list(collection.find({"category": category}, {"_id": 0}))


# get candies with a key word in the description
@app.get("/candies/search/{keyword}")
def list_candies_by_keyword(keyword: str):
    return list(
        collection.find(
            {"description": {"$regex": keyword, "$options": "i"}}, {"_id": 0}
        )
    )


# get candies with a key word in the name
@app.get("/candies/name/{keyword}")
def list_candies_by_name(keyword: str):
    return list(
        collection.find({"name": {"$regex": keyword, "$options": "i"}}, {"_id": 0})
    )


# get candies by price range
@app.get("/candies/price/{min_price}/{max_price}")
def list_candies_by_price(min_price: float, max_price: float):
    return list(
        collection.find({"price": {"$gte": min_price, "$lte": max_price}}, {"_id": 0})
    )


# get candy with a specific id
@app.get("/candies/id/{id}")
def list_candies_by_id(id: int):
    return list(collection.find({"id": id}, {"_id": 0}))


# get a candy image
@app.get("/candies/image/{id}")
def get_candy_image(id: int):
    candy = collection.find_one({"id": id}, {"_id": 0})
    if candy:
        return FileResponse(candy["image"])
    else:
        raise HTTPException(status_code=404, detail="Candy not found")


# update a candy price
@app.put("/candies/price/{id}/{price}")
def update_candy_price(id: int, price: float):
    candy = collection.find_one({"id": id}, {"_id": 0})
    if candy:
        collection.update_one({"id": id}, {"$set": {"price": price}})
        return {"message": "Candy price updated"}
    else:
        raise HTTPException(status_code=404, detail="Candy not found")


# delete a candy
@app.delete("/candies/{id}")
def delete_candy(id: int):
    candy = collection.find_one({"id": id}, {"_id": 0})
    if candy:
        collection.delete_one({"id": id})
        return {"message": "Candy deleted"}
    else:
        raise HTTPException(status_code=404, detail="Candy not found")


# update all fields of a candy
@app.put("/candies/{id}")
def update_candy(
    id: int, name: str, category: str, price: float, description: str, image: str
):
    candy = collection.find_one({"id": id}, {"_id": 0})
    if candy:
        collection.update_one(
            {"id": id},
            {
                "$set": {
                    "name": name,
                    "category": category,
                    "price": price,
                    "description": description,
                    "image": image,
                }
            },
        )
        return {"message": "Candy updated"}
    else:
        raise HTTPException(status_code=404, detail="Candy not found")


if __name__ == "__main__":
    uvicorn.run(
        "api:app", host="mater.systems", port=8084, log_level="debug", reload=True
    )
