# data
from flask import Flask, jsonify
import json


user_data = \
[
    {
        "name":"Harry",
        "email":"Harry@gmail.com",
        "password":"123456",
        "payment":"5412 3590 8320 2793",
    },

    {
        "name":"Ziwei",
        "email":"Ziwei@gmail.com",
        "password":"123456",
        "payment":"3278 2497 2489 5710"
    },

    {
        "name":"Cassie",
        "email":"Cassie@gmail.com",
        "password":"123456",
        "payment":"5489 3298 2309 2898"
    },

    {
        "name":"Kevin",
        "email":"Kevin@gmail.com",
        "password":"123456",
        "payment":"3298 3892 3820 1154"
    },

    {
        "name":"Worde",
        "email":"Worde@gmail.com",
        "password":"123456",
        "payment":"3289 2390 3090 4353"
    },

    {
        "name":"Francis1",
        "email":"Francis1@gmail.com",
        "password":"123456",
        "payment":"3823 9382 8393 9323"
    },

    {
        "name":"Francis2",
        "email":"Francis2@gmail.com",
        "password":"123456",
        "payment":"3823 9382 8393 9323"
    },

    {
        "name":"Francis3",
        "email":"Francis3@gmail.com",
        "password":"123456",
        "payment":"3823 9382 8393 9323"
    },

    {
        "name":"Francis4",
        "email":"Francis4@gmail.com",
        "password":"123456",
        "payment":"3823 9382 8393 9323"
    },

    {
        "name":"Francis5",
        "email":"Francis5@gmail.com",
        "password":"123456",
        "payment":"3823 9382 8393 9323"
    },

    {
        "name":"Francis6",
        "email":"Francis6@gmail.com",
        "password":"123456",
        "payment":"3823 9382 8393 9323"
    },

    {
        "name":"Francis7",
        "email":"Francis7@gmail.com",
        "password":"123456",
        "payment":"3823 9382 8393 9323"
    },

    {
        "name":"Francis8",
        "email":"Francis8@gmail.com",
        "password":"123456",
        "payment":"3823 9382 8393 9323"
    }

]

