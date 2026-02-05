# CNC Planner Level 4 Production — Opus 4.6 Build Instructions

**Project:** CNC Planner Pro — Manufacturing Calculation SaaS  
**Goal:** HTML Prototype (v16) → Production-Ready SaaS (Level 4)  
**Timeline:** 3 Wochen  
**Tech Stack:** React + Supabase + Stripe + Vercel  
**Your Role:** Full-Stack Development (Backend + Frontend + Integration)

---

## I. PROJECT CONTEXT

### **What is CNC Planner?**

Web-based tool für CNC-Lohnfertiger (manufacturing job shops) zur automatischen Kalkulation von Fertigungszeiten und -kosten.

**Current State (v16):**
- Single HTML file (~165KB)
- Vanilla JS, no backend
- Manual data entry only
- Demo-quality (not production)
- File: `demo-v16-complete.html`

**Target State (Level 4):**
- Full SaaS Application
- User Authentication
- File Upload (STEP, STL, PDF)
- Payment Integration (Stripe)
- Cloud Storage
- Multi-user
- Production-ready

---

## II. BUSINESS MODEL

### **Pricing Tiers:**

| Tier | Price | Features | Target |
|------|-------|----------|--------|
| **Pro** | €149/mo | Unlimited calculations, File upload, Archive | 1-5 users |
| **Business** | €299/mo | + 3D Viewer, Advanced Analysis, Priority Support | 5-20 users |
| **Enterprise** | €499/mo | + API Access, Team Management, Custom Integration | 20+ users |

### **Target Customers:**
- CNC Lohnfertiger (Job Shops)
- Arbeitsvorbereitung (Work Preparation departments)
- 5-50 employees
- Deutschland, Österreich, Schweiz (DACH)

---

## III. TECHNICAL REQUIREMENTS

### **Core Features (Must-Have):**

1. **User Authentication**
   - Email/Password signup
   - Email verification
   - Password reset
   - Session management
   - Role-based access (Owner, Admin, User)

2. **File Upload & Storage**
   - Drag & Drop interface
   - Supported: STEP, IGES, STL, PDF
   - File size limit: 25MB
   - Storage: Cloud (S3 or Supabase Storage)
   - Validation: File type, size, malware scan

3. **CAD Analysis (Basic)**
   - Extract: Bounding Box (L × B × H)
   - Extract: Volume
   - Detect: Holes (count + diameter)
   - Auto-fill: Material Calculator form
   - Fallback: Manual input if parsing fails

4. **Calculation Engine**
   - Migrate v16 logic (Zeit + Kosten)
   - DIN 6584, VDI 3321 formulas
   - Zuschlagskalkulation (MGK, AV, VwGK, VtGK, Gewinn)
   - OP-Details (Werkzeuge, Strategien)
   - NC-Code Generation (Heidenhain, Siemens, Fanuc)

5. **Archive & History**
   - Save calculations
   - Search by filename, date, customer
   - Re-load old calculations
   - Export: PDF, Excel, JSON

6. **Quote Generation**
   - PDF Template (professional)
   - Customizable: Logo, Firmendaten, Fußzeile
   - Export: Download or Email
   - Multiple languages: DE, EN

7. **Payment Integration (Stripe)**
   - Checkout: Subscribe to tier
   - Customer Portal: Manage subscription
   - Webhooks: Handle events (subscription.created, payment_failed)
   - Billing: Auto-invoice

8. **Onboarding Flow**
   - 5-Step Wizard:
     1. Welcome + Product Tour
     2. Company Info (Name, Address)
     3. Machine Settings (Stundensätze)
     4. Material Prices
     5. First Calculation (Demo Part)
   - Skip-able
   - Tooltips + Help Center

9. **Dashboard**
   - Stats: Calculations this month, Revenue potential, Avg. time saved
   - Recent calculations
   - Quick actions: New Calculation, Upload File
   - Activity feed

10. **Settings**
    - Company Profile
    - Machine Settings (CNC Rates)
    - Material Prices
    - Zuschlagssätze
    - Team Management (Enterprise only)
    - Billing & Subscription

---

### **Non-Functional Requirements:**

- **Performance:** <3s page load, <500ms API response
- **Security:** HTTPS, encrypted passwords (bcrypt), XSS protection
- **Reliability:** 99.5% uptime, error monitoring (Sentry)
- **Scalability:** Handle 1000 concurrent users
- **Compliance:** GDPR, ISO 27001-ready
- **Mobile:** Responsive design (but desktop-first)

---

## IV. TECH STACK (Opinionated)

