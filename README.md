# Student Management System

## Description
A Python-based Student Management System that allows adding, removing, searching, and updating student records.

## Project Files
- student.py
- test_student.py
- requirements.txt
- .github/workflows/python.yml

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
python -m pytest
```

## Git Commands Used

```bash
git init
git add .
git commit -m "Initial Student Management System"
git push

git checkout -b feature-student-search
git add .
git commit -m "Improved search_student function"
git push

git checkout main
git merge feature-student-search
```

## GitHub Actions

GitHub Actions automatically runs the test suite whenever code is pushed or a pull request is created.