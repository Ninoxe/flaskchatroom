var socketio = io();

socketio.on("message", function (message) {
    displayMessage(message.message, message.sender);
});

function displayMessage(message, sender) {
    var messages = document.getElementById("messages");

    var senderIsUser = "user" === sender;
    var content = `<li class="message-item ${senderIsUser ? "user-message" : "agent-message"}" value="${message}">
        ${message}
        <p><small>${new Date().toLocaleString()}</small></p>
    </li>`;

    messages.innerHTML += content;
}

function sendMessage() {
    // Check for empty message
    var msgInput = document.getElementById("message-input");
    if (msgInput.value === "") return;

    // Retrieve all chat and parse it to json to send.
    // messages = {
    //     0: {
    //         sender: "agent",
    //         message: "this is my message",
    //     }
    // }
    var msg = msgInput.value;
    displayMessage(msg, "user");
    var targetmessages = document.getElementsByTagName("li");
    var messages = {};

    for (var i = 0; i < targetmessages.length; i++) {
        var senderIsUser = targetmessages[i].getAttribute("class").indexOf("user") > 0;
        messages[i] = { sender: senderIsUser ? "user" : "agent", message: targetmessages[i].getAttribute("value") };
    }

    socketio.emit("message", { messages: messages });
    // TODO: try to catch error

    msgInput.value = "";
}