event_data = \
[
    {
        "host_id": 1,
        "title": "Amazon Mini Working Backwards Workshop",
        "description": "Join a half day workshop led by Amazon/AWS Educate followed by drinks"
                       "Amazon was founded in 1994, and every year continuously accelerates the pace of innovation across the organisation with the mission to be Earth’s most customer-centric company. Our hallmark mechanism to consistently drive customer-centric innovative thinking and execution is the ‘Working Backwards’ process."
                       "In this session we share how Amazon formulates customer obsessed ideas and getting them to market quickly. Learn about the rapid pace of innovation at Amazon, and the culture that formulates the magic behind the scenes."
                       "Participants then get an accelerated hands-on experience of Amazon's innovation approach - the ‘Working Backwards’ process. During this half-day working session, we will help you articulate a customers need, define a solution, and create some but not all of the components of an Amazonian Press Release.",
        "venue": "Scientia Building (Gallery 6) UNSW",
        "start_date": "2020-08-29 10:00:00",
        "end_date": "2020-08-29 13:00:00",
        "tickets_num": 100,
        "ticket_price": 20,
        "tags": "Company",
        "capacity": "small",
        "status": "upcoming",
        "url": '../static/img/1.jpg'
    }
    ,
    {   
        "host_id": 2,
        "title": "The Art of Authenticity & Stakeholder Management - Deloitte ",
        "description":  "Presented by Bevan Brownhill, Head of contract and commercial management at Deloitte."
                        "Bevan is a strong negotiator and has led major international commercial negotiations and agreements in acquisition and exports on behalf of the UK Government. He is also experienced in managing legal and commercial issue resolution when tendering and managing contracts with both international governments, agencies and industry."
                        "Bevan leads the Commercial Management team that is responsible for supporting Deloitte’s largest accounts with commercial management, negotiation and advice, driving commercial management activities as part of the wider client experience program to the strategic partners of Deloitte’s key clients. He has extensive legal, procurement and contract management subject matter expertise based on experience gained across the public and private sector and professional services, consulting, advisory and technology delivery industries."
                        "Prior to joining Deloitte he was a senior procurement and sourcing legal advisor in UK Government providing specialist advice on managing vendors across the full contract life-cycle. Bevan has served organisations including the UK Ministry of Defence, Cabinet Office, and Home Office as well as other International Government Departments and Agencies including NATO and the EU."
                        "Prior to joining Deloitte he was a senior procurement and sourcing legal advisor in UK Government providing specialist advice on managing vendors across the full contract life-cycle. Bevan has served organisations including the UK Ministry of Defence, Cabinet Office, and Home Office as well as other International Government Departments and Agencies including NATO and the EU."
                        "Bevan is a fully accredited senior project and program manager with over 10 years experience leading delivery of strategic acquisition programs (the largest over $500m) and managing blue-chip contractors across a range of technical fields.",
        "venue": "Level 9/225 George St, Sydney NSW 2000",
        "start_date": "2020-08-31 12:00:00",
        "end_date": "2020-08-31 14:00:00",
        "tickets_num": 200,
        "ticket_price": 20,
        "tags": "Company",
        "capacity": "small",
        "status": "upcoming",
        "url": '../static/img/2.jpg'
    }
    ,
    {
        "host_id":3,
        "title": "EY 'Emerging Technologies'",
        "description": "Presented by Daniel Souza, Director Advisory, EY"
                        "Daniel has 18 years of experience delivering technology solutions and advisory services across the Mining, Media, Consumer goods, Industrial engineering, Manufacturing, Retail, and State/Federal Government industries."
                        "Daniel is a senior director and management consultant in IT Advisory at EY, with a focus on technology strategy, business change, and technology-enabled transformation."
                        "Daniel focuses on helping clients to improve their performance and manage their riks more effectively - particularly important in a challenging and uncertain business enviornment, with escalating competition. The allows IT to drive efficiencies throughout the organisation and better support and deliver transformational business change."
                        "Through IT transformation, services including demand management, sourcing, and infrastructure optimisation are measured, enabled and improved to increase overall return and effectiveness. By drawing upon deep business and technical experience, Daniel supports the implementations of industry software packages and focuses on managing the overall transformation, including management of 3rd party vendors."
                        "Daniel's workshop explores the role of emerging tech in the corporate sector. He explores the impact of technology on the operation and performance of tasks in the past and future of business.",
        "venue": "EY (Site Visit) 200 George Street Sydney, NSW 2000",
        "start_date": "2020-08-03 10:00:00",
        "end_date": "2020-08-03 12:30:00",
        "tickets_num": 50,
        "ticket_price": 10,
        "tags": "Company",
        "capacity": "small",
        "status": "upcoming",
        "url": '../static/img/3.jpg'
    }
    ,
    {
            "host_id": 4,
            "title": "Microsoft - Building your brand with LinkedIn Session",
            "description": "Presented by Max Ferfoglia, Community Manager, Microsoft Sydney."
                           "LinkedIn is an online network of professional relationships, used to present yourself and your qualiﬁcations, grow your network, and connect with new opportunities."
                           "In this workshop you will to learn to create a compelling profile of your capabilities and accomplishments and grow your business’s professional network."
                           "Build your brand and grow your network! Reserve your workshop spot by registering today.",
            "venue":"Microsoft Store - Westfield Sydney Pitt Street Sydney, NSW 2000",
            "start_date": "2020-08-15 10:30:00",
            "end_date": "2020-08-15 12:00:00",
            "tickets_num": 15 ,
            "ticket_price" :0,
            "tags": "Company",
            "capacity": "small",
            "status": "upcoming",
            "url": '../static/img/4.jpg'
    }
    ,
    {
            "host_id": 5,
            "title": "Leadership in Action - UNSW DVCA",
            "description": "Leadership in Practice, delivered by Rachel Abel, General Manager, DVCA UNSW"
                           "Rachel holds a Masters in Leadership, is an accredited leadership coach, and teaches on the 'Leadership in a Complex Environment' course for UNSW's MBAX program."
                           "This session wll focus on two key areas of leadership, and is designed to explore the concepts of leadership, what leadership means to you personally, and deliver some practical take-aways to use for your studies and future career.",
            "venue": "EY (Site Visit) 200 George Street Sydney, NSW 2000",
            "start_date": "2020-08-28 12:00:00",
            "end_date": "2020-08-28 14:00:00",
            "tickets_num": 100,
            "ticket_price": 10,
            "tags": "Education",
            "capacity": "small",
            "status": "upcoming",
            "url": '../static/img/5.jpg'
    }
    ,
    {
            "host_id": 5,
            "title": "Agile in Action - Session 2 - UNSW IT",
            "description": "Agility in action presented by Alyce Katsanos, Agile coach and scrum master practice lead, UNSW IT."
                           "Embracing agility improves performance, encourages cultures of innovation, and enables us to build stronger partnership with customers."
                           "Agile is not a one size fits all recipe, and we always need to embrace the values of experimentation, continuous improvement, and collaboration in order to find out what will work best in each environment."
                           "In this session, we will start out by walking you through the foundations of agility, give you some insight into how we are using agility at UNSW, and importantly, share some tangible tips and tricks for embracing agility in your world. Then, it will be over to you for an interactive workshop where you will put into practice what you’ve learnt."
                           "The aim – for you to emerge from the session ready to ‘agile’ a project of your own and continue to expand your knowledge of agility in the workforce.",
            "venue": "Michael Hinzte Theatre, Kensington Campus UNSW Kensington, NSW 2033",
            "start_date": "2020-08-31 11:30:00",
            "end_date": "2020-08-31 13:00:00",
            "tickets_num": 75,
            "ticket_price": 5,
            "tags": "Education",
            "capacity": "medium",
            "status": "upcoming",
            "url": '../static/img/6.jpg'
    }
    ,
    {
            "host_id": 5,
            "title": "'Empty your pockets'- TLC UNSW",
            "description": "This will be a fun, interactive workshop that tests your confidence, creativity and 'sales pitch'. What's in your pockets? Ever learnt from an actress? Come along and find out more!",
            "venue": "Mathews 214, Kensington Campus",
            "start_date": "2020-09-11 10:00:00",
            "end_date": "2020-09-11 12:00:00",
            "tickets_num": 45,
            "ticket_price": 10,
            "tags": "Education",
            "capacity": "medium",
            "status": "upcoming",
            "url": '../static/img/7.jpg'
    }
    ,
    {
            "host_id": 6,
            "title": "taylor swift reputation",
            "description": "Reputation (stylized in all lowercase) is the sixth studio album by American singer-songwriter Taylor Swift."
                           " It was released on November 10, 2017, through Big Machine Records. The record was primarily produced by Jack Antonoff, Max Martin, Shellback and Swift herself,who also serves as the executive producer. Described by Swift as her 'most cathartic album', the album is influenced by Swift's highly publicized personal life and disputes."
                           " The album's sound features a darker and heavier tone compared to Swift's previous projects, delving into her vulnerable side.Musically, it is a pop, electropop and synth-pop record that contains influences of hip hop, EDM, trap and tropical house.",
            "venue":"Sydney Olympic Park Qudos",
            "start_date": "2020-08-12 20:00:00",
            "end_date": "2020-08-12 23:00:00",
            "tickets_num": "1000000",
            "ticket_price": "175",
            "tags": "Music",
            "capacity": "medium",
            "status": "upcoming",
            "url": "../static/img/img5.jpg"
    }
    ,
    {
            "host_id": 6,
            "title": "Seoul Rumor Event",
            "description": "This is a very popular south korea singer. Attend this, u will like it. u will like it."
                           " u will like it. u will like it. u will like it. u will like it. u will like it. ",
            "venue": "Sydney Olympic Park Ken Rosewall area",
            "start_date": "2020-08-13 20:00:00",
            "end_date": "2020-08-13 23:00:00",
            "tickets_num": "500000",
            "ticket_price": "160",
            "tags": "Music",
            "capacity": "medium",
            "status": "upcoming",
            "url": "../static/img/img_F.jpg"
    }
    ,
    {
            "host_id": 6,
            "title": "MayDay Event",
            "description": "Mayday Just Rock It!!!  welcome! Attend this, u will like it.",
            "venue": "Sydney Olympic Park Qudos",
            "start_date": "2020-08-14 20:00:00",
            "end_date": "2020-08-14 23:00:00",
            "tickets_num": "500000",
            "ticket_price": "150",
            "tags": "Music",
            "capacity": "medium",
            "status": "upcoming",
            "url": "../static/img/img_C.jpg"
    }
    ,
    {
            "host_id": 6,
            "title": "Voice of China",
            "description": "One of the most popular singer ziwei would attend this event, and tutors include harry, cassie, kevin and worde which is a great squads;"
                           "Attend this, u will like it.",
            "venue": "Sydney Olympic Park Ken Rosewall area",
            "start_date": "2020-08-16 20:00:00",
            "end_date": "2020-08-16 23:00:00",
            "tickets_num": "500000",
            "ticket_price": "150",
            "tags": "Music",
            "capacity": "medium",
            "status": "upcoming",
            "url": "../static/img/img1.jpg"
    }
    ,
    {
            "host_id": 6,
            "title": "Rapper America Event",
            "description": "There’s nothing quite like the energy you can find at a USA hip hop music festival."
                           "It’s electric, it’s authentic and it’s a loud voice for many. It has grown from its beginnings within African American and Latino communities of The Bronx in New York City to being embraced and loved by all races, creeds, ethnicities and genders.",
            "venue": "Sydney Olympic Park Qudos",
            "start_date": "2020-08-24 20:00:00",
            "end_date": "2020-08-24 23:00:00",
            "tickets_num": "500000",
            "ticket_price": "150",
            "tags": "Music",
            "capacity": "medium",
            "status": "upcoming",
            "url": "../static/img/img2.jpg"
    }
    ,
    {
            "host_id": 6,
            "title": "Zeroscape Karmaking Event",
            "description": "Members: JUSSI VEHMAN - Laulu & Basso PEKKA SAASTAMOINEN - Kitara & Laulu JESSE KOSO - Kitara SAMI PETMAN - Rummut",
            "venue": "Sydney Olympic Park Qudos",
            "start_date": "2020-09-05 20:00:00",
            "end_date": "2020-09-05 23:00:00",
            "tickets_num": "500000",
            "ticket_price": "150",
            "tags": "Music",
            "capacity": "medium",
            "status": "upcoming",
            "url": "../static/img/img3.jpg"
    }
    ,
    {
            "host_id": 8,
            "title": "IBM- Artificial Intelligence ",
            "description": "Presented by Dev Mookerjee, Chief Technology Officer, IBM Watson Solutions, Asia Pacific"
                           "Dev’s workshop focuses on machine learning and the role of it at IBM. He emphasises on the ease of using this form of technology and the impact it has had on past and current markets. Dev’s vast knowledge on technology is also helpful in assisting students with their innovation projects.",
            "venue": "IBM (site visit) Level 17/ 259 George Street Sydney, NSW",
            "start_date": "2020-09-11 10:30:00",
            "end_date": "2020-09-11 12:00:00",
            "tickets_num": 50,
            "ticket_price":10,
            "tags": "Company",
            "capacity": "large",
            "status": "upcoming",
            "url": "../static/img/9.jpg"
    }
    ,
    {
            "host_id": 9,
            "title": "Uber 'Selling Yourself is Fair Game'",
            "description": "*** Short and Sweet*** In this session, we'll understand what personal brand is, and how to leverage a strong personal brand to improve your networking and job hunting skills.",
            "venue": "580 George St, Sydney NSW 2000",
            "start_date": "2020-09-13 13:30:00",
            "end_date": "2020-09-13 15:30:00",
            "tickets_num": 40,
            "ticket_price": 0,
            "tags": "Company",
            "capacity": "large",
            "status": "upcoming",
            "url": "../static/img/10.jpg"
    }
    ,
    {
            "host_id": 10,
            "title": "Pitching and Resilience - SBS",
            "description": "To improve your chances of successfully getting your ideas adopted. The workshop looks at some of the fundamentals around the growth mindset, pitching and resilience and provides an opportunity to practise necessary skills",
            "venue": "Level 32/1 Market St, Sydney NSW 2000",
            "start_date": "2020-09-14 12:00:00",
            "end_date": "2020-09-14 14:00:00",
            "tickets_num": 60,
            "ticket_price": 20,
            "tags": "Company",
            "capacity": "large",
            "status": "upcoming",
            "url": "../static/img/11.jpg"
    }
    ,
    {
            "host_id": 11,
            "title": "The Virtual Beer Festival Episode 4",
            "description": "The Virtual Beer Festival is back for round 4 and this interactive beer experience comes straight to your living room along with a case of 10 special West Coast beers and featured brewery swag. The event is a virtual experience featuring guided tastings with different breweries, guests, interactive games, comedy sketches, and band performances with this month's special guest co-host, comedian Tom Green. On June 13th, the show will be live streamed at 7pm where you can interact with our hosts, brewers, and other virtual beer festival attendees."
                           "Expect all new breweries and bands that did not appear in our last Festivals.",
            "venue": "Online",
            "start_date": "2020-07-23 12:00:00",
            "end_date": "2020-07-24 14:00:00",
            "tickets_num": 60,
            "ticket_price": 40,
            "tags": "Foods & Drinks",
            "capacity": "large",
            "status": "upcoming",
            "url": "../static/img/12.jpg"
    }
    ,
    {
            "host_id": 12,
            "title": "Herbal Cocktail Class",
            "description": "Watermelon Elderflower Gimlet"
                           "You'll be introduced to the medicinal properties of elderflower, learn how to make a cordial that you can sip all summer long, plus you'll shake everything together, like professional bartenders, into a delicious watermelon cocktail."
                           "If you’re looking for a reason to wear jeans, this is it. This live virtual community experience offers a casual and fun way to interact with real humans, learn an impressive new skill and catch a little buzz with good company. No experience necessary, and options for a non-alcoholic version will be available.",
            "venue": "Online",
            "start_date": "2020-07-29 12:00:00",
            "end_date": "2020-07-29 14:00:00",
            "tickets_num": 60,
            "ticket_price": 25,
            "tags": "Foods & Drinks",
            "capacity": "large",
            "status": "upcoming",
            "url": "../static/img/13.jpg"
    }
    ,
    {
            "host_id": 12,
            "title": "Isolation Cocktail and Tapas Class",
            "description": " Come to the event of a lifetime, that you won't want to miss, grab your boose, party outfits and fun filled attitude."
                           "This event includes easy to follow cocktail repcipes and tapas plates run by a complete amatur for your entertainment. watch an upcoming comedian trying to figure out how to make all the things presented, with you in real time on a live stream."
                           "After cocktails tapas class is finished there is a seperate afterparty that is avaliable where you get to sociallize and dance with other particpants in this lighthearted cokctail filled event.",
            "venue": "Online",
            "start_date": "2020-09-14 12:00:00",
            "end_date": "2020-09-14 14:00:00",
            "tickets_num": 30,
            "ticket_price": 0,
            "tags": "Foods & Drinks",
            "capacity": "large",
            "status": "upcoming",
            "url": "../static/img/14.jpg"
    }
    ,
    {
            "host_id": 13,
            "title": "How has Covid-19 changed our food and sustainability behaviours?",
            "description": "In this 60 min webinar, you will:"
                           "Understand the impact of COVID-19 on consumers’ grocery shopping habits, as well as their cooking routines and attitudes towards food sustainability"
                           "Identify what will happen next and which products and services are already meeting the new consumer needs"
                           "Better understand where new innovation opportunities exist for your business.",
            "venue": "Online",
            "start_date": "2020-09-24 17:00:00",
            "end_date": "2020-09-24 18:00:00",
            "tickets_num": 50,
            "ticket_price": 0,
            "tags": "Foods & Drinks",
            "capacity": "large",
            "status": "upcoming",
            "url": "../static/img/15.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "What makes a 'good' idea? - UNSW Hero Program introduction",
        "description": "Presented by David George, Program lead of Heroes at UNSW."
                       "As workplaces cope with Industry 4.0, we continue to witness the rise (and fall) of viral marketing, online tribalism, and questionable personal branding. Come discuss with us in an open forum -"
                       "Understanding challenges between ideation and implementation."
                       "Personal Branding that weaves together your life and your work in a way that tells an authentic story to an audience."
                       "Our goal is to ensure that you understand there are opportunities for sustainable partnerships and mentoring between yourself, established UNSW business units, and the Heroes industry partner network."
                       " Examples of successful Hero projects"
                       "How teams have met the expectations of industry representatives and UNSW staff"
                       "Common roadblocks when managing projects"
                       "What can make you stand out (methods for additional engagement with the program)",
        "venue": "Ainsworth G02, Kensington Campus NSW Kensington, NSW 2033",
        "start_date": "2020-09-24 17:00:00",
        "end_date": "2020-09-24 18:00:00",
        "tickets_num": 40,
        "ticket_price": 12,
        "tags": "Education",
        "capacity": "large",
        "status": "upcoming",
        "url": "../static/img/16.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "Stage Presence- Aaron Ngan",
        "description": "Take time with Aaron to manage your stance and voice on stage. This workshop will give you a practical opportunity to prepare yourself for the Heroes pitching events, and all further times you may need to take the stage in your life.",
        "venue": "Columbo Theatre C",
        "start_date": "2020-09-24 17:00:00",
        "end_date": "2020-09-24 18:00:00",
        "tickets_num": 60,
        "ticket_price": 10,
        "tags": "Education",
        "capacity": "large",
        "status": "upcoming",
        "url": "../static/img/17.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "Effective Networking - Cochlear",
        "description": "Matthew Prior is currently in charge of Cochlear’s Asia Pacific Finance and Commercial Operations Team with 13 years’ experience analysing the healthcare and hearing industry, 10 of which as an equities analyst at Evans & Partners, Merrill Lynch and Deutsche Bank. Before financial markets and finding a passion at Cochlear, Matt had a career in accountancy at Deloitte and Ernst & Young in Assurance and Corporate Finance. Matt is a member of the Chartered Accountants Australia & New Zealand. Matthews Workshop: How much time do you spend studying, learning, and developing a career interest / passion? And how much time do you spend working on how best to ensure that this acquired knowledge and experience is effective in getting you to where you want to go / have the impact that you want from your career? Most areas of business involve people making decisions about other people - your “network” is one of the most important areas of professional development but also one of the most overlooked. There is no easy way to develop strength in this area and whilst I do not claim expertise in networking, I am passionate about its benefits and can share my own journey in to develop this skill.",
        "venue": "Mathews 214 Kensington, NSW 2052",
        "start_date": "2020-11-24 13:00:00",
        "end_date": "2020-11-24 14:00:00",
        "tickets_num": 40,
        "ticket_price": 0,
        "tags": "Education",
        "capacity": "large",
        "status": "upcoming",
        "url": "../static/img/18.jpg"
    }
    ,
    #past
    {
        "host_id": 1,
        "title": "Exploring Inclusive and Authentic Leadership",
        "description": "Exploring Inclusive and Authentic Leadership"
                       "As future leaders, how we engage and influence others ultimately determines our effectiveness and our ability to leverage outcomes."
                       "Overview"
                       "Sam will discuss what authentic leadership looks and feels like, with some real life examples to illustrate the impact of authenticity on inclusivity, collaboration and self-accountability. How do you bring your whole self as a leader? What does it mean to be an inclusive leader? Why is inclusion and building an inclusive team important?"
                       "Sam will provide practical tips and tools as well as personal insights about the concepts of inclusion, belonging and authenticity.",
        "venue": "Mathews 214 Sydney, NSW 2052",
        "start_date": "2020-02-24 17:00:00",
        "end_date": "2020-02-24 18:00:00",
        "tickets_num": 100,
        "ticket_price": 11,
        "tags": "Education",
        "capacity": "large", 
        "status": "finished", 
        "url": "../static/img/19.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "Food And Mood",
        "description": "A talk exploring the link between what we eat and our mood and brain function, and nutritional tips to help support mood and brain health.",
        "venue": "Round House Sydney, NSW 2052",
        "start_date": "2020-02-24 17:00:00",
        "end_date": "2020-02-24 18:00:00",
        "tickets_num": 60,
        "ticket_price": 15,
        "tags": "Foods & Drinks",
        "capacity": "large", 
        "status": "finished",
        "url": "../static/img/20.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "Jai Ho! Virtual Party",
        "description": "FRIDAY, June 12th - BOLLYWOOD ARABIAN NIGHT!"
                       "Get ready for an Arabian Night with Bollywood fusion! DJ Prashant is playing all the Arabic & Desi hits from his living room to yours!"
                       "This party will be our last virtual event for June, as we begin transitioning back into LIVE, IN PERSON events! We have so enjoyed the last two months sharing music and dance with our friends & fans around the world, so we will be back on your screens in no time!"
                       "Sign up to receive Zoom, Twitch links at https://bit.ly/jaiho_TGIF",
        "venue": "Darling Square Sydney, NSW 2022",
        "start_date": "2020-04-23 17:00:00",
        "end_date": "2020-04-23 18:00:00",
        "tickets_num": 100,
        "ticket_price": 40,
        "tags": "Music",
        "capacity": "large", 
        "status": "finished", 
        "url": "../static/img/21.jpg"
    }
    ,
    # Other
    {
        "host_id": 4,
        "title": "A FEMINIST'S GUIDE TO BOTANY: Online Botanical Painting Session",
        "description": "Join London Drawing Group as we step inside the magical world of BOTANY for a summer-term special exploring the history of the heroic women artists, explorers and scientists that helped forge the way that we see the world around us!"
                       "Drawing from both the rich history of female presence Botanical Art, as well as the inspiring stories of women botanical explorers through the ages, this class will be an incredible opportunity to immerse yourself in the work of artists such as Maria Sybilla Merian, Marianne North, Rachel Ruysch and others!"
                       "The session will comprise a 1 hour visual lecture during which you will be able to make quick sketches if you choose, then students will be led in some basic watercolour techniques and exercises to help you create your own Botanical Paintings!"
                       "This will truly be a totally unique class and we are very excited to get drawing with you all!",
        "venue": "Online",
        "start_date": "2020-12-04 17:00:00",
        "end_date": "2020-12-04 18:00:00",
        "tickets_num": 100,
        "ticket_price": 70,
        "tags": "Others",
        "capacity": "large",
        "status": "upcoming",
        "url": "../static/img/22.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "Small Business Requirements and Resources (SBRR) COVID-19 Impact Webinar",
        "description": "The COVID-19 pandemic has brought us into unprecedented times, and State and federal leaders have had to react for the health of our people and economy. This webinar provides a quick overview of some of the state responses, resources, and other impacts affecting small businesses.",
        "venue": "Bull center Burwood Sydney, NSW 2012",
        "start_date": "2020-08-24 12:00:00",
        "end_date": "2020-08-24 14:00:00",
        "tickets_num": 50,
        "ticket_price": 20,
        "tags": "Others",
        "capacity": "large",
        "status": "upcoming",
        "url": "../static/img/23.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "Supporting yourself to support others [WEBINAR]",
        "description": "A webinar for any parent or professional support an individual with an additional need, challenging behaviours or neuro-diverse condition "
                       "About this Event "
                       "Supporting others can be hugely rewarding. It can also be very challenging at times. Particularly if those individuals see the world very differently or require more support then others to access the world around them safely and comfortably.",
        "venue": "Online",
        "start_date": "2020-09-04 17:00:00",
        "end_date": "2020-09-04 18:00:00",
        "tickets_num": 60,
        "ticket_price": 11,
        "tags": "Others",
        "capacity": "large",
        "status": "upcoming",
        "url": "../static/img/24.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "Practical Ways to Help You Be With Others Again",
        "description": "About this Event"
                       "A great FREE way to meet other businesses owners"
                       "A friendly and fun meet up that starts with everyone just having a chat and getting to know each other."
                       "You will have the chance to introduce yourself and your business to others before a couple of short but informative presentations are made to the group by other business owners from within the group."
                       "Ended by time to speak to other businesses or ask questions to those businesses who have presented."
                       "Organised and hosted by Blaze Monroe Associates Ltd",
        "venue": "Online",
        "start_date": "2020-11-04 17:00:00",
        "end_date": "2020-11-04 18:00:00",
        "tickets_num": 20,
        "ticket_price": 30,
        "tags": "Others",
        "capacity": "large",
        "status": "upcoming",
        "url": "../static/img/25.jpg"
    }
    ,
    {
        "host_id": 4,
        "title": "The future roles in developing others",
        "description": "The World has not just changed because of recent events, the World is always changing."
                       "Those people who have roles in the area of developing others (some people call this learning and development) must now start to think differently about how they operate. We purposefully have written the word differently rather than new as we believe that this change in our thinking is long overdue."
                       "Some people may have been using language that made people consider what they where offering or doing was different, but as many can attest too, there can be a huge void between What is said and How it is applied."
                       "The time is here to think different, talk different, lead different and apply differently.... to ensure we offer people and buiness exactly what they need moving forward."
                       "Change hasn't just happened and the change will not end....",
        "venue": "Online",
        "start_date": "2020-09-14 17:00:00",
        "end_date": "2020-09-14 18:00:00",
        "tickets_num": 60,
        "ticket_price": 10,
        "tags": "Others",
        "capacity": "large",
        "status": "upcoming",
        "url": "../static/img/26.jpg"
    }
    ,
    {
        "host_id": 1,  
        "title": "Harry Portter",  
        "description": "Harry Portter good movie",  
        "venue": "Sydney",  
        "start_date": "2020-7-28 16:45:00",
        "end_date": "2020-7-28 18:45:00", 
        "tickets_num": 50,
        "ticket_price": 20,
        "tags": "Others", 
        "capacity": "large", 
        "status": "finished",  
        "url": "../static/img/27.jpg"
    }
]


