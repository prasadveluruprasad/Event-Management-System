# coding:utf-8
import time

from eventManager import create_app, create_database
from eventManager.modules import User, Event, Booked_event, Review, Reply, Db_operations
from eventManager.send_email import send
from flask import render_template, request, session, redirect, url_for, flash
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo
import os
import copy
import random

import cv2 as cv

from flask import render_template, request, redirect, url_for, session, flash # Make sure flash is imported
from . import create_app, db # Assuming db and create_app are defined in your __init__.py
from .modules import Db_operations, AI_Operations # >>> IMPORT AI_Operations <<<
# >>> START: New AI related imports and class <<<
from huggingface_hub import InferenceClient
import os # For robust API key handling (though hardcoded for this example)
# >>> END: New AI related imports and class <<<
# create app
app = create_app("develop")


# create WTForms for getting user input from webpage
class reviewForm(FlaskForm):
    description = TextAreaField(label="Review", id="review box", validators=[DataRequired("Type your reviews")])

    submit = SubmitField(label="submit",id="review_button")

class replyForm(FlaskForm):
    description = TextAreaField(label="Reply", validators=[DataRequired("Type your replies")])

    submit = SubmitField(label="post")

# define the route for home page
@app.route("/", methods=['GET', 'POST'])
def index():
    # test if database is correctly connected
    first_init = create_database()
    if first_init:
        Db_operations.init_data()
    username = session.get('username')
    email = session.get('email')
    user = User.query.filter_by(email=email).first()
    event = Event.query.all()
    event = title_description_spacing(event)
    popular = [] 
    popular.append(Event.query.filter_by(id=8).first())
    popular.append(Event.query.filter_by(id=20).first())
    popular.append(Event.query.filter_by(id=5).first())
    popular.append(Event.query.filter_by(id=9).first())
    Db_operations.event_ending_authentication(event)

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        music = request.form.get('music')
        food = request.form.get('food')
        education = request.form.get('education')
        company = request.form.get('company')
        more = request.form.get('more')
        search_input = request.form.get('searchInput')
        result = Db_operations.search_events(title, description, music, food, education, company, more, search_input, event)
        result = title_description_spacing(result)
        if request.method == 'POST' and len(result) == 0:
            
            return render_template('no_matching.html')

        return render_template("search_results.html", user=user, username=username, event=result)

    return render_template("index.html", user=user, username=username, event=event, popular=popular)

#define the route for search result diplay page
@app.route("/search_results", methods=['GET', 'POST'])
def search_results():
    username = session.get('username')
    email = session.get('email')
    user = User.query.filter_by(email=email).first()

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        music = request.form.get('music')
        food = request.form.get('food')
        education = request.form.get('education')
        company = request.form.get('company')
        more = request.form.get('more')
        search_input = request.form.get('searchInput')
        result = Db_operations.search_events(title, description, music, food, education, company, more, search_input, event)
        result = title_description_spacing(result)
        if request.method == 'POST' and len(result) == 0:
            
            return render_template('no_matching.html')

        return render_template("search_results.html", user=user, username=username, event=result)
    
    return render_template("search_results.html", user=user, username=username, event=result)

# this function is used to change the length of event title and event description
def title_description_spacing(events):
    # solving db trivial bug
    for i in events:
        i.title = i.title
    event = copy.deepcopy(events)
    string = "(Come and join us! This is going to be fun and interesting.You, of course will like it! )"
    for i in event:
        if len(i.title) > 29:
            i.title = i.title[0:30] + "..."
        if len(i.title) <= 29:
            i.title = i.title + " " + string[0:30 - len(i.title)]

        if len(i.description) > 50:
            i.description = i.description[0:50] + "..."
        if len(i.description) <= 50:
            i.description = i.description + " " + string[0:50 - len(i.description)]
    return event

