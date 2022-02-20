import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)

db = firestore.client() 
collection = db.collection('drivers')  


res = collection.document()
res.set({"name":"loganatha"})
print(res.id)