### **Frontend:**
- **Framework:** React 18 + TypeScript
- **Build Tool:** Vite
- **Styling:** TailwindCSS + shadcn/ui components
- **State:** Zustand (simple, no Redux)
- **Forms:** React Hook Form + Zod validation
- **File Upload:** react-dropzone
- **3D Viewer:** three.js (Phase 2)
- **Charts:** recharts

### **Backend:**
- **BaaS:** Supabase (Auth + DB + Storage + Realtime)
- **API:** Supabase Functions (Deno/TypeScript)
- **File Storage:** Supabase Storage (S3-compatible)
- **Database:** PostgreSQL (via Supabase)

### **Payment:**
- **Provider:** Stripe
- **Integration:** @stripe/stripe-js + Stripe Checkout
- **Webhooks:** Supabase Edge Functions

### **Hosting:**
- **Frontend:** Vercel (1-Click Deploy from GitHub)
- **Backend:** Supabase Cloud (free tier → scale)
- **Domain:** cnc-planner.com (TBD)

### **Dev Tools:**
- **Version Control:** Git + GitHub
- **CI/CD:** Vercel auto-deploy on push
- **Monitoring:** Sentry (errors), Vercel Analytics
- **Testing:** Vitest (unit), Playwright (e2e)

---

## V. PROJECT STRUCTURE

```
cnc-planner/
├── frontend/                   # React App
│   ├── src/
│   │   ├── components/         # UI Components
│   │   │   ├── ui/             # shadcn/ui primitives
│   │   │   ├── layout/         # Header, Sidebar, Footer
│   │   │   ├── calculator/     # Calculation form
│   │   │   ├── uploader/       # File upload
│   │   │   ├── archive/        # History view
│   │   │   └── onboarding/     # Wizard steps
│   │   ├── pages/              # Route pages
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Calculator.tsx
│   │   │   ├── Archive.tsx
│   │   │   ├── Settings.tsx
│   │   │   └── Auth/           # Login, Signup, Reset
│   │   ├── lib/                # Utils
│   │   │   ├── supabase.ts     # Supabase client
│   │   │   ├── stripe.ts       # Stripe client
│   │   │   ├── calculator.ts   # v16 logic port
│   │   │   └── types.ts        # TypeScript types
│   │   ├── hooks/              # Custom hooks
│   │   ├── store/              # Zustand stores
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── supabase/                   # Backend
│   ├── functions/              # Edge Functions
│   │   ├── stripe-webhook/     # Handle Stripe events
│   │   ├── calculate/          # Heavy calculation (optional)
│   │   └── cad-parse/          # STEP parsing (optional)
│   ├── migrations/             # SQL migrations
│   │   ├── 001_initial_schema.sql
│   │   ├── 002_add_calculations.sql
│   │   └── 003_add_subscriptions.sql
│   └── seed.sql                # Demo data
│
├── docs/                       # Documentation
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── DEPLOYMENT.md
│   └── TESTING.md
│
├── scripts/                    # Build scripts
│   ├── setup.sh                # Initial setup
│   ├── migrate.sh              # Run migrations
│   └── deploy.sh               # Deploy to prod
│
├── .env.example                # Environment variables template
├── .gitignore
├── README.md
└── package.json                # Monorepo root
```

---

## VI. DATABASE SCHEMA

