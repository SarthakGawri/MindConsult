
const chatLog = document.getElementById('chat-log');
const consultantName = JSON.parse(document.getElementById('name').textContent);
const userName = JSON.parse(document.getElementById('user_name').textContent);

/* if (userName === consultantName) {
    Name = userName
} else {
    Name = consultantName
} */

/* if (chatLog.childNodes.length <= 1) {
    const emptyText = document.createElement('h3')
    emptyText.id = 'emptyText'
    emptyText.innerText = 'No Messages'
    emptyText.className = 'emptyText'
    chatLog.appendChild(emptyText)
} */


const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/consultation/new/'
    + consultantName
    + '/'
);
console.log(window.location.host)
console.log(window.location.pathname)

console.log(chatSocket.url)

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    let message = document.createElement('div');

    const userId = data['user_id'];
    console.log(userId)
    console.log(consultantName)
    const loggedInUserId = JSON.parse(document.getElementById('user_id').textContent);
    console.log(loggedInUserId);
    message.innerText = data.message;
    
    if (userId === loggedInUserId) {
        message.classList.add('message', 'sender', 'col-4', 'text-center');
    } else {
        message.classList.add('message', 'receiver', 'col-4', 'text-center');
    }

    chatLog.appendChild(message)

    if (document.querySelector('#emptyText')) {
        document.querySelector('#emptyText').remove()
    }
};

chatSocket.onerror = function (e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInput = document.querySelector('#chat-message-input');
    const message = messageInput.value;
    const userId = document.getElementById('user_id').textContent;
    chatSocket.send(JSON.stringify({
        'message': message,
        'user_id': userId
    }));
    messageInput.value = '';
};
