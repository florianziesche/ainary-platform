/**
 * DepoDigest Pro - Frontend Application
 * Handles UI interactions and data display
 */

// Demo data - pre-generated analysis for Martinez v. Acme Trucking
const DEMO_DATA = {
    metadata: {
        case_name: "Martinez v. Acme Trucking, Inc. and James Wilson",
        case_number: "2025-CV-04521",
        deposition_date: "2026-01-15",
        analyzed_at: new Date().toISOString(),
        version: "1.0"
    },
    witness: {
        name: "James Wilson",
        role: "Defendant - Commercial Truck Driver",
        credibility_assessment: "Witness credibility is significantly compromised. Wilson provided inconsistent statements about his sleep duration (first claiming 4-5 hours, then admitting times that calculate to approximately 3 hours). He was evasive about texting while driving, claiming he 'doesn't remember' despite phone records showing a text sent 2 minutes before impact. His demeanor shifted notably when confronted with documentary evidence, becoming defensive and vague. The officer's contemporaneous observation that Wilson 'appeared fatigued' and his own statement about being 'distracted' are powerful admissions that undermine any attempt to shift blame to the plaintiff.",
        demeanor_notes: "Became defensive and evasive when confronted with cell phone records. Frequently used phrases like 'I don't remember' and 'I guess' when pressed on critical details. Appeared uncomfortable when discussing his prior disciplinary record.",
        key_weaknesses: [
            "Admitted to only 3 hours of sleep before operating commercial vehicle",
            "Cannot explain or deny texting 2 minutes before accident",
            "Prior disciplinary record for hours-of-service violations",
            "Admitted to driving 10 mph over speed limit",
            "Told officer at scene he was 'distracted'",
            "Safety training was deferred and not completed"
        ],
        key_strengths: [
            "15 years of driving experience with only one serious accident",
            "Expressed genuine remorse for the incident",
            "Immediately called 911 after the accident",
            "No evidence of alcohol or drug impairment"
        ]
    },
    executive_summary: `This deposition provides exceptionally strong evidence for the plaintiff's case. Defendant James Wilson made multiple critical admissions that establish negligence and severely damage his credibility.

Key findings: Wilson admitted to operating a commercial truck on approximately 3 hours of sleep after staying up late watching a baseball game. Cell phone records prove he sent a text message just 2 minutes before striking the plaintiff. He was traveling 10 mph over the posted speed limit. At the scene, Wilson told the responding officer he "might have been distracted," and the officer noted Wilson "appeared fatigued."

Wilson's employment file reveals prior disciplinary actions for hours-of-service violations, and his safety training was deferred and never completed before the accident. These facts establish a pattern of disregard for safety regulations.

The combination of fatigue, distracted driving (texting), speeding, and inadequate training creates a compelling case for negligence. Wilson's inability to provide consistent testimony about his sleep duration and his evasive responses about the texting further damage his credibility. This deposition significantly strengthens the plaintiff's position for both liability and potential punitive damages.`,
    narrative_summary: `On October 14, 2025, at approximately 7:30 AM, James Wilson was operating a commercial truck for Acme Trucking when he struck pedestrian Maria Martinez in a crosswalk at the intersection of Atlantic Avenue and Flatbush Avenue in Brooklyn, New York.

Wilson began his shift at 4:00 AM after getting only about 3 hours of sleep. He had stayed up until after midnight watching a Yankees playoff game the night before. Despite feeling "a little bit" tired, Wilson chose to drive anyway, noting that he has "driven on less sleep before."

As Wilson approached the intersection, the traffic light turned yellow. Rather than stopping, Wilson decided to proceed through while traveling at approximately 35 mph in a 25 mph zone. He testified that he saw Ms. Martinez "at the last second" in the crosswalk before impact.

Cell phone records introduced as evidence show Wilson sent a text message at 7:28 AM—just two minutes before the accident at 7:30 AM. When asked about this, Wilson claimed he "doesn't remember texting" and suggested he might have been at a red light, though this is inconsistent with his testimony about proceeding through the yellow light.

At the scene, Wilson made a critical admission to Officer Daniels, stating he "might have been distracted." The officer also noted in his report that Wilson "appeared fatigued."

Wilson's employment records reveal prior disciplinary actions for hours-of-service violations, including driving 14 hours in a single shift (maximum is 11 hours) and driving without required rest breaks. His safety training, which was recommended in January 2025, was "deferred due to scheduling" and never completed.

Ms. Martinez suffered severe injuries including a fractured pelvis, traumatic brain injury, multiple broken ribs, and internal bleeding. She was hospitalized for three weeks and has undergone four surgeries. She may never walk normally again.

When confronted with the totality of his conduct—speeding, possible texting, and fatigue—Wilson admitted it would constitute "bad judgment" that "could seriously injure or kill someone." He acknowledged that is "exactly what happened here."`,
    key_admissions: [
        {
            quote: "I'd say maybe four or five hours... Around midnight, maybe a little after... Around 3:15 or so [woke up]... I guess so, if you do the math [approximately 3 hours].",
            type: "negligence",
            severity: "critical",
            reference: { page: 8, line_start: 24, line_end: 26, formatted: "Pages 8-10, Lines 24-22" },
            context: "Questioning about sleep before the shift",
            impeachment_value: "Wilson contradicted himself within minutes, first claiming 4-5 hours then providing times that calculate to only 3 hours. This inconsistency damages credibility and establishes fatigue as a factor."
        },
        {
            quote: "I was feeling tired that morning... A little bit, I suppose. But I've driven on less sleep before.",
            type: "negligence",
            severity: "critical",
            reference: { page: 10, line_start: 10, line_end: 14, formatted: "Page 10, Lines 10-14" },
            context: "Asked if he was tired that morning",
            impeachment_value: "Direct admission of driving while fatigued. The cavalier attitude about driving tired ('I've driven on less sleep before') suggests pattern of reckless behavior."
        },
        {
            quote: "I'd estimate around 35 miles per hour... I believe it's 25 [speed limit].",
            type: "negligence",
            severity: "significant",
            reference: { page: 11, line_start: 7, line_end: 13, formatted: "Page 11, Lines 7-13" },
            context: "Speed at time of accident",
            impeachment_value: "Admitted to traveling 10 mph over the speed limit. Combined with fatigue and possible distraction, establishes multiple simultaneous negligent acts."
        },
        {
            quote: "It shows a text message sent [at 7:28 AM]... Yes [the accident occurred at approximately 7:30 AM]... It's possible [texting while the truck was in motion]. I really don't remember.",
            type: "negligence",
            severity: "critical",
            reference: { page: 23, line_start: 20, line_end: 26, formatted: "Pages 23-25, Lines 20-17" },
            context: "Cell phone records showing text 2 minutes before accident",
            impeachment_value: "Documentary evidence proves phone use immediately before accident. Wilson's inability to explain or deny is damning—either he was texting while driving or has convenient memory loss about incriminating evidence."
        },
        {
            quote: "I told Officer Daniels... 'I didn't see her until it was too late. I might have been distracted.'... I might have said something like that.",
            type: "liability",
            severity: "critical",
            reference: { page: 31, line_start: 11, line_end: 22, formatted: "Page 31, Lines 11-22" },
            context: "Statement made to officer at scene",
            impeachment_value: "Contemporaneous admission of distraction at the scene, before he had time to construct a defense narrative. This is the most damaging admission—his own words at the moment of truth."
        },
        {
            quote: "Driver appeared fatigued. Driver admitted to starting shift at 4 AM.",
            type: "negligence",
            severity: "significant",
            reference: { page: 32, line_start: 8, line_end: 11, formatted: "Page 32, Lines 8-11" },
            context: "Officer's observations in accident report",
            impeachment_value: "Third-party professional observation corroborating fatigue. Officer had no bias and recorded what he saw at the scene."
        },
        {
            quote: "It was a warning about hours of service violations... I had exceeded my allowable driving hours on a few occasions... I drove 14 hours in a single shift when the maximum is 11 hours.",
            type: "negligence",
            severity: "significant",
            reference: { page: 45, line_start: 14, line_end: 24, formatted: "Pages 45-46, Lines 14-10" },
            context: "Prior disciplinary record",
            impeachment_value: "Establishes pattern of disregarding safety regulations. Not an isolated incident—Wilson has a history of prioritizing schedule over safety."
        },
        {
            quote: "Refresher training was recommended in January 2025 but was listed as 'deferred due to scheduling.'... I was still qualified. The training wasn't mandatory.",
            type: "negligence",
            severity: "moderate",
            reference: { page: 52, line_start: 18, line_end: 11, formatted: "Pages 52-53, Lines 18-11" },
            context: "Safety training records",
            impeachment_value: "Shows both driver and company negligence—recommended training was skipped. Wilson's dismissive attitude ('training wasn't mandatory') shows lack of safety consciousness."
        },
        {
            quote: "That would be bad judgment, yes... Bad judgment that could seriously injure or kill someone?... Yes... And that's exactly what happened here?... Yes.",
            type: "liability",
            severity: "critical",
            reference: { page: 60, line_start: 4, line_end: 21, formatted: "Page 60, Lines 4-21" },
            context: "Final line of plaintiff questioning",
            impeachment_value: "Complete admission that his conduct was reckless and caused the injuries. Wilson agreed that texting while driving a commercial truck on 3 hours sleep at 10 mph over the limit 'is exactly what happened here.'"
        },
        {
            quote: "I made a mistake. I should have been more careful... I shouldn't have tried to make the yellow light. I should have stopped... I should have gotten more sleep.",
            type: "liability",
            severity: "significant",
            reference: { page: 59, line_start: 4, line_end: 19, formatted: "Page 59, Lines 4-19" },
            context: "Wilson's acknowledgment of fault",
            impeachment_value: "Defendant's own words accepting responsibility. These admissions can be highlighted in closing arguments as defendant's acknowledgment of his failures."
        }
    ],
    timeline: [
        {
            date: "2024-06-22",
            time: null,
            description: "Wilson received disciplinary warning for hours-of-service violations (drove 14 hours in single shift)",
            reference: { page: 45, line_start: 10, line_end: 24, formatted: "Page 45, Lines 10-24" },
            significance: "Establishes prior pattern of safety violations"
        },
        {
            date: "2025-01-01",
            time: null,
            description: "Safety refresher training recommended but deferred",
            reference: { page: 52, line_start: 18, line_end: 21, formatted: "Page 52, Lines 18-21" },
            significance: "Training that might have prevented accident was skipped"
        },
        {
            date: "2025-03-01",
            time: null,
            description: "Wilson's last completed safety training (over 2.5 years before accident)",
            reference: { page: 52, line_start: 11, line_end: 14, formatted: "Page 52, Lines 11-14" },
            significance: "Long gap in safety training"
        },
        {
            date: "2025-10-13",
            time: "24:00",
            description: "Wilson went to bed around midnight after watching Yankees playoff game",
            reference: { page: 9, line_start: 8, line_end: 13, formatted: "Page 9, Lines 8-13" },
            significance: "Establishes inadequate rest before shift"
        },
        {
            date: "2025-10-14",
            time: "03:15",
            description: "Wilson woke up (approximately 3 hours of sleep)",
            reference: { page: 9, line_start: 15, line_end: 18, formatted: "Page 9, Lines 15-18" },
            significance: "Only 3 hours sleep before operating commercial vehicle"
        },
        {
            date: "2025-10-14",
            time: "04:00",
            description: "Wilson started his shift at Acme Trucking",
            reference: { page: 8, line_start: 11, line_end: 13, formatted: "Page 8, Lines 11-13" },
            significance: "Began driving while severely fatigued"
        },
        {
            date: "2025-10-14",
            time: "07:28",
            description: "Wilson sent text message (2 minutes before accident)",
            reference: { page: 23, line_start: 15, line_end: 25, formatted: "Page 23, Lines 15-25" },
            significance: "Evidence of distracted driving immediately before impact"
        },
        {
            date: "2025-10-14",
            time: "07:30",
            description: "Wilson struck Maria Martinez in crosswalk at Atlantic & Flatbush",
            reference: { page: 11, line_start: 21, line_end: 24, formatted: "Page 11-12" },
            significance: "The accident - severe injuries to plaintiff"
        }
    ],
    contradictions: [
        {
            statement_1: "I'd say maybe four or five hours [of sleep]",
            statement_1_ref: { page: 8, line_start: 24, line_end: 26, formatted: "Page 8, Lines 24-26" },
            statement_2: "Around midnight, maybe a little after [went to bed]... Around 3:15 or so [woke up]",
            statement_2_ref: { page: 9, line_start: 13, line_end: 18, formatted: "Page 9, Lines 13-18" },
            explanation: "Wilson first claimed 4-5 hours of sleep, but the times he provided (midnight to 3:15 AM) calculate to approximately 3 hours. When confronted, he tried to suggest he 'might have fallen asleep during the game' to explain the discrepancy.",
            severity: "critical"
        },
        {
            statement_1: "I don't remember texting while driving",
            statement_1_ref: { page: 24, line_start: 4, line_end: 6, formatted: "Page 24, Lines 4-6" },
            statement_2: "I might have been at a red light [when texting]",
            statement_2_ref: { page: 24, line_start: 20, line_end: 20, formatted: "Page 24, Line 20" },
            explanation: "Wilson first claimed no memory of texting, then offered an explanation for when he might have texted. Either he remembers or he doesn't—offering an explanation suggests he does remember and is trying to minimize.",
            severity: "significant"
        },
        {
            statement_1: "I was pretty shook up at the time [when I said I was distracted]",
            statement_1_ref: { page: 31, line_start: 17, line_end: 17, formatted: "Page 31, Line 17" },
            statement_2: "I was shaken up from the accident. Anyone would look fatigued after something like that.",
            statement_2_ref: { page: 32, line_start: 16, line_end: 18, formatted: "Page 32, Lines 16-18" },
            explanation: "Wilson tried to explain away both his 'distracted' admission and the officer's fatigue observation by claiming post-accident stress. This suggests a pattern of post-hoc rationalization rather than truthful testimony.",
            severity: "moderate"
        }
    ],
    cross_exam_questions: [
        {
            question: "Mr. Wilson, you testified earlier that you got 4 to 5 hours of sleep the night before the accident, correct?",
            purpose: "Lock in the initial sleep claim before impeaching with calculated time",
            based_on: { page: 8, line_start: 24, line_end: 26, formatted: "Page 8, Lines 24-26" },
            follow_up_if_admits: "And you also testified you went to bed around midnight and woke up at 3:15 AM, correct?",
            follow_up_if_denies: "Let me read from your deposition, page 8, lines 24-26..."
        },
        {
            question: "If you went to bed at midnight and woke up at 3:15 AM, that's approximately 3 hours of sleep, isn't it?",
            purpose: "Force acknowledgment of the actual sleep duration",
            based_on: { page: 9, line_start: 15, line_end: 22, formatted: "Page 9, Lines 15-22" },
            follow_up_if_admits: "So when you told this jury you got 4 to 5 hours of sleep, that wasn't accurate, was it?",
            follow_up_if_denies: "Can you explain how midnight to 3:15 AM equals 4 to 5 hours?"
        },
        {
            question: "At 7:28 AM on October 14, 2025—two minutes before you struck my client—you sent a text message, correct?",
            purpose: "Establish texting close to accident with documentary proof",
            based_on: { page: 23, line_start: 20, line_end: 25, formatted: "Page 23, Lines 20-25" },
            follow_up_if_admits: "And you can't tell this jury with certainty that you weren't looking at your phone when you hit Maria Martinez, can you?",
            follow_up_if_denies: "Your Honor, I'd like to show the witness Exhibit 2, his cell phone records..."
        },
        {
            question: "When Officer Daniels arrived at the scene, you told him you 'might have been distracted,' didn't you?",
            purpose: "Highlight contemporaneous admission of distraction",
            based_on: { page: 31, line_start: 11, line_end: 22, formatted: "Page 31, Lines 11-22" },
            follow_up_if_admits: "You said that before you had a chance to talk to any lawyers or think about your legal exposure, correct?",
            follow_up_if_denies: "Let me show you Exhibit 3, the accident report prepared by Officer Daniels..."
        },
        {
            question: "You were traveling 35 miles per hour in a 25 mile per hour zone, correct?",
            purpose: "Establish speeding as additional negligent act",
            based_on: { page: 11, line_start: 7, line_end: 13, formatted: "Page 11, Lines 7-13" },
            follow_up_if_admits: "That's 10 miles per hour—40%—over the legal limit?",
            follow_up_if_denies: "Let me read your testimony from page 11 of your deposition..."
        },
        {
            question: "In June 2024, you were disciplined by Acme Trucking for driving 14 hours in a single shift when the legal maximum is 11 hours, weren't you?",
            purpose: "Establish pattern of safety violations",
            based_on: { page: 45, line_start: 22, line_end: 24, formatted: "Page 45, Lines 22-24" },
            follow_up_if_admits: "So this wasn't your first time disregarding safety rules designed to protect the public?",
            follow_up_if_denies: "I'd like to show the witness Exhibit 4, his personnel file..."
        }
    ],
    impeachment_points: [
        "Sleep duration contradiction: Claimed 4-5 hours but times provided calculate to 3 hours",
        "Texting timeline: Sent text at 7:28 AM, accident at 7:30 AM—cannot explain or deny phone use",
        "Scene admission: Told Officer Daniels he 'might have been distracted' before any legal consultation",
        "Speeding: Admitted to 35 mph in 25 mph zone (40% over limit)",
        "Prior violations: History of hours-of-service violations shows pattern of disregard for safety",
        "Deferred training: Recommended safety training was never completed",
        "Memory convenience: Claims not to remember texting but offers explanation for when he might have texted"
    ],
    settlement_impact: {
        overall_score: 82,
        liability_strength: 88,
        damages_support: 75,
        credibility_issues: 85,
        key_factors: [
            "Multiple concurrent negligent acts: fatigue, speeding, texting, running yellow light",
            "Contemporaneous admission of distraction to responding officer",
            "Documentary evidence of phone use 2 minutes before impact",
            "Prior disciplinary history for safety violations",
            "Witness credibility damaged by contradictory sleep testimony",
            "Defendant's own admission that his conduct was 'bad judgment' that 'could seriously injure or kill someone'"
        ],
        settlement_range_adjustment: "+25-35%",
        reasoning: `This deposition significantly strengthens the plaintiff's negotiating position and case value. The defendant made multiple critical admissions that establish clear negligence: operating a commercial vehicle on approximately 3 hours of sleep, texting within 2 minutes of the accident, exceeding the speed limit by 40%, and attempting to beat a yellow light.

The contemporaneous statement to Officer Daniels ("I might have been distracted") is particularly powerful because it was made at the scene before Wilson had any opportunity to consult with counsel or craft a defensive narrative. Combined with the officer's observation that Wilson "appeared fatigued," this creates a compelling picture of a drowsy, distracted driver who caused catastrophic injuries.

Wilson's credibility is severely compromised. He provided contradictory testimony about his sleep duration within minutes of each statement, and his "I don't remember" responses about texting are undermined by his subsequent attempt to explain when the texting might have occurred. Juries do not respond well to witnesses who appear evasive or dishonest.

The prior disciplinary history for hours-of-service violations transforms this from an isolated mistake into a pattern of reckless behavior. Combined with the deferred safety training, this evidence could support a punitive damages argument in front of the right jury.

Given the severity of Ms. Martinez's injuries (fractured pelvis, TBI, four surgeries, potential permanent disability), the baseline case value was already substantial. This deposition testimony increases that value by an estimated 25-35% based on the strength of the liability evidence and the potential jury impact of the defendant's admissions.

Recommendation: This deposition provides excellent leverage for settlement negotiations. The defense faces significant exposure, and a jury would likely respond negatively to the combination of fatigue, texting, speeding, and Wilson's evasive testimony. Consider demanding in the upper range of case value, with the deposition admissions as primary leverage points.`
    }
};