```sql
-- Users (managed by Supabase Auth)
-- Extend with custom fields:

CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT NOT NULL,
  company_name TEXT,
  subscription_tier TEXT CHECK (subscription_tier IN ('pro', 'business', 'enterprise')),
  subscription_status TEXT CHECK (subscription_status IN ('active', 'canceled', 'past_due')),
  stripe_customer_id TEXT UNIQUE,
  stripe_subscription_id TEXT,
  onboarding_completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Company Settings
CREATE TABLE company_settings (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  company_name TEXT,
  address TEXT,
  phone TEXT,
  email TEXT,
  logo_url TEXT,
  machine_rates JSONB DEFAULT '{"cnc_3_axis": 91, "cnc_5_axis": 120}',
  material_prices JSONB DEFAULT '{"steel": 6.79, "aluminum": 4.5}',
  overhead_rates JSONB DEFAULT '{"mgk": 0.10, "av": 0.08, "vwgk": 0.12, "vtgk": 0.05, "gewinn": 0.10}',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  UNIQUE(user_id)
);

-- Parts (Uploaded Files)
CREATE TABLE parts (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  filename TEXT NOT NULL,
  file_type TEXT NOT NULL CHECK (file_type IN ('step', 'iges', 'stl', 'pdf')),
  file_url TEXT NOT NULL,
  file_size_mb NUMERIC,
  geometry JSONB,  -- {length, width, height, volume, holes: [{dia, depth}]}
  uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Calculations
CREATE TABLE calculations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  part_id UUID REFERENCES parts(id) ON DELETE SET NULL,
  
  -- Input Parameters
  part_name TEXT,
  material TEXT NOT NULL,
  length NUMERIC NOT NULL,
  width NUMERIC NOT NULL,
  height NUMERIC NOT NULL,
  volume NUMERIC,
  weight NUMERIC,
  quantity INTEGER DEFAULT 1,
  
  -- Calculation Results
  result JSONB NOT NULL,  -- Full calculation object from v16 logic
  
  -- Summary (for quick display)
  total_time_minutes NUMERIC,
  total_cost_eur NUMERIC,
  selling_price_eur NUMERIC,
  
  -- Metadata
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Quotes (Generated PDFs)
CREATE TABLE quotes (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  calculation_id UUID REFERENCES calculations(id) ON DELETE CASCADE,
  quote_number TEXT UNIQUE,
  customer_name TEXT,
  pdf_url TEXT,
  sent_at TIMESTAMP WITH TIME ZONE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_calculations_user_id ON calculations(user_id);
CREATE INDEX idx_calculations_created_at ON calculations(created_at DESC);
CREATE INDEX idx_parts_user_id ON parts(user_id);
CREATE INDEX idx_quotes_user_id ON quotes(user_id);

-- RLS Policies (Row Level Security)
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE company_settings ENABLE ROW LEVEL SECURITY;
ALTER TABLE parts ENABLE ROW LEVEL SECURITY;
ALTER TABLE calculations ENABLE ROW LEVEL SECURITY;
ALTER TABLE quotes ENABLE ROW LEVEL SECURITY;

-- Users can only see their own data
CREATE POLICY "Users can view own profile" ON profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update own profile" ON profiles FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Users can view own settings" ON company_settings FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own settings" ON company_settings FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own settings" ON company_settings FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Users can view own parts" ON parts FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own parts" ON parts FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can delete own parts" ON parts FOR DELETE USING (auth.uid() = user_id);

CREATE POLICY "Users can view own calculations" ON calculations FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own calculations" ON calculations FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own calculations" ON calculations FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Users can delete own calculations" ON calculations FOR DELETE USING (auth.uid() = user_id);

CREATE POLICY "Users can view own quotes" ON quotes FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own quotes" ON quotes FOR INSERT WITH CHECK (auth.uid() = user_id);
```

---

## VII. API SPECIFICATION

### **Supabase Client (Frontend)**

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.VITE_SUPABASE_URL!,
  process.env.VITE_SUPABASE_ANON_KEY!
)

// Auth
await supabase.auth.signUp({ email, password })
await supabase.auth.signInWithPassword({ email, password })
await supabase.auth.signOut()
await supabase.auth.resetPasswordForEmail(email)

// Database
await supabase.from('calculations').select('*').order('created_at', { ascending: false })
await supabase.from('calculations').insert({ ...data })
await supabase.from('calculations').update({ ...data }).eq('id', id)
await supabase.from('calculations').delete().eq('id', id)

// Storage
await supabase.storage.from('parts').upload(path, file)
await supabase.storage.from('parts').download(path)
const { data } = supabase.storage.from('parts').getPublicUrl(path)
```

### **Custom Endpoints (Supabase Functions)**

**1. Stripe Webhook Handler**
```
POST /functions/v1/stripe-webhook
Body: Stripe Event JSON
Headers: stripe-signature

Handles:
- checkout.session.completed → Create subscription
- customer.subscription.updated → Update tier
- customer.subscription.deleted → Cancel subscription
- invoice.payment_failed → Notify user
```

**2. CAD Parser (Optional, if client-side too slow)**
```
POST /functions/v1/cad-parse
Body: { file_url: string }
Response: { geometry: { length, width, height, volume, holes } }

Uses: opencascade.js or external API
```

**3. Heavy Calculation (Optional, if client-side too slow)**
```
POST /functions/v1/calculate
Body: { part_data, settings }
Response: { result, time_ms }