book_data = \
[
    {
        "user_id": 1,   
        "event_id": 32, 
        "seats": "A1",
        "ticket_number": 1,
        "total_price": 20,
        "booked_time": "2020-7-26 16:45:00",
        "status": "finished"
    }
    ,
    {
        "user_id": 4,   
        "event_id": 14, 
        "seats": "A1",
        "ticket_number": 1,
        "total_price": 0,
        "booked_time": "2020-7-30 16:45:00",
        "status": "upcoming"
    }
    ,
    {
        "user_id": 4, 
        "event_id": 24,  
        "seats": "A1",
        "ticket_number": 1,
        "total_price": 11,
        "booked_time": "2020-02-20 17:45:00",
        "status": "finished"
    }
    ,
    {
        "user_id": 4,
        "event_id": 25,
        "seats": "A1",
        "ticket_number": 1,
        "total_price": 15,
        "booked_time": "2020-02-20 17:45:00",
        "status": "finished"
    }
    ,
    {
        "user_id": 4,
        "event_id": 26,
        "seats": "A1",
        "ticket_number": 1,
        "total_price": 40,
        "booked_time": "2020-04-20 17:45:00",
        "status": "finished"
    }
]

review_data = \
[
    {
        "user_id": 2,                       
        "description": "Harry Potter! My favourite movie!",
        "event_id": 32,                     
        "time": "2020-7-29 16:50:00"        
    }
    ,
    {
        "user_id" : 3,
        "description": "This is an amazing workshop, It's recommended that you all come！ ",
        "event_id": 24,
        "time": "2020-02-27 17:35:00",
    }
    ,
    {
        "user_id" : 1,
        "description": "The foods and drinks are amazing , It's recommended that you all come！ ",
        "event_id": 25,
        "time": "2020-02-27 17:35:00",
    }
    ,
    {
        "user_id" : 4,
        "description": "This is an amazing concert, It's recommended that you all come！ ",
        "event_id": 26,
        "time": "2020-04-27 17:05:00",
    }

]

