# n8n Automation Playbook
*15 Complete Workflow Blueprints for Building Your Personal Automation Engine*

Last updated: 2026-02-06

---

## How to Use This Playbook

Each workflow below includes everything you need to build it in one sitting:
- Exact node names from n8n
- Step-by-step connection flow
- Configuration details for each node
- AI integration specifics
- Time estimates and difficulty ratings

**Before you start:**
1. Have your n8n instance running (cloud or self-hosted)
2. Gather API keys for the services you'll use
3. Start with Beginner workflows to learn the patterns
4. Test each workflow with sample data before going live

---

## Workflow Index

| # | Workflow | Difficulty | Setup Time | Time Saved/Month |
|---|----------|------------|------------|------------------|
| 1 | AI Email Triage | Intermediate | 45 min | 10+ hours |
| 2 | Content Repurposing Engine | Intermediate | 60 min | 15+ hours |
| 3 | Lead Enrichment Pipeline | Advanced | 75 min | 12+ hours |
| 4 | Meeting Prep Automation | Intermediate | 50 min | 8+ hours |
| 5 | RSS AI Digest | Beginner | 30 min | 5+ hours |
| 6 | Social Media Scheduler | Intermediate | 60 min | 10+ hours |
| 7 | Competitor Monitor | Advanced | 90 min | 6+ hours |
| 8 | Invoice Processor | Intermediate | 55 min | 8+ hours |
| 9 | Job Application Tracker | Beginner | 40 min | 5+ hours |
| 10 | Customer Feedback Analyzer | Advanced | 80 min | 12+ hours |
| 11 | Personal CRM | Advanced | 90 min | 10+ hours |
| 12 | AI Research Assistant | Intermediate | 45 min | 15+ hours |
| 13 | Daily Standup Bot | Beginner | 35 min | 4+ hours |
| 14 | Portfolio Monitor | Intermediate | 50 min | 3+ hours |
| 15 | Knowledge Base Builder | Intermediate | 55 min | 8+ hours |

---

## 1. AI Email Triage

**Description:** Automatically classify incoming emails by urgency and topic, apply labels, and send priority notifications only for what matters.

### Nodes Needed
1. **Gmail Trigger** (Poll for new emails)
2. **OpenAI** (Classify email)
3. **Switch** (Route based on classification)
4. **Gmail** (Apply labels - 3 instances)
5. **Telegram** (Send notification)
6. **Function** (Format notification text)

### Step-by-Step Flow

**Node 1: Gmail Trigger**
- Mode: `Message Received`
- Label Filter: `INBOX`
- Poll Interval: Every 5 minutes
- Output: Email subject, body, sender, timestamp

**Node 2: OpenAI (Classification)**
- Model: `gpt-4o-mini` (fast + cheap)
- System Message:
  ```
  You are an email classifier. Analyze the email and respond with JSON:
  {
    "urgency": "high|medium|low",
    "category": "work|personal|newsletter|sales|spam",
    "action_required": true/false,
    "one_line_summary": "..."
  }
  ```
- User Message: 
  ```
  Subject: {{$json.subject}}
  From: {{$json.from}}
  Body: {{$json.body}}
  ```
- Output Mode: `JSON`

**Node 3: Switch (Route by Urgency)**
- Rule 1: `{{$json.urgency}} === 'high'` → High Priority Branch
- Rule 2: `{{$json.urgency}} === 'medium'` → Medium Priority Branch
- Rule 3: `{{$json.urgency}} === 'low'` → Low Priority Branch

**Node 4a: Gmail (Apply High Priority Label)**
- Action: `Add Label`
- Message ID: `{{$node["Gmail Trigger"].json.id}}`
- Label: `Priority/High`

**Node 4b: Gmail (Apply Medium Priority Label)**
- Action: `Add Label`
- Message ID: `{{$node["Gmail Trigger"].json.id}}`
- Label: `Priority/Medium`

**Node 4c: Gmail (Apply Low Priority Label)**
- Action: `Add Label`
- Message ID: `{{$node["Gmail Trigger"].json.id}}`
- Label: `Priority/Low`

**Node 5: Function (Format Notification - High Priority Only)**
- Connect only to Node 4a
- Code:
  ```javascript
  return {
    json: {
      message: `🚨 High Priority Email\n\n` +
               `From: ${$input.item.json.from}\n` +
               `Subject: ${$input.item.json.subject}\n` +
               `Summary: ${$node["OpenAI"].json.one_line_summary}\n\n` +
               `Action needed: ${$node["OpenAI"].json.action_required ? 'Yes' : 'No'}`
    }
  };
  ```

**Node 6: Telegram (Send Notification)**
- Chat ID: Your chat ID
- Message: `{{$json.message}}`
- Parse Mode: `Markdown`

### Trigger Type
**Poll-based trigger** - Checks Gmail every 5 minutes

### AI Integration
- **Model:** OpenAI GPT-4o-mini
- **Purpose:** Classify urgency, category, and extract summary
- **Cost:** ~$0.001 per email (very cheap)
- **Why this model:** Fast, cheap, excellent at structured classification

### Setup Details
1. Create Gmail labels: `Priority/High`, `Priority/Medium`, `Priority/Low`
2. Get OpenAI API key
3. Get Telegram bot token and your chat ID
4. Test with 5-10 old emails first
5. Adjust classification prompt based on your needs

### Estimated Setup Time
**45 minutes**

### Difficulty
**Intermediate** - Requires API setup and prompt engineering

### Monthly Time Saved
**10+ hours** - No more manual inbox sorting, instant awareness of urgent emails

---

## 2. Content Repurposing Engine

**Description:** Transform one blog post into multiple formats: LinkedIn post, Twitter thread, newsletter snippet, and Instagram caption.

### Nodes Needed
1. **Webhook** (Trigger with blog URL or text)
2. **HTTP Request** (Fetch blog content if URL provided)
3. **OpenAI** (Generate LinkedIn version)
4. **OpenAI** (Generate Twitter thread)
5. **OpenAI** (Generate newsletter snippet)
6. **OpenAI** (Generate Instagram caption)
7. **Google Sheets** (Log all versions)
8. **Telegram** (Send completion notification)

### Step-by-Step Flow

**Node 1: Webhook**
- Method: `POST`
- Path: `/content-repurpose`
- Expected payload:
  ```json
  {
    "blog_url": "https://...",
    "blog_text": "Full text if no URL",
    "title": "Post title"
  }
  ```

**Node 2: HTTP Request (Conditional)**
- Only if `blog_url` is provided
- Method: `GET`
- URL: `{{$json.blog_url}}`
- Extract: Use CSS selector or full HTML
- Output: Raw blog content

**Node 3: OpenAI (LinkedIn Version)**
- Model: `gpt-4o`
- System Message:
  ```
  You are a LinkedIn content strategist. Convert this blog post into an engaging LinkedIn post:
  - Start with a hook (1-2 sentences)
  - Key insights in bullet points
  - Professional but approachable tone
  - End with a question or CTA
  - Max 1300 characters
  - Include 3-5 relevant hashtags
  ```
- User Message: `{{$json.blog_text || $node["HTTP Request"].json.content}}`

**Node 4: OpenAI (Twitter Thread)**
- Model: `gpt-4o`
- System Message:
  ```
  Convert this blog post into a Twitter thread:
  - Tweet 1: Hook (must grab attention)
  - Tweets 2-7: Key points (one idea per tweet)
  - Final tweet: CTA + link
  - Each tweet max 280 chars
  - Use line breaks for readability
  - Include relevant emoji
  
  Format as JSON array: [{"tweet": "...", "order": 1}, ...]
  ```
- Output Mode: `JSON`

**Node 5: OpenAI (Newsletter Snippet)**
- Model: `gpt-4o`
- System Message:
  ```
  Create a newsletter teaser for this blog post:
  - 2-3 paragraphs
  - Conversational tone
  - Highlight the "why you should care"
  - End with "Read more: [link]"
  - Max 200 words
  ```

**Node 6: OpenAI (Instagram Caption)**
- Model: `gpt-4o`
- System Message:
  ```
  Create an Instagram carousel post caption:
  - Hook in first line
  - 5-7 short paragraphs with line breaks
  - Casual, visual language
  - Strong CTA
  - 10-15 relevant hashtags
  - Max 2000 characters
  ```

**Node 7: Google Sheets (Log Everything)**
- Spreadsheet: `Content Repurposing Log`
- Sheet: `Generated Content`
- Columns to write:
  - Timestamp: `{{$now}}`
  - Original Title: `{{$node["Webhook"].json.title}}`
  - LinkedIn: `{{$node["OpenAI"].json.choices[0].message.content}}`
  - Twitter Thread: `{{$node["OpenAI 1"].json.choices[0].message.content}}`
  - Newsletter: `{{$node["OpenAI 2"].json.choices[0].message.content}}`
  - Instagram: `{{$node["OpenAI 3"].json.choices[0].message.content}}`

**Node 8: Telegram (Notification)**
- Message:
  ```
  ✅ Content repurposed successfully!
  
  📝 Original: {{$node["Webhook"].json.title}}
  
  Created:
  - LinkedIn post
  - Twitter thread ({{$node["OpenAI 1"].json.length}} tweets)
  - Newsletter snippet
  - Instagram caption
  
  Check Google Sheet for full content.
  ```

### Trigger Type
**Webhook** - Call via HTTP POST whenever you publish a blog post

### AI Integration
- **Model:** OpenAI GPT-4o
- **Purpose:** Transform content for 4 different platforms
- **Cost:** ~$0.05 per blog post (4 API calls)
- **Why this model:** Best at maintaining voice while adapting style per platform

### Setup Details
1. Create Google Sheet with columns listed above
2. Get OpenAI API key
3. Test with 2-3 existing blog posts
4. Adjust prompts to match your brand voice
5. Optional: Add nodes to auto-post to platforms (Buffer, Later, etc.)

### Estimated Setup Time
**60 minutes**

### Difficulty
**Intermediate** - Multiple AI calls with different prompts

### Monthly Time Saved
**15+ hours** - Eliminates manual content adaptation for each platform

---

## 3. Lead Enrichment Pipeline

**Description:** When a new lead enters your CRM, automatically enrich it with company data, social profiles, contact info, and AI-generated research summary.

### Nodes Needed
1. **Webhook** or **CRM Trigger** (New lead)
2. **Clearbit Enrichment** (HTTP Request to Clearbit API)
3. **Hunter.io** (HTTP Request for email finding)
4. **LinkedIn Profile Scraper** (HTTP Request or RapidAPI)
5. **OpenAI** (Generate research summary)
6. **Google Search** (via SerpAPI) - Company news
7. **Function** (Merge all data)
8. **CRM Update** (Write back enriched data)
9. **Slack** (Notify sales team)

### Step-by-Step Flow

**Node 1: Webhook**
- Path: `/new-lead`
- Expected payload:
  ```json
  {
    "name": "Jane Doe",
    "company": "Acme Corp",
    "email": "jane@acme.com",
    "crm_id": "12345"
  }
  ```

**Node 2: HTTP Request (Clearbit Enrichment)**
- Method: `GET`
- URL: `https://person.clearbit.com/v2/combined/find?email={{$json.email}}`
- Authentication: Bearer token (Clearbit API key)
- Error handling: Continue on fail
- Output: Company data, social profiles, role, seniority

**Node 3: HTTP Request (Hunter.io - if email missing)**
- Condition: Only if `email` is empty
- Method: `GET`
- URL: `https://api.hunter.io/v2/email-finder?domain={{$json.company_domain}}&first_name={{$json.first_name}}&last_name={{$json.last_name}}&api_key=YOUR_KEY`
- Output: Verified email address

**Node 4: HTTP Request (LinkedIn Profile)**
- Method: `POST`
- URL: RapidAPI LinkedIn scraper endpoint
- Body:
  ```json
  {
    "name": "{{$json.name}}",
    "company": "{{$json.company}}"
  }
  ```
- Output: LinkedIn URL, headline, experience

**Node 5: HTTP Request (SerpAPI - Company News)**
- Method: `GET`
- URL: `https://serpapi.com/search?q={{$json.company}}+news&tbm=nws&api_key=YOUR_KEY&num=5`
- Output: Recent news articles about company

**Node 6: OpenAI (Generate Research Brief)**
- Model: `gpt-4o`
- System Message:
  ```
  You are a sales research assistant. Create a concise lead brief:
  - Company overview (2 sentences)
  - Recent news/updates (if any)
  - Person's role and background
  - Potential pain points based on industry
  - Suggested talking points for outreach
  
  Keep it under 200 words, actionable for sales.
  ```
- User Message:
  ```
  Lead: {{$node["Webhook"].json.name}}
  Company: {{$node["Clearbit"].json.company.name}}
  Role: {{$node["Clearbit"].json.employment.title}}
  Industry: {{$node["Clearbit"].json.company.category.industry}}
  Recent news: {{$node["SerpAPI"].json.news_results[0].snippet}}
  ```

