document.getElementById('acceptFeedback').addEventListener('click', () => {
    fetch('/api/submit-feedback/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ feedback: 'accepted' }),
    }).then(response => response.json())
      .then(data => console.log('Feedback submitted:', data))
      .catch(error => console.error('Error:', error));
});

document.getElementById('rejectFeedback').addEventListener('click', () => {
    fetch('/api/submit-feedback/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ feedback: 'rejected' }),
    }).then(response => response.json())
      .then(data => console.log('Feedback submitted:', data))
      .catch(error => console.error('Error:', error));
});
