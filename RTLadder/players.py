from google.appengine.ext import ndb


class Player(ndb.Model):
    name = ndb.StringProperty()
    inviteToken = ndb.StringProperty(required=True)
    color = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)

    def __repr__(self):
        return str(self.key.id()) + " " + self.name