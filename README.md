# 🧠 NextSkill AI – Intelligent Career Path Matching with O*NET

NextSkill AI is an AI-powered career discovery tool that analyzes your resume skills and matches them to real-world job roles using the U.S. Department of Labor’s **O*NET** database.

Built with [Streamlit](https://streamlit.io), the app delivers a fast, visual experience for identifying high-potential career paths — complete with skill gaps and job-fit insights.

---

## 🚀 Live App

👉 [Click to launch the app on Streamlit Cloud](https://nextskill.streamlit.app/)  
*(Replace with your actual app URL once deployed)*

---

## 🧩 Features

✅ Upload or paste your resume skills  
✅ Matches to over **1,000 job titles** from the official O*NET database  
✅ Shows:
- Top matching jobs
- Skill coverage %
- Matched vs. missing skills  
✅ Easy to deploy, adapt, or expand

---

## 🗂 File Structure

```
📁 nextskill-ai/
│
├── nextskill_updated_with_full_onet.py    # Streamlit app
├── onet_job_skill_full.json               # Full O*NET job-to-skill mappings
└── README.md                              # This file
```

---

## 💻 Run Locally

### Requirements
- Python 3.8+
- Streamlit

### Quick Start

```bash
pip install streamlit
streamlit run nextskill_updated_with_full_onet.py
```

Make sure `onet_job_skill_full.json` is in the same directory.

---

## 📚 Data Source

This project uses data from the **O*NET 29.3 Database**  
© National Center for O*NET Development | [onetcenter.org](https://www.onetcenter.org/)

---

## 🤝 Contributing

Pull requests are welcome! Ideas, improvements, and features are encouraged.

To contribute:
1. Fork the repo
2. Create a feature branch
3. Open a pull request

---

## 💡 Roadmap

- [ ] Resume file upload + skill extraction
- [ ] Personalized learner dashboard
- [ ] Admin + employer views
- [ ] AI-powered skill gap recommendations

---

## 📬 Contact

Built by [Your Name or Org]  
Have ideas or questions? Open an issue or email: your@email.com

---

## 🛡 License

MIT License — use, fork, and build freely.