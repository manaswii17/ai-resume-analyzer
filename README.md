# AI Resume Analyzer & Job Matching System

A Python-based application that helps users compare a resume with a job description and identify relevant skills and missing requirements.

## Features

- Upload a resume in PDF format.
- Provide a job description for comparison.
- Extract text from resumes.
- Identify relevant skills and keywords.
- Calculate a resume–job similarity score.
- Highlight matching and missing skills.
- Suggest areas for resume improvement.

*Note: Features still under development may not be fully functional.*

## Tech Stack

- **Language:** Python
- **Interface:** Streamlit
- **Data Processing:** Pandas
- **NLP and Machine Learning:** scikit-learn, TF-IDF, cosine similarity
- **Testing:** Python

## Project Structure

```text
ai-resume-analyzer/
├── app.py
├── src/
├── tests/
├── requirements.txt
└── README.md
```

## Getting Started

1. Clone the repository:

   `git clone https://github.com/manaswii17/ai-resume-analyzer.git`

2. Open the project folder:

   `cd ai-resume-analyzer`

3. Install dependencies:

   `pip install -r requirements.txt`

4. Run the application:

   `streamlit run app.py`

## Project Status

Currently under development. Some features and tests may require further implementation and validation.

## Future Improvements

- Improve skill extraction and matching accuracy.
- Add more robust input validation and error handling.
- Expand automated tests.
- Improve the user interface and reporting.
