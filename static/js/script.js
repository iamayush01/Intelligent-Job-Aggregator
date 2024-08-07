document.getElementById('scrape-button').addEventListener('click', function(e) {
    fetch('/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
    })
    .then(response => response.json())
    .then(data => {
        let output = '';
        for (let company in data) {
            output += `
                <div class="company-column">
                    <h2>${company}</h2>
                    ${data[company].map(job => `
                        <div class="job">
                            <h3>${job.title}</h3>
                            <!-- 
                            <p><strong>Company:</strong> ${job.company}</p>
                            <p><strong>Location:</strong> ${job.location}</p>
                            <p><strong>Type:</strong> ${job.type}</p>
                            <p><strong>Posted on:</strong> ${job.posted}</p>
                            -->
                        </div>
                    `).join('')}
                </div>
            `;
        }
        document.getElementById('results').innerHTML = output;
    })
    .catch(error => console.error('Error:', error));
});