// Application State
let analysisData = null;

// Tab Navigation
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const tabId = link.dataset.tab;
        
        // Update nav
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        
        // Update content
        document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
        document.getElementById(tabId).classList.add('active');
    });
});

// File Upload
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const transcriptText = document.getElementById('transcriptText');

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const file = e.dataTransfer.files[0];
    handleFile(file);
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    handleFile(file);
});

function handleFile(file) {
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            transcriptText.value = e.target.result;
        };
        reader.readAsText(file);
    }
}

// Load Demo
document.getElementById('loadDemoBtn').addEventListener('click', () => {
    analysisData = DEMO_DATA;
    populateUI(analysisData);
    
    // Switch to analysis tab
    document.querySelector('.nav-link[data-tab="analysis"]').click();
});

// Analyze Button
document.getElementById('analyzeBtn').addEventListener('click', async () => {
    const transcript = transcriptText.value.trim();
    if (!transcript) {
        alert('Please upload a file or paste transcript text.');
        return;
    }
    
    // For demo purposes, use demo data
    // In production, this would call the backend API
    showLoading('Analyzing deposition...');
    
    // Simulate API call
    setTimeout(() => {
        analysisData = DEMO_DATA;
        populateUI(analysisData);
        hideLoading();
        document.querySelector('.nav-link[data-tab="analysis"]').click();
    }, 2000);
});

