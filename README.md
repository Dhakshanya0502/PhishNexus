# PhishNexus
# 🛡️ Phishing Email Analysis Tool

A Python-based rule-driven phishing email detection system that classifies emails into:

- 🔴 HIGH RISK PHISHING
- 🟡 SUSPICIOUS
- 🟢 SAFE

This project is designed for academic and cybersecurity learning purposes.

---

## 📌 Project Description

Phishing attacks are one of the most common cyber threats today.  
This tool analyzes email text files and detects potential phishing content using:

- Keyword-based analysis
- Suspicious URL detection
- Risk scoring mechanism

The system scans sample email files and classifies them based on calculated risk levels.

---

## 📂 Project Structure
phishing detection tool
│
├── Sample_Emails/
│ ├── high_risk_1.txt
│ ├── high_risk_2.txt
│ ├── high_risk_3.txt
│ ├── suspicious_1.txt
│ ├── suspicious_2.txt
│ ├── suspicious_3.txt
│ ├── safe_1.txt
│ ├── safe_2.txt
│ ├── safe_3.txt
│ └── safe_4.txt
│
├── scripts/
│ └── phishing_detector.py
│
└── README.md


---

## ⚙️ Requirements

- Python 3.x
- Windows / Linux / macOS

Check Python version:

```bash
python --version
▶️ How to Run
1️⃣ Clone the Repository
git clone https://github.com/your-username/phishing-email-analysis.git
2️⃣ Navigate to Project Folder
cd "phishing detection tool"
cd scripts
3️⃣ Run the Script
python phishing_detector.py

OR

py phishing_detector.py
🧠 How It Works

The system performs:

📌 Keyword scanning (urgent, verify, OTP, password, etc.)

🌐 Suspicious URL detection

🔎 Risk scoring based on detected indicators

📊 Classification output based on score thresholds

🧪 Sample Output
high_risk_1.txt --> HIGH RISK PHISHING
high_risk_2.txt --> HIGH RISK PHISHING
suspicious_1.txt --> SUSPICIOUS
safe_1.txt --> SAFE

🎯 Features

✔ Rule-based phishing detection

✔ URL pattern scanning

✔ Risk scoring logic

✔ Lightweight and beginner-friendly

✔ Academic project ready

🚀 Future Enhancements

Machine Learning-based detection

Email header analysis module

Attachment scanning

GUI interface (Tkinter)

Web application deployment

Real-time email monitoring

🎓 Academic Purpose

This project was developed as part of a Cyber Security academic initiative to understand phishing detection techniques.

👩‍💻 Author

Dhakshanya Manga
Cyber Security Student
