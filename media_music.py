import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('music-in-media-firebase-adminsdk-ezcoo-a52d0e2da3.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

class Music(object):
    def __init__(self, title, artist, album, length=0, film=[],
                 tv=[]):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.film = film
        self.tv = tv

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        song = Music(source[u'title'], source[u'artist'], source[u'album'])

        if u'length' in source:
            song.length = source[u'length']

        if u'film' in source:
            song.film = source[u'film']

        if u'tv' in source:
            song.tv = source[u'tv']

        return song
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'title': self.title,
            u'artist': self.artist,
            u'album': self.album
        }

        if self.length:
            dest[u'length'] = self.length

        if self.film:
            dest[u'film'] = self.film

        if self.tv:
            dest[u'tv'] = self.tv

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            f'Music(\
                title={self.title}, \
                artist={self.artist}, \
                length={self.length}, \
                film={self.film}, \
                tv={self.tv}\
            )'
        )
# [END firestore_data_custom_type_definition]
# [END custom_class_def]

music_ref = db.collection(u'music')
music_ref.document(u'Heart of Courage').set(
    Music(u'Heart of Courage', u'Two Steps from Hell', u'Invincible', 117, None, [u'Mass Effect 2 Launch Trailer', u'The Pacific']).to_dict())
music_ref.document(u'Keep Yourself Warm').set(
    Music(u'Keep Yourself Warm', u'Frightened Rabbit', u'The Midnight Organ Fight', 333, None,
         [u'Chuck']).to_dict())
music_ref.document(u'How to Save a Life').set(
    Music(u'How to Save a Life', u'The Fray', u'How to Save a Life', 262, [u'The Blind Side'],
         [u'Scrubs']).to_dict())
music_ref.document(u'Sun and Stars').set(
    Music(u'Sun and Stars', u'Really Slow Motion', u'Elevation', 173, None,
         [u'Battlefield 1 - Trailer']).to_dict())        

# [START get_simple_query]
# [START firestore_data_query]
# Note: Use of CollectionRef stream() is prefered to get()
docs = db.collection(u'music').where(u'artist', u'==', u'Frightened Rabbit').stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
# [END firestore_data_query]
# [END get_simple_query]

def listen_document():
    # [START listen_document]
    # [START firestore_listen_document]

    # Create an Event for notifying main thread.
    # callback_done = threading.Event()

    # Create a callback on_snapshot function to capture changes
    def on_snapshot(doc_snapshot, changes, read_time):
        for doc in doc_snapshot:
            print(f'Received document snapshot: {doc.id}')
        # callback_done.set()

    doc_ref = db.collection(u'cities').document(u'SF')

    # Watch the document
    doc_watch = doc_ref.on_snapshot(on_snapshot)
    # [END firestore_listen_document]
    # [END listen_document]

listen_document()