# define the route for personal profile page
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    email = session.get('email')
    user = User.query.filter_by(email=email).first()

    if request.method == 'POST':

        bankcard = request.form.get('bankcard')
        money = request.form.get('money')
        bankcard_no = str(bankcard).replace(' ', '')

        if bankcard is not None:
            if (not Db_operations.is_number(bankcard_no)) or (len(bankcard_no) != 16):
                return render_template('profile.html', user=user, username=user.name,
                                           msg="Please enter a valid bank card number with 16 digits!")
        if money is not None:
            if not Db_operations.is_number(money):
                return render_template('profile.html', user=user, username=user.name,
                                       msg="Please enter a valid number!")

            if float(money) < 0:
                return render_template('profile.html', user=user, username=user.name,
                                       msg="Please enter a positive number!")

        if money is None:
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            Url = ".." + os.path.join(app.config['UPLOAD_FOLDER'], filename)[12:]

            # resize all images to be of size 500 x 400
            img_path = "eventManager/static/img/" + filename
            img = cv.imread(img_path)
            resized = cv.resize(img, (400, 400))
            cv.imwrite(img_path, resized)

            # update to database
            Db_operations.update_data(User.query.filter_by(email=email), "url", Url)

        else:
            # update to database
            Db_operations.update_data(User.query.filter_by(email=email), "balance", user.balance + float(money))

        return redirect(url_for('profile'))

    return render_template('profile.html', user=user, username=user.name)

#define the route for company event page
@app.route("/company_event", methods=['GET', 'POST'])
def show_company_event():
    username = session.get('username')
    user = User.query.filter_by(email=session.get('email')).first()
    events = Event.query.filter_by(tags="Company").all()
    Db_operations.event_ending_authentication(events)
    event = title_description_spacing(events)
    return render_template('company_event.html', user=user, username=username, event=event)

#define the route for food event page
@app.route("/food_event", methods=['GET', 'POST'])
def show_food_event():
    username = session.get('username')
    user = User.query.filter_by(email=session.get('email')).first()
    events = Event.query.filter_by(tags="Foods & Drinks").all()
    Db_operations.event_ending_authentication(events)
    events = title_description_spacing(events)
    return render_template('food_event.html', user=user, username=username, event=events)

#define the route for educationl event page
@app.route("/education_event", methods=['GET', 'POST'])
def show_education_event():
    username = session.get('username')
    user = User.query.filter_by(email=session.get('email')).first()
    events = Event.query.filter_by(tags="Education").all()
    Db_operations.event_ending_authentication(events)
    event = title_description_spacing(events)
    return render_template('education_event.html', user=user, username=username, event=event)

#define the route for musical event page
@app.route("/music_event", methods=['GET', 'POST'])
def show_music_event():
    username = session.get('username')
    user = User.query.filter_by(email=session.get('email')).first()
    events = Event.query.filter_by(tags="Music").all()
    Db_operations.event_ending_authentication(events)
    events = title_description_spacing(events)
    return render_template('music_event.html', user=user, username=username, event=events)

#define the route for other types of event page
@app.route("/more_event", methods=['GET', 'POST'])
def show_more_event():
    username = session.get('username')
    user = User.query.filter_by(email=session.get('email')).first()
    events = Event.query.filter_by(tags="Others").all()
    Db_operations.event_ending_authentication(events)
    events = title_description_spacing(events)
    return render_template('more_event.html', user=user, username=username, event=events)

#define the route for sign up page
@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        new_name = request.form['username']
        new_email = request.form['email']
        new_password = request.form['password']
        new_payment = request.form['payment']

        bankcard_no = str(new_payment).replace(' ', '')

        if new_payment is not None:
            if (not Db_operations.is_number(bankcard_no)) or (len(bankcard_no) != 16):
                return render_template('sign_up.html', msg="Sorry, please enter a valid bankcard number with 16 digits!")

        if Db_operations.sign_up_email_authentication(new_email):
            new_user = User(name=new_name, email=new_email, password=new_password, payment=new_payment, balance = 0, 
                                url = 'static/img/user_profile.png')
            Db_operations.add_to_database(new_user)
            session['username'] = new_name
            session['id'] = User.query.filter_by(email=new_email).first().id
            session['email'] = new_email
        else:
            return render_template('sign_up.html', msg="Sorry, the email has been used!")

        return redirect(url_for('index'))

    return render_template('sign_up.html')

