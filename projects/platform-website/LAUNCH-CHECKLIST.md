# Ainary Platform Website — Launch Checklist

**Target Launch:** Week 1 (Static Site Live)  
**Product Launch:** Week 4-6 (Full Backend + Product)  
**Growth Phase:** Week 6+

---

## Phase 1: Static Site Live (Week 1)

**Goal:** Professional website live with lead capture capability.

| Task | Effort | Owner | Priority | Dependencies | Status |
|------|--------|-------|----------|--------------|--------|
| Domain kaufen (ainary.com oder ainary.ai) | S | Florian | 🔴 Critical | None | [ ] |
| GitHub Pages oder Vercel deployment | S | Florian | 🔴 Critical | Domain | [ ] |
| DNS konfigurieren | S | Florian | 🔴 Critical | Domain, Deployment | [ ] |
| SSL/HTTPS | S | Auto (Vercel/GH Pages) | 🔴 Critical | DNS | [ ] |
| OG Images für alle Seiten erstellen | M | Mia/External | 🟡 High | None | [ ] |
| Footer-Seiten: About, Terms, Privacy, Imprint | M | Mia | 🔴 Critical | None | [ ] |
| "243 sources" → echte Zahl ersetzen (aktuell: 9) | S | Florian | 🟡 High | Research Engine finalized | [ ] |
| Alle # Links mit echten Zielen ersetzen | S | Florian | 🔴 Critical | None | [ ] |
| Mobile/Responsive Test | M | Florian | 🔴 Critical | Deployment | [ ] |
| Lighthouse Performance Check | S | Florian | 🟡 High | Deployment | [ ] |
| Google Search Console einrichten | S | Florian | 🟢 Medium | Domain live | [ ] |
| Analytics (Plausible oder Umami, NICHT Google Analytics) | M | Florian | 🟡 High | Domain live | [ ] |

**Definition of Done:**
- Website accessible via custom domain
- All pages render correctly on mobile
- Footer links functional
- Lighthouse score >90
- Basic analytics tracking page views

---

## Phase 2: Email Capture (Week 2)

**Goal:** Functional email capture + automated welcome sequence.

| Task | Effort | Owner | Priority | Dependencies | Status |
|------|--------|-------|----------|--------------|--------|
| Resend oder Loops Account | S | Florian | 🔴 Critical | None | [ ] |
| Email capture forms funktionsfähig machen | M | Florian | 🔴 Critical | Email provider | [ ] |
| Welcome Email automatisieren | M | Florian/Mia | 🔴 Critical | Email provider | [ ] |
| Daily Brief Email Template | L | Mia | 🟡 High | Email provider | [ ] |

**Definition of Done:**
- Email signups stored in database
- Welcome email sent within 5 minutes
- Daily Brief template ready for manual/automated sends
- Unsubscribe link functional

---

## Phase 3: Auth + Backend (Week 3-4)

**Goal:** User accounts, auth, credit system infrastructure ready.

| Task | Effort | Owner | Priority | Dependencies | Status |
|------|--------|-------|----------|--------------|--------|
| Tech Stack entscheiden (Supabase? Clerk? NextAuth?) | S | Florian | 🔴 Critical | None | [ ] |
| Auth implementieren (Email + Google SSO) | L | Florian/External | 🔴 Critical | Tech stack | [ ] |
| User DB | M | Florian/External | 🔴 Critical | Auth | [ ] |
| Credit System | L | Florian/External | 🔴 Critical | User DB | [ ] |
| X-Ray Backend hosten (Railway/Fly.io) | M | Florian/External | 🔴 Critical | Tech stack | [ ] |

**Definition of Done:**
- Users can sign up with email or Google
- User sessions persist
- Credit balance visible in account
- Backend deployed and accessible via API
- 3 free credits granted on signup

---

## Phase 4: Product Live (Week 4-6)

**Goal:** Core intelligence products functional and accessible to users.

| Task | Effort | Owner | Priority | Dependencies | Status |
|------|--------|-------|----------|--------------|--------|
| Corporate X-Ray via API | L | Florian/External | 🔴 Critical | Backend, Credit System | [ ] |
| Startup X-Ray via API | L | Florian/External | 🟡 High | Corporate X-Ray | [ ] |
| Report Storage + PDF Export | M | Florian/External | 🔴 Critical | API functional | [ ] |
| Dashboard: My Reports, Credits, Settings | M | Florian | 🔴 Critical | Auth, Reports | [ ] |

**Definition of Done:**
- User can run Corporate X-Ray and receive full report
- Reports stored in user account
- PDF export functional
- Credit deducted correctly per report
- Dashboard shows report history

---

## Phase 5: Growth (Week 6+)

**Goal:** Content engine + referral system driving organic growth.

| Task | Effort | Owner | Priority | Dependencies | Status |
|------|--------|-------|----------|--------------|--------|
| Daily Brief auto-publish | L | Florian/External | 🟡 High | Research Engine | [ ] |
| Blog CMS oder Markdown→HTML Pipeline | M | Florian | 🟢 Medium | None | [ ] |
| Referral System | L | External | 🟢 Medium | Credit System | [ ] |
| First paid customer | - | Florian | 🔴 Critical | Product live | [ ] |

**Definition of Done:**
- Daily Brief publishes automatically every morning
- Blog posts can be added without manual HTML editing
- Users can refer friends for bonus credits
- At least 1 paying customer (Starter tier or above)

---

## Effort Legend

- **S (Small):** <2 hours
- **M (Medium):** 2-8 hours
- **L (Large):** 8+ hours or multi-day

## Priority Legend

- 🔴 **Critical:** Blocks launch or core functionality
- 🟡 **High:** Important but not blocking
- 🟢 **Medium:** Nice to have, can be deferred

---

## Key Milestones

- **Week 1:** Static site live, domain configured, email capture working
- **Week 2:** Welcome emails automated, Daily Brief template ready
- **Week 3:** Auth functional, user accounts working
- **Week 4:** First X-Ray report generated via product
- **Week 5:** Dashboard live, reports stored
- **Week 6:** First paid customer

---

## Risk Factors

1. **Backend complexity underestimated** — Credit system + multi-agent orchestration may take longer than 2 weeks
2. **API rate limits** — Need to validate cost/performance for real-time report generation
3. **Quality control** — Reports need manual review before full automation
4. **Payments integration** — Stripe setup + subscription logic can be finicky

## Mitigation

- Start with manual report generation (Florian runs backend locally, delivers via email) until automation proven
- Tier 1 (Starter) = async delivery (up to 24h) to reduce infrastructure pressure
- Launch with Corporate X-Ray only, add Startup X-Ray in Week 5-6
- Use Lemon Squeezy instead of Stripe for faster payment setup

---

*Last updated: 2026-02-12*
