# Setup Guide - AI Advisory Board

## Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Set OpenAI API Key

You need an OpenAI API key to run this tool.

**Get your key:**
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it

**Set the key:**

**Option A: Environment Variable (Recommended)**
```bash
export OPENAI_API_KEY='sk-proj-...'
```

**Option B: .env File**
```bash
echo 'OPENAI_API_KEY=sk-proj-...' > .env
source .env
```

**Option C: Add to your shell profile (Permanent)**
```bash
# Add to ~/.zshrc or ~/.bashrc
echo 'export OPENAI_API_KEY=sk-proj-...' >> ~/.zshrc
source ~/.zshrc
```

### 3. Run the Tool

```bash
node board.js "Your question here"
```

**Example:**
```bash
node board.js "Should I launch on Monday with an MVP or wait until the product is polished?"
```

### 4. View Output

Open the generated HTML file in `output/` directory in your browser.

```bash
open output/should-i-launch-on-monday-with-an-mvp-or-wait-un.html
```

## Test Script

Use the included test script to verify everything works:

```bash
./test.sh
```

This will:
- Check if your API key is set
- Run a test question
- Generate a sample report

## Troubleshooting

### "OPENAI_API_KEY environment variable is missing"

**Solution:** Follow Step 2 above to set your API key.

### "Command not found: node"

**Solution:** Install Node.js from https://nodejs.org (v18+ required)

### "Cannot find module 'openai'"

**Solution:** Run `npm install` in the project directory

### API Rate Limits

If you hit rate limits:
- Wait a few seconds and try again
- Upgrade your OpenAI plan for higher limits
- The tool makes 6 parallel API calls (one per advisor)

## Cost Estimate

Each advisory session makes 6 API calls to GPT-4o:
- ~500 tokens per response
- ~3000 tokens total per session
- Cost: ~$0.015 per session (at GPT-4o pricing)

## Project Structure

```
ai-advisory-board/
├── board.js              # Main orchestrator
├── advisors/             # 6 advisor modules
│   ├── operator.js
│   ├── investor.js
│   ├── contrarian.js
│   ├── technologist.js
│   ├── strategist.js
│   └── customer.js
├── renderer.js           # HTML generator
├── output/               # Generated reports
├── package.json          # Dependencies
└── README.md             # Documentation
```

## Customization

### Change Advisors

Edit files in `advisors/` to customize:
- Name
- Role
- Icon (SVG)
- System prompt (perspective & style)

### Modify Design

Edit `renderer.js` to customize:
- Colors (CSS variables)
- Layout
- Typography
- Features

### Add More Advisors

1. Create new file in `advisors/`
2. Import in `board.js`
3. Add to `advisors` array

## Support

Issues? Check:
- README.md for usage
- SETUP.md (this file) for configuration
- Example output in `output/`

---

Ready to make better decisions? 🎯
