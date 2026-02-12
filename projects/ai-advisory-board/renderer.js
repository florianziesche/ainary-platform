/**
 * HTML Renderer for AI Advisory Board
 */

const fs = require('fs');
const path = require('path');

function renderHTML(question, advisors, responses) {
  const timestamp = new Date().toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });

  const advisorCards = advisors.map((advisor, index) => `
    <div class="advisor-card">
      <div class="advisor-header">
        <div class="advisor-icon">${advisor.icon}</div>
        <div class="advisor-info">
          <h3>${advisor.name}</h3>
          <p class="advisor-role">${advisor.role}</p>
        </div>
      </div>
      <div class="advisor-response">
        ${formatResponse(responses[index])}
      </div>
    </div>
  `).join('');

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advisory Board: ${escapeHtml(question)}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --gold: #c8aa50;
            --bg-dark: #0a0a0a;
            --bg-card: rgba(20, 20, 20, 0.6);
            --bg-glass: rgba(255, 255, 255, 0.05);
            --border-glass: rgba(255, 255, 255, 0.1);
            --text-primary: #ffffff;
            --text-secondary: #a0a0a0;
            --text-muted: #666666;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg-dark);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
            padding: 2rem 1rem;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--border-glass);
        }

        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, var(--gold) 0%, #f4e4b5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .question {
            font-size: 1.5rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }

        .meta {
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .advisors-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .advisor-card {
            background: var(--bg-glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 2rem;
            transition: all 0.3s ease;
        }

        .advisor-card:hover {
            border-color: var(--gold);
            box-shadow: 0 8px 32px rgba(200, 170, 80, 0.1);
            transform: translateY(-2px);
        }

        .advisor-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border-glass);
        }

        .advisor-icon {
            width: 48px;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(200, 170, 80, 0.1);
            border-radius: 12px;
            color: var(--gold);
        }

        .advisor-info h3 {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .advisor-role {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        .advisor-response {
            font-size: 1rem;
            color: var(--text-secondary);
            line-height: 1.8;
        }

        .advisor-response p {
            margin-bottom: 1rem;
        }

        .advisor-response p:last-child {
            margin-bottom: 0;
        }

        .banner {
            background: linear-gradient(135deg, rgba(200, 170, 80, 0.1) 0%, rgba(200, 170, 80, 0.05) 100%);
            border: 1px solid var(--gold);
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            margin-bottom: 3rem;
        }

        .banner h2 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            color: var(--gold);
        }

        .banner p {
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
        }

        .btn {
            display: inline-block;
            padding: 0.75rem 2rem;
            background: var(--gold);
            color: var(--bg-dark);
            font-weight: 600;
            text-decoration: none;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
        }

        .btn:hover {
            background: #d4b960;
            transform: scale(1.05);
        }

        .feedback-section {
            background: var(--bg-glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .feedback-section h2 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        .feedback-options {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .feedback-btn {
            flex: 1;
            padding: 1rem;
            background: var(--bg-glass);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1rem;
        }

        .feedback-btn:hover {
            border-color: var(--gold);
            color: var(--gold);
        }

        textarea {
            width: 100%;
            padding: 1rem;
            background: var(--bg-glass);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            resize: vertical;
            min-height: 100px;
            margin-bottom: 1rem;
        }

        textarea:focus {
            outline: none;
            border-color: var(--gold);
        }

        footer {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid var(--border-glass);
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        /* Modal Styles */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(5px);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            padding: 2rem;
            max-width: 500px;
            width: 90%;
        }

        .modal-content h2 {
            font-size: 1.75rem;
            margin-bottom: 1rem;
            color: var(--gold);
        }

        .modal-content input {
            width: 100%;
            padding: 0.75rem;
            background: var(--bg-glass);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            margin-bottom: 1rem;
        }

        .modal-content input:focus {
            outline: none;
            border-color: var(--gold);
        }

        .modal-actions {
            display: flex;
            gap: 1rem;
        }

        .btn-secondary {
            background: var(--bg-glass);
            color: var(--text-primary);
            border: 1px solid var(--border-glass);
        }

        .btn-secondary:hover {
            background: var(--border-glass);
        }

        /* Print Styles */
        @media print {
            body {
                background: white;
                color: black;
            }

            .banner, .feedback-section, footer, .modal {
                display: none;
            }

            .advisor-card {
                break-inside: avoid;
                border: 1px solid #ddd;
                background: white;
            }

            .advisor-icon {
                color: #c8aa50;
            }

            h1 {
                color: #c8aa50;
                -webkit-text-fill-color: #c8aa50;
            }

            .question, .advisor-info h3 {
                color: black;
            }

            .advisor-response, .advisor-role, .meta {
                color: #333;
            }
        }

        @media (max-width: 768px) {
            .advisors-grid {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 2rem;
            }

            .question {
                font-size: 1.25rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>AI Advisory Board</h1>
            <p class="question">"${escapeHtml(question)}"</p>
            <p class="meta">Generated on ${timestamp}</p>
        </header>

        <main>
            <div class="advisors-grid">
                ${advisorCards}
            </div>

            <div class="banner">
                <h2>Want Deeper Analysis?</h2>
                <p>Get a custom deep-dive report with additional frameworks, case studies, and implementation roadmap.</p>
                <button class="btn" onclick="openEmailGate()">Request Detailed Analysis</button>
            </div>

            <div class="feedback-section">
                <h2>How helpful was this advisory session?</h2>
                <div class="feedback-options">
                    <button class="feedback-btn" onclick="submitFeedback('very-helpful')">Very Helpful</button>
                    <button class="feedback-btn" onclick="submitFeedback('somewhat-helpful')">Somewhat Helpful</button>
                    <button class="feedback-btn" onclick="submitFeedback('not-helpful')">Not Helpful</button>
                </div>
                <textarea placeholder="Additional feedback (optional)..." id="feedback-text"></textarea>
                <button class="btn" onclick="submitDetailedFeedback()">Submit Feedback</button>
            </div>
        </main>

        <footer>
            <p>AI Advisory Board • Powered by GPT-4o • 6 Perspectives, One Decision</p>
        </footer>
    </div>

    <!-- Email Gate Modal -->
    <div class="modal" id="email-modal">
        <div class="modal-content">
            <h2>Get Your Deep-Dive Analysis</h2>
            <p style="color: var(--text-secondary); margin-bottom: 1.5rem;">
                Enter your email to receive a comprehensive analysis report including implementation frameworks and case studies.
            </p>
            <input type="email" id="email-input" placeholder="your@email.com" />
            <div class="modal-actions">
                <button class="btn btn-secondary" style="flex: 1;" onclick="closeEmailGate()">Cancel</button>
                <button class="btn" style="flex: 1;" onclick="submitEmail()">Get Analysis</button>
            </div>
        </div>
    </div>

    <script>
        function openEmailGate() {
            document.getElementById('email-modal').classList.add('active');
        }

        function closeEmailGate() {
            document.getElementById('email-modal').classList.remove('active');
        }

        function submitEmail() {
            const email = document.getElementById('email-input').value;
            if (email && email.includes('@')) {
                alert('Thank you! Your detailed analysis will be sent to ' + email);
                // In production, this would send to a backend API
                console.log('Email submitted:', email);
                closeEmailGate();
            } else {
                alert('Please enter a valid email address');
            }
        }

        function submitFeedback(rating) {
            console.log('Feedback rating:', rating);
            alert('Thank you for your feedback!');
        }

        function submitDetailedFeedback() {
            const text = document.getElementById('feedback-text').value;
            console.log('Detailed feedback:', text);
            alert('Thank you for your detailed feedback!');
            document.getElementById('feedback-text').value = '';
        }
    </script>
</body>
</html>`;
}

function formatResponse(text) {
  // Convert markdown-like formatting to HTML
  return text
    .split('\n\n')
    .map(para => `<p>${escapeHtml(para.trim())}</p>`)
    .join('');
}

function escapeHtml(text) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  return text.replace(/[&<>"']/g, m => map[m]);
}

module.exports = { renderHTML };
