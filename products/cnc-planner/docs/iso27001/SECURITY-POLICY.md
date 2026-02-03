# CNC Planner Pro — Information Security Policy

**Document ID:** ISO27001-SP-001  
**Version:** 1.0  
**Classification:** Public  
**Effective Date:** 2026-02-03  
**Review Date:** 2027-02-03  
**Owner:** Florian Ziesche, CEO

---

## 1. Purpose

This Information Security Policy establishes the framework for protecting CNC Planner Pro's information assets, customer data, and system integrity in accordance with ISO/IEC 27001:2022 standards.

---

## 2. Scope

This policy applies to:
- All CNC Planner Pro software components
- Customer project data and calculations
- User credentials and authentication data
- System configurations and backups
- All personnel with access to systems

---

## 3. Information Security Objectives

| Objective | Target | Measure |
|-----------|--------|---------|
| Confidentiality | Protect customer data from unauthorized access | Access controls, encryption |
| Integrity | Ensure data accuracy and completeness | Validation, audit trails |
| Availability | Maintain 99.5% system uptime | Redundancy, backups |

---

## 4. Data Classification

### 4.1 Classification Levels

| Level | Description | Examples | Handling |
|-------|-------------|----------|----------|
| **Public** | No restrictions | Marketing materials, public docs | Standard handling |
| **Internal** | Business use only | Procedures, templates | Access controlled |
| **Confidential** | Sensitive business data | Customer data, pricing | Encrypted, logged |
| **Restricted** | Highly sensitive | Credentials, keys | Encrypted, MFA required |

### 4.2 Customer Data Classification

All customer data (projects, calculations, company information) is classified as **Confidential** and handled accordingly.

---

## 5. Access Control

### 5.1 Authentication Requirements

| User Type | Requirements |
|-----------|-------------|
| Standard User | Email + Password (min. 8 chars, complexity required) |
| Admin User | Email + Password + MFA |
| API Access | API Key + IP Whitelist |

### 5.2 Password Policy

- Minimum length: 8 characters
- Complexity: At least 1 uppercase, 1 lowercase, 1 number
- Expiry: 90 days (recommended)
- History: Cannot reuse last 5 passwords
- Lockout: 5 failed attempts → 15 min lockout

### 5.3 Session Management

- Session timeout: 30 minutes idle
- Concurrent sessions: Max 3 per user
- Session invalidation on password change

---

## 6. Data Protection

### 6.1 Encryption Standards

| Data State | Method | Standard |
|------------|--------|----------|
| At Rest | AES-256 | NIST approved |
| In Transit | TLS 1.3 | HTTPS only |
| Backups | AES-256 | Encrypted archives |

### 6.2 Data Retention

| Data Type | Retention Period | Disposal Method |
|-----------|------------------|-----------------|
| Active projects | Indefinite (user controlled) | User deletion |
| Deleted projects | 30 days (recovery) | Secure wipe |
| Audit logs | 2 years | Secure archive |
| Backups | 90 days | Secure wipe |

### 6.3 Data Minimization

- Collect only necessary data for service delivery
- No tracking of user behavior beyond security logging
- No sale or sharing of customer data with third parties

---

## 7. System Security

### 7.1 Infrastructure Security

- Hosting: EU-based data centers (GDPR compliant)
- Network: Firewall, DDoS protection
- Updates: Security patches within 48 hours (critical)

### 7.2 Application Security

- Input validation on all user inputs
- SQL injection prevention (parameterized queries)
- XSS prevention (output encoding)
- CSRF protection (tokens)
- Security headers (CSP, HSTS, X-Frame-Options)

### 7.3 Vulnerability Management

| Severity | Response Time | Action |
|----------|---------------|--------|
| Critical | 24 hours | Immediate patch, notify users |
| High | 7 days | Patch in next release |
| Medium | 30 days | Scheduled patch |
| Low | 90 days | Next major release |

---

## 8. Incident Response

### 8.1 Incident Classification

| Level | Description | Response Time |
|-------|-------------|---------------|
| P1 - Critical | Data breach, system down | Immediate |
| P2 - High | Security vulnerability exploited | 4 hours |
| P3 - Medium | Suspicious activity | 24 hours |
| P4 - Low | Policy violation | 72 hours |

### 8.2 Response Procedure

1. **Detect** — Identify and classify incident
2. **Contain** — Isolate affected systems
3. **Investigate** — Determine scope and cause
4. **Remediate** — Fix vulnerability, restore service
5. **Report** — Notify affected users (within 72h for breaches)
6. **Review** — Post-incident analysis, update procedures

### 8.3 Contact Information

- Security Contact: security@cncplanner.de
- Emergency: +49 [TBD]
- Data Protection: datenschutz@cncplanner.de

---

## 9. Business Continuity

### 9.1 Backup Strategy

| Type | Frequency | Retention | Location |
|------|-----------|-----------|----------|
| Full backup | Weekly | 90 days | Offsite EU |
| Incremental | Daily | 30 days | Primary + Offsite |
| Transaction logs | Continuous | 7 days | Primary |

### 9.2 Recovery Objectives

- **RPO (Recovery Point Objective):** 24 hours
- **RTO (Recovery Time Objective):** 4 hours

---

## 10. Compliance

### 10.1 Regulatory Compliance

| Regulation | Scope | Status |
|------------|-------|--------|
| GDPR | EU customer data | Compliant |
| BDSG | German data protection | Compliant |
| ISO 27001 | Information security | Aligned |

### 10.2 Audit Trail

All security-relevant events are logged:
- Login attempts (success/failure)
- Data access and modifications
- Configuration changes
- Admin actions

Logs are retained for 2 years and protected against tampering.

---

## 11. Employee Security

### 11.1 Security Awareness

- Security training on onboarding
- Annual security refresher
- Phishing awareness training

### 11.2 Acceptable Use

- Company devices for business use only
- No sharing of credentials
- Report security incidents immediately
- Clear desk policy

---

## 12. Third-Party Security

### 12.1 Vendor Assessment

All third-party services must:
- Provide SOC 2 or ISO 27001 certification
- Sign Data Processing Agreement (DPA)
- Undergo annual security review

### 12.2 Current Third Parties

| Vendor | Service | Certification |
|--------|---------|---------------|
| [Hosting Provider] | Infrastructure | ISO 27001, SOC 2 |
| [Payment Provider] | Payments | PCI DSS |

---

## 13. Policy Review

This policy is reviewed:
- Annually (minimum)
- After security incidents
- When regulations change
- When business requirements change

---

## 14. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-03 | F. Ziesche | Initial release |

---

## Approval

**Approved by:** Florian Ziesche  
**Role:** CEO / Information Security Owner  
**Date:** 2026-02-03

---

*This document is part of CNC Planner Pro's ISO 27001 aligned Information Security Management System (ISMS).*
