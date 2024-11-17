## Requirements

* Python 3.x
* Flask
* Flask-SocketIO


## Installation
Go to the correct folder 
`cd flaskchatroom/back`

Install requirements
`pip install -r requirements.txt`

Run the server
`flask --app main run`

Now ou can go to http://127.0.0.1:5000/ or http://localhost:5000/

## Decisions

I decided to use Flask for two reasons. The first was the requirement of two separate "back" and "front" folders, the second was that I wasn't sure if Django was allowed (but it would have complicated things for folders).

After some research, I opted for Socketio because of its ease of learning, its ability to send messages in real time without reloading, for the fairly substantial help on the internet and that it's actively maintained.

## Futur work

* Connection and room
* Allow multiple users instead of a simple 'bot' agent
* Save history in db
* Add tests
* Remove favicon error in console