**Node 7: Function (Merge All Data)**
- Code:
  ```javascript
  const clearbit = $node["Clearbit"].json;
  const hunter = $node["Hunter"].json;
  const linkedin = $node["LinkedIn"].json;
  const news = $node["SerpAPI"].json.news_results;
  const ai_brief = $node["OpenAI"].json.choices[0].message.content;
  
  return {
    json: {
      crm_id: $node["Webhook"].json.crm_id,
      enriched_data: {
        // Company info
        company_name: clearbit.company?.name,
        company_domain: clearbit.company?.domain,
        company_size: clearbit.company?.metrics?.employees,
        company_industry: clearbit.company?.category?.industry,
        company_location: clearbit.company?.geo?.city,
        
        // Person info
        full_name: clearbit.person?.name?.fullName,
        email_verified: clearbit.person?.email || hunter.email,
        title: clearbit.employment?.title,
        seniority: clearbit.employment?.seniority,
        linkedin_url: linkedin.profile_url,
        
        // Social
        twitter: clearbit.person?.twitter?.handle,
        
        // Research
        recent_news: news.slice(0, 3).map(n => n.title),
        ai_research_brief: ai_brief,
        
        // Meta
        enriched_at: new Date().toISOString()
      }
    }
  };
  ```

**Node 8: HTTP Request (Update CRM)**
- Method: `PATCH`
- URL: Your CRM API endpoint (HubSpot, Pipedrive, Airtable, etc.)
- Example for HubSpot:
  - URL: `https://api.hubapi.com/crm/v3/objects/contacts/{{$json.crm_id}}`
  - Body: Map enriched data to CRM fields
  - Headers: `Authorization: Bearer YOUR_HUBSPOT_KEY`

**Node 9: Slack (Notify Sales Team)**
- Channel: `#new-leads`
- Message:
  ```
  🎯 *New Enriched Lead*
  
  👤 *{{$node["Function"].json.enriched_data.full_name}}*
  🏢 {{$node["Function"].json.enriched_data.company_name}}
  💼 {{$node["Function"].json.enriched_data.title}}
  📊 Company size: {{$node["Function"].json.enriched_data.company_size}}
  
  📰 *Recent News:*
  {{$node["Function"].json.enriched_data.recent_news[0]}}
  
  🤖 *AI Research Brief:*
  {{$node["Function"].json.enriched_data.ai_research_brief}}
  
  🔗 <{{$node["Function"].json.enriched_data.linkedin_url}}|LinkedIn Profile>
  ```

### Trigger Type
**Webhook or CRM Trigger** - Fires when new lead is added to CRM

### AI Integration
- **Model:** OpenAI GPT-4o
- **Purpose:** Synthesize enrichment data into actionable sales brief
- **Cost:** ~$0.02 per lead
- **Why this model:** Excellent at synthesizing multiple data sources into concise briefs

### Setup Details
1. Get API keys: Clearbit, Hunter.io, RapidAPI (LinkedIn), SerpAPI, OpenAI
2. Configure your CRM API connection
3. Test with 5 sample leads
4. Free tier limits: Clearbit (50/month), Hunter.io (50/month)
5. Consider fallbacks if APIs fail

### Estimated Setup Time
**75 minutes**

### Difficulty
**Advanced** - Multiple API integrations, error handling needed

### Monthly Time Saved
**12+ hours** - Eliminates manual lead research

---

## 4. Meeting Prep Automation

**Description:** When a calendar event is created with specific attendees, automatically research them and generate a prep brief delivered to Slack or email.

### Nodes Needed
1. **Google Calendar Trigger** (Event created/updated)
2. **Function** (Extract attendee emails)
3. **HTTP Request** (Clearbit lookup per attendee)
4. **HTTP Request** (SerpAPI - recent mentions)
5. **OpenAI** (Generate meeting brief)
6. **Gmail** or **Slack** (Deliver brief)
7. **Google Calendar** (Add notes to event)

### Step-by-Step Flow

**Node 1: Google Calendar Trigger**
- Trigger: `Event Created` or `Event Updated`
- Calendar: Your primary calendar
- Poll Interval: Every 10 minutes
- Filter: Only events with attendees (not solo events)

**Node 2: Function (Parse Attendees)**
- Code:
  ```javascript
  const attendees = $input.item.json.attendees || [];
  
  // Filter out yourself and meeting rooms
  const externalAttendees = attendees.filter(a => 
    !a.email.includes('your-domain.com') && 
    !a.email.includes('calendar')
  );
  
  return externalAttendees.map(a => ({
    json: {
      email: a.email,
      event_id: $input.item.json.id,
      event_title: $input.item.json.summary,
      event_time: $input.item.json.start.dateTime,
      event_description: $input.item.json.description
    }
  }));
  ```

**Node 3: HTTP Request (Clearbit - per attendee)**
- Method: `GET`
- URL: `https://person.clearbit.com/v2/combined/find?email={{$json.email}}`
- Authentication: Bearer token
- Mode: `Execute once per item`
- Continue on fail: Yes

**Node 4: HTTP Request (SerpAPI - recent mentions)**
- Method: `GET`
- URL: `https://serpapi.com/search?q="{{$json.name}}"&tbm=nws&num=3&api_key=YOUR_KEY`
- Output: Recent articles or mentions

**Node 5: Function (Aggregate All Attendees)**
- Mode: `All items`
- Code:
  ```javascript
  const items = $input.all();
  const event = items[0].json;
  
  const attendeeProfiles = items.map(item => {
    const clearbit = item.json.clearbit_data;
    const news = item.json.news_data;
    
    return {
      name: clearbit?.person?.name?.fullName || item.json.email,
      title: clearbit?.employment?.title || 'Unknown',
      company: clearbit?.company?.name,
      linkedin: clearbit?.person?.linkedin?.handle,
      recent_news: news?.news_results?.[0]?.title || 'None found',
      bio: clearbit?.person?.bio
    };
  });
  
  return [{
    json: {
      event_title: event.event_title,
      event_time: event.event_time,
      event_description: event.event_description,
      event_id: event.event_id,
      attendees: attendeeProfiles
    }
  }];
  ```

**Node 6: OpenAI (Generate Meeting Brief)**
- Model: `gpt-4o`
- System Message:
  ```
  You are an executive assistant preparing meeting briefs. Create a concise prep document:
  
  Structure:
  1. Meeting context (what it's about)
  2. Attendee profiles (name, title, company, key background)
  3. Recent news/context per attendee
  4. Suggested discussion topics
  5. Questions to ask
  6. Goals for the meeting
  
  Keep it scannable, under 400 words, actionable.
  ```
- User Message:
  ```
  Meeting: {{$json.event_title}}
  Time: {{$json.event_time}}
  Description: {{$json.event_description}}
  
  Attendees:
  {{$json.attendees.map(a => `- ${a.name} (${a.title} at ${a.company}): ${a.bio || 'No bio available'}`).join('\n')}}
  
  Recent news:
  {{$json.attendees.map(a => `- ${a.name}: ${a.recent_news}`).join('\n')}}
  ```

**Node 7: Slack (Deliver Brief)**
- Channel: DM to yourself or `#meeting-prep`
- Message:
  ```
  📅 *Meeting Prep Brief*
  
  🕐 {{$node["Function 2"].json.event_time}}
  📝 {{$node["Function 2"].json.event_title}}
  
  {{$node["OpenAI"].json.choices[0].message.content}}
  
  ---
  _Auto-generated {{Math.floor((new Date($node["Function 2"].json.event_time) - new Date()) / 3600000)}} hours before meeting_
  ```
- Timing: Set condition to only send if meeting is >2 hours away

**Node 8: Google Calendar (Add Brief to Notes)**
- Action: `Update Event`
- Event ID: `{{$node["Function 2"].json.event_id}}`
- Description: Append AI brief to existing description
- Format:
  ```
  [Original description]
  
  ---
  🤖 AI Meeting Prep Brief:
  {{$node["OpenAI"].json.choices[0].message.content}}
  ```

### Trigger Type
**Calendar Trigger** - Polls Google Calendar every 10 minutes for new events

### AI Integration
- **Model:** OpenAI GPT-4o
- **Purpose:** Synthesize attendee research into actionable brief
- **Cost:** ~$0.03 per meeting
- **Why this model:** Excellent at synthesizing profiles and generating structured briefs

### Setup Details
1. Connect Google Calendar
2. Get API keys: Clearbit, SerpAPI, OpenAI
3. Configure Slack incoming webhook
4. Set up filters to exclude internal-only meetings
5. Test with upcoming meeting

### Estimated Setup Time
**50 minutes**

### Difficulty
**Intermediate** - Multiple data sources, array handling

### Monthly Time Saved
**8+ hours** - Eliminates pre-meeting research scramble

---

## 5. RSS AI Digest

**Description:** Aggregate multiple RSS feeds, use AI to summarize and rank articles, generate a weekly digest newsletter, and send to subscribers.

### Nodes Needed
1. **Schedule Trigger** (Weekly)
2. **RSS Feed Read** (Multiple instances for different feeds)
3. **Function** (Merge and deduplicate)
4. **OpenAI** (Summarize each article)
5. **OpenAI** (Rank articles by relevance)
6. **Function** (Format newsletter)
7. **Gmail** or **SendGrid** (Send email)
8. **Google Sheets** (Archive sent digests)

### Step-by-Step Flow

**Node 1: Schedule Trigger**
- Frequency: `Every Monday at 8:00 AM`
- Timezone: Your timezone

**Node 2a-2e: RSS Feed Read (5 instances)**
- Configure 5 different RSS feeds
- Examples:
  - Node 2a: TechCrunch AI - `https://techcrunch.com/category/artificial-intelligence/feed/`
  - Node 2b: The Verge - `https://www.theverge.com/rss/index.xml`
  - Node 2c: Hacker News - `https://news.ycombinator.com/rss`
  - Node 2d: MIT Tech Review - `https://www.technologyreview.com/feed/`
  - Node 2e: Your industry-specific feed
- Limit: 20 items per feed
- Output: Title, link, description, pubDate

**Node 3: Function (Merge & Deduplicate)**
- Code:
  ```javascript
  const allItems = $input.all();
  const oneWeekAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
  
  // Filter: only items from last 7 days
  const recentItems = allItems.filter(item => {
    const pubDate = new Date(item.json.pubDate);
    return pubDate > oneWeekAgo;
  });
  
  // Deduplicate by title similarity (basic)
  const unique = [];
  const seenTitles = new Set();
  
  recentItems.forEach(item => {
    const normalizedTitle = item.json.title.toLowerCase().trim();
    if (!seenTitles.has(normalizedTitle)) {
      seenTitles.add(normalizedTitle);
      unique.push(item);
    }
  });
  
  return unique.slice(0, 30); // Limit to 30 articles
  ```

**Node 4: OpenAI (Summarize Each Article)**
- Model: `gpt-4o-mini` (cheaper for bulk)
- Mode: `Execute once per item`
- System Message:
  ```
  Summarize this article in 2-3 sentences. Focus on:
  - Main point
  - Why it matters
  - Key takeaway
  
  Keep it concise and engaging.
  ```
- User Message:
  ```
  Title: {{$json.title}}
  Description: {{$json.description}}
  ```

**Node 5: Function (Aggregate Summaries)**
- Mode: `All items`
- Code:
  ```javascript
  return $input.all().map(item => ({
    json: {
      title: item.json.title,
      link: item.json.link,
      source: new URL(item.json.link).hostname,
      summary: item.json.summary_text,
      pubDate: item.json.pubDate
    }
  }));
  ```

**Node 6: OpenAI (Rank by Relevance)**
- Model: `gpt-4o`
- System Message:
  ```
  You are a content curator. Rank these articles by relevance and interest for a tech-savvy professional audience.
  
  Return JSON array with:
  - Top 10 articles in order of importance
  - Brief explanation why each matters
  - Add a category tag (AI, Product, Business, Research, Industry)
  
  Format:
  [
    {
      "title": "...",
      "why_it_matters": "...",
      "category": "...",
      "original_index": 0
    }
  ]
  ```
- User Message: Full list of articles (titles + summaries)
- Output Mode: JSON