// Loading Overlay
function showLoading(text) {
    document.getElementById('loadingText').textContent = text;
    document.getElementById('loadingOverlay').classList.add('active');
}

function hideLoading() {
    document.getElementById('loadingOverlay').classList.remove('active');
}

// Populate UI with Analysis Data
function populateUI(data) {
    // Case Header
    document.getElementById('caseName').textContent = data.metadata.case_name;
    document.getElementById('caseNumber').textContent = data.metadata.case_number;
    document.getElementById('depoDate').textContent = formatDate(data.metadata.deposition_date);
    document.getElementById('witnessName').textContent = data.witness.name;
    
    // Witness Section
    document.getElementById('witnessFullName').textContent = data.witness.name;
    document.getElementById('witnessRole').textContent = data.witness.role;
    document.getElementById('credibilityText').textContent = data.witness.credibility_assessment;
    
    // Weaknesses
    const weaknessesList = document.getElementById('weaknessesList');
    weaknessesList.innerHTML = data.witness.key_weaknesses.map(w => `<li>${w}</li>`).join('');
    
    // Strengths
    const strengthsList = document.getElementById('strengthsList');
    strengthsList.innerHTML = data.witness.key_strengths.map(s => `<li>${s}</li>`).join('');
    
    // Executive Summary
    document.getElementById('executiveSummary').innerHTML = data.executive_summary.split('\n\n').map(p => `<p>${p}</p>`).join('');
    
    // Timeline
    const timeline = document.getElementById('timeline');
    timeline.innerHTML = data.timeline.map(event => `
        <div class="timeline-item">
            <div class="timeline-date">${formatDate(event.date)}${event.time ? ' at ' + event.time : ''}</div>
            <div class="timeline-content">
                <p>${event.description}</p>
                <p class="timeline-ref">${event.reference.formatted}</p>
                <p><em>${event.significance}</em></p>
            </div>
        </div>
    `).join('');
    
    // Admissions
    const admissionsList = document.getElementById('admissionsList');
    admissionsList.innerHTML = data.key_admissions.map(admission => `
        <div class="admission-card" data-type="${admission.type}" data-severity="${admission.severity}">
            <div class="admission-header">
                <span class="admission-type ${admission.type}">${admission.type}</span>
                <span class="severity-badge ${admission.severity}">${admission.severity}</span>
            </div>
            <div class="admission-body">
                <div class="admission-quote">"${admission.quote}"</div>
                <div class="admission-meta">
                    <span>${admission.reference.formatted}</span>
                    <span>${admission.context}</span>
                </div>
                <div class="admission-value">
                    <strong>Impeachment Value:</strong> ${admission.impeachment_value}
                </div>
            </div>
        </div>
    `).join('');
    
    // Contradictions
    const contradictionsList = document.getElementById('contradictionsList');
    contradictionsList.innerHTML = data.contradictions.map(c => `
        <div class="contradiction-card">
            <div class="contradiction-header">
                <span class="admission-type credibility">Contradiction</span>
                <span class="severity-badge ${c.severity}">${c.severity}</span>
            </div>
            <div class="contradiction-body">
                <div class="contradiction-statements">
                    <div class="statement-box">
                        <div class="statement-label">Statement 1</div>
                        <div class="statement-text">"${c.statement_1}"</div>
                        <div class="statement-ref">${c.statement_1_ref.formatted}</div>
                    </div>
                    <div class="vs-badge">VS</div>
                    <div class="statement-box">
                        <div class="statement-label">Statement 2</div>
                        <div class="statement-text">"${c.statement_2}"</div>
                        <div class="statement-ref">${c.statement_2_ref.formatted}</div>
                    </div>
                </div>
                <div class="contradiction-explanation">
                    <strong>Analysis:</strong> ${c.explanation}
                </div>
            </div>
        </div>
    `).join('');
    
    // Impeachment Points
    const impeachmentList = document.getElementById('impeachmentList');
    impeachmentList.innerHTML = data.impeachment_points.map(point => `<li>${point}</li>`).join('');
    
    // Cross-Exam Questions
    const questionsList = document.getElementById('questionsList');
    questionsList.innerHTML = data.cross_exam_questions.map(q => `
        <div class="question-card">
            <div class="question-text">"${q.question}"</div>
            <div class="question-purpose">${q.purpose}</div>
            <div class="question-ref">Based on: ${q.based_on.formatted}</div>
            <div class="follow-ups">
                <div class="follow-up-box admits">
                    <div class="follow-up-label">If Admits</div>
                    <div>${q.follow_up_if_admits}</div>
                </div>
                <div class="follow-up-box denies">
                    <div class="follow-up-label">If Denies</div>
                    <div>${q.follow_up_if_denies}</div>
                </div>
            </div>
        </div>
    `).join('');
    
    // Settlement Impact
    const impact = data.settlement_impact;
    document.getElementById('overallScore').querySelector('.score-number').textContent = impact.overall_score;
    document.getElementById('adjustmentValue').textContent = impact.settlement_range_adjustment;
    
    document.getElementById('liabilityBar').style.width = impact.liability_strength + '%';
    document.getElementById('liabilityValue').textContent = impact.liability_strength;
    
    document.getElementById('damagesBar').style.width = impact.damages_support + '%';
    document.getElementById('damagesValue').textContent = impact.damages_support;
    
    document.getElementById('credibilityBar').style.width = impact.credibility_issues + '%';
    document.getElementById('credibilityValue').textContent = impact.credibility_issues;
    
    // Key Factors
    const keyFactors = document.getElementById('keyFactors');
    keyFactors.innerHTML = impact.key_factors.map(f => `<li>${f}</li>`).join('');
    
    // Reasoning
    document.getElementById('settlementReasoning').innerHTML = impact.reasoning.split('\n\n').map(p => `<p>${p}</p>`).join('');
}

// Filters
document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        const filter = btn.dataset.filter;
        document.querySelectorAll('.admission-card').forEach(card => {
            if (filter === 'all' || card.dataset.type === filter || card.dataset.severity === filter) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
});

// Utility Functions
function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    });
}
