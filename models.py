from .extensions import db


# Participant
class Participant(db.Model):
    id = db.Column(db.Integer,primary_key= True, identity= )
    participant_name = db.Column(db.String(50))

participant_table = db.Table('message_participant',
    db.Column('message_id',db.Integer,db.ForeignKey('Message.id'),primary_key=True),
    db.Column('participant_id',db.Integer,db.ForeignKey('Participant.id'),primary_key=True)
)

class A_Message(db.Model):
    id = db.Column(db.string(50),primary_key=True)
    messgaes = db.realationship('Message', backref='a_mmessage', lazy=True)

# Message
class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    application_id = db.Column(db.Integer)
    session_id = db.Column(db.String(50),unique= True) 
    message_id = db.Column(db.ForeignKey('A_Message.messages')) # This ForeignKey is to make possible to call the field- 'Message_Id' and have an 'id' field in addittion.
    content = db.Column(db.String(250))
    participants = db.realationship('Participant', secondary = participant_table, lazy = True,
                        backref=db.backref('message',lazy = True))

    def convert_to_json(self):    
        participants = []
        for participant in self.participants:
            participant.append(Participant.id)

        json = {
            'application_id' : self.application_id,
            'session_id' : self.session_id,
            'message_id' : self.message_id,
            'participants' : participants,
            'content' : self.content
            }   

        return json





