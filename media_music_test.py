import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('music-in-media-firebase-adminsdk-ezcoo-a52d0e2da3.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

# doc_ref = db.collection(u'users').document(u'aturing')
# doc_ref.set({
#     u'first': u'Alan',
#     u'middle': u'Mathison',
#     u'last': u'Turing',
#     u'born': 1912
# })

# users_ref = db.collection(u'users')
# docs = users_ref.stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

# data = {
#     u'name': u'Los Angeles',
#     u'state': u'CA',
#     u'country': u'USA'
# }

# class City(object):
#     def __init__(self, name, state, country, capital=False, population=0,
#                  regions=[]):
#         self.name = name
#         self.state = state
#         self.country = country
#         self.capital = capital
#         self.population = population
#         self.regions = regions

#     @staticmethod
#     def from_dict(source):
#         # [START_EXCLUDE]
#         city = City(source[u'name'], source[u'state'], source[u'country'])

#         if u'capital' in source:
#             city.capital = source[u'capital']

#         if u'population' in source:
#             city.population = source[u'population']

#         if u'regions' in source:
#             city.regions = source[u'regions']

#         return city
#         # [END_EXCLUDE]

#     def to_dict(self):
#         # [START_EXCLUDE]
#         dest = {
#             u'name': self.name,
#             u'state': self.state,
#             u'country': self.country
#         }

#         if self.capital:
#             dest[u'capital'] = self.capital

#         if self.population:
#             dest[u'population'] = self.population

#         if self.regions:
#             dest[u'regions'] = self.regions

#         return dest
#         # [END_EXCLUDE]

#     def __repr__(self):
#         return(
#             f'City(\
#                 name={self.name}, \
#                 country={self.country}, \
#                 population={self.population}, \
#                 capital={self.capital}, \
#                 regions={self.regions}\
#             )'
#         )

# city = City(name=u'Los Angeles', state=u'CA', country=u'USA')
# db.collection(u'cities').document(u'LA').set(city.to_dict())
# Add a new doc in collection 'cities' with ID 'LA'
# db.collection(u'cities').document(u'LA').set(data)

# db.collection(u'cities').document(u'new-city-id').set(data)

# city = City(name=u'Tokyo', state=None, country=u'Japan')
# db.collection(u'cities').add(city.to_dict())

# def add_new_doc():
#     # [START add_new_doc]
#     # [START firestore_data_set_id_random_document_ref]
#     new_city_ref = db.collection(u'cities').document()

#     # later...
#     new_city_ref.set({
#         # ...
#     })
#     # [END firestore_data_set_id_random_document_ref]

# add_new_doc()

# def update_doc():
#     db.collection(u'cities').document(u'DC').set(
#         City(u'Washington D.C.', None, u'USA', True, 680000,
#              [u'east_coast']).to_dict())

#     # [START update_doc]
#     # [START firestore_data_set_field]
#     city_ref = db.collection(u'cities').document(u'DC')

#     # Set the capital field
#     city_ref.update({u'capital': True})
#     # [END firestore_data_set_field]
#     # [END update_doc]

# update_doc()

# city_ref = db.collection(u'cities').document(u'DC')

# # Set the capital field
# city_ref.update({u'capital': True})

# [START custom_class_def]
# [START firestore_data_custom_type_definition]
# class City(object):
#     def __init__(self, name, state, country, capital=False, population=0,
#                  regions=[]):
#         self.name = name
#         self.state = state
#         self.country = country
#         self.capital = capital
#         self.population = population
#         self.regions = regions

#     @staticmethod
#     def from_dict(source):
#         # [START_EXCLUDE]
#         city = City(source[u'name'], source[u'state'], source[u'country'])

#         if u'capital' in source:
#             city.capital = source[u'capital']

#         if u'population' in source:
#             city.population = source[u'population']

#         if u'regions' in source:
#             city.regions = source[u'regions']

#         return city
#         # [END_EXCLUDE]

#     def to_dict(self):
#         # [START_EXCLUDE]
#         dest = {
#             u'name': self.name,
#             u'state': self.state,
#             u'country': self.country
#         }

#         if self.capital:
#             dest[u'capital'] = self.capital

#         if self.population:
#             dest[u'population'] = self.population

#         if self.regions:
#             dest[u'regions'] = self.regions

#         return dest
#         # [END_EXCLUDE]

#     def __repr__(self):
#         return(
#             f'City(\
#                 name={self.name}, \
#                 country={self.country}, \
#                 population={self.population}, \
#                 capital={self.capital}, \
#                 regions={self.regions}\
#             )'
#         )
# # [END firestore_data_custom_type_definition]
# # [END custom_class_def]


# def add_example_data():
#     # [START add_example_data]
#     # [START firestore_data_get_dataset]
#     cities_ref = db.collection(u'cities')
#     cities_ref.document(u'BJ').set(
#         City(u'Beijing', None, u'China', True, 21500000, [u'hebei']).to_dict())
#     cities_ref.document(u'SF').set(
#         City(u'San Francisco', u'CA', u'USA', False, 860000,
#              [u'west_coast', u'norcal']).to_dict())
#     cities_ref.document(u'LA').set(
#         City(u'Los Angeles', u'CA', u'USA', False, 3900000,
#              [u'west_coast', u'socal']).to_dict())
#     cities_ref.document(u'DC').set(
#         City(u'Washington D.C.', None, u'USA', True, 680000,
#              [u'east_coast']).to_dict())
#     cities_ref.document(u'TOK').set(
#         City(u'Tokyo', None, u'Japan', True, 9000000,
#              [u'kanto', u'honshu']).to_dict())
#     # [END firestore_data_get_dataset]
#     # [END add_example_data]

# add_example_data()

# doc_ref = db.collection(u'cities').document(u'SF')

# # Get a document
# doc = doc_ref.get()
# if doc.exists:
#     print(f'Document data: {doc.to_dict()}')
# else:
#     print(u'No such document!')

# # Custom Objects - converts class into document
# doc_ref = db.collection(u'cities').document(u'BJ')

# doc = doc_ref.get()
# city = City.from_dict(doc.to_dict())
# print(city)

# # Get multiple documents
# docs = db.collection(u'cities').where(u'capital', u'==', True).stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

# # Get all documents
# docs = db.collection(u'cities').stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

# # Get Subcollections of Document
# collections = db.collection('cities').document('SF').collections()
# for collection in collections:
#     for doc in collection.stream():
#         print(f'{doc.id} => {doc.to_dict()}')


# [START custom_class_def]
# [START firestore_data_custom_type_definition]
class City(object):
    def __init__(self, name, state, country, capital=False, population=0,
                 regions=[]):
        self.name = name
        self.state = state
        self.country = country
        self.capital = capital
        self.population = population
        self.regions = regions

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        city = City(source[u'name'], source[u'state'], source[u'country'])

        if u'capital' in source:
            city.capital = source[u'capital']

        if u'population' in source:
            city.population = source[u'population']

        if u'regions' in source:
            city.regions = source[u'regions']

        return city
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'name': self.name,
            u'state': self.state,
            u'country': self.country
        }

        if self.capital:
            dest[u'capital'] = self.capital

        if self.population:
            dest[u'population'] = self.population

        if self.regions:
            dest[u'regions'] = self.regions

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            f'City(\
                name={self.name}, \
                country={self.country}, \
                population={self.population}, \
                capital={self.capital}, \
                regions={self.regions}\
            )'
        )
# [END firestore_data_custom_type_definition]
# [END custom_class_def]

# cities_ref = db.collection(u'cities')
# cities_ref.document(u'BJ').set(
#     City(u'Beijing', None, u'China', True, 21500000, [u'hebei']).to_dict())
# cities_ref.document(u'SF').set(
#     City(u'San Francisco', u'CA', u'USA', False, 860000,
#          [u'west_coast', u'norcal']).to_dict())
# cities_ref.document(u'LA').set(
#     City(u'Los Angeles', u'CA', u'USA', False, 3900000,
#          [u'west_coast', u'socal']).to_dict())
# cities_ref.document(u'DC').set(
#     City(u'Washington D.C.', None, u'USA', True, 680000,
#          [u'east_coast']).to_dict())
# cities_ref.document(u'TOK').set(
#     City(u'Tokyo', None, u'Japan', True, 9000000,
#          [u'kanto', u'honshu']).to_dict())

# [START get_simple_query]
# [START firestore_data_query]
# Note: Use of CollectionRef stream() is prefered to get()
docs = db.collection(u'cities').where(u'regions', u'array_contains', u'west_coast').stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
# [END firestore_data_query]
# [END get_simple_query]