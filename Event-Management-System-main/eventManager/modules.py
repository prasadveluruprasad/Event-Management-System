from . import db
from eventManager.data import user_data, event_data, book_data, review_data
from datetime import datetime
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random
import cv2 as cv

import pymysql
pymysql.install_as_MySQLdb()

class User(db.Model):
    """user table"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    payment = db.Column(db.String(128))
    balance = db.Column(db.Float)
    url = db.Column(db.String(64))
    bookings = db.relationship('Booked_event', backref='users')
    events = db.relationship('Event', backref='users')
    reviews = db.relationship('Review', backref='users')
    replies = db.relationship('Reply', backref='users')

    def __repr__(self):
        return "User object: name=%s, email=%s, password=%s, payment=%s" % self.name % self.email % self.password % self.payment


class Event(db.Model):
    '''event table'''
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(128))
    description = db.Column(db.String(2048))
    venue = db.Column(db.String(128))
    start_date = db.Column(db.DATETIME(32))
    end_date = db.Column(db.DATETIME(32))
    tickets_num = db.Column(db.Integer)
    ticket_price = db.Column(db.Float)
    tags = db.Column(db.String(64))
    url = db.Column(db.String(64))
    capacity = db.Column(db.String(32))
    row_num = db.Column(db.Integer)
    col_num = db.Column(db.Integer)
    status = db.Column(db.String(64))
    bookings = db.relationship('Booked_event', backref='events')
    reviews = db.relationship('Review', backref='events')
    
    def __repr__(self):
        return "Event object: hostid=%d, title=%s" % self.host_id % self.title

class Review(db.Model):
    '''review table'''
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String(128))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    # rating = db.Column(db.Integer)
    time = db.Column(db.DATETIME(32))
    replies = db.relationship('Reply', backref='reviews')

    def __repr__(self):
        return "Review object: userid=%d, eventid=%d" % self.user_id % self.event_id

class Reply(db.Model):
    '''reply table'''
    __tablename__ = 'replies'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    replyer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reply_to = db.Column(db.String(32))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    description = db.Column(db.String(128))
    time = db.Column(db.DATETIME(32))
    reply_to_time = db.Column(db.DATETIME(32))

    def __repr__(self):
        return "Reply object: replyerid=%d" % self.replyer_id

class Booked_event(db.Model):
    '''my_booking table'''
    __tablename__ = 'my_bookings'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    seats = db.Column(db.String(300))
    ticket_number = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    booked_time = db.Column(db.DATETIME(32))
    status = db.Column(db.String(32))


    def __repr__(self):
        return "My booking object: eventid=%d" % self.event_id

'''
simple bubble sort for array (format: [(a, num), (b, num) ... (n, num)])
'''
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] < arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

'''
sort recommendation by frequency, recommendation with more frequency will be displayed first
in 'you may also like'
'''
def sorted_reco(reco):
    result = []
    dict = {}
    for i in reco:
        dict[i] = reco.count(i)
    
    sorted_dict = sorted(dict.items(), key=lambda item:item[1], reverse = True)
    for i in sorted_dict:
        result.append(i[0])

    return result

'''
use random.sample() function flexiblely even if the number of events randomly chosen is out of index for the list
'''
def randomly_choose(list, n):
    if n < len(list):
        return random.sample(list, n)
    else:
        return list

'''
initialize row number of init_event (small = 5 rows, medium or large = 10 rows)
'''
def init_row_num(capacity):
    if capacity == 'small':
        return 5
    elif capacity == 'medium' or capacity == 'large':
        return 10

'''
initialize column number of init_event (small or medium = 5 cols, large = 10 cols)
'''
def init_col_num(capacity):
    if capacity == 'small' or capacity == 'medium':
        return 5
    elif capacity == 'large':
        return 10



'''
some functions about insert, delete, update, or search elements in database
'''
class Db_operations():

    '''
    initialize origin events, users, bookings and reviews
    '''
    @staticmethod
    def init_data():
        for i in range(len(user_data)):
            host = User(
                name = user_data[i]["name"],
                email = user_data[i]["email"],
                password = user_data[i]["password"],
                payment = user_data[i]["payment"],
                balance = 0,
                url = 'static/img/user_profile.png'
            )

            Db_operations.add_to_database(host)

        for i in range(len(event_data)):
            event = Event(
                host_id = event_data[i]["host_id"],
                title = event_data[i]["title"],
                description = event_data[i]["description"],
                venue = event_data[i]["venue"],
                start_date = event_data[i]["start_date"],
                end_date = event_data[i]["end_date"],
                ticket_price = event_data[i]["ticket_price"],
                tags = event_data[i]["tags"],
                url = event_data[i]["url"],
                capacity = event_data[i]["capacity"],
                row_num = init_row_num(event_data[i]["capacity"]),
                col_num = init_col_num(event_data[i]["capacity"]),
                tickets_num = init_row_num(event_data[i]["capacity"]) * init_col_num(event_data[i]["capacity"]),
                status = event_data[i]["status"]
            )
            Db_operations.add_to_database(event)
        
        for i in range(len(book_data)):
            booking = Booked_event(
                user_id = book_data[i]["user_id"],
                event_id = book_data[i]["event_id"],
                seats = book_data[i]["seats"],
                ticket_number = book_data[i]["ticket_number"],
                total_price = book_data[i]["total_price"],
                booked_time = book_data[i]["booked_time"],
                status = book_data[i]["status"]
            )
            Db_operations.add_to_database(booking)

        for i in range(len(review_data)):
            review = Review(
                user_id = review_data[i]["user_id"],
                description = review_data[i]["description"],
                event_id = review_data[i]["event_id"],
                time = review_data[i]["time"]
            )
            Db_operations.add_to_database(review)
            
            # resize all images to be of size 500 x 400
            img_path = "eventManager" + str(event_data[i]["url"][2:])
            img = cv.imread(img_path)
            resized = cv.resize(img, (500,400))
            cv.imwrite(img_path, resized)

    '''
    add new data to database
    '''
    @staticmethod
    def add_to_database(data):
        db.session.add(data)
        db.session.commit()

    '''
    count already booked tickets for current event
    '''
    @staticmethod
    def booked_tickets(event_id):
        bookings = Booked_event.query.filter_by(event_id=event_id).all()
        tickets = 0
        for booking in bookings:
            tickets += booking.ticket_number

        return tickets

    '''
    search the emails for all customers who booked this event
    '''
    @staticmethod
    def get_customers_emails(bookings):
        emails = []
        for booking in bookings:
            emails.append(booking.users.email)
        
        return emails

    '''
    refund the money back to all customers who booked this event, when the event had been cancelled by host
    '''
    @staticmethod
    def refund_money_to_customers(bookings):
        for booking in bookings:
            currBalance = User.query.filter_by(id=booking.user_id).first().balance
            currBalance = booking.total_price + currBalance
            Db_operations.update_data(User.query.filter_by(id=booking.user_id), "balance", currBalance)

    '''
    search all seats that had been already booked for current event
    '''
    @staticmethod
    def get_booked_seats(event_id):
        seats = ''
        bookings = Booked_event.query.filter_by(event_id=event_id).all()
        for booking in bookings:
            seats += booking.seats + ', '

        return seats

    '''
    create row array for each capacity
    '''
    @staticmethod
    def get_row(capacity):
        if capacity == 'small':
            return ['A', 'B', 'C', 'D', 'E']
        elif capacity == 'medium' or capacity == 'large':
            return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    '''
    create col array for each capacity
    '''
    @staticmethod
    def get_col(capacity):
        if capacity == 'small' or capacity == 'medium':
            return ['1', '2', '3', '4', '5']
        elif capacity == 'large':
            return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    '''
    host cancel event
    '''
    @staticmethod
    def cancel_event(event_id):
        Event.query.filter_by(id=event_id).update({"status":"cancelled"})
        db.session.commit()

    '''
    host delete event from its history
    '''
    @staticmethod
    def delete_event(event_id):
        Event.query.filter_by(id=event_id).update({"status":"deleted"})
        db.session.commit()

    '''
    check whether current user had already left a review for current event or not
    '''
    @staticmethod
    def already_leave_review(event_id, user_id):
        reviews = Review.query.filter_by(event_id=event_id).all()
        for review in reviews:
            if review.user_id == user_id:
                return True
        
        return False

    '''
    update data in database
    '''
    @staticmethod
    def update_data(type, attribute, new):
        type.update({attribute:new})
        db.session.commit()

    '''
    delete data in database
    '''
    @staticmethod
    def delete_data(data):
        db.session.delete(data)
        db.session.commit()

    '''
    search all events cancelled by hosts or customers
    '''
    @staticmethod
    def get_cancelled_bookings(bookings):
        result = []
        for booking in bookings:
            if "cancelled" in booking.status:
                result.append(booking)
        
        return result

    '''
    customer cancel booking
    '''
    @staticmethod
    def cancel_booking_by_customer(booked_time):
        Booked_event.query.filter_by(booked_time=booked_time).update({"status":"cancelled by customer"})
        db.session.commit()

    '''
    host cancel booking
    '''
    @staticmethod
    def cancel_booking_by_host(event_id):
        Booked_event.query.filter_by(event_id=event_id).update({"status":"cancelled by host"})
        db.session.commit()

    '''
    check whether some events are ended or not
    '''
    @staticmethod
    def event_ending_authentication(events):
        if type(events) == type([]):
            for event in events:
                if event.end_date <= datetime.now() and event.status == "upcoming":
                    # update event
                    Event.query.filter_by(id=event.id).update({"status":"finished"})
                    db.session.commit()

                    # update booking
                    if Booked_event.query.filter_by(event_id=event.id) != []:
                        Booked_event.query.filter_by(event_id=event.id).update({"status":"finished"})
                        db.session.commit()
        
        else:
            if events.end_date <= datetime.now() and events.status == "upcoming":
                # update event
                Event.query.filter_by(id=events.id).update({"status":"finished"})
                db.session.commit()

                # update booking
                if Booked_event.query.filter_by(event_id=events.id) != []:
                    Booked_event.query.filter_by(event_id=events.id).update({"status":"finished"})
                    db.session.commit()

    '''
    check whether the email has been used by others or not when sign up
    '''
    @staticmethod
    def sign_up_email_authentication(email):
        result = User.query.filter_by(email=email).all()
        if result == []:
            return True
        else:
            return False

    '''
    check whether user typed correct email and password or not when sign in
    '''
    @staticmethod
    def sign_in_email_authentication(email, password):
        result = User.query.filter_by(email=email).all()
        if result == []:
            return False
        else:
            if result[0].password != password:
                return False
        return True

    '''
    check whether the start date is before end date or not of the advertised event
    '''
    @staticmethod
    def advertise_date_authentication(start_date, end_date):
        if start_date < end_date:
            return True
        else:
            return False

    '''
    check whether current user has booked current event or not
    '''
    @staticmethod
    def already_booked(event_id, user_id):
        bookings = Booked_event.query.filter_by(event_id=event_id).all()
        for booking in bookings:
            if booking.user_id == user_id and 'cancelled' not in booking.status:
                return True
        
        return False

    '''
    randomly recommendation for all users click into any event
    '''
    @staticmethod
    def get_recommendation_with_event_selected(event_id):
        # when the user click into any event, there will be multiple recommendations which are the same tag as the event it chose
        reco = []
        events = Event.query.all()
        curr_event = Event.query.filter_by(id=event_id).first()

        for event in events:
            if event.tags == curr_event.tags:
                reco.append(event)

        return randomly_choose(reco, 4)

    '''
    create the designed recommendation about the same host_id, same type, and similar description events for all users
    '''
    @staticmethod
    def get_recommendation_with_event_booked(user_id):
        booked_event = Booked_event.query.filter_by(user_id=user_id).all()
        booked_events = []
        for booking in booked_event:
            if booking.status != 'cancelled by customer':
                booked_events.append(booking)
        
        # if current user hasn't booked a event yet, then no recommendation.
        if booked_events == []:
            return []

        booked_tags = []
        booked_hosts = []
        booked_des = []
        tags_reco = []  # recommendation for same tags
        host_reco = []  # recommendation for same host id
        des_reco = []   # recommendation for similar description

        for booking in booked_events:
            booked_tags.append(booking.events.tags)
            booked_hosts.append(booking.events.host_id)
            booked_des.append(booking.events.description)

        events = Event.query.all()
        events_des_dict = {}    # store description to its corresponding event_id
        events_des = []         # description for all events to calculate edit distance
        
        for event in events:
            events_des.append(event.description)
            events_des_dict[event.description] = event.id
            
            if event.tags in booked_tags:
                tags_reco.append(event)
            
            if event.host_id in booked_hosts:
                host_reco.append(event)

        top_des = []
        for des in booked_des:
            top_des += process.extract(des, events_des, limit=3)
        
        bubbleSort(top_des)

        # choose top 3 description which are more similar to booked event
        for i in range(3):
            event_id = events_des_dict[top_des[i][0]]
            event = Event.query.filter_by(id=event_id).first()
            des_reco.append(event)

        all_reco = randomly_choose(tags_reco, 2) + randomly_choose(host_reco, 2) + des_reco   # recommendate randomly by tag
        recommendation = sorted_reco(all_reco)                                                  # sorted by frequency

        return recommendation

    '''
    search events for title, description or type
    '''
    @staticmethod
    def search_events(title, des, music, food, education, company, more, input, events):
        result = []
        music_events = []
        food_events = []
        education_events = []
        company_events = []
        more_events = []
        type_filter = 'off'

        if music == 'on':
            music_events = Event.query.filter_by(tags='Music').all()
            type_filter = 'on'
        
        if food == 'on':
            food_events = Event.query.filter_by(tags='Foods & Drinks').all()
            type_filter = 'on'

        if education == 'on':
            education_events = Event.query.filter_by(tags='Education').all()
            type_filter = 'on'

        if company == 'on':
            company_events = Event.query.filter_by(tags='Company').all()
            type_filter = 'on'
        
        if more == 'on':
            more_events = Event.query.filter_by(tags='Others').all()
            type_filter = 'on'

        if type_filter == 'on':
            filted_events = music_events + food_events + education_events + company_events + more_events
            for event in filted_events:
                if title == 'on':
                    if input.lower() in event.title.lower() and event not in result:
                        result.append(event)

                if des == 'on':
                    if input.lower() in event.description.lower() and event not in result:
                        result.append(event)
                
                if title == None and des == None:
                    if input.lower() in event.description.lower() or input.lower() in event.title.lower():
                        result.append(event)

        else:
            for event in events:
                if title == 'on':
                    if input.lower() in event.title.lower() and event not in result:
                        result.append(event)

                if des == 'on':
                    if input.lower() in event.description.lower() and event not in result:
                        result.append(event)

                if title == None and des == None:
                    if input.lower() in event.description.lower() or input.lower() in event.title.lower():
                        result.append(event)

        return result

    '''
    check if a string is number type
    '''
    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

# filename : eventManager/modules.py
# (Keep all your existing imports and code above this. Make sure 'requests' is imported!)

# ... (your existing imports, like from . import db, from eventManager.data import ...)
from . import db
from eventManager.data import user_data, event_data, book_data, review_data
from datetime import datetime
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random
import cv2 as cv

import pymysql
pymysql.install_as_MySQLdb()

# >>> START: Changed AI related imports and class (using requests) <<<
# REMOVE: from huggingface_hub import InferenceClient
# REMOVE: from openai import OpenAI
# ADD:
import requests # <-- Make sure this is imported!
import os 
# >>> END: Changed AI related imports and class <<<

# ... (your existing User, Event, Review, Reply, Booked_event, Db_operations models and classes) ...

# >>> START: AI_Operations Class (Updated to use RapidAPI with requests) <<<
class AI_Operations:
    '''
    Class for AI-related operations using a RapidAPI endpoint for GPT-like models.
    '''
    @staticmethod
    def get_chat_completion(user_message: str):
        """
        Sends a message to the specified RapidAPI endpoint and returns the response.
        """
        # Your RapidAPI key and host
        RAPIDAPI_KEY = "bedfd2e2d1mshe54779f69714142p15bf88jsndbe0289456d2"
        RAPIDAPI_HOST = "chat-gpt26.p.rapidapi.com"
        
        # The URL for the RapidAPI endpoint
        url = "https://chat-gpt26.p.rapidapi.com/"

        if not RAPIDAPI_KEY:
            print("RapidAPI key not found. Please ensure it's set.")
            return "Sorry, the AI service is not configured correctly."

        try:
            payload = {
                "model": "GPT-4.1-Mini", # As specified in your example
                "messages": [
                    {
                        "role": "user",
                        "content": user_message # Use the user's actual message from the form
                    }
                ]
            }
            headers = {
                "x-rapidapi-key": RAPIDAPI_KEY,
                "x-rapidapi-host": RAPIDAPI_HOST,
                "Content-Type": "application/json"
            }

            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)

            # Assuming the response structure is similar to OpenAI's chat completions
            # You might need to inspect the actual response.json() to confirm this.
            response_data = response.json()
            
            # This is the expected path based on standard chat completion APIs
            if 'choices' in response_data and response_data['choices']:
                first_choice = response_data['choices'][0]
                if 'message' in first_choice and 'content' in first_choice['message']:
                    return first_choice['message']['content']
                else:
                    print(f"Unexpected API response structure: {response_data}")
                    return "Sorry, I received an unexpected response from the AI."
            else:
                print(f"No choices found in API response: {response_data}")
                return "Sorry, the AI did not provide a complete response."

        except requests.exceptions.RequestException as req_e:
            print(f"Network or API connection error: {req_e}")
            return "Sorry, there was a network issue connecting to the AI service. Please try again."
        except Exception as e:
            print(f"General error calling AI API: {e}") 
            return "Sorry, I couldn't process your request at this moment. Please try again later."
# >>> END: AI_Operations Class (Updated) <<<

# ... (rest of your modules.py code) ...