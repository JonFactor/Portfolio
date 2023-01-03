TICKER = input('Ticker: ')
import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("C:\\Users\Factor_Jon\Documents\GitHub\Portfolioplz\python\WebScrapers\Selnium\StockScraper\Complez\stocks-18069-firebase-adminsdk-8byjf-cc5c5e8338.json")
firebase_admin.initialize_app(cred, {'databaseURL'})
db = firestore.client()