**Node 7: Function (Format Newsletter HTML)**
- Code:
  ```javascript
  const rankedArticles = $json.ranked_articles;
  const date = new Date().toLocaleDateString('en-US', { 
    weekday: 'long', 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  });
  
  const html = `
  <!DOCTYPE html>
  <html>
  <head>
    <style>
      body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; }
      .header { background: #0066cc; color: white; padding: 20px; }
      .article { border-bottom: 1px solid #eee; padding: 20px 0; }
      .category { background: #f0f0f0; padding: 4px 8px; border-radius: 4px; font-size: 12px; }
      .summary { color: #666; margin: 10px 0; }
      .read-more { color: #0066cc; text-decoration: none; }
    </style>
  </head>
  <body>
    <div class="header">
      <h1>📰 Your Weekly Tech Digest</h1>
      <p>${date}</p>
    </div>
    
    <div style="padding: 20px;">
      <p>Here are the 10 most important tech stories this week, summarized by AI:</p>
      
      ${rankedArticles.map((article, i) => `
        <div class="article">
          <h2>${i + 1}. ${article.title}</h2>
          <span class="category">${article.category}</span>
          <p class="summary">${article.summary}</p>
          <p><strong>Why it matters:</strong> ${article.why_it_matters}</p>
          <a href="${article.link}" class="read-more">Read full article →</a>
        </div>
      `).join('')}
      
      <hr style="margin: 30px 0;">
      <p style="color: #999; font-size: 12px;">
        This digest was automatically curated and summarized by AI from your RSS feeds.
        <br>Delivered every Monday at 8 AM.
      </p>
    </div>
  </body>
  </html>
  `;
  
  return {
    json: {
      html: html,
      subject: `📰 Your Weekly Tech Digest - ${date}`,
      date: date
    }
  };
  ```

**Node 8: Gmail (Send Newsletter)**
- To: Your email or subscriber list
- Subject: `{{$json.subject}}`
- Email Type: `HTML`
- Message (HTML): `{{$json.html}}`

**Node 9: Google Sheets (Archive)**
- Spreadsheet: `RSS Digest Archive`
- Columns:
  - Date Sent: `{{$json.date}}`
  - Articles Count: `{{$json.ranked_articles.length}}`
  - Top Story: `{{$json.ranked_articles[0].title}}`
  - Full HTML: `{{$json.html}}` (for reference)

### Trigger Type
**Schedule Trigger** - Every Monday at 8:00 AM

### AI Integration
- **Models:** 
  - GPT-4o-mini for bulk summarization
  - GPT-4o for ranking/curation
- **Purpose:** Summarize 30+ articles and rank top 10
- **Cost:** ~$0.10 per digest
- **Why these models:** Mini is cheap for bulk summaries, GPT-4o better at editorial judgment

### Setup Details
1. Collect 5-10 RSS feeds in your niche
2. Get OpenAI API key
3. Set up Gmail or SendGrid for sending
4. Test with sample feeds first
5. Adjust ranking criteria in prompt to match your interests

### Estimated Setup Time
**30 minutes**

### Difficulty
**Beginner** - Straightforward flow, great for learning n8n

### Monthly Time Saved
**5+ hours** - No more manual RSS checking and reading

---

## 6. Social Media Scheduler

**Description:** Input a content calendar entry, AI generates platform-specific variants (LinkedIn, Twitter, Instagram), schedules them across platforms at optimal times.

### Nodes Needed
1. **Google Sheets Trigger** (New row in content calendar)
2. **OpenAI** (Generate LinkedIn post)
3. **OpenAI** (Generate Twitter post)
4. **OpenAI** (Generate Instagram caption)
5. **HTTP Request** (Buffer API - schedule LinkedIn)
6. **HTTP Request** (Buffer API - schedule Twitter)
7. **HTTP Request** (Buffer API - schedule Instagram)
8. **Google Sheets** (Mark as scheduled)
9. **Slack** (Confirmation notification)

### Step-by-Step Flow

**Node 1: Google Sheets Trigger**
- Spreadsheet: `Content Calendar`
- Sheet: `Pending Posts`
- Trigger: `On Row Added`
- Expected columns:
  - Topic/Idea
  - Key Points (bullet list)
  - Target Date
  - LinkedIn (checkbox)
  - Twitter (checkbox)
  - Instagram (checkbox)
  - Status

**Node 2: OpenAI (LinkedIn Version)**
- Condition: Only if LinkedIn checkbox is checked
- Model: `gpt-4o`
- System Message:
  ```
  Create a LinkedIn post:
  - Start with a compelling hook (question, bold statement, or story)
  - Break into short paragraphs (1-2 sentences each)
  - Include relevant data or insights
  - Professional yet authentic voice
  - End with a question or CTA
  - Add 3-5 hashtags
  - Max 1300 characters
  
  Use line breaks generously for mobile readability.
  ```
- User Message:
  ```
  Topic: {{$json.topic}}
  Key points:
  {{$json.key_points}}
  ```

**Node 3: OpenAI (Twitter Version)**
- Condition: Only if Twitter checkbox is checked
- Model: `gpt-4o`
- System Message:
  ```
  Create a Twitter post:
  - Single tweet format (not a thread)
  - Hook in first line
  - Punchy, conversational
  - 1-2 relevant emoji
  - Max 280 characters
  - No hashtags (looks spammy)
  
  Make it shareable and engaging.
  ```
- User Message:
  ```
  Topic: {{$json.topic}}
  Key insight: {{$json.key_points.split('\n')[0]}}
  ```

**Node 4: OpenAI (Instagram Caption)**
- Condition: Only if Instagram checkbox is checked
- Model: `gpt-4o`
- System Message:
  ```
  Create an Instagram caption:
  - Hook that works without seeing the image
  - 5-7 short paragraphs with line breaks
  - Conversational, personal tone
  - Story or insight-driven
  - Strong CTA at the end
  - 10-15 hashtags (mix of broad and niche)
  - Emojis sparingly
  - Max 2000 characters
  ```
- User Message:
  ```
  Topic: {{$json.topic}}
  Story angle: {{$json.key_points}}
  ```

**Node 5: Function (Prepare Buffer API Calls)**
- Code:
  ```javascript
  const targetDate = new Date($json.target_date);
  const platforms = [];
  
  if ($json.linkedin_checked) {
    platforms.push({
      profile_id: 'YOUR_LINKEDIN_BUFFER_PROFILE_ID',
      text: $node["OpenAI LinkedIn"].json.choices[0].message.content,
      scheduled_at: targetDate.setHours(9, 0) / 1000, // 9 AM
      platform: 'linkedin'
    });
  }
  
  if ($json.twitter_checked) {
    platforms.push({
      profile_id: 'YOUR_TWITTER_BUFFER_PROFILE_ID',
      text: $node["OpenAI Twitter"].json.choices[0].message.content,
      scheduled_at: targetDate.setHours(12, 0) / 1000, // 12 PM
      platform: 'twitter'
    });
  }
  
  if ($json.instagram_checked) {
    platforms.push({
      profile_id: 'YOUR_INSTAGRAM_BUFFER_PROFILE_ID',
      text: $node["OpenAI Instagram"].json.choices[0].message.content,
      scheduled_at: targetDate.setHours(18, 0) / 1000, // 6 PM
      platform: 'instagram',
      media: { photo: 'YOUR_IMAGE_URL' } // Requires pre-uploaded image
    });
  }
  
  return platforms.map(p => ({ json: p }));
  ```

**Node 6: HTTP Request (Schedule via Buffer)**
- Mode: `Execute once per item`
- Method: `POST`
- URL: `https://api.bufferapp.com/1/updates/create.json`
- Authentication: `access_token=YOUR_BUFFER_TOKEN`
- Body:
  ```json
  {
    "profile_ids[]": "{{$json.profile_id}}",
    "text": "{{$json.text}}",
    "scheduled_at": "{{$json.scheduled_at}}",
    "media": {{$json.media}}
  }
  ```

**Node 7: Google Sheets (Update Status)**
- Action: `Update Row`
- Row: Original trigger row
- Columns to update:
  - Status: `Scheduled`
  - LinkedIn Scheduled: `{{$json.linkedin_scheduled_time}}`
  - Twitter Scheduled: `{{$json.twitter_scheduled_time}}`
  - Instagram Scheduled: `{{$json.instagram_scheduled_time}}`
  - Scheduled At: `{{$now}}`

**Node 8: Slack (Confirmation)**
- Message:
  ```
  ✅ Content scheduled successfully!
  
  📅 *{{$node["Google Sheets Trigger"].json.topic}}*
  
  Scheduled for {{$node["Google Sheets Trigger"].json.target_date}}:
  {{$json.platforms_scheduled.includes('linkedin') ? '✓ LinkedIn (9 AM)\n' : ''}}
  {{$json.platforms_scheduled.includes('twitter') ? '✓ Twitter (12 PM)\n' : ''}}
  {{$json.platforms_scheduled.includes('instagram') ? '✓ Instagram (6 PM)\n' : ''}}
  
  View in Buffer: https://buffer.com/app/queue
  ```

### Trigger Type
**Google Sheets Trigger** - Fires when new row is added

### AI Integration
- **Model:** OpenAI GPT-4o
- **Purpose:** Generate platform-optimized content from raw idea
- **Cost:** ~$0.04 per content piece (3 API calls)
- **Why this model:** Best at adapting voice and format per platform

### Setup Details
1. Create Google Sheet with content calendar template
2. Get Buffer account and API token
3. Get profile IDs for each social platform from Buffer
4. Get OpenAI API key
5. Test with 2-3 sample posts
6. Adjust optimal posting times based on your audience

### Alternative Platforms
- Replace Buffer with: Hootsuite, Later, or direct API calls to each platform
- Instagram requires image URL - integrate with Canva API or manual upload

### Estimated Setup Time
**60 minutes**

### Difficulty
**Intermediate** - Multiple API integrations, conditional logic

### Monthly Time Saved
**10+ hours** - Eliminates manual content adaptation and scheduling

---

## 7. Competitor Monitor

**Description:** Track competitor websites for changes, analyze updates with AI, compile weekly report with strategic insights.

### Nodes Needed
1. **Schedule Trigger** (Daily)
2. **HTTP Request** (Fetch competitor pages - multiple)
3. **HTML Extract** (Parse content)
4. **Google Sheets** (Store historical snapshots)
5. **Function** (Detect changes)
6. **OpenAI** (Analyze changes)
7. **Function** (Aggregate weekly)
8. **OpenAI** (Generate strategic report)
9. **Gmail** or **Notion** (Deliver report)

### Step-by-Step Flow

**Node 1: Schedule Trigger**
- Frequency: `Every day at 10:00 AM`
- Timezone: Your timezone

**Node 2a-2e: HTTP Request (Fetch Competitor Pages)**
- Create 5 instances for different competitors/pages
- Examples:
  - Node 2a: Competitor A homepage - `https://competitor-a.com/`
  - Node 2b: Competitor A pricing - `https://competitor-a.com/pricing`
  - Node 2c: Competitor B blog - `https://competitor-b.com/blog`
  - Node 2d: Competitor C product page - `https://competitor-c.com/product`
  - Node 2e: Industry leader features - `https://leader.com/features`
- Method: `GET`
- Output: Full HTML

**Node 3: HTML Extract**
- Mode: `Execute once per item`
- Extraction Rules:
  - CSS Selector: Depends on target (e.g., `.pricing-table`, `article.blog-post`, `.feature-list`)
  - Extract: Text content
  - Attribute: Depends on what you're tracking
- Output: Cleaned text of monitored sections

**Node 4: Function (Calculate Content Hash)**
- Code:
  ```javascript
  const crypto = require('crypto');
  
  const content = $json.extracted_content;
  const hash = crypto.createHash('md5').update(content).digest('hex');
  
  return {
    json: {
      url: $json.url,
      competitor: $json.competitor_name,
      content: content,
      content_hash: hash,
      checked_at: new Date().toISOString(),
      word_count: content.split(/\s+/).length
    }
  };
  ```

**Node 5: Google Sheets (Load Previous Hash)**
- Spreadsheet: `Competitor Monitoring`
- Sheet: `Page Snapshots`
- Action: `Lookup` by URL
- Output: Previous hash and content

**Node 6: Function (Detect Changes)**
- Code:
  ```javascript
  const currentHash = $node["Function Hash"].json.content_hash;
  const previousHash = $node["Google Sheets Lookup"].json.content_hash;
  const previous Content = $node["Google Sheets Lookup"].json.content;
  const currentContent = $node["Function Hash"].json.content;
  
  if (currentHash !== previousHash && previousHash) {
    return {
      json: {
        changed: true,
        url: $node["Function Hash"].json.url,
        competitor: $node["Function Hash"].json.competitor,
        previous_content: previousContent,
        current_content: currentContent,
        detected_at: new Date().toISOString()
      }
    };
  }
  
  return {
    json: {
      changed: false,
      url: $node["Function Hash"].json.url
    }
  };
  ```

**Node 7: Switch (Route Based on Change)**
- Rule 1: `{{$json.changed}} === true` → Change Detected Branch
- Rule 2: `{{$json.changed}} === false` → No Change Branch

**Node 8: OpenAI (Analyze Change)**
- Only processes items from "Change Detected" branch
- Model: `gpt-4o`
- System Message:
  ```
  You are a competitive intelligence analyst. Analyze what changed on this competitor page:
  
  1. What specifically changed?
  2. What does this signal about their strategy?
  3. How significant is this change? (Low/Medium/High)
  4. Recommended response or action
  
  Be concise, strategic, actionable. Max 150 words.
  ```
- User Message:
  ```
  Competitor: {{$json.competitor}}
  Page: {{$json.url}}
  
  PREVIOUS VERSION:
  {{$json.previous_content}}
  
  CURRENT VERSION:
  {{$json.current_content}}
  ```

**Node 9: Google Sheets (Update Snapshot)**
- Action: `Append or Update`
- Sheet: `Page Snapshots`
- Columns:
  - URL
  - Competitor
  - Content Hash: `{{$node["Function Hash"].json.content_hash}}`
  - Content: `{{$node["Function Hash"].json.content}}`
  - Last Checked: `{{$node["Function Hash"].json.checked_at}}`
  - Changed: `{{$json.changed}}`
  - Analysis: `{{$node["OpenAI Analysis"].json.analysis}}`

**Node 10: Google Sheets (Append to Changes Log)**
- Only for changes detected
- Sheet: `Change History`
- Action: `Append Row`
- Columns:
  - Date: `{{$json.detected_at}}`
  - Competitor: `{{$json.competitor}}`
  - URL: `{{$json.url}}`
  - Change Summary: `{{$node["OpenAI Analysis"].json.what_changed}}`
  - Significance: `{{$node["OpenAI Analysis"].json.significance}}`
  - Recommendation: `{{$node["OpenAI Analysis"].json.recommendation}}`

**Node 11: Schedule Trigger (Weekly Report)**
- Separate workflow branch
- Frequency: `Every Monday at 9:00 AM`

**Node 12: Google Sheets (Load Week's Changes)**
- Sheet: `Change History`
- Filter: `Date > (today - 7 days)`
- Output: All changes from past week

**Node 13: OpenAI (Generate Strategic Report)**
- Model: `gpt-4o`
- System Message:
  ```
  You are a competitive intelligence strategist. Review this week's competitor activity and create an executive summary:
  
  Structure:
  1. Executive Summary (3 sentences - what matters most)
  2. Key Changes This Week (bullet list, prioritized by significance)
  3. Strategic Insights (what patterns do you see?)
  4. Recommended Actions (3-5 specific actions)
  5. Competitive Landscape Assessment
  
  Tone: Strategic, actionable, concise. Max 500 words.
  ```
- User Message:
  ```
  This week's competitor changes:
  
  {{$json.changes_array.map(c => `
  [${c.date}] ${c.competitor} - ${c.url}
  Change: ${c.change_summary}
  Significance: ${c.significance}
  Recommendation: ${c.recommendation}
  `).join('\n\n')}}
  ```

**Node 14: Gmail (Send Weekly Report)**
- To: Leadership team email list
- Subject: `🔍 Weekly Competitive Intelligence Report - {{new Date().toLocaleDateString()}}`
- Body (Markdown):
  ```
  # Weekly Competitive Intelligence Report
  
  {{$node["OpenAI Report"].json.choices[0].message.content}}
  
  ---
  
  **Monitoring:**
  - Competitor A (homepage, pricing, blog)
  - Competitor B (product pages, docs)
  - Industry Leader (features, changelog)
  
  **Changes detected this week:** {{$node["Google Sheets Week"].json.length}}
  
  [View detailed change log →](link_to_google_sheet)
  
  ---
  *Auto-generated competitive intelligence report*
  ```

### Trigger Type
- **Daily:** Schedule trigger for monitoring
- **Weekly:** Schedule trigger for report generation

### AI Integration
- **Models:** OpenAI GPT-4o
- **Purpose:** 
  - Analyze individual changes as they happen
  - Synthesize weekly strategic insights
- **Cost:** ~$0.20 per week (varies with change frequency)
- **Why this model:** Excellent at strategic analysis and pattern recognition

### Setup Details
1. List 5-10 competitor pages to monitor
2. Identify CSS selectors for content you care about
3. Set up Google Sheets with two sheets: `Page Snapshots`, `Change History`
4. Test HTML extraction with actual competitor pages
5. Adjust analysis prompt based on your industry/context
6. Consider legal/ethical implications of scraping

### Advanced Additions
- **Screenshot comparison:** Use Puppeteer node to capture visual changes
- **Price tracking:** Specific extraction for pricing changes with alerts
- **SEO monitoring:** Track meta descriptions, titles, keywords
- **API monitoring:** If competitors have public APIs, track endpoint changes

### Estimated Setup Time
**90 minutes**

### Difficulty
**Advanced** - Web scraping, hash comparison, weekly aggregation logic

### Monthly Time Saved
**6+ hours** - Eliminates manual competitor checks and research

---

## 8. Invoice Processor

**Description:** Monitor Gmail for invoice attachments, extract data via OCR, categorize with AI, log to spreadsheet, notify accounting team.

### Nodes Needed
1. **Gmail Trigger** (Watch for attachments)
2. **Function** (Filter for invoices)
3. **HTTP Request** (OCR.space or Google Vision API)
4. **OpenAI** (Extract structured data)
5. **OpenAI** (Categorize and validate)
6. **Google Sheets** (Log invoice)
7. **Slack** or **Email** (Notify accounting)
8. **Gmail** (Apply label and move)

### Step-by-Step Flow

**Node 1: Gmail Trigger**
- Trigger: `Message Received`
- Filter: `has:attachment`
- Label: `INBOX` (or specific accounting inbox)
- Poll: Every 5 minutes
- Output: Email with attachment details

**Node 2: Function (Filter for Invoice PDFs)**
- Code:
  ```javascript
  const attachments = $json.attachments || [];
  
  // Filter for PDFs with invoice-like names
  const invoiceAttachments = attachments.filter(att => {
    const filename = att.filename.toLowerCase();
    return (
      filename.endsWith('.pdf') &&
      (filename.includes('invoice') || 
       filename.includes('bill') || 
       filename.includes('receipt'))
    );
  });
  
  if (invoiceAttachments.length === 0) {
    return { json: { skip: true } };
  }
  
  return invoiceAttachments.map(att => ({
    json: {
      email_id: $json.id,
      email_subject: $json.subject,
      email_from: $json.from,
      email_date: $json.date,
      attachment_id: att.id,
      attachment_name: att.filename
    }
  }));
  ```

**Node 3: Switch (Skip or Process)**
- Rule: `{{$json.skip}} !== true` → Process branch

**Node 4: Gmail (Download Attachment)**
- Action: `Get Attachment`
- Message ID: `{{$json.email_id}}`
- Attachment ID: `{{$json.attachment_id}}`
- Output: Binary PDF data

**Node 5: HTTP Request (OCR - Extract Text)**
- Method: `POST`
- URL: `https://api.ocr.space/parse/image`
- Headers:
  - `apikey: YOUR_OCR_SPACE_KEY`
- Body (Multipart):
  - `file`: `{{$binary.data}}`
  - `language`: `eng`
  - `isTable`: `true`
- Alternative: Google Vision API for better accuracy
- Output: Extracted text from PDF

**Node 6: OpenAI (Extract Structured Data)**
- Model: `gpt-4o`
- System Message:
  ```
  Extract invoice data from this OCR text. Return JSON:
  {
    "invoice_number": "...",
    "invoice_date": "YYYY-MM-DD",
    "due_date": "YYYY-MM-DD",
    "vendor_name": "...",
    "vendor_address": "...",
    "total_amount": 0.00,
    "currency": "USD",
    "line_items": [
      {"description": "...", "amount": 0.00}
    ],
    "tax_amount": 0.00,
    "payment_terms": "..."
  }
  
  If any field is unclear, use null. Be precise with numbers and dates.
  ```
- User Message: `{{$node["OCR"].json.ParsedText}}`
- Output Mode: `JSON`

**Node 7: OpenAI (Categorize & Validate)**
- Model: `gpt-4o-mini`
- System Message:
  ```
  Categorize this invoice and validate it. Return JSON:
  {
    "category": "Software|Hardware|Consulting|Marketing|Office|Legal|Other",
    "subcategory": "...",
    "is_valid": true/false,
    "validation_notes": "Any issues or red flags",
    "requires_review": true/false,
    "confidence": "high|medium|low"
  }
  ```
- User Message:
  ```
  Vendor: {{$json.vendor_name}}
  Amount: {{$json.total_amount}} {{$json.currency}}
  Description: {{$json.line_items[0].description}}
  ```

**Node 8: Function (Merge & Format)**
- Code:
  ```javascript
  const invoice = $node["OpenAI Extract"].json;
  const classification = $node["OpenAI Categorize"].json;
  const email = $node["Function Filter"].json;
  
  return {
    json: {
      // Invoice data
      invoice_number: invoice.invoice_number,
      invoice_date: invoice.invoice_date,
      due_date: invoice.due_date,
      vendor_name: invoice.vendor_name,
      vendor_address: invoice.vendor_address,
      total_amount: invoice.total_amount,
      currency: invoice.currency,
      tax_amount: invoice.tax_amount,
      
      // Classification
      category: classification.category,
      subcategory: classification.subcategory,
      
      // Metadata
      received_date: email.email_date,
      email_from: email.email_from,
      attachment_name: email.attachment_name,
      
      // Status
      status: classification.requires_review ? 'Needs Review' : 'Ready to Pay',
      confidence: classification.confidence,
      validation_notes: classification.validation_notes,
      
      // Links
      email_link: `https://mail.google.com/mail/u/0/#all/${email.email_id}`
    }
  };
  ```

**Node 9: Google Sheets (Log Invoice)**
- Spreadsheet: `Invoice Tracker`
- Sheet: `Invoices`
- Action: `Append Row`
- Columns: Map all fields from Node 8

**Node 10: Switch (Review Required?)**
- Rule 1: `{{$json.requires_review}} === true` → Review Branch
- Rule 2: `{{$json.requires_review}} === false` → Auto-Process Branch

**Node 11a: Slack (Needs Review Notification)**
- Channel: `#accounting`
- Message:
  ```
  ⚠️ *Invoice Needs Review*
  
  📄 *{{$json.invoice_number}}*
  From: {{$json.vendor_name}}
  Amount: {{$json.currency}} {{$json.total_amount}}
  Due: {{$json.due_date}}
  
  ❗ Issue: {{$json.validation_notes}}
  Confidence: {{$json.confidence}}
  
  [View Email]({{$json.email_link}}) | [View in Sheet](link_to_row)
  ```

**Node 11b: Slack (Auto-Processed Notification)**
- Channel: `#accounting`
- Message:
  ```
  ✅ *New Invoice Auto-Processed*
  
  📄 {{$json.invoice_number}}
  From: {{$json.vendor_name}}
  Amount: {{$json.currency}} {{$json.total_amount}}
  Category: {{$json.category}} / {{$json.subcategory}}
  Due: {{$json.due_date}}
  
  Status: Ready to pay
  [View in Sheet](link_to_row)
  ```

**Node 12: Gmail (Apply Label & Archive)**
- Action: `Add Label`
- Label: `Invoices/Processed`
- Message ID: `{{$node["Function Filter"].json.email_id}}`
- Also: Remove from INBOX

### Trigger Type
**Gmail Trigger** - Polls every 5 minutes for new emails with attachments

### AI Integration
- **Models:** 
  - GPT-4o for extraction (better with complex layouts)
  - GPT-4o-mini for categorization (cheaper, sufficient)
- **Purpose:** Extract structured data from OCR text, categorize and validate
- **Cost:** ~$0.03 per invoice
- **Why these models:** GPT-4o excellent at parsing messy OCR output, mini good enough for classification

### Setup Details
1. Get OCR.space API key (free tier: 25,000 requests/month) or Google Vision API
2. Get OpenAI API key
3. Create Google Sheet with proper columns
4. Set up Slack webhook or accounting team email
5. Test with 10 sample invoices of varying formats
6. Create Gmail labels: `Invoices/Processed`, `Invoices/Needs Review`

### Accuracy Notes
- OCR accuracy varies by PDF quality (90-99%)
- AI extraction accuracy: 85-95% depending on format
- Always have human review for high-value invoices
- Train the system over time by adjusting prompts based on errors

### Estimated Setup Time
**55 minutes**

### Difficulty
**Intermediate** - OCR integration, structured data extraction

### Monthly Time Saved
**8+ hours** - Eliminates manual data entry and invoice processing

---

## 9. Job Application Tracker

**Description:** Automatically detect job application emails, extract company/role details, log to Airtable, set follow-up reminders.

### Nodes Needed
1. **Gmail Trigger** (Filter for application-related emails)
2. **Function** (Parse application details)
3. **OpenAI** (Extract structured data)
4. **Airtable** (Create record)
5. **Function** (Calculate follow-up dates)
6. **Google Calendar** (Create follow-up reminders)
7. **Telegram** (Confirmation notification)

### Step-by-Step Flow

**Node 1: Gmail Trigger**
- Trigger: `Message Sent` OR `Message Received`
- Filter: 
  - Sent: `to:(*@*.* AND (jobs OR careers OR hiring OR apply))`
  - Received: `from:(*@*.* AND (application OR applied OR received))`
- Label: `Jobs` (create this label)
- Poll: Every 10 minutes

**Node 2: Function (Determine Email Type)**
- Code:
  ```javascript
  const isSent = $json.labelIds?.includes('SENT');
  const isReceived = !isSent;
  
  return {
    json: {
      email_type: isSent ? 'application_sent' : 'response_received',
      email_id: $json.id,
      email_subject: $json.subject,
      email_from: $json.from,
      email_to: $json.to,
      email_body: $json.body,
      email_date: $json.date,
      email_thread_id: $json.threadId
    }
  };
  ```

**Node 3: OpenAI (Extract Application Details)**
- Model: `gpt-4o`
- System Message:
  ```
  Extract job application details from this email. Return JSON:
  {
    "company_name": "...",
    "job_title": "...",
    "job_location": "City, State/Country",
    "application_date": "YYYY-MM-DD",
    "job_posting_url": "...",
    "contact_name": "...",
    "contact_email": "...",
    "application_status": "Applied|Screening|Interview Scheduled|Rejected|Offer",
    "salary_range": "...",
    "notes": "Any important details from email"
  }
  
  Infer missing data where possible. Use null if truly unknown.
  ```
- User Message:
  ```
  Email Type: {{$json.email_type}}
  Subject: {{$json.email_subject}}
  From: {{$json.email_from}}
  To: {{$json.email_to}}
  Body:
  {{$json.email_body}}
  ```

**Node 4: Function (Enrich with Metadata)**
- Code:
  ```javascript
  const extracted = $json;
  const email = $node["Function Type"].json;
  
  // Calculate follow-up dates
  const appliedDate = new Date(extracted.application_date);
  const followUp1 = new Date(appliedDate);
  followUp1.setDate(followUp1.getDate() + 7); // 1 week
  const followUp2 = new Date(appliedDate);
  followUp2.setDate(followUp2.getDate() + 14); // 2 weeks
  
  return {
    json: {
      // Core data
      company_name: extracted.company_name,
      job_title: extracted.job_title,
      job_location: extracted.job_location,
      application_date: extracted.application_date,
      job_posting_url: extracted.job_posting_url,
      
      // Contacts
      contact_name: extracted.contact_name,
      contact_email: extracted.contact_email,
      
      // Status
      current_status: extracted.application_status,
      
      // Metadata
      salary_range: extracted.salary_range,
      notes: extracted.notes,
      email_thread_url: `https://mail.google.com/mail/u/0/#all/${email.email_thread_id}`,
      
      // Reminders
      follow_up_1_date: followUp1.toISOString().split('T')[0],
      follow_up_2_date: followUp2.toISOString().split('T')[0],
      
      // Tracking
      created_at: new Date().toISOString(),
      last_updated: new Date().toISOString()
    }
  };
  ```

**Node 5: Airtable (Check if Record Exists)**
- Action: `Search Records`
- Base: `Job Search Tracker`
- Table: `Applications`
- Formula: `{Company Name} = "{{$json.company_name}}" AND {Job Title} = "{{$json.job_title}}"`

**Node 6: Switch (New or Update?)**
- Rule 1: `{{$json.records.length}} === 0` → Create New
- Rule 2: `{{$json.records.length}} > 0` → Update Existing

**Node 7a: Airtable (Create New Record)**
- Action: `Create Record`
- Base: `Job Search Tracker`
- Table: `Applications`
- Fields: Map all fields from Node 4

**Node 7b: Airtable (Update Existing Record)**
- Action: `Update Record`
- Record ID: `{{$node["Airtable Check"].json.records[0].id}}`
- Fields to update:
  - Current Status
  - Last Updated
  - Notes (append new notes)
  - Email Thread URL

**Node 8: Google Calendar (Create Follow-Up 1)**
- Action: `Create Event`
- Calendar: Your primary calendar
- Event details:
  - Title: `Follow up: {{$json.company_name}} - {{$json.job_title}}`
  - Description: 
    ```
    Follow up on job application
    
    Company: {{$json.company_name}}
    Role: {{$json.job_title}}
    Applied: {{$json.application_date}}
    
    [View application email]({{$json.email_thread_url}})
    [View in tracker](airtable_link)
    ```
  - Start: `{{$json.follow_up_1_date}}T09:00:00`
  - End: `{{$json.follow_up_1_date}}T09:30:00`
  - Reminder: 1 day before

**Node 9: Google Calendar (Create Follow-Up 2)**
- Same as Node 8, but for `follow_up_2_date`

**Node 10: Telegram (Confirmation)**
- Message:
  ```
  {{$json.is_new ? '🆕 New Application Tracked' : '📝 Application Updated'}}
  
  🏢 *{{$json.company_name}}*
  💼 {{$json.job_title}}
  📍 {{$json.job_location}}
  
  Status: {{$json.current_status}}
  Applied: {{$json.application_date}}
  
  ⏰ Follow-up reminders set:
  - {{$json.follow_up_1_date}}
  - {{$json.follow_up_2_date}}
  
  [View in Airtable](link) | [Email Thread]({{$json.email_thread_url}})
  ```

### Trigger Type
**Gmail Trigger** - Polls every 10 minutes for sent/received application emails

### AI Integration
- **Model:** OpenAI GPT-4o
- **Purpose:** Extract structured application details from unstructured emails
- **Cost:** ~$0.01 per email
- **Why this model:** Excellent at extracting entities and inferring missing information

### Setup Details
1. Create Airtable base: `Job Search Tracker`
2. Create table: `Applications` with these fields:
   - Company Name (Text)
   - Job Title (Text)
   - Job Location (Text)
   - Application Date (Date)
   - Current Status (Single Select: Applied, Screening, Interview, Rejected, Offer)
   - Job Posting URL (URL)
   - Contact Name (Text)
   - Contact Email (Email)
   - Salary Range (Text)
   - Notes (Long Text)
   - Email Thread URL (URL)
   - Follow Up 1 (Date)
   - Follow Up 2 (Date)
   - Created At (Date)
   - Last Updated (Date)
3. Get Airtable API key and base ID
4. Create Gmail label: `Jobs`
5. Test with past application emails

### Advanced Features
- **Interview scheduling:** Parse interview invites and add to calendar with prep time
- **Rejection tracking:** Automatically update status when rejection emails arrive
- **Company research:** Trigger research workflow when new application logged
- **Analytics:** Track application-to-interview rate by job title, company size, etc.

### Estimated Setup Time
**40 minutes**

### Difficulty
**Beginner** - Good introduction to CRM integration + AI extraction

### Monthly Time Saved
**5+ hours** - Eliminates manual tracking, ensures no follow-up is missed

---

## 10. Customer Feedback Analyzer

**Description:** Aggregate feedback from multiple sources (email, surveys, support tickets, social), analyze sentiment and themes with AI, generate dashboard insights.

### Nodes Needed
1. **Schedule Trigger** (Daily aggregation)
2. **Gmail** (Fetch feedback emails)
3. **HTTP Request** (Typeform API - survey responses)
4. **HTTP Request** (Zendesk/Intercom API - support tickets)
5. **HTTP Request** (Twitter API - mentions)
6. **Function** (Merge all sources)
7. **OpenAI** (Sentiment analysis per item)
8. **Function** (Aggregate sentiment)
9. **OpenAI** (Extract themes and topics)
10. **OpenAI** (Generate insights summary)
11. **Google Sheets** (Log to dashboard)
12. **Slack** (Daily summary)

### Step-by-Step Flow

**Node 1: Schedule Trigger**
- Frequency: `Every day at 8:00 AM`
- Looks back: 24 hours of feedback

**Node 2: Gmail (Fetch Feedback Emails)**
- Action: `Search`
- Query: `label:feedback after:{{$now.minus({days: 1}).toFormat('yyyy/MM/dd')}}`
- Max Results: 50
- Output: Subject, from, body, date

**Node 3: HTTP Request (Typeform Responses)**
- Method: `GET`
- URL: `https://api.typeform.com/forms/YOUR_FORM_ID/responses?since={{$now.minus({days: 1}).toISO()}}`
- Headers: `Authorization: Bearer YOUR_TYPEFORM_TOKEN`
- Output: Survey responses from last 24h

**Node 4: HTTP Request (Zendesk Tickets)**
- Method: `GET`
- URL: `https://YOUR_DOMAIN.zendesk.com/api/v2/search.json?query=type:ticket created>{{$now.minus({days: 1}).toFormat('yyyy-MM-dd')}}`
- Authentication: Basic auth (email + API token)
- Output: Support tickets from last 24h

**Node 5: HTTP Request (Twitter Mentions)**
- Method: `GET`
- URL: `https://api.twitter.com/2/tweets/search/recent?query=@YOUR_HANDLE&start_time={{$now.minus({days: 1}).toISO()}}`
- Headers: `Authorization: Bearer YOUR_TWITTER_BEARER_TOKEN`
- Output: Mentions from last 24h

**Node 6: Function (Normalize All Feedback)**
- Code:
  ```javascript
  const allFeedback = [];
  
  // Process Gmail
  const emails = $node["Gmail"].json;
  emails.forEach(email => {
    allFeedback.push({
      source: 'Email',
      text: email.body,
      author: email.from,
      date: email.date,
      id: email.id,
      url: `https://mail.google.com/mail/u/0/#all/${email.id}`
    });
  });
  
  // Process Typeform
  const surveys = $node["Typeform"].json.items || [];
  surveys.forEach(response => {
    const answers = response.answers.map(a => 
      `${a.field.title}: ${a.text || a.choice?.label || a.number}`
    ).join('\n');
    allFeedback.push({
      source: 'Survey',
      text: answers,
      author: response.hidden?.email || 'Anonymous',
      date: response.submitted_at,
      id: response.token,
      url: `https://admin.typeform.com/form/YOUR_FORM_ID/results#responses`
    });
  });
  
  // Process Zendesk
  const tickets = $node["Zendesk"].json.results || [];
  tickets.forEach(ticket => {
    allFeedback.push({
      source: 'Support',
      text: ticket.description,
      author: ticket.requester.name,
      date: ticket.created_at,
      id: ticket.id,
      url: `https://YOUR_DOMAIN.zendesk.com/agent/tickets/${ticket.id}`
    });
  });
  
  // Process Twitter
  const tweets = $node["Twitter"].json.data || [];
  tweets.forEach(tweet => {
    allFeedback.push({
      source: 'Twitter',
      text: tweet.text,
      author: tweet.author_id,
      date: tweet.created_at,
      id: tweet.id,
      url: `https://twitter.com/i/web/status/${tweet.id}`
    });
  });
  
  return allFeedback.map(f => ({ json: f }));
  ```

**Node 7: OpenAI (Sentiment Analysis)**
- Mode: `Execute once per item`
- Model: `gpt-4o-mini` (cheap for bulk processing)
- System Message:
  ```
  Analyze the sentiment of this customer feedback. Return JSON:
  {
    "sentiment": "positive|neutral|negative|mixed",
    "sentiment_score": 0.0-1.0,
    "emotion": "happy|frustrated|confused|angry|excited|neutral",
    "urgency": "low|medium|high",
    "is_actionable": true/false,
    "one_line_summary": "..."
  }
  ```
- User Message:
  ```
  Source: {{$json.source}}
  Feedback: {{$json.text}}
  ```

**Node 8: Function (Aggregate All Results)**
- Mode: `All Items`
- Code:
  ```javascript
  const items = $input.all();
  
  const analyzed = items.map(item => ({
    source: item.json.source,
    text: item.json.text,
    author: item.json.author,
    date: item.json.date,
    url: item.json.url,
    sentiment: item.json.sentiment_analysis.sentiment,
    sentiment_score: item.json.sentiment_analysis.sentiment_score,
    emotion: item.json.sentiment_analysis.emotion,
    urgency: item.json.sentiment_analysis.urgency,
    is_actionable: item.json.sentiment_analysis.is_actionable,
    summary: item.json.sentiment_analysis.one_line_summary
  }));
  
  // Calculate aggregate metrics
  const total = analyzed.length;
  const positive = analyzed.filter(a => a.sentiment === 'positive').length;
  const negative = analyzed.filter(a => a.sentiment === 'negative').length;
  const neutral = analyzed.filter(a => a.sentiment === 'neutral').length;
  const avgScore = analyzed.reduce((sum, a) => sum + a.sentiment_score, 0) / total;
  const urgent = analyzed.filter(a => a.urgency === 'high');
  const actionable = analyzed.filter(a => a.is_actionable);
  
  return [{
    json: {
      date: new Date().toISOString().split('T')[0],
      total_feedback: total,
      by_source: {
        email: analyzed.filter(a => a.source === 'Email').length,
        survey: analyzed.filter(a => a.source === 'Survey').length,
        support: analyzed.filter(a => a.source === 'Support').length,
        twitter: analyzed.filter(a => a.source === 'Twitter').length
      },
      sentiment_breakdown: {
        positive: positive,
        negative: negative,
        neutral: neutral,
        positive_pct: (positive / total * 100).toFixed(1),
        negative_pct: (negative / total * 100).toFixed(1)
      },
      avg_sentiment_score: avgScore.toFixed(2),
      urgent_items: urgent,
      actionable_items: actionable,
      all_feedback: analyzed
    }
  }];
  ```

**Node 9: OpenAI (Extract Themes)**
- Model: `gpt-4o`
- System Message:
  ```
  Analyze this collection of customer feedback and identify key themes. Return JSON:
  {
    "top_themes": [
      {
        "theme": "Theme name",
        "frequency": 0-10 scale,
        "sentiment": "positive|negative|mixed",
        "example": "Representative feedback quote"
      }
    ],
    "feature_requests": ["...", "...", "..."],
    "pain_points": ["...", "...", "..."],
    "praise": ["What customers love"],
    "urgent_issues": ["Issues needing immediate attention"]
  }
  
  Limit to 5-7 themes maximum. Be specific and actionable.
  ```
- User Message:
  ```
  Today's feedback ({{$json.total_feedback}} items):
  
  {{$json.all_feedback.slice(0, 50).map(f => `[${f.source}] ${f.summary} (${f.sentiment})`).join('\n')}}
  ```

**Node 10: OpenAI (Generate Executive Summary)**
- Model: `gpt-4o`
- System Message:
  ```
  Create an executive summary of today's customer feedback:
  
  Structure:
  1. Overview (2-3 sentences - overall mood + volume)
  2. Key Themes (top 3-5 patterns)
  3. Urgent Issues (anything needing immediate action)
  4. Positive Highlights (what's working well)
  5. Recommendations (2-3 actionable next steps)
  
  Tone: Executive-friendly, data-driven, actionable. Max 300 words.
  ```
- User Message:
  ```
  Metrics:
  - Total: {{$node["Function Aggregate"].json.total_feedback}}
  - Sentiment: {{$node["Function Aggregate"].json.sentiment_breakdown.positive_pct}}% positive, {{$node["Function Aggregate"].json.sentiment_breakdown.negative_pct}}% negative
  - Urgent: {{$node["Function Aggregate"].json.urgent_items.length}}
  - Actionable: {{$node["Function Aggregate"].json.actionable_items.length}}
  
  Themes:
  {{$json.top_themes.map(t => `- ${t.theme} (${t.sentiment}, frequency: ${t.frequency}/10)`).join('\n')}}
  
  Feature Requests:
  {{$json.feature_requests.join('\n')}}
  
  Pain Points:
  {{$json.pain_points.join('\n')}}
  ```

**Node 11: Google Sheets (Log Daily Metrics)**
- Spreadsheet: `Feedback Dashboard`
- Sheet: `Daily Summary`
- Action: `Append Row`
- Columns:
  - Date
  - Total Feedback
  - Email Count
  - Survey Count
  - Support Count
  - Twitter Count
  - Positive %
  - Negative %
  - Avg Sentiment Score
  - Urgent Count
  - Top Theme 1
  - Top Theme 2
  - Top Theme 3
  - Executive Summary

**Node 12: Google Sheets (Log Individual Feedback)**
- Sheet: `All Feedback`
- Action: `Append Multiple Rows`
- Data: `{{$node["Function Aggregate"].json.all_feedback}}`

**Node 13: Slack (Daily Report)**
- Channel: `#product` or `#customer-insights`
- Message:
  ```
  📊 *Daily Customer Feedback Report* - {{$node["Function Aggregate"].json.date}}
  
  📈 *Metrics*
  • Total feedback: {{$node["Function Aggregate"].json.total_feedback}}
  • Sources: Email ({{$node["Function Aggregate"].json.by_source.email}}), Survey ({{$node["Function Aggregate"].json.by_source.survey}}), Support ({{$node["Function Aggregate"].json.by_source.support}}), Twitter ({{$node["Function Aggregate"].json.by_source.twitter}})
  • Sentiment: {{$node["Function Aggregate"].json.sentiment_breakdown.positive_pct}}% 👍 {{$node["Function Aggregate"].json.sentiment_breakdown.negative_pct}}% 👎
  • Avg Score: {{$node["Function Aggregate"].json.avg_sentiment_score}}/1.0
  
  🎯 *Top Themes*
  {{$node["OpenAI Themes"].json.top_themes.slice(0, 3).map((t, i) => `${i+1}. ${t.theme} (${t.sentiment})`).join('\n')}}
  
  ⚠️ *Urgent Issues* ({{$node["Function Aggregate"].json.urgent_items.length}})
  {{$node["Function Aggregate"].json.urgent_items.slice(0, 3).map(u => `• ${u.summary}`).join('\n')}}
  
  ---
  
  {{$node["OpenAI Summary"].json.choices[0].message.content}}
  
  ---
  
  [View Dashboard](link_to_google_sheet) | [View All Feedback](link_to_all_feedback_sheet)
  ```

### Trigger Type
**Schedule Trigger** - Daily at 8:00 AM

### AI Integration
- **Models:** 
  - GPT-4o-mini for bulk sentiment analysis
  - GPT-4o for theme extraction and summary generation
- **Purpose:** Sentiment analysis, theme extraction, executive summary
- **Cost:** ~$0.30 per day (depends on feedback volume)
- **Why these models:** Mini efficient for repetitive analysis, GPT-4o better at synthesis and strategic insights

### Setup Details
1. Connect all feedback sources (Gmail, Typeform, Zendesk, Twitter)
2. Create Google Sheet: `Feedback Dashboard` with two sheets
3. Get API keys for all services
4. Test with last week's feedback first
5. Adjust theme extraction prompt based on your product/industry
6. Set up Slack webhook

### Advanced Features
- **Real-time alerts:** Add webhook trigger for urgent/negative feedback
- **Competitive intelligence:** Track mentions of competitors in feedback
- **Trend analysis:** Compare week-over-week, month-over-month metrics
- **Auto-response:** Draft responses to common feedback themes
- **Customer segmentation:** Analyze sentiment by customer tier, industry, etc.

### Estimated Setup Time
**80 minutes**

### Difficulty
**Advanced** - Multiple API integrations, complex aggregation logic

### Monthly Time Saved
**12+ hours** - Eliminates manual feedback review and theme analysis

---

## 11. Personal CRM

**Description:** Auto-log interactions from calendar and email, score relationship strength, generate follow-up reminders based on recency and importance.

### Nodes Needed
1. **Schedule Trigger** (Daily sync)
2. **Google Calendar** (Fetch meetings from last 24h)
3. **Gmail** (Fetch sent/received emails)
4. **Function** (Extract unique contacts)
5. **Airtable** (Lookup existing contacts)
6. **OpenAI** (Classify relationship and context)
7. **Function** (Calculate relationship score)
8. **Airtable** (Create or update contact)
9. **Function** (Determine follow-up needs)
10. **Google Calendar** (Create follow-up reminders)
11. **Notion** (Optional: Create relationship note)

### Step-by-Step Flow

**Node 1: Schedule Trigger**
- Frequency: `Every day at 9:00 PM`
- Purpose: End-of-day relationship logging

**Node 2: Google Calendar (Fetch Today's Meetings)**
- Action: `Get Many`
- Calendar: Your primary calendar
- Time Min: `{{$now.startOf('day').toISO()}}`
- Time Max: `{{$now.endOf('day').toISO()}}`
- Output: Meetings with attendees

**Node 3: Function (Extract Calendar Contacts)**
- Code:
  ```javascript
  const events = $input.all();
  const contacts = [];
  
  events.forEach(event => {
    if (!event.json.attendees) return;
    
    event.json.attendees.forEach(attendee => {
      // Skip yourself and rooms
      if (attendee.email.includes('your-domain.com') || attendee.organizer) return;
      
      contacts.push({
        email: attendee.email,
        name: attendee.displayName || attendee.email.split('@')[0],
        interaction_type: 'Meeting',
        interaction_date: event.json.start.dateTime,
        context: event.json.summary,
        duration_minutes: Math.round(
          (new Date(event.json.end.dateTime) - new Date(event.json.start.dateTime)) / 60000
        ),
        notes: event.json.description
      });
    });
  });
  
  return contacts.map(c => ({ json: c }));
  ```

**Node 4: Gmail (Fetch Today's Emails)**
- Action: `Search`
- Query: `after:{{$now.minus({days: 1}).toFormat('yyyy/MM/dd')}} (from:* OR to:*)`
- Max Results: 100
- Only fetch emails with actual conversation (not newsletters)

**Node 5: Function (Extract Email Contacts)**
- Code:
  ```javascript
  const emails = $input.all();
  const contacts = [];
  
  emails.forEach(email => {
    // Determine if sent or received
    const isSent = email.json.labelIds?.includes('SENT');
    const otherParty = isSent ? email.json.to : email.json.from;
    
    // Skip newsletters and automated emails
    if (email.json.from.includes('noreply') || 
        email.json.from.includes('newsletter') ||
        email.json.subject.toLowerCase().includes('unsubscribe')) {
      return;
    }
    
    contacts.push({
      email: otherParty,
      name: otherParty.split('@')[0], // Will be enriched later
      interaction_type: isSent ? 'Email Sent' : 'Email Received',
      interaction_date: email.json.date,
      context: email.json.subject,
      email_preview: email.json.snippet,
      thread_id: email.json.threadId
    });
  });
  
  return contacts.map(c => ({ json: c }));
  ```

**Node 6: Function (Merge and Deduplicate)**
- Code:
  ```javascript
  const calendarContacts = $node["Function Calendar"].json || [];
  const emailContacts = $node["Function Email"].json || [];
  
  const allContacts = [...calendarContacts, ...emailContacts];
  
  // Group by email
  const contactMap = {};
  allContacts.forEach(contact => {
    if (!contactMap[contact.email]) {
      contactMap[contact.email] = {
        email: contact.email,
        name: contact.name,
        interactions: []
      };
    }
    
    contactMap[contact.email].interactions.push({
      type: contact.interaction_type,
      date: contact.interaction_date,
      context: contact.context,
      duration: contact.duration_minutes,
      notes: contact.notes || contact.email_preview
    });
  });
  
  return Object.values(contactMap).map(c => ({ json: c }));
  ```

**Node 7: Airtable (Lookup Contact)**
- Mode: `Execute once per item`
- Action: `Search Records`
- Base: `Personal CRM`
- Table: `Contacts`
- Formula: `{Email} = "{{$json.email}}"`

**Node 8: OpenAI (Classify Relationship)**
- Only for new contacts or those needing classification
- Model: `gpt-4o-mini`
- System Message:
  ```
  Analyze this contact and their interaction history. Return JSON:
  {
    "relationship_type": "Professional|Personal|Both",
    "category": "Colleague|Client|Investor|Friend|Family|Mentor|Vendor|Other",
    "importance": "high|medium|low",
    "suggested_follow_up_days": 7-90,
    "relationship_notes": "Brief context about this person"
  }
  ```
- User Message:
  ```
  Contact: {{$json.name}} ({{$json.email}})
  
  Recent interactions:
  {{$json.interactions.map(i => `- ${i.type}: ${i.context} (${i.date})`).join('\n')}}
  ```

**Node 9: Function (Calculate Relationship Score)**
- Code:
  ```javascript
  const contact = $json;
  const existing = $node["Airtable Lookup"].json.records[0];
  
  // Calculate interaction frequency
  const allInteractions = [
    ...contact.interactions,
    ...(existing?.fields['Interaction History'] || [])
  ];
  
  const last30Days = allInteractions.filter(i => 
    new Date(i.date) > new Date(Date.now() - 30 * 24 * 60 * 60 * 1000)
  );
  
  const last90Days = allInteractions.filter(i => 
    new Date(i.date) > new Date(Date.now() - 90 * 24 * 60 * 60 * 1000)
  );
  
  // Score based on:
  // - Recency of last interaction
  // - Frequency (interactions per month)
  // - Importance level
  // - Interaction types (meetings > emails)
  
  const daysSinceLastContact = Math.floor(
    (Date.now() - new Date(contact.interactions[0].date)) / (24 * 60 * 60 * 1000)
  );
  
  const recencyScore = Math.max(0, 100 - daysSinceLastContact);
  const frequencyScore = Math.min(100, last30Days.length * 10);
  const importanceMultiplier = {
    'high': 1.5,
    'medium': 1.0,
    'low': 0.7
  }[contact.importance || 'medium'];
  
  const meetingBonus = contact.interactions.filter(i => i.type === 'Meeting').length * 10;
  
  const relationshipScore = Math.min(100, 
    (recencyScore * 0.4 + frequencyScore * 0.4 + meetingBonus) * importanceMultiplier
  );
  
  return {
    json: {
      ...contact,
      relationship_score: Math.round(relationshipScore),
      days_since_contact: daysSinceLastContact,
      interactions_last_30d: last30Days.length,
      interactions_last_90d: last90Days.length,
      last_contact_date: contact.interactions[0].date,
      needs_follow_up: daysSinceLastContact > contact.suggested_follow_up_days
    }
  };
  ```

**Node 10: Airtable (Create or Update Contact)**
- Action: Conditional (Create if new, Update if exists)
- Base: `Personal CRM`
- Table: `Contacts`
- Fields:
  - Name: `{{$json.name}}`
  - Email: `{{$json.email}}`
  - Relationship Type: `{{$json.relationship_type}}`
  - Category: `{{$json.category}}`
  - Importance: `{{$json.importance}}`
  - Relationship Score: `{{$json.relationship_score}}`
  - Last Contact Date: `{{$json.last_contact_date}}`
  - Days Since Contact: `{{$json.days_since_contact}}`
  - Interactions (30d): `{{$json.interactions_last_30d}}`
  - Interactions (90d): `{{$json.interactions_last_90d}}`
  - Suggested Follow-Up Days: `{{$json.suggested_follow_up_days}}`
  - Interaction History: Append new interactions as JSON array
  - Last Updated: `{{$now}}`

**Node 11: Function (Identify Follow-Up Needed)**
- Code:
  ```javascript
  const items = $input.all();
  
  const needsFollowUp = items.filter(item => {
    const contact = item.json;
    
    // Follow-up needed if:
    // 1. High importance + 7+ days since contact
    // 2. Medium importance + days > suggested follow-up
    // 3. Low relationship score (<40) for important contacts
    
    if (contact.importance === 'high' && contact.days_since_contact > 7) {
      return true;
    }
    
    if (contact.days_since_contact > contact.suggested_follow_up_days) {
      return true;
    }
    
    if (contact.importance === 'high' && contact.relationship_score < 40) {
      return true;
    }
    
    return false;
  });
  
  return needsFollowUp;
  ```

**Node 12: Google Calendar (Create Follow-Up Reminder)**
- Mode: `Execute once per item`
- Action: `Create Event`
- Calendar: Your primary calendar
- Event details:
  - Title: `☎️ Follow up: {{$json.name}}`
  - Description:
    ```
    Time to reconnect with {{$json.name}}
    
    Last contact: {{$json.days_since_contact}} days ago
    Relationship score: {{$json.relationship_score}}/100
    Category: {{$json.category}}
    
    Last interaction: {{$json.interactions[0].context}}
    
    Suggested talking points:
    - [Let AI generate based on history]
    
    [View full profile in Airtable](link)
    ```
  - Start: Tomorrow at 10:00 AM
  - Duration: 30 min
  - Reminder: 1 hour before

**Node 13: Notion (Create Relationship Note - Optional)**
- For high-importance contacts
- Database: `People`
- Properties:
  - Name: `{{$json.name}}`
  - Email: `{{$json.email}}`
  - Last Contacted: `{{$json.last_contact_date}}`
  - Relationship Score: `{{$json.relationship_score}}`
  - Notes: Template with recent interactions

**Node 14: Telegram (Daily CRM Summary)**
- Message:
  ```
  📊 *Daily Relationship Update*
  
  Today's interactions: {{$node["Function Merge"].json.length}} contacts
  
  🔥 *Strong Relationships* (Score 80+):
  {{$json.strong_relationships.map(c => `• ${c.name} (${c.relationship_score})`).join('\n')}}
  
  ⚠️ *Needs Attention* ({{$json.needs_follow_up_count}}):
  {{$json.needs_follow_up.slice(0, 5).map(c => `• ${c.name} - ${c.days_since_contact}d ago`).join('\n')}}
  
  📅 Follow-up reminders created: {{$json.reminders_created}}
  
  [View CRM](airtable_link)
  ```

### Trigger Type
**Schedule Trigger** - Daily at 9:00 PM (end of day sync)

### AI Integration
- **Model:** OpenAI GPT-4o-mini
- **Purpose:** Classify relationships and suggest follow-up timing
- **Cost:** ~$0.10 per day
- **Why this model:** Sufficient for relationship classification, cost-effective for daily runs

### Setup Details
1. Create Airtable base: `Personal CRM`
2. Create table: `Contacts` with all fields listed above
3. Connect Google Calendar and Gmail
4. Get OpenAI API key
5. Test with last week's interactions
6. Adjust relationship scoring formula based on your networking style
7. Customize follow-up thresholds (high importance = 7 days, etc.)

### Airtable Table Structure
**Contacts** table:
- Name (Text)
- Email (Email)
- Relationship Type (Single Select: Professional, Personal, Both)
- Category (Single Select: Colleague, Client, Investor, Friend, etc.)
- Importance (Single Select: High, Medium, Low)
- Relationship Score (Number, 0-100)
- Last Contact Date (Date)
- Days Since Contact (Formula: `DATETIME_DIFF(NOW(), {Last Contact Date}, 'days')`)
- Interactions (30d) (Number)
- Interactions (90d) (Number)
- Suggested Follow-Up Days (Number)
- Interaction History (Long Text - JSON array)
- Notes (Long Text)
- LinkedIn (URL)
- Company (Text)
- Last Updated (Date)

### Advanced Features
- **Enrichment:** Add Clearbit lookup for new contacts
- **Email drafts:** AI-generated follow-up email drafts based on history
- **Birthday tracking:** Parse calendar for birthdays, set annual reminders
- **Relationship trends:** Visualize relationship score over time
- **Network map:** Identify mutual connections and warm intro paths

### Estimated Setup Time
**90 minutes**

### Difficulty
**Advanced** - Complex scoring algorithm, multi-source aggregation

### Monthly Time Saved
**10+ hours** - Eliminates manual CRM logging, ensures no relationship falls through cracks

---

## 12. AI Research Assistant

**Description:** Input a research topic, AI performs web search, synthesizes findings into structured brief, saves to Notion with sources.

### Nodes Needed
1. **Webhook** or **Manual Trigger** (Input topic)
2. **HTTP Request** (SerpAPI - web search)
3. **HTTP Request** (Fetch top articles via web scraping)
4. **OpenAI** (Summarize each article)
5. **OpenAI** (Synthesize all findings)
6. **OpenAI** (Generate key takeaways and questions)
7. **Notion** (Create research page)
8. **Telegram** (Notify completion)

### Step-by-Step Flow

**Node 1: Webhook**
- Path: `/research`
- Expected payload:
  ```json
  {
    "topic": "AI regulation in the EU",
    "depth": "standard|deep",
    "focus": "overview|technical|business|legal"
  }
  ```

**Node 2: HTTP Request (SerpAPI - Web Search)**
- Method: `GET`
- URL: `https://serpapi.com/search?q={{$json.topic}}&num=10&api_key=YOUR_KEY`
- Output: Top 10 search results with titles, snippets, URLs

**Node 3: Function (Filter and Rank Sources)**
- Code:
  ```javascript
  const results = $json.organic_results || [];
  
  // Filter out low-quality sources
  const filtered = results.filter(result => {
    const domain = new URL(result.link).hostname;
    
    // Prioritize quality domains
    const highQuality = [
      'edu', 'gov', '.org',
      'nytimes', 'wsj', 'reuters', 'bloomberg',
      'techcrunch', 'theverge', 'arstechnica',
      'arxiv', 'papers', 'research'
    ];
    
    return highQuality.some(tld => domain.includes(tld));
  });
  
  // Take top 5
  return filtered.slice(0, 5).map(r => ({ json: r }));
  ```

**Node 4: HTTP Request (Fetch Article Content)**
- Mode: `Execute once per item`
- Method: `GET`
- URL: `{{$json.link}}`
- Alternative: Use Jina AI Reader API for cleaner extraction
  - URL: `https://r.jina.ai/{{$json.link}}`
- Output: Full article text

**Node 5: OpenAI (Summarize Each Article)**
- Mode: `Execute once per item`
- Model: `gpt-4o`
- System Message:
  ```
  Summarize this article for a research brief:
  
  Include:
  1. Main thesis/argument (2-3 sentences)
  2. Key findings or evidence (bullet points)
  3. Notable quotes or data points
  4. Author's credentials/source credibility
  5. Relevance score to topic (0-10)
  
  Be objective and comprehensive.
  ```
- User Message:
  ```
  Article Title: {{$node["HTTP Request Fetch"].json.title}}
  URL: {{$json.link}}
  
  Content:
  {{$node["HTTP Request Fetch"].json.content}}
  ```

**Node 6: Function (Aggregate All Summaries)**
- Mode: `All Items`
- Code:
  ```javascript
  const items = $input.all();
  
  const articles = items.map(item => ({
    title: item.json.title,
    url: item.json.link,
    summary: item.json.article_summary,
    relevance: item.json.relevance_score
  }));
  
  // Sort by relevance
  articles.sort((a, b) => b.relevance - a.relevance);
  
  return [{
    json: {
      topic: $node["Webhook"].json.topic,
      focus: $node["Webhook"].json.focus,
      depth: $node["Webhook"].json.depth,
      articles: articles
    }
  }];
  ```

**Node 7: OpenAI (Synthesize Research Brief)**
- Model: `gpt-4o`
- System Message:
  ```
  You are a research analyst. Synthesize these article summaries into a comprehensive research brief:
  
  Structure:
  1. **Executive Summary** (3-4 sentences)
  2. **Background & Context** (what you need to know)
  3. **Key Findings** (synthesize insights from all sources)
  4. **Perspectives & Debate** (different viewpoints, if any)
  5. **Data & Evidence** (key statistics or studies)
  6. **Implications** (so what? why does this matter?)
  7. **Open Questions** (what's still unclear or contested)
  
  Cite sources inline using [1], [2], etc.
  Be analytical, not just descriptive.
  Length: 800-1000 words.
  ```
- User Message:
  ```
  Research Topic: {{$json.topic}}
  Focus: {{$json.focus}}
  
  Source Summaries:
  {{$json.articles.map((a, i) => `
  [${i+1}] ${a.title}
  URL: ${a.url}
  Summary: ${a.summary}
  `).join('\n\n')}}
  ```

**Node 8: OpenAI (Generate Key Takeaways)**
- Model: `gpt-4o`
- System Message:
  ```
  From this research brief, extract:
  
  1. **3-5 Key Takeaways** (most important insights)
  2. **3-5 Open Questions** (areas for further research)
  3. **3-5 Recommended Actions** (if applicable based on topic)
  4. **Related Topics** (what to explore next)
  
  Return as JSON:
  {
    "key_takeaways": ["...", "..."],
    "open_questions": ["...", "..."],
    "recommendations": ["...", "..."],
    "related_topics": ["...", "..."]
  }
  ```
- User Message: `{{$node["OpenAI Synthesize"].json.choices[0].message.content}}`

**Node 9: Function (Format for Notion)**
- Code:
  ```javascript
  const topic = $node["Function Aggregate"].json.topic;
  const brief = $node["OpenAI Synthesize"].json.choices[0].message.content;
  const takeaways = $node["OpenAI Takeaways"].json;
  const articles = $node["Function Aggregate"].json.articles;
  
  // Convert markdown brief to Notion blocks
  const blocks = [
    {
      type: 'heading_1',
      heading_1: { rich_text: [{ text: { content: topic } }] }
    },
    {
      type: 'paragraph',
      paragraph: { rich_text: [{ text: { content: `Research Date: ${new Date().toLocaleDateString()}` } }] }
    },
    {
      type: 'divider',
      divider: {}
    }
  ];
  
  // Add research brief (convert markdown to Notion blocks)
  // [Simplified - actual implementation needs markdown-to-notion-blocks converter]
  blocks.push({
    type: 'paragraph',
    paragraph: { rich_text: [{ text: { content: brief } }] }
  });
  
  // Add key takeaways
  blocks.push({
    type: 'heading_2',
    heading_2: { rich_text: [{ text: { content: '🎯 Key Takeaways' } }] }
  });
  
  takeaways.key_takeaways.forEach(takeaway => {
    blocks.push({
      type: 'bulleted_list_item',
      bulleted_list_item: { rich_text: [{ text: { content: takeaway } }] }
    });
  });
  
  // Add open questions
  blocks.push({
    type: 'heading_2',
    heading_2: { rich_text: [{ text: { content: '❓ Open Questions' } }] }
  });
  
  takeaways.open_questions.forEach(question => {
    blocks.push({
      type: 'bulleted_list_item',
      bulleted_list_item: { rich_text: [{ text: { content: question } }] }
    });
  });
  
  // Add sources
  blocks.push({
    type: 'heading_2',
    heading_2: { rich_text: [{ text: { content: '📚 Sources' } }] }
  });
  
  articles.forEach((article, i) => {
    blocks.push({
      type: 'numbered_list_item',
      numbered_list_item: { 
        rich_text: [
          { text: { content: article.title, link: { url: article.url } } }
        ]
      }
    });
  });
  
  return {
    json: {
      page_title: topic,
      blocks: blocks,
      properties: {
        'Research Date': new Date().toISOString().split('T')[0],
        'Focus': $node["Function Aggregate"].json.focus,
        'Sources': articles.length,
        'Status': 'Complete'
      }
    }
  };
  ```

**Node 10: Notion (Create Research Page)**
- Action: `Create Database Page`
- Database: `Research Library`
- Properties:
  - Title: `{{$json.page_title}}`
  - Research Date: `{{$json.properties['Research Date']}}`
  - Focus: `{{$json.properties.Focus}}`
  - Sources: `{{$json.properties.Sources}}`
  - Status: `{{$json.properties.Status}}`
- Content (Children Blocks): `{{$json.blocks}}`

**Node 11: Telegram (Notify Completion)**
- Message:
  ```
  ✅ *Research Complete*
  
  📚 Topic: {{$node["Function Aggregate"].json.topic}}
  📊 Sources analyzed: {{$node["Function Aggregate"].json.articles.length}}
  
  🎯 *Top Takeaways:*
  {{$node["OpenAI Takeaways"].json.key_takeaways.slice(0, 3).map(t => `• ${t}`).join('\n')}}
  
  [View full brief in Notion]({{$node["Notion"].json.url}})
  
  ---
  *Generated in {{Math.round((Date.now() - $workflow.startedAt) / 1000)}} seconds*
  ```

### Trigger Type
**Webhook** - Call via HTTP POST with research topic

### AI Integration
- **Model:** OpenAI GPT-4o
- **Purpose:** 
  - Summarize individual articles
  - Synthesize cross-source insights
  - Extract key takeaways
- **Cost:** ~$0.15-0.30 per research brief (depending on depth)
- **Why this model:** Best at synthesis, analytical thinking, and structured output

### Setup Details
1. Get API keys: SerpAPI, OpenAI, Notion
2. Create Notion database: `Research Library` with properties listed
3. Set up webhook endpoint
4. Test with 2-3 sample topics
5. Adjust synthesis prompt for your research style
6. Optional: Add specialized sources for your industry

### Alternative Improvements
- **Academic focus:** Add arXiv, Google Scholar APIs
- **News focus:** Add NewsAPI for recent articles
- **Visual research:** Add image/chart extraction
- **Comparative analysis:** Compare multiple topics side-by-side
- **Auto-scheduling:** Periodic research on saved topics

### Estimated Setup Time
**45 minutes**

### Difficulty
**Intermediate** - Web scraping, content synthesis, Notion API

### Monthly Time Saved
**15+ hours** - Eliminates manual research and source aggregation

---

## 13. Daily Standup Bot

**Description:** Schedule collects updates from team via Slack, AI summarizes and formats, shares digest automatically.

### Nodes Needed
1. **Schedule Trigger** (Daily morning)
2. **Slack** (Send update request to team)
3. **Wait** (2 hours for responses)
4. **Slack** (Fetch thread replies)
5. **OpenAI** (Summarize team updates)
6. **Function** (Format digest)
7. **Slack** (Post summary to channel)
8. **Google Docs** (Append to weekly log)

### Step-by-Step Flow

**Node 1: Schedule Trigger**
- Frequency: `Every weekday at 9:00 AM`
- Timezone: Team timezone

**Node 2: Slack (Post Update Request)**
- Channel: `#standup` or team channel
- Message:
  ```
  🌅 *Daily Standup - {{new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' })}}*
  
  Reply in this thread with your update:
  ✅ **Done yesterday:**
  🚧 **Working on today:**
  🚫 **Blockers:**
  
  _You have until 11 AM to submit. AI summary will be posted at 11:15._
  ```
- Output: Message timestamp (for fetching thread later)

**Node 3: Wait**
- Duration: `2 hours`
- Purpose: Give team time to respond

**Node 4: Slack (Fetch Thread Replies)**
- Action: `Get Thread Messages`
- Channel: Same as Node 2
- Thread TS: `{{$node["Slack Post"].json.ts}}`
- Output: All replies in thread

**Node 5: Function (Parse Updates)**
- Code:
  ```javascript
  const messages = $json.messages || [];
  
  // Skip the bot's initial message
  const updates = messages.slice(1).map(msg => {
    const user = msg.user;
    const text = msg.text;
    
    // Try to parse structured format
    const doneMatch = text.match(/✅.*?Done.*?:(.*?)(?=🚧|🚫|$)/is);
    const todayMatch = text.match(/🚧.*?(?:Working on )?today.*?:(.*?)(?=🚫|$)/is);
    const blockersMatch = text.match(/🚫.*?Blockers.*?:(.*?)$/is);
    
    return {
      user_id: user,
      done: doneMatch ? doneMatch[1].trim() : '',
      today: todayMatch ? todayMatch[1].trim() : '',
      blockers: blockersMatch ? blockersMatch[1].trim() : 'None',
      raw_text: text,
      timestamp: msg.ts
    };
  });
  
  return updates.map(u => ({ json: u }));
  ```

**Node 6: Slack (Get User Info)**
- Mode: `Execute once per item`
- Action: `Get User Info`
- User ID: `{{$json.user_id}}`
- Output: Real name, display name

**Node 7: Function (Merge User Names)**
- Mode: `All Items`
- Code:
  ```javascript
  return $input.all().map(item => ({
    json: {
      name: item.json.real_name || item.json.display_name,
      done: item.json.done,
      today: item.json.today,
      blockers: item.json.blockers
    }
  }));
  ```

**Node 8: OpenAI (Generate Summary)**
- Model: `gpt-4o-mini` (sufficient for this task)
- System Message:
  ```
  Summarize this team's daily standup. Create:
  
  1. **Team Velocity** (1-2 sentences on overall progress)
  2. **Key Accomplishments** (Yesterday's wins, grouped by theme if applicable)
  3. **Today's Focus** (Main priorities, highlight cross-team dependencies)
  4. **Blockers & Risks** (Call out anything blocking progress)
  5. **Shoutouts** (Any notable achievements worth celebrating)
  
  Tone: Brief, energizing, action-oriented. Max 200 words.
  ```
- User Message:
  ```
  Team updates for {{new Date().toLocaleDateString()}}:
  
  {{$input.all().map(item => `
  **${item.json.name}**
  Done: ${item.json.done}
  Today: ${item.json.today}
  Blockers: ${item.json.blockers}
  `).join('\n\n')}}
  ```

**Node 9: Function (Format Slack Digest)**
- Code:
  ```javascript
  const summary = $node["OpenAI"].json.choices[0].message.content;
  const updates = $node["Function Merge"].json;
  
  return {
    json: {
      message: `📊 *Daily Standup Summary* - ${new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' })}\n\n` +
               `${summary}\n\n` +
               `---\n\n` +
               `*Individual Updates* (${updates.length} team members)\n` +
               updates.map(u => `
  *${u.name}*
  ✅ Done: ${u.done || 'No update'}
  🚧 Today: ${u.today || 'No update'}
  🚫 Blockers: ${u.blockers}
               `).join('\n') +
               `\n---\n` +
               `_Posted ${updates.length} of ${updates.length} submitted updates • AI-generated summary_`
    }
  };
  ```

**Node 10: Slack (Post Summary)**
- Channel: `#standup`
- Message: `{{$json.message}}`

**Node 11: Google Docs (Append to Log)**
- Document: `Standup Archive - {{$now.toFormat('yyyy-MM')}}`
- Action: `Append`
- Content:
  ```markdown
  ## {{$now.toFormat('EEEE, MMMM d, yyyy')}}
  
  {{$node["OpenAI"].json.choices[0].message.content}}
  
  ### Individual Updates
  {{$node["Function Merge"].json.map(u => `
  **${u.name}**
  - Done: ${u.done}
  - Today: ${u.today}
  - Blockers: ${u.blockers}
  `).join('\n')}}
  
  ---
  ```

### Trigger Type
**Schedule Trigger** - Every weekday at 9:00 AM

### AI Integration
- **Model:** OpenAI GPT-4o-mini
- **Purpose:** Summarize team updates into executive-friendly digest
- **Cost:** ~$0.01 per standup
- **Why this model:** Cheap, sufficient for summarization, fast

### Setup Details
1. Create Slack channel: `#standup`
2. Get Slack bot token with permissions: `chat:write`, `channels:history`, `users:read`
3. Get OpenAI API key
4. Create Google Doc template for monthly archive
5. Test with team for one week, gather feedback
6. Adjust timing based on team's availability

### Variations
- **Async standup:** Don't wait, just process updates as they come
- **Video option:** Allow Loom links, transcribe with AI
- **Metrics:** Track completion rate, blocker frequency
- **Manager digest:** Separate summary for leadership

### Estimated Setup Time
**35 minutes**

### Difficulty
**Beginner** - Great intro to Slack workflows + AI summarization

### Monthly Time Saved
**4+ hours** - Eliminates manual standup meetings or digest compilation

---

## 14. Portfolio Monitor

**Description:** Track stock/crypto portfolio via APIs, detect threshold changes, send alerts with AI-generated market context.

### Nodes Needed
1. **Schedule Trigger** (Hourly during market hours)
2. **HTTP Request** (Alpha Vantage or Yahoo Finance API - stocks)
3. **HTTP Request** (CoinGecko or CoinMarketCap API - crypto)
4. **Function** (Calculate portfolio value and changes)
5. **Google Sheets** (Load portfolio holdings)
6. **Function** (Detect threshold alerts)
7. **OpenAI** (Generate market context)
8. **Telegram** (Send alert)
9. **Google Sheets** (Log price history)

### Step-by-Step Flow

**Node 1: Schedule Trigger**
- Frequency: `Every hour from 9 AM to 4 PM EST, Monday-Friday`
- For crypto: `Every 2 hours, 24/7`

**Node 2: Google Sheets (Load Portfolio)**
- Spreadsheet: `Portfolio Tracker`
- Sheet: `Holdings`
- Action: `Read All Rows`
- Expected columns:
  - Symbol (AAPL, BTC, ETH, etc.)
  - Type (Stock, Crypto)
  - Quantity
  - Buy Price
  - Target Price (optional)
  - Stop Loss (optional)
  - Alert Threshold % (e.g., 5 for 5% change)

**Node 3: HTTP Request (Fetch Stock Prices)**
- Mode: `Execute once per item` (filter: Type = Stock)
- Method: `GET`
- URL: `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={{$json.Symbol}}&apikey=YOUR_KEY`
- Alternative: Yahoo Finance API (free, no key needed)
- Output: Current price, change %, volume

**Node 4: HTTP Request (Fetch Crypto Prices)**
- Mode: `Execute once per item` (filter: Type = Crypto)
- Method: `GET`
- URL: `https://api.coingecko.com/api/v3/simple/price?ids={{$json.Symbol}}&vs_currencies=usd&include_24hr_change=true`
- Output: Current price, 24h change %

**Node 5: Function (Calculate Position Values)**
- Mode: `All Items`
- Code:
  ```javascript
  const holdings = $node["Google Sheets Load"].json;
  const priceData = $input.all();
  
  const portfolio = holdings.map(holding => {
    // Find price data for this symbol
    const priceInfo = priceData.find(p => 
      p.json.symbol?.toLowerCase() === holding.Symbol.toLowerCase()
    );
    
    if (!priceInfo) return null;
    
    const currentPrice = priceInfo.json.price || priceInfo.json['05. price'];
    const changePercent = priceInfo.json.change_percent_24h || 
                         parseFloat(priceInfo.json['10. change percent'].replace('%', ''));
    
    const positionValue = holding.Quantity * currentPrice;
    const costBasis = holding.Quantity * holding['Buy Price'];
    const profitLoss = positionValue - costBasis;
    const profitLossPct = (profitLoss / costBasis) * 100;
    
    // Check if alert threshold crossed
    const alertThreshold = holding['Alert Threshold %'] || 5;
    const significantMove = Math.abs(changePercent) >= alertThreshold;
    
    // Check stop loss / target
    const hitStopLoss = holding['Stop Loss'] && currentPrice <= holding['Stop Loss'];
    const hitTarget = holding['Target Price'] && currentPrice >= holding['Target Price'];
    
    return {
      symbol: holding.Symbol,
      type: holding.Type,
      quantity: holding.Quantity,
      buy_price: holding['Buy Price'],
      current_price: currentPrice,
      position_value: positionValue,
      profit_loss: profitLoss,
      profit_loss_pct: profitLossPct.toFixed(2),
      change_24h_pct: changePercent.toFixed(2),
      alert_triggered: significantMove || hitStopLoss || hitTarget,
      alert_reason: hitStopLoss ? 'STOP LOSS' : 
                   hitTarget ? 'TARGET HIT' : 
                   significantMove ? `${changePercent > 0 ? '+' : ''}${changePercent.toFixed(1)}% move` : 
                   null
    };
  }).filter(p => p !== null);
  
  const totalValue = portfolio.reduce((sum, p) => sum + p.position_value, 0);
  const totalPL = portfolio.reduce((sum, p) => sum + p.profit_loss, 0);
  const totalPLPct = (totalPL / (totalValue - totalPL)) * 100;
  
  return [{
    json: {
      timestamp: new Date().toISOString(),
      portfolio: portfolio,
      total_value: totalValue.toFixed(2),
      total_profit_loss: totalPL.toFixed(2),
      total_pl_pct: totalPLPct.toFixed(2),
      alerts: portfolio.filter(p => p.alert_triggered)
    }
  }];
  ```

**Node 6: Google Sheets (Log Snapshot)**
- Spreadsheet: `Portfolio Tracker`
- Sheet: `Price History`
- Action: `Append Row`
- Columns:
  - Timestamp: `{{$json.timestamp}}`
  - Total Value: `{{$json.total_value}}`
  - Total P/L: `{{$json.total_profit_loss}}`
  - Total P/L %: `{{$json.total_pl_pct}}`

**Node 7: Switch (Any Alerts?)**
- Rule: `{{$json.alerts.length}} > 0` → Alert Branch

**Node 8: OpenAI (Generate Market Context)**
- Only processes if alerts triggered
- Model: `gpt-4o-mini`
- System Message:
  ```
  You are a financial analyst. Provide brief context for this price movement:
  
  1. What likely drove this move? (1-2 sentences)
  2. Is this part of a broader market trend?
  3. Recommended action (hold, buy more, sell, wait)?
  
  Be concise and actionable. Max 100 words.
  ```
- User Message:
  ```
  Asset: {{$json.alert.symbol}}
  Type: {{$json.alert.type}}
  Price move: {{$json.alert.change_24h_pct}}%
  Current price: ${{$json.alert.current_price}}
  Your position: {{$json.alert.quantity}} units @ ${{$json.alert.buy_price}} ({{$json.alert.profit_loss_pct}}% P/L)
  Alert reason: {{$json.alert.alert_reason}}
  ```

**Node 9: Function (Format Alert Message)**
- Code:
  ```javascript
  const alerts = $json.alerts;
  const portfolio = $json.portfolio;
  const aiContext = $node["OpenAI Context"]?.json?.choices[0]?.message?.content;
  
  const message = `🚨 *Portfolio Alert*\n\n` +
    alerts.map(alert => `
  📊 *${alert.symbol}* (${alert.type})
  Current: $${alert.current_price}
  Change: ${alert.change_24h_pct > 0 ? '+' : ''}${alert.change_24h_pct}%
  Position: ${alert.quantity} @ $${alert.buy_price}
  P/L: $${alert.profit_loss.toFixed(2)} (${alert.profit_loss_pct}%)
  
  ⚠️ *${alert.alert_reason}*
  
  💡 AI Context:
  ${aiContext || 'No additional context available'}
    `).join('\n---\n') +
    `\n\n📈 *Portfolio Summary*\n` +
    `Total Value: $${$json.total_value}\n` +
    `Total P/L: $${$json.total_profit_loss} (${$json.total_pl_pct}%)\n\n` +
    `[View full portfolio →](link_to_google_sheet)`;
  
  return { json: { message: message } };
  ```

**Node 10: Telegram (Send Alert)**
- Message: `{{$json.message}}`
- Parse Mode: `Markdown`

**Node 11: Function (Daily Summary - 4 PM)**
- Separate branch from Schedule Trigger
- Condition: `{{$now.hour}} === 16` (4 PM)
- Code:
  ```javascript
  const portfolio = $node["Function Calculate"].json.portfolio;
  
  const topGainer = portfolio.reduce((max, p) => 
    parseFloat(p.change_24h_pct) > parseFloat(max.change_24h_pct) ? p : max
  );
  
  const topLoser = portfolio.reduce((min, p) => 
    parseFloat(p.change_24h_pct) < parseFloat(min.change_24h_pct) ? p : min
  );
  
  return {
    json: {
      summary: `📊 *Daily Portfolio Summary*\n\n` +
               `Total Value: $${$node["Function Calculate"].json.total_value}\n` +
               `Today's P/L: ${$node["Function Calculate"].json.total_pl_pct}%\n\n` +
               `🏆 Top Gainer: ${topGainer.symbol} (+${topGainer.change_24h_pct}%)\n` +
               `📉 Top Loser: ${topLoser.symbol} (${topLoser.change_24h_pct}%)\n\n` +
               `Holdings: ${portfolio.length} positions`
    }
  };
  ```

**Node 12: Telegram (Daily Summary)**
- Message: `{{$json.summary