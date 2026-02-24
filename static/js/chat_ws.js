


//! this particular file is fully written by Gemini 3,
//! the sole reason for this is that I don't know a word in js
//! so if you find some stupid shit in here don't blame me
//! if it is degenerate level of stupid you can try to fix it



console.log("Chat WS Script Loaded"); // Debug check

// Extract user_id/chat_id from URL
const pathParts = window.location.pathname.split('/');
const chatId = pathParts[pathParts.length - 1];

// Use dynamic host (works for both localhost and real IP)
const socket = new WebSocket(`ws://${window.location.host}/ws/${chatId}`);

const chatForm = document.getElementById('chat-form');
const messageInput = document.getElementById('message_input');
const messagesContainer = document.querySelector('.messages-container');

socket.onopen = () => console.log("WebSocket Connected!");

socket.onmessage = function(event) {
    // Parse the string back into a JS object
    const data = JSON.parse(event.data);
    
    const newMessage = document.createElement('div');
    
    // Logic: if I am the sender, show on the right, else on the left
    // (chatId here is used as current user ID for testing)
    const isMe = data.sender_id == chatId;
    newMessage.className = isMe ? 'message outgoing' : 'message incoming';
    
    newMessage.innerHTML = `
        <div class="message-content">
            ${data.text}
            <span class="msg-time">${data.timestamp}</span>
        </div>
    `;
    messagesContainer.appendChild(newMessage);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
};

chatForm.onsubmit = function(event) {
    event.preventDefault();
    
    if (messageInput.value && socket.readyState === WebSocket.OPEN) {
        // Create an object to send
        const messageObject = {
            text: messageInput.value
        };
        
        // Convert object to string (JSON)
        socket.send(JSON.stringify(messageObject));
        messageInput.value = '';
    }
};