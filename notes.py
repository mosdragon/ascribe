import random
from users import field_userId

field_title = 'title'
field_content = 'content'
field_noteId = 'noteId'

class Note(object):

    def __init__(self, userId, title, content, noteId=None):
        if not userId:
                raise ValueError

        self.userId = int(userId)
        self.title = str(title)
        self.content = str(content)

        if noteId is None:
            noteId = random.randint(54321, 16171617)

        self.noteId = noteId


    def to_json(self):
        mynote = dict()

        mynote[field_userId] = self.userId
        mynote[field_title] = self.title
        mynote[field_content] = self.content
        mynote[field_noteId] = self.noteId

        return mynote

    @classmethod
    def from_json(constructor, myuser):

        userId = myuser[field_userId]
        title = myuser[field_title]
        content = myuser[field_content]
        noteId = myuser[field_noteId]

        return constructor(userId, title, content, noteId)