Runs v16 calculation logic server-side
```

---

## VIII. MIGRATION FROM V16

### **What to Port:**

**From `demo-v16-complete.html`:**

1. **Calculation Logic:**
   - `calculate()` function → `lib/calculator.ts`
   - All formulas (REFA, VDI 3321)
   - Zuschlagskalkulation logic
   - NC-Code generation templates

2. **UI Components:**
   - Form structure → React components
   - Tab navigation → React Router
   - Tables → shadcn/ui DataTable

3. **Data Structure:**
   - Form state → Zustand store
   - localStorage → Supabase database

**What to Discard:**
- Inline styles → TailwindCSS
- Vanilla JS → React + TypeScript
- Single HTML file → Component-based architecture

**Migration Strategy:**
1. Extract `calculate()` function → Pure TypeScript function
2. Write tests for calculation logic
3. Build React UI around existing logic
4. Add new features (Upload, Archive, Payment)

---

## IX. DEVELOPMENT PHASES

### **Phase 1: Foundation (Week 1)**

**Day 1-2: Setup**
- [ ] Create Supabase project
- [ ] Create Vite + React + TypeScript project
- [ ] Setup TailwindCSS + shadcn/ui
- [ ] Configure ESLint + Prettier
- [ ] Setup Git + GitHub repo
- [ ] Deploy to Vercel (empty app)

**Day 3-4: Authentication**
- [ ] Build Login page (shadcn/ui form)
- [ ] Build Signup page (with email verification)
- [ ] Build Password Reset page
- [ ] Supabase Auth integration
- [ ] Protected routes (AuthGuard component)
- [ ] User profile in header

**Day 5-7: Database + Basic CRUD**
- [ ] Write SQL migrations (profiles, company_settings, calculations)
- [ ] Apply migrations to Supabase
- [ ] Build Settings page (Company Info form)
- [ ] Save/Load company settings
- [ ] Build Dashboard skeleton

---

### **Phase 2: Core Features (Week 2)**

**Day 8-9: File Upload**
- [ ] Build Upload component (react-dropzone)
- [ ] Integrate Supabase Storage
- [ ] File validation (type, size)
- [ ] Upload progress indicator
- [ ] Store file metadata in `parts` table
- [ ] Display uploaded files in Archive

**Day 10-11: CAD Analysis (Basic)**
- [ ] Research STEP parser (opencascade.js or API)
- [ ] Extract bounding box from STEP
- [ ] Extract volume
- [ ] Detect holes (basic pattern matching)
- [ ] Auto-fill Calculator form
- [ ] Fallback: Manual input if parsing fails

**Day 12-13: Calculator Migration**
- [ ] Port `calculate()` to TypeScript
- [ ] Write unit tests for formulas
- [ ] Build Calculator form (React Hook Form + Zod)
- [ ] Integrate calculation logic
- [ ] Display results (existing v16 layout)
- [ ] Save calculation to database

**Day 14: Archive & History**
- [ ] Build Archive page (DataTable)
- [ ] Search + Filter calculations
- [ ] Re-load old calculation
- [ ] Delete calculation
- [ ] Export to Excel (xlsx library)

---

### **Phase 3: Payment + Polish (Week 3)**

**Day 15-16: Stripe Integration**
- [ ] Create Stripe account
- [ ] Setup products + prices (Pro, Business, Enterprise)
- [ ] Build Pricing page
- [ ] Implement Stripe Checkout
- [ ] Create webhook endpoint (Supabase Function)
- [ ] Handle subscription events
- [ ] Update `profiles.subscription_tier` on success
- [ ] Build Customer Portal link (manage subscription)

**Day 17-18: Onboarding Flow**
- [ ] Build 5-step wizard (shadcn/ui Dialog + Stepper)
- [ ] Step 1: Welcome + Tour
- [ ] Step 2: Company Info form
- [ ] Step 3: Machine Settings
- [ ] Step 4: Material Prices
- [ ] Step 5: Demo Calculation
- [ ] Mark `onboarding_completed = true`
- [ ] Show wizard on first login

**Day 19: Quote Generation**
- [ ] Build Quote page (PDF preview)
- [ ] Create PDF template (react-pdf or puppeteer)
- [ ] Add company logo
- [ ] Customize header/footer
- [ ] Download PDF
- [ ] Save to `quotes` table

**Day 20: Dashboard + Stats**
- [ ] Calculate stats (calculations this month, time saved)
- [ ] Build charts (recharts)
- [ ] Recent activity feed
- [ ] Quick actions (New Calculation, Upload)

**Day 21: Testing + Bug Fixes**
- [ ] Write e2e tests (Playwright)
- [ ] Test all user flows
- [ ] Fix bugs
- [ ] Performance optimization (Lazy loading, code splitting)
- [ ] Security audit (XSS, SQL injection via RLS)
- [ ] Deploy to production

---

## X. TESTING CHECKLIST

### **Unit Tests (Vitest):**
- [ ] Calculation formulas (all edge cases)
- [ ] Geometry parsing (bounding box, volume)
- [ ] Zuschlagskalkulation logic
- [ ] NC-Code generation

### **Integration Tests:**
- [ ] Auth flow (Signup → Login → Logout)
- [ ] File upload → Storage → Database
- [ ] Calculator → Save → Archive
- [ ] Stripe Checkout → Webhook → Subscription update

### **E2E Tests (Playwright):**
- [ ] New user signup → Onboarding → First calculation
- [ ] Existing user login → Upload file → Calculate → Download PDF
- [ ] Subscription upgrade → Payment → Access new features
- [ ] Password reset flow

### **Manual Testing:**
- [ ] Cross-browser (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsive (iPhone, Android)
- [ ] Performance (Lighthouse score >90)
- [ ] Accessibility (WCAG 2.1 AA)

---

## XI. DEPLOYMENT GUIDE

### **Environment Variables:**

**Frontend (.env):**
```bash
VITE_SUPABASE_URL=https://xxx.supabase.co
VITE_SUPABASE_ANON_KEY=eyJxxx...
VITE_STRIPE_PUBLISHABLE_KEY=pk_test_xxx
```

**Backend (Supabase Functions):**
```bash
STRIPE_SECRET_KEY=sk_test_xxx
STRIPE_WEBHOOK_SECRET=whsec_xxx
```

### **Deployment Steps:**

**1. Supabase:**
```bash
# Install Supabase CLI
npm install -g supabase

