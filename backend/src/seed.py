from Tesco import Tesco
from Supervalu import Supervalu
from database import DBConnector
from Aldi import Aldi

# Testing python code used to seed the database.

catagories = ["Milk chocolate digestives",
              "milk",
              "butter",
              "carrots",
              "parsnip",
              "Raspberries",
              "bananas",
              "wine",
              "porridge",
              "cereal",
              "mandarins",
              "Mushrooms",
              "Broccoli",
              "Potato",
              "Apple",
              "Orange",
              "Cabbage",
              "beans",
              "Cucumber",
              "Celery",
              "Pear",
              "Eggs",
              "Blueberry",
              "Spinach",
              "beetroot",
              "garlic",
              "pepper",
              "olive oil",
              "tofu",
              "vinegar",
              "lemon",
              "lime",
              "onion",
              "Kale",
              "Grape",
              "Pepper",
              "Tomato",
              "avocado",
              "noodles",
              "bread",
              "Dog food",
              "Granulated sugar",
              "Cola",
              "Fanta",
              "Lemonade",
              "Crisps",
              "Nuts",
              "Nachos",
              "Coca-Cola",
              "Cadbury",
              "Avonmore",
              "Brennans",
              "Lucozade",
              "Tayto",
              "7 up",
              "Jacobs",
              "Goodfellas",
              "Monster",
              "Nescafe",
              "Red Bull",
              "Pringles",
              "Ballygowan",
              "Dairygold",
              "Kinder",
              "Yoplait",
              "McVities",
              "Pat The Baker",
              "Club",
              "chickpea",
              "pasta"]

db = DBConnector()

tesco = Tesco(catagories)
sql = tesco.get_tesco_products()
db.perform_insert(sql)

sv = Supervalu(catagories)
sql = sv.get_supervalu_products()
db.perform_insert(sql)

aldi = Aldi(catagories)
sql = aldi.get_aldi_products()
db.perform_insert(sql)
