from flask import Flask, render_template, abort
from flask_socketio import SocketIO, send
import random

app = Flask(
    __name__, template_folder="../front/templates", static_folder="../front/static"
)
app.config["SECRET_KEY"] = "thesecretkey"
socketio = SocketIO(app)

agent_string = ["hello", "Yes!", "Can I help you?", "This is so cool!"]


@socketio.on("message")
def handle_message(data):
    """
    Check sanity of data and send an automatic response from an agent
    """
    # Check if data are correctly formated
    previous_sender = "agent"
    for index, (k, v) in enumerate(data["messages"].items()):
        current_sender = v["sender"]
        while current_sender != previous_sender and index < len(data["messages"]):
            previous_sender = current_sender
            break
        else:
            abort(400, "Error on messages history")

    # Return 'agent' response
    send({"message": random.choice(agent_string), "sender": "agent"})


@app.route("/", methods=["GET"])
def home():
    """
    Access to home page
    """
    return render_template("main.html")


# TODO: Manage connection and room system

# @socketio.on("connect")
# def handle_connect():
#     send({"sender": "", "message": f"{user} join the chat"}, to=room)


# @socketio.on("disconnect")
# def handle_disconnect():
#     send(
#         {
#             "message": f"{user} left the chat",
#         },
#         to=room,
#     )


if __name__ == "__main__":
    socketio.run(app, debug=True)
