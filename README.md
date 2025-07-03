# AI Project Basic — Part 1

## 📌 Overview
Initial setup for the AI Project:
- Initialized Git repository.
- Created a Python virtual environment.
- Added base folders: `data/`, `src/`, `notebooks/`.
- Created `.gitignore` to exclude environment files & caches.


# 🚀 AI Project Basic — Domain Name Suggestion LLM

This project demonstrates a **simple end-to-end AI pipeline** for generating domain name suggestions using a fine-tuned LLM.  
It follows best practices for:
- Synthetic dataset creation
- Baseline LLM testing (GPT-2)
- Evaluation using a simple LLM-as-a-Judge approach
- Edge case discovery
- Safety guardrails to block inappropriate input
- Version control and reproducibility

---

## 📂 Project Structure

AI_Project_01/
│
├── env/ # Python virtual environment
├── data/ # Datasets & results
│ ├── synthetic_domains.csv
│ ├── evaluation_results.csv
│ ├── safety_test.csv
├── notebooks/ # Jupyter notebooks
│ ├── test_dataset.ipynb
│ ├── baseline_training.ipynb
│ ├── evaluate.ipynb
│ ├── safety_test.ipynb
├── src/ # Python scripts
│ ├── create_dataset.py
│ ├── fine_tune_baseline.py
│ ├── evaluate.py
│ ├── safety_guard.py
├── .gitignore
├── README.md
├── overview.pdf



---

## ⚙️ Tech Stack

- **Python**
- `torch` (PyTorch)
- `transformers` (Hugging Face)
- `pandas`
- `jupyter`

---

## ✅ Setup Instructions

**1️⃣ Clone this repo**

```bash
git clone https://github.com/<your-username>/AI_Project_Basic.git
cd AI_Project_Basic

2️⃣ Create a virtual environment

python -m venv env

3️⃣ Activate the environment

Windows env\Scripts\activate
macOS/Linux source env/bin/activate


4️⃣ Install dependencies
pip install torch transformers pandas jupyter

📌 How to Run
👉 Create synthetic dataset
python src/create_dataset.py

👉 Test baseline GPT-2 generation
python src/fine_tune_baseline.py

👉 Run evaluation framework
python src/evaluate.py

👉 Run safety guardrails test
python src/safety_guard.py

👉 Open notebooks for inspection
Use VS Code or:
jupyter notebook

to open:

test_dataset.ipynb

baseline_training.ipynb

evaluate.ipynb

safety_test.ipynb

See overview.pdf for:

Synthetic dataset methodology

Baseline model test results

Evaluation logic

Edge case detection

Safety approach

Improvement recommendations

✅ Deliverables
🗂️ Reproducible Python scripts

📓 Notebooks for exploration & tests

📝 README.md with full instructions

📑 overview.pdf summarizing the project

✨ Next Steps
Fine-tune GPT-2 with real domain data

Improve scoring with an advanced LLM-as-a-Judge

Deploy as a simple REST API (optional)

Add more edge case tests and filtering

🟢 License
Open source — for learning & demonstration purposes.


---

## ✅ **How to use**

✔️ Replace **`<your-username>`** with your real GitHub username.  
✔️ Put this as your root **`README.md`**.  
✔️ Push it with:
```bash
git add README.md
git commit -m "Add final README.md"
git push


