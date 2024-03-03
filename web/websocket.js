// Create a WebSocket connection
const socket = new WebSocket('ws://127.0.0.1:8787');

// Set a timeout to close the WebSocket if no request is received within 60 minutes
let timeout;

socket.onopen = () => {
    console.log('WebSocket connectiown established');
    // Start the timeout when the connection is opened
    timeout = setTimeout(() => {
        socket.close();
        console.log('WebSocket connection closed due to inactivity');
    }, 60 * 60 * 1000); // 60 minutes in milliseconds
};

socket.onmessage = (event) => {
    console.log('Received message:', event.data);
    // Reset the timeout whenever a request is received
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        socket.close();
        console.log('WebSocket connection closed due to inactivity');
    }, 60 * 60 * 1000); // 60 minutes in milliseconds
};

socket.onclose = () => {
    console.log('WebSocket connection closed');
};

socket.onerror = (error) => {
    console.error('WebSocket error:', error);
};