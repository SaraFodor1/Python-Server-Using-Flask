from flask import jsonify, request, redirect, url_for, render_template, make_response, Blueprint #,Flask
from .models import Message, A_Message, Participant
from .extensions import db


main= Blueprint('main',__name__)


@main.route('/')
def index():
    return '<h1>hello<!h1>'

@main.route('/json')
def json():
    return jsonify({'MyKey' : 'JSON value!' , 'MyList' : [1,2,3,4,5]})

# Add_Message
@main.route('/Add_Message', methods=['POST'])
def add_message():
    req_data = request.get_json() #Getting the json object from postmen
    api_input = req_data['data']

    # session_id needs to be uniqe, check if alreadu exsists
    check_session = Message.query.filter_by(session_id=request.get_json('session_id')).first()
    if check_session is not None
        return make_response(jsonify({'Result':'Session ID must be uniqe. This one is already exsists'}),404)

    # message_id needs to be uniqe, check if alreadu exsists
    check_message = A_Message.query.filter_by(id=request.get_json('message_id')).first()
    if check_message is not None
        return make_response(jsonify({'Result':'Message ID must be uniqe. This one is already exsists'}),404)
    
    check_message = A_Message(id= request.get_json('message_id'))   
    db.session.add(check_message)

    participants = []
    for prtc in request.get_json('participants'):
        new_prtc = Participant.query.filter_by(participant_name=prtc).first()
        if new_prtc is None
            new_prtc = Participant(participant_name = prtc)
            db.session.add(new_prtc)
        participants.append(new_prtc)

    new_message = Message(
        application_id= request.get_json('application_id')
        session_id= request.get_json('session_id')
        message_id= check_message 
        participants= participants
        content= request.get_json('content')

    )

    db.session.add(new_message)
    db.session.commit()

    return make_response(jsonify({'Result':'Message recieved!','data': api_input}),200)


#Get_Message
@main.route('/Get_Message')
def get_message():
    applicationID = request.args.get('applicationID')
    sessionID = request.args.get('sessionID')
    messageID = request.args.get('messageID')


    listOfMessages=[]
     
    if applicationID is not None and None in (sessionID,messageID): #list of messages with this applicationID
        listOfMessages = Message.query.filter_by(application_id=applicationID)

    elif sessionID is not None and None in (applicationID,messageID):#list of messages with this sessionID
        listOfMessages = Message.query.filter_by(session_id=sessionID)

    elif messageID is not None and None in (applicationID,sessionID): # return only 1 message wuth this message_ID
        result = Message.query.filter_by(message_id=messageID).first()
        if result is not None
            return make_response(jsonify({'The message is':[result.convert_to_json()]}),200)

    if listOfMessages.count()!=0 
        return make_response(jsonify({'The messages are:': [result.convert_to_json() for result in listOfMessages]}),200)
    else 
        return make_response(jsonify({'Result':'There is no message with this parameter'}),404)
    
    return (make_response(jsonify({'Result':'Failed'}),404)) # if no parameters entered
    



#Delete_Message
@main.route('/Delete_Message',methods=['DELETE'])
def delete_message():
    applicationID = request.args.get('applicationID')
    sessionID = request.args.get('sessionID')
    messageID = request.args.get('messageID')


    if applicationID is not None and None in (sessionID,messageID): #delete all messages with this applicationID
        messages_to_delete = Message.query.filter_by(application_id=applicationID)

    elif sessionID is not None and None in (applicationID,messageID):#delete all messages with this sessionID
        messages_to_delete = Message.query.filter_by(session_id=sessionID)

    elif messageID is not None and None in (applicationID,sessionID): # delete the only 1 message wuth this message_ID
        messages_to_delete = Message.query.filter_by(message_id=messageID).first()
    
    if messages_to_delete is not None

        for msg in messages_to_delete:
            ms = A_Message.query.filter_by(id=msg.message_id).first()
            # no need to delete related records in the participant_table (the many to many relationship table)
            # because a special behavior of the relationship.secondary argument, that the Table is automatically
            # subject to INSERT and DELETE statements, as objects are added or removed from the collection.
            db.session.delete(ms)
            db.session.delete(msg)
            db.session.commit()

        return make_response('Succesfully deleted',200)
    
    return (make_response(jsonify({'Result':'Failed'}),404)) # if no parameters entered or messages not exists











