document.getElementById('scrape-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const url = document.getElementById('url').value;

    fetch('/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        let output = '<h2>Job Listings</h2>';
        data.forEach(job => {
            output += `
                <div class="job">
                    <h3>${job.title}</h3>
                    <!-- 
                    <p><strong>Company:</strong> ${job.company}</p>
                    <p><strong>Location:</strong> ${job.location}</p>
                    <p><strong>Type:</strong> ${job.type}</p>
                    <p><strong>Posted on:</strong> ${job.posted}</p>
                    -->
                </div>
            `;
        });
        document.getElementById('results').innerHTML = output;
    })
    .catch(error => console.error('Error:', error));
});