#define the route for sign in page
@app.route("/sign_in", methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':

        Email = request.form['email']
        Password = request.form['password']

        if Db_operations.sign_in_email_authentication(Email, Password):
            session['username'] = User.query.filter_by(email=Email).first().name
            session['id'] = User.query.filter_by(email=Email).first().id
            session['email'] = Email
            return redirect(url_for('index'))
        else:
            return render_template('sign_in.html', msg="Sorry, incorrect email or password ")

    return render_template('sign_in.html')

#define the route for my event page
@app.route("/my_events", methods=['GET', 'POST'])
def my_events():
    Host_id = User.query.filter_by(email=session.get('email')).first().id
    event = Event.query.filter_by(host_id=Host_id).all()
    Db_operations.event_ending_authentication(event)
    user = User.query.filter_by(email=session.get('email')).first()
    upcoming_event = Event.query.filter_by(host_id=Host_id, status="upcoming").all()
    cancelled_event = Event.query.filter_by(host_id=Host_id, status="cancelled").all()
    finished_event = Event.query.filter_by(host_id=Host_id, status="finished").all()



    if request.method == 'POST':

        Title = request.form['title']
        Description = request.form['description']
        Venue = request.form['venue']
        Start_date = request.form['start']
        End_date = request.form['end']
        Ticket_price = request.form['price']
        Tags = request.form['tag']
        file = request.files['file']
        capacity = request.form['capacity']
        row_num = len(Db_operations.get_row(capacity))
        col_num = len(Db_operations.get_col(capacity))
        Tickets_num = row_num * col_num

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        Url = ".." + os.path.join(app.config['UPLOAD_FOLDER'], filename)[12:]

        # resize all images to be of size 500 x 400
        img_path = "eventManager/static/img/" + filename
        img = cv.imread(img_path)
        resized = cv.resize(img, (500, 400))
        cv.imwrite(img_path, resized)
        curr_time = time.strftime("%Y-%m-%dT%H:%M", time.localtime())

        if Ticket_price is not None:
            if not Db_operations.is_number(Ticket_price):
                return render_template('my_events.html', user=user, username=user.name, event=event,
                                   upcoming_event=upcoming_event,
                                   cancelled_event=cancelled_event, finished_event=finished_event,
                                   msg="Sorry, the ticket price must be a number!")

            if float(Ticket_price) < 0:
                return render_template('my_events.html', user=user, username=user.name, event=event,
                                   upcoming_event=upcoming_event,
                                   cancelled_event=cancelled_event, finished_event=finished_event,
                                   msg="Sorry, please enter a positive number for ticket price!")


        if Start_date < curr_time:
            return render_template('my_events.html', user=user, username=user.name, event=event,
                                   upcoming_event=upcoming_event,
                                   cancelled_event=cancelled_event, finished_event=finished_event,
                                   msg="The start time must after the current time!")

        if Start_date > End_date:
            return render_template('my_events.html', user=user, username=user.name, event=event,
                                   upcoming_event=upcoming_event,
                                   cancelled_event=cancelled_event, finished_event=finished_event, msg="The start time must before the end time!")

        else:
            new_event = Event(host_id=Host_id, title=Title, description=Description, venue=Venue, start_date=Start_date, capacity=capacity,
                              end_date=End_date,tickets_num=Tickets_num, ticket_price=Ticket_price, tags=Tags, url=Url, row_num=row_num,
                              col_num=col_num,status="upcoming")

            Db_operations.add_to_database(new_event)

        return redirect(url_for('my_events'))

    return render_template('my_events.html', user=user, username=user.name, event=event, upcoming_event=upcoming_event, 
                            cancelled_event=cancelled_event, finished_event=finished_event)


#define the route for a page for showing only upcoming events
@app.route("/events_upcoming_filter")
def events_upcoming_filter():
    Host_id = User.query.filter_by(email=session.get('email')).first().id
    event = Event.query.filter_by(host_id=Host_id, status="upcoming").all()
    user = User.query.filter_by(email=session.get('email')).first()

    return render_template('my_events.html', user=user, username=user.name, event=event)

#define the route for a page for showing only canceled events
@app.route("/events_cancel_filter")
def events_cancel_filter():
    Host_id = User.query.filter_by(email=session.get('email')).first().id
    event = Event.query.filter_by(host_id=Host_id, status="cancelled").all()
    user = User.query.filter_by(email=session.get('email')).first()

    return render_template('my_events.html', user=user, username=user.name, event=event)


#define the route for my bookings page
@app.route("/my_bookings", methods=['POST', 'GET'])
def my_bookings():
    user_id = session.get('id')
    user = User.query.filter_by(email=session.get('email')).first()
    booked_events = Booked_event.query.filter_by(user_id=user_id).all()
    upcoming_events = Booked_event.query.filter_by(user_id=user_id, status="upcoming").all()
    cancelled_events = Db_operations.get_cancelled_bookings(booked_events)
    finished_events = Booked_event.query.filter_by(user_id=user_id, status="finished").all()
    recommendation = Db_operations.get_recommendation_with_event_booked(user_id)
    reco = title_description_spacing(recommendation)

    return render_template('my_bookings.html', user=user, upcoming_events=upcoming_events, cancelled_events=cancelled_events,
                            finished_events=finished_events, username=session.get('username'), curr_time=datetime.now(), 
                            reco=reco)


#define the route for logout function, back to hompage after log out
@app.route("/logout")
def logout():
    session['username'] = None
    return redirect(url_for('index'))

#define the route for booking event page
@app.route('/book_event:<id>', methods=['GET', 'POST'])
def book_event(id):
    username = session.get('username')
    event = Event.query.filter_by(id=id).first()
    Db_operations.event_ending_authentication(event)
    user_id = session.get('id')
    user = User.query.filter_by(email=session.get('email')).first()
    available_tickets = event.tickets_num - Db_operations.booked_tickets(event.id)
    reviews = Review.query.filter_by(event_id=event.id).all()
    replies = Reply.query.filter_by(event_id=event.id).all()
    already_leave_review = Db_operations.already_leave_review(event.id, user_id)
    already_booked = Db_operations.already_booked(event.id, user_id)
    recommendation = Db_operations.get_recommendation_with_event_selected(event.id)
    booked_time = str(datetime.now())[:19]
    size = 100 / event.col_num
    row = Db_operations.get_row(event.capacity)
    col = Db_operations.get_col(event.capacity)
    booked_seats = Db_operations.get_booked_seats(event.id)

    # when click submit button
    rvForm = reviewForm()
    if rvForm.validate_on_submit():
        des = rvForm.description.data
        review = Review(user_id=user_id, description=des, event_id=event.id, time=booked_time)
        Db_operations.add_to_database(review)

        return redirect(url_for('book_event', id=id))
    
    # when click reply button
    rpForm = replyForm()

    if request.method == 'POST':
        seat = request.form['seat']
        if seat != '':
            ticket_number = request.form['ticket_number']
            total = event.ticket_price * int(ticket_number)


            if total > user.balance:
                return render_template("booking_event.html", user=user, event=event, username=username,
                                available_tickets=available_tickets, size=size, row_len=event.row_num, col_len=event.col_num,
                                msg="Sorry! You do not have enough money", rvForm=rvForm, row=row, col=col, booked_seats=booked_seats,
                                reviews=reviews, rpForm=rpForm, replies=replies, review_len=len(reviews), reply_len=len(replies),
                                already_leave_review=already_leave_review, already_booked=already_booked, reco=recommendation)


            booking = Booked_event(event_id=id, user_id=user_id, seats=seat, ticket_number=ticket_number, total_price=total,
                                   booked_time=booked_time, status="upcoming")

            Db_operations.add_to_database(booking)
            Db_operations.update_data(User.query.filter_by(id=user_id), "balance", user.balance - total)

            # send booking confirmation to current customer
            msg1 = 'Dear %s, <br><br>' % username
            msg2 = 'You have successfully booked this event, event details are shown below: <br>'
            msg3 = 'event title: %s <br>' % event.title
            msg4 = 'host name: %s <br>' % event.users.name
            msg5 = 'start time: %s <br>' % event.start_date
            msg6 = 'end time: %s <br>' % event.end_date
            msg7 = 'venue: %s <br>' % event.venue
            msg8 = 'please notice that you cannot cancel it if there are less than 7 days from the start of the event.'
            msg = msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7 + msg8
            send(msg, 'booking confirmation', [session.get('email')])

            return redirect(url_for('my_bookings'))


    return render_template("booking_event.html", user=user, event=event, username=username, available_tickets=available_tickets,
                             size=size, row_len=event.row_num, col_len=event.col_num, row=row, col=col, rvForm=rvForm, rpForm=rpForm,
                                reviews=reviews, user_id=user_id, replies=replies, review_len=len(reviews), reply_len=len(replies), 
                                    already_leave_review=already_leave_review, already_booked=already_booked, reco=recommendation,
                                        booked_seats=booked_seats)


#define the route for a page for sending email
@app.route('/send_email:<id>', methods=['GET', 'POST'])
def send_email(id):
    user = User.query.filter_by(email=session.get('email')).first()
    event = Event.query.filter_by(id=id).first()
    bookings = Booked_event.query.filter_by(event_id=id).all()
    emails = Db_operations.get_customers_emails(bookings)

    if request.method == 'POST':
        subject = request.form['subject']
        msg = 'You have received an email from %s, ' % event.users.name
        msg += 'who is the host for %s: <br> <br>' % event.title
        msg += request.form['message']
        msg += '<br> if you have any further question, you can contact with the email of this host: %s' % event.users.email
        send(msg, subject, emails)

        return render_template('confirmation.html')

    return render_template('send_email.html', username=session.get('username'), user=user, id=id)


#define a route and a function for customer cancels booked event
@app.route('/customer_cancel', methods=['POST', 'GET'])
def customer_cancel():
    booked_time = request.args.get('booked_time')
    booking = Booked_event.query.filter_by(booked_time=booked_time).first()
    currBalance = User.query.filter_by(id=booking.user_id).first().balance
    currBalance = booking.total_price + currBalance
    Db_operations.update_data(User.query.filter_by(id=booking.user_id), "balance", currBalance)
    Db_operations.cancel_booking_by_customer(booked_time)

    return redirect(url_for('my_bookings'))

# #define a route and a function for host cancels advertised event
@app.route('/host_cancel', methods=['POST', 'GET'])
def host_cancel():
    event_id = request.args.get('event_id')
    event = Event.query.filter_by(id=event_id).first()
    bookings = Booked_event.query.filter_by(event_id=event_id).all()
    emails = Db_operations.get_customers_emails(bookings)
    Db_operations.refund_money_to_customers(bookings)
    msg1 = 'Sorry, your booked event has been cancelled by its host for some reason: <br>'
    msg2 = 'event title: %s <br>' % event.title
    msg3 = 'host name: %s <br>' % event.users.name
    msg4 = 'start time: %s <br>' % event.start_date
    msg5 = 'end time: %s <br>' % event.end_date
    msg6 = 'venue: %s <br>' % event.venue
    msg7 = 'Booking fee has been returned to your account recently.'
    msg = msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7
    Db_operations.cancel_booking_by_host(event_id)
    Db_operations.cancel_event(event_id)
    send(msg, 'event cancellation', emails)

    return redirect(url_for('my_events'))

#define a route and a function for customer deletes booked event
@app.route('/customer_delete', methods=['POST', 'GET'])
def customer_delete():
    booked_time = request.args.get('booked_time')
    booking = Booked_event.query.filter_by(booked_time=booked_time).first()

    Db_operations.delete_data(booking)
    return redirect(url_for('my_bookings'))

#define a route and a function for host deletes booked event
@app.route('/host_delete', methods=['POST', 'GET'])
def host_delete():
    event_id = request.args.get('event_id')
    Db_operations.delete_event(event_id)

    return redirect(url_for('my_events'))

#define a route and a function for host replys to customer comments
@app.route('/reply_to_review', methods=['POST', 'GET'])
def reply_to_review():
    user_id = session.get('id')
    id = request.args.get('id')
    temp = id.split('?')
    rpForm = replyForm()
    des = rpForm.description.data
    review = Review.query.filter_by(event_id=temp[0], time=temp[1]).first()
    reply = Reply(event_id=temp[0], replyer_id=user_id, description=des, review_id=review.id, reply_to=review.users.name, time=str(datetime.now())[:19],
                    reply_to_time=review.time)
    Db_operations.add_to_database(reply)  

    return redirect(url_for('book_event', id=temp[0]))

#define a route and a function for customers to reply to others replies
@app.route('/reply_to_reply', methods=['POST', 'GET'])
def reply_to_reply():
    user_id = session.get('id')
    id = request.args.get('id')
    temp = id.split('?')
    rpForm = replyForm()
    des = rpForm.description.data
    review = Review.query.filter_by(event_id=temp[0], time=temp[2]).first()
    reply = Reply.query.filter_by(replyer_id=temp[1]).first()
    new_reply = Reply(event_id=temp[0], replyer_id=user_id, description=des, review_id=review.id, reply_to=reply.users.name, 
                        time=str(datetime.now())[:19], reply_to_time=review.time)
    Db_operations.add_to_database(new_reply)

    return redirect(url_for('book_event', id=temp[0]))


@app.route('/ai_chat', methods=['GET', 'POST'])
def ai_chat():
    """
    Handles the AI chat interface.
    GET: Displays the chat input form.
    POST: Processes the user's message and displays the AI's response.
    """
    ai_response = None
    user_query_display = "" # To optionally display the user's last query

    if request.method == 'POST':
        user_message = request.form.get('user_query')
        if user_message:
            user_query_display = user_message # Store for displaying in template
            ai_response = AI_Operations.get_chat_completion(user_message)
        else:
            flash("Please enter a message for the AI.", "warning")

    # Render the template, passing the AI's response and the user's query
    return render_template('ai_chat.html', ai_response=ai_response, user_query=user_query_display)
# >>> END: New AI Chat Route <<<

# ... (rest of your existing routes) ...