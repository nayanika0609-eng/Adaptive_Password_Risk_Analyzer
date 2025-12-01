# 🔐 Adaptive Password Risk Analyzer

The **Adaptive Password Risk Analyzer** evaluates password strength using dynamic, multi-factor risk scoring.  
It analyzes entropy, character patterns, dictionary words, repetition, and known weak patterns to compute a **risk score** (Low, Medium, High).

This project demonstrates cybersecurity concepts, password auditing, and secure coding practices.

---

## 🚀 Features
- Adaptive scoring based on password complexity
- Checks for:
  - Length weakness
  - Repeated characters
  - Common patterns
  - Dictionary word matches
  - Special-character balance
- Outputs:
  - Risk Score (0–100)
  - Risk Level (Low / Medium / High)
  - Reasoning breakdown
- Beginner-friendly Python implementation

---

## 📂 Project Structure
adaptive-password-risk-analyzer/
│── adaptive_password_risk_analyzer.py
│── README.md
│── requirements.txt
│── .gitignore


---


---

## ▶️ Usage

Run the analyzer:

```bash
python adaptive_password_risk_analyzer.py
Enter a password to analyze: MyPass123!
Score: 72
Risk Level: Medium
Reasons:
- Contains uppercase, lowercase, digits, and symbols
- Length is sufficient
- Pattern detected: common word fragment "pass"
 How It Works

The analyzer assigns points based on:

Entropy calculations

Character set diversity

Known weak substring detection

Levenshtein-based dictionary similarity

Final score → mapped to risk category.
