# Voice Interface (ElevenLabs + OpenClaw) Research Report
**Date:** 2026-02-10  
**Focus:** Voice input/output setup for AI assistant (speech-to-text + TTS)

---

## Overview

A voice interface for your AI assistant enables natural spoken interactions: dictate queries, hear responses. Instead of typing, you speak; instead of reading walls of text, the AI speaks back.

**The Voice Loop:**
```
You speak → Speech-to-Text → AI processes → Text-to-Speech → AI speaks back
```

**Key Benefits:**
- 🎙️ **Hands-free operation** — Work while talking (CNC setup, driving, etc.)
- 🧠 **Faster thought capture** — Speak 3x faster than typing
- 🎧 **Multitasking friendly** — Listen while doing other work
- 📖 **Narrative content** — Stories, summaries, reports sound better spoken

**Why this matters for you:**
- Dictate CNC setup notes while working
- Have AI read back calculation results while you check the machine
- Voice journal entries during commute
- Get story summaries in engaging voices (use `sag` skill for ElevenLabs TTS)

---

## Top 3 Options

### 1. **ElevenLabs Conversational AI** (All-in-One, Cloud)
**Website:** https://elevenlabs.io/conversational-ai  
**Type:** Fully managed cloud service  
**Status:** ✅ Production-ready (Conversational AI 2.0 launched Jan 2026)

**What it does:**
- Complete voice agent platform (speech-to-text + LLM + TTS)
- Real-time conversational AI (low latency, <1s turnaround)
- 32+ languages with natural, emotional voices
- Built-in knowledge base (RAG) and tool integration
- SDKs: JavaScript, React, Python, iOS
- Integrations: Twilio, Zapier, Slack, webhony providers

**Architecture:**
```
User speaks → ElevenLabs STT → LLM (GPT-4/Claude/custom) → ElevenLabs TTS → Audio response
                                       ↓
                             Knowledge Base (RAG) + Tools
```