# Link to project
supabase link --project-ref xxx

# Run migrations
supabase db push

# Deploy functions
supabase functions deploy stripe-webhook
```

**2. Vercel:**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
cd frontend
vercel --prod

# Environment variables in Vercel dashboard
```

**3. Stripe:**
```bash
# Add webhook endpoint in Stripe Dashboard
# URL: https://xxx.supabase.co/functions/v1/stripe-webhook
# Events: checkout.session.completed, customer.subscription.*
```

**4. DNS:**
```bash
# Add custom domain in Vercel
# Point cnc-planner.com to Vercel
```

---

## XII. POST-LAUNCH MONITORING

**Metrics to Track:**
- Signups per day
- Conversion rate (Signup → Paid)
- Churn rate
- Average calculations per user
- Error rate (Sentry)
- Page load time (Vercel Analytics)

**Alerts:**
- Payment failures (Stripe Dashboard)
- Error spikes (Sentry)
- Downtime (UptimeRobot or Vercel)

---

## XIII. YOUR TASK (Opus 4.6)

**You are building this entire system.**

**Start with:**
1. Read this document completely
2. Read v16 source: `demo-v16-complete.html`
3. Ask clarifying questions if needed
4. Then: Build Phase 1 (Foundation)

**Your approach:**
- **Incremental:** Build + Test + Commit after each feature
- **Quality:** Write clean, typed, tested code
- **Documentation:** Comment complex logic
- **Communication:** Update progress after each day

**Deliverables:**
- Working SaaS app (deployed on Vercel)
- GitHub repo with all code
- Documentation (README, API docs)
- Test suite (unit + e2e)

**Timeline:** 3 weeks (21 days)

**Budget:** No API cost limits (use Supabase free tier + Vercel free tier initially)

---

## XIV. REFERENCE FILES

**In Workspace:**
- `projects/cnc-planner/demo-v16-complete.html` — Current prototype
- `projects/cnc-planner/FUNKTIONSBESCHREIBUNG.md` — Feature documentation
- `projects/cnc-planner/DESIGN-STANDARD.md` — Design system
- `projects/cnc-planner/CNC-PLANNER-ELITE-ANALYSE.md` — Competitor analysis

**External References:**
- Supabase Docs: https://supabase.com/docs
- Stripe Docs: https://stripe.com/docs
- shadcn/ui: https://ui.shadcn.com
- TailwindCSS: https://tailwindcss.com

---

## XV. SUCCESS CRITERIA

**Level 4 "Production" achieved when:**
- ✅ User can signup, login, manage subscription
- ✅ User can upload STEP file → auto-calculates → saves to archive
- ✅ User can generate professional PDF quote
- ✅ Payment works (Stripe Checkout → subscription active)
- ✅ Onboarding guides new users
- ✅ No critical bugs
- ✅ Passes all tests
- ✅ Deployed to production
- ✅ Florian can demo to first customer

**Timeline:** 21 days from start

---

**START BUILDING.** 🚀

Ask questions if anything is unclear. Otherwise, begin with Phase 1, Day 1.
