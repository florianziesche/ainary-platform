# Discord Server Recommendations

*For VC intelligence, AI insights, and founder networking*

---

## 🎯 Priority: High Value for Your Goals

### 1. OpenClaw
- **Link:** https://discord.com/invite/clawd
- **Why:** Direct access to AI agent tooling community, early adopter insights
- **Channels to monitor:** #general, #announcements, #showcase
- **Status:** ✅ Ready to join

### 2. Latent Space
- **Link:** https://discord.gg/latentspace
- **Why:** AI engineers & founders, technical discussions, swyx (host) has great network
- **Channels:** #papers, #projects, #jobs
- **Status:** High priority

### 3. Eleuther AI
- **Link:** https://discord.gg/eleutherai
- **Why:** Open-source AI research, early signals on model capabilities
- **Channels:** #research, #announcements
- **Status:** Technical deep-dives

### 4. Buildspace (nights & weekends)
- **Link:** https://buildspace.so (Discord via site)
- **Why:** Builder community, many AI projects, founder energy
- **Channels:** #builds, #feedback
- **Status:** Good for founder pulse

### 5. On Deck (if you have access)
- **Link:** Via fellowship membership
- **Why:** High-quality founder network, VC intros
- **Status:** Check if alumni access available

---

## 📊 Secondary: Worth Monitoring

### 6. Hugging Face
- **Link:** https://discord.gg/huggingface
- **Why:** Model releases, open-source AI community
- **Focus:** #announcements, #transformers

### 7. LangChain
- **Link:** https://discord.gg/langchain
- **Why:** Agent/RAG tooling, relevant to your Legal AI work
- **Focus:** #general, #showcase

### 8. Weights & Biases
- **Link:** https://discord.gg/wandb
- **Why:** ML infrastructure, practitioner insights
- **Focus:** #general

---

## 🔍 To Research Further

- **South Park Commons** — SF founder community (need intro)
- **a]i forum** — AI safety/capabilities discussions
- **Replit Discord** — Builder community, AI coding focus
- **YC Slack** — If accessible via VC Lab connections

---

## 🛠️ Setup Plan

**Phase 1 (This Week):**
1. Join OpenClaw Discord ✅
2. Join Latent Space
3. Set up Discord monitoring in OpenClaw config

**Phase 2 (Next Week):**
4. Join Eleuther AI, HuggingFace
5. Configure channel allowlists
6. Set up digest automation

---

## ⚙️ OpenClaw Discord Config (Draft)

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "servers": {
        "openclaw": {
          "channels": ["general", "announcements"],
          "mode": "monitor"
        }
      }
    }
  }
}
```

*Note: Need to create a Discord bot or use user token for monitoring*

---

*Last updated: 2026-02-01*