**Pros:**
✅ Turnkey solution (zero infrastructure)  
✅ Best-in-class voice quality (independently rated #1 TTS)  
✅ Low latency (<1s end-to-end)  
✅ Supports interruptions & natural conversation flow  
✅ Built-in knowledge base (connect your docs)  
✅ Phone integration (Twilio)  
✅ Grant program (33M free credits = $4,000 value for startups)  

**Cons:**
❌ Cloud-based (not local/offline)  
❌ Costs money after free tier ($0.08/min on Business plan)  
❌ Requires internet connection  
❌ Less control vs self-hosted  

**Use Cases:**
- Customer support bots
- Phone agents (sales, scheduling)
- Gaming NPCs (real-time voice)
- Learning simulations (role-play)
- Voice shopping assistants

**Pricing:**
- **Free tier:** Test & prototype
- **Business:** $0.08/min (annual) + lower rates for volume
- **Grant:** 33M credits free (680 hours) for new products/startups

**Setup Complexity:** ⭐⭐⚪⚪⚪ (2/5)

**Best for:** Production voice agents, phone bots, gaming, customer service

---

### 2. **Whisper (OpenAI) + ElevenLabs TTS** (Best Quality, Modular)
**Type:** Combine best-of-breed STT + TTS  
**Status:** ✅ Production-ready

**What it does:**
- **Whisper (STT):** State-of-the-art speech recognition (OpenAI)
  - 99+ languages, ultra-accurate
  - Runs locally (whisper.cpp) or via API
  - Handles accents, noise, technical terms
- **ElevenLabs (TTS):** Best voice synthesis
  - Natural, emotional, multilingual
  - Voice cloning (create custom voices)
  - Real-time streaming or batch

**Architecture:**
```
Microphone → Whisper (local or API) → Text → Your AI (Claude/GPT) → ElevenLabs TTS → Audio
```

**Pros:**
✅ Best quality STT (Whisper) + best quality TTS (ElevenLabs)  
✅ Flexible (swap components as needed)  
✅ Can run Whisper locally (privacy)  
✅ ElevenLabs offers OpenClaw integration (check clawhub.com)  
✅ Voice cloning (custom voices)  
✅ Works with any LLM (Claude, GPT, local)  

**Cons:**
❌ Requires integration work (connect the pieces)  
❌ ElevenLabs TTS is cloud-only (paid API)  
❌ Whisper API costs $0.006/min (cheap but adds up)  
❌ Local Whisper needs GPU for real-time (slower on CPU)  

**Implementation:**
```python
# Pseudo-code
audio = record_microphone()
text = whisper.transcribe(audio)  # Local or API
response = ai_assistant.process(text)  # Claude, GPT, etc.
audio_output = elevenlabs.tts(response)  # ElevenLabs API
play_audio(audio_output)
```

**Setup Complexity:** ⭐⭐⭐⚪⚪ (3/5)

**Best for:** Custom AI assistants where you control the middle (AI reasoning)

---

### 3. **Local Stack: Whisper.cpp + Piper TTS** (100% Local, Free)
**Type:** Fully offline, privacy-first  
**Status:** ✅ Production-ready (open source)

**What it does:**
- **Whisper.cpp:** Local Whisper inference (C++, fast)
  - Runs on Mac (Metal GPU acceleration)
  - Models: tiny (75MB) → large-v3 (3GB)
  - Real-time or faster-than-real-time transcription
- **Piper TTS:** Local neural TTS
  - 100+ voices, 20+ languages
  - Lightweight (models 10-50MB each)
  - Fast inference (real-time on CPU)

**Architecture:**
```
Microphone → Whisper.cpp → Text → Your AI (local LLM) → Piper TTS → Audio
```

**Pros:**
✅ 100% local & offline (zero cloud, zero cost)  
✅ Complete privacy (no data leaves your machine)  
✅ Fast (Metal acceleration on Mac)  
✅ Open source (MIT/Apache licenses)  
✅ One-time setup, forever free  

**Cons:**
❌ Voice quality < ElevenLabs (but still good)  
❌ Requires technical setup (compile whisper.cpp, install Piper)  
❌ Needs decent hardware (Mac M1+ ideal)  
❌ No voice cloning (limited voice selection)  

**Installation (macOS):**
```bash
# Install Whisper.cpp
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make  # Compiles with Metal support
./models/download-ggml-model.sh base.en  # 142MB model

# Install Piper
brew install piper-tts
# Or: pip install piper-tts

# Test
echo "Hello world" | piper --model en_US-lessac-medium > output.wav
```

**Setup Complexity:** ⭐⭐⭐⭐⚪ (4/5)

**Best for:** Privacy-focused users, offline scenarios, dev experiments

---

## Comparison Matrix

| Feature | ElevenLabs Conversational AI | Whisper + ElevenLabs | Whisper.cpp + Piper |
|---------|------------------------------|----------------------|---------------------|
| **Voice Quality (TTS)** | ★★★★★ (best) | ★★★★★ (best) | ★★★⭐⚪ (good) |
| **Speech Recognition** | ★★★★★ (built-in) | ★★★★★ (Whisper) | ★★★★★ (Whisper) |
| **Latency** | <1s (cloud optimized) | 1-3s (depends on setup) | 1-2s (local, fast) |
| **Cost** | $0.08/min (after free) | $0.006/min STT + TTS | $0 (free forever) |
| **Privacy** | ❌ Cloud | ⚠️ STT local option | ✅ 100% local |
| **Setup** | ⭐⭐ Easy | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ Hard |
| **Flexibility** | ⚠️ Platform-locked | ✅ Modular | ✅ Fully open |
| **Voice Cloning** | ✅ Yes (paid) | ✅ Yes (paid) | ❌ No |
| **Best For** | Production agents | Custom assistants | Privacy/offline |

---

## Implementation Steps

### Option 1: ElevenLabs Conversational AI (Fastest to Production)

#### Step 1: Sign Up & Get API Key (5 mins)
```bash
# Sign up at https://elevenlabs.io/
# Navigate to API settings
# Copy API key
export ELEVENLABS_API_KEY="your_key_here"
```

#### Step 2: Install SDK (5 mins)
```bash
# Python
pip install elevenlabs

# JavaScript
npm install elevenlabs

# Or use their web widget (no-code)
```

#### Step 3: Create Agent (15 mins)
- Go to https://elevenlabs.io/conversational-ai
- Click "Create Agent"
- Configure:
  - **Voice:** Choose from library (try "Nova" - warm, British)
  - **LLM:** GPT-4, Claude, or custom
  - **System Prompt:** "You are a helpful assistant for CNC machining"
  - **Knowledge Base:** Upload PDFs, connect URLs
  - **Tools:** (optional) Connect calendar, database, etc.

#### Step 4: Test (5 mins)
```python
from elevenlabs import ElevenLabs

client = ElevenLabs(api_key="your_key")
agent = client.conversational_ai.create(
    name="CNC Assistant",
    voice="nova",
    system_prompt="You help with CNC machining calculations"
)

# Web interface: Test in browser
# Or integrate via WebSocket API for real-time
```

#### Step 5: Integrate with OpenClaw (10 mins)
- Check if OpenClaw has ElevenLabs skill on clawhub.com
- If yes: Install skill, configure API key
- If no: Use ElevenLabs web interface or build custom integration

**Total time:** 40 minutes to working voice agent

---

### Option 2: Whisper + ElevenLabs (Best Quality, Custom AI)

#### Step 1: Set Up Whisper (15 mins)
**Option A: OpenAI API (easiest)**
```python
pip install openai
import openai

openai.api_key = "your_openai_key"
audio_file = open("recording.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript.text)
```

**Option B: Local Whisper (privacy)**
```bash
# Install whisper.cpp (Mac)
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make
./models/download-ggml-model.sh base.en  # Or: small, medium, large

# Transcribe
./main -m models/ggml-base.en.bin -f recording.wav
```

#### Step 2: Set Up ElevenLabs TTS (10 mins)
```bash
pip install elevenlabs

# Test
from elevenlabs import generate, play
audio = generate(
    text="Hello, this is a test of voice synthesis.",
    voice="Bella",  # Or: Adam, Antoni, Josh, etc.
    model="eleven_multilingual_v2"
)
play(audio)
```

#### Step 3: Connect to Your AI (20 mins)
```python
# Full pipeline
def voice_assistant(audio_input):
    # 1. Speech to Text
    transcript = whisper.transcribe(audio_input)
    
    # 2. AI Processing (your existing AI)
    response = claude_api.complete(transcript)
    
    # 3. Text to Speech
    audio_output = elevenlabs.generate(text=response)
    
    return audio_output

# Record mic → transcribe → AI → speak
```

#### Step 4: Build Interface (30-60 mins)
- **CLI:** Simple script with audio recording
- **GUI:** tkinter, PyQt, or Electron app
- **OpenClaw integration:** Check clawhub.com for ElevenLabs skill

**Total time:** 1.5-2 hours to working pipeline

---

### Option 3: Local Stack (Privacy-First)

#### Step 1: Install Whisper.cpp (30 mins)
```bash
# Clone & build
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
make  # Compiles with Metal (Mac) or CUDA (Linux)

# Download model
./models/download-ggml-model.sh base.en  # 142MB, fast
# Or: small.en (466MB), medium.en (1.5GB), large-v3 (3GB)

# Test
./main -m models/ggml-base.en.bin -f samples/jfk.wav
```

#### Step 2: Install Piper TTS (15 mins)
```bash
# Mac
brew install piper-tts

# Linux
pip install piper-tts

# Download voice model
wget https://github.com/rhasspy/piper/releases/download/v1.2.0/en_US-lessac-medium.onnx
wget https://github.com/rhasspy/piper/releases/download/v1.2.0/en_US-lessac-medium.onnx.json

# Test
echo "Hello from Piper" | piper --model en_US-lessac-medium --output_file output.wav
```

#### Step 3: Record Audio (10 mins)
```bash
# Mac: Use sox or ffmpeg
brew install sox

# Record 10 seconds
rec -r 16000 -c 1 recording.wav trim 0 10
```

#### Step 4: Build Pipeline (60 mins)
```bash
#!/bin/bash
# voice_assistant.sh

# 1. Record audio
echo "Listening..."
rec -r 16000 -c 1 /tmp/input.wav silence 1 0.1 1% 1 2.0 1%

# 2. Transcribe
TRANSCRIPT=$(whisper.cpp/main -m whisper.cpp/models/ggml-base.en.bin -f /tmp/input.wav | tail -1)
echo "You said: $TRANSCRIPT"

# 3. AI processes (your LLM)
RESPONSE=$(echo "$TRANSCRIPT" | your_ai_script)
echo "AI says: $RESPONSE"

# 4. Speak response
echo "$RESPONSE" | piper --model en_US-lessac-medium --output_file /tmp/output.wav
play /tmp/output.wav
```

**Total time:** 2-3 hours to working local system

---

## Effort Estimate

| Option | Setup Time | Ongoing Effort | Difficulty | Cost |
|--------|------------|----------------|------------|------|
| **ElevenLabs Conversational AI** | 40 mins | Very Low | ⭐⭐ Easy | $0.08/min |
| **Whisper + ElevenLabs** | 1.5-2 hours | Low | ⭐⭐⭐ Medium | $0.01-0.02/min |
| **Local Stack** | 2-3 hours | Medium | ⭐⭐⭐⭐ Hard | $0 (free) |

**Breakdown (ElevenLabs Conversational AI):**
1. **Account setup:** 5 mins
2. **SDK install:** 5 mins
3. **Agent configuration:** 15 mins
4. **Testing:** 10 mins
5. **OpenClaw integration:** 5-10 mins (if skill exists)
6. **Total:** **40 mins**

**Breakdown (Whisper + ElevenLabs):**
1. **Whisper setup:** 15 mins (API) or 30 mins (local)
2. **ElevenLabs setup:** 10 mins
3. **Pipeline integration:** 20 mins
4. **Interface build:** 30-60 mins
5. **Testing:** 15 mins
6. **Total:** **1.5-2 hours**

**Breakdown (Local Stack):**
1. **Whisper.cpp compile:** 30 mins
2. **Piper install:** 15 mins
3. **Audio recording setup:** 10 mins
4. **Pipeline scripting:** 60 mins
5. **Testing/debugging:** 30 mins
6. **Total:** **2.5-3 hours**

---

## OpenClaw Integration

### Check for ElevenLabs Skill
1. Visit **clawhub.com** (OpenClaw skill marketplace)
2. Search for "ElevenLabs" or "voice" or "TTS"
3. If skill exists:
   - Install via OpenClaw CLI
   - Configure API key
   - Use via commands or natural language
4. If not:
   - Request skill on OpenClaw Discord/GitHub
   - Or build custom integration (see below)

### Manual Integration (If No Skill)
```python
# Add to OpenClaw as custom tool
def speak_text(text: str):
    """Convert text to speech using ElevenLabs"""
    from elevenlabs import generate, play
    audio = generate(text=text, voice="Nova")
    play(audio)
    return "Spoken"

# Register with OpenClaw
register_tool("speak", speak_text)
```

### Simplest Setup (No OpenClaw Skill)
If no OpenClaw integration exists yet:
1. Use ElevenLabs web interface (https://elevenlabs.io/speech-synthesis)
2. Copy AI response text
3. Paste into ElevenLabs
4. Play audio

Or:
1. Use ElevenLabs API directly in terminal
2. Pipe AI output → ElevenLabs CLI → audio player

---

## Links & Sources

### ElevenLabs
- **Conversational AI:** https://elevenlabs.io/conversational-ai
- **Documentation:** https://elevenlabs.io/docs/conversational-ai/overview
- **API Reference:** https://elevenlabs.io/docs/api-reference
- **Conversational AI 2.0 Announcement:** https://elevenlabs.io/blog/conversational-ai-2-0 (Jan 2026)
- **SDKs:** JavaScript, React, Python, iOS
- **Pricing:** https://elevenlabs.io/pricing/api
- **Grant Program:** 33M free credits for startups (https://elevenlabs.io/conversational-ai)
- **Examples:** https://github.com/elevenlabs/elevenlabs-examples
- **vs OpenAI Realtime API:** https://elevenlabs.io/blog/comparing-elevenlabs-conversational-ai-v-openai-realtime-api

### Whisper (Speech-to-Text)
- **OpenAI Whisper:** https://openai.com/research/whisper
- **Whisper.cpp (local):** https://github.com/ggerganov/whisper.cpp
- **Whisper API:** https://platform.openai.com/docs/guides/speech-to-text
- **Pricing:** $0.006/minute (API)
- **Models:** tiny (75MB) → large-v3 (3GB)
- **Languages:** 99+ languages supported

### Piper TTS (Local)
- **GitHub:** https://github.com/rhasspy/piper
- **Voices:** https://rhasspy.github.io/piper-samples/
- **Models:** 100+ voices, 20+ languages
- **Size:** 10-50MB per voice

### Other TTS Options
- **Coqui TTS:** https://github.com/coqui-ai/TTS (open source)
- **Bark:** https://github.com/suno-ai/bark (realistic, slow)
- **StyleTTS 2:** https://github.com/yl4579/StyleTTS2 (high quality)
- **Mac Built-in:** `say` command (decent for basic needs)

### OpenClaw
- **ClawHub:** clawhub.com (skill marketplace)
- **ElevenLabs Search:** Check for existing voice/TTS skills

### Use Cases & Examples
- **Twilio Integration:** https://elevenlabs.io/blog/twilio-conversation-relay
- **Fortnite (Darth Vader):** https://www.fortnite.com/news/this-will-be-a-day-long-remembered-speak-with-darth-vader-in-fortnite
- **Customer Support:** https://elevenlabs.io/blog/the-state-of-conversational-ai-in-support
- **Perplexity Partnership:** https://elevenlabs.io/blog/elevenlabs-and-perplexity-announce-partnership-2

---

## Recommendations for Your Setup

### Immediate (This Week): ElevenLabs API for TTS
**Why:**
- ✅ You already have `sag` skill (check TOOLS.md)
- ✅ OpenClaw may support ElevenLabs TTS already
- ✅ Best voice quality for storytelling, summaries
- ✅ Instant setup (API key + done)

**Action:**
1. Get ElevenLabs API key (free tier)
2. Check if OpenClaw has TTS skill
3. Test: "Read this story in a funny voice" → use `sag`
4. Use for: movie summaries, stories, long-form content

**Time:** 10 minutes

---

### Short-term (Week 2-3): Add Speech-to-Text with Whisper
**Why:**
- ✅ Complete the loop (speak → AI → speak back)
- ✅ Hands-free note-taking
- ✅ Dictate while working on CNC

**Option A: OpenAI Whisper API (easiest)**
- Sign up for OpenAI account
- Use Whisper API ($0.006/min, very cheap)
- Integrate with OpenClaw or standalone script

**Option B: Local Whisper.cpp (privacy)**
- Install whisper.cpp
- Download base.en model (142MB)
- Run locally, no API costs

**Time:** 30 mins (API) or 60 mins (local)

---

### Medium-term (Month 1): Build Complete Voice Loop
**Why:**
- ✅ Full conversational interface
- ✅ Dictate → AI processes → speaks back
- ✅ Hands-free workflow

**Implementation:**
```
Microphone → Whisper (local or API) → OpenClaw/Claude → ElevenLabs TTS → Speaker
```

**Tools:**
- **Voice input:** Whisper API or whisper.cpp
- **AI:** Your existing Claude setup
- **Voice output:** ElevenLabs (via `sag` or API)
- **Interface:** CLI script or simple GUI

**Time:** 2-4 hours to build and test

---

### Long-term (Month 2+): Evaluate ElevenLabs Conversational AI
**Why:**
- ✅ Turnkey solution (less maintenance)
- ✅ Better latency (<1s)
- ✅ Phone integration (Twilio)
- ✅ Grant program (free for startups/new products)

**Use Cases:**
- Voice assistant for CNC shop floor
- Phone agent for scheduling/quotes
- Training simulations (role-play scenarios)

**Time:** 1-2 hours to prototype

---

## Key Takeaways

✅ **ElevenLabs is production-ready** — Best TTS quality, Conversational AI 2.0 launched Jan 2026  
✅ **Whisper is the STT standard** — 99+ languages, local or API  
✅ **OpenClaw may already support** — Check clawhub.com for ElevenLabs skill  
✅ **100% local is possible** — whisper.cpp + Piper = free forever  
✅ **Start with TTS** — Add voice output first (easier, instant value)  

⚠️ **Watch out for:**
- **Latency:** Cloud adds 0.5-1s, local is faster but needs GPU
- **Cost:** ElevenLabs API is ~$0.01-0.08/min (adds up for heavy use)
- **Voice quality:** Local TTS < ElevenLabs (but good enough for many uses)
- **Privacy:** Cloud solutions send audio to servers (consider local for sensitive data)

**Bottom line:** 
1. **Start simple:** Use ElevenLabs TTS for reading content (check if OpenClaw has skill)
2. **Add input:** Whisper API for speech-to-text ($0.006/min, very cheap)
3. **Close the loop:** Connect them for full voice interface
4. **Go local later:** If you need offline/privacy, switch to whisper.cpp + Piper

The hardest part is the "glue code" connecting pieces. Start with ElevenLabs TTS this week (you may already have it), then add STT next month.
