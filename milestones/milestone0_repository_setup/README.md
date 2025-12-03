# Milestone 0 – Repository & Project Board Setup

This milestone establishes the foundation for the entire **diabetes-risk-xai**
project. It prepares the repository for open‑source collaboration and ensures
contributors have a clear, structured, and professional workflow.

---

## 🎯 Objectives

* Initialize the project repository with a clean, organized structure.
* Configure a GitHub Project Board for transparent task management.
* Add essential documentation to ensure a smooth onboarding experience.
* Set up branch protections and contribution workflows.

---

## 📁 Repository Structure (Initial)

```markdown
diabetes-risk-xai/
│
├── app/                  # Streamlit application
├── data/                 # Placeholder for datasets (excluded from repo if sensitive)
├── notebooks/            # Jupyter notebooks for exploration
├── models/               # Python modules (modeling, preprocessing, XAI)
│
├── LICENSE               # MIT license file
├── CONTRIBUTING.md       # Contributor guidelines
├── README.md             # Main project overview
├── .gitignore            # Pre-configured
```

---

## 🧭 GitHub Project Board Setup

Create a **Project Board** named: `Project Board`.\
can be reached through `Project` / `Project Board`\
or directly via [this link](
https://github.com/users/mohd-makki/projects/2/views/1)

### Columns

* **Backlog** – Ideas, features, tasks not yet started.
* **To Do** – Clear items ready to be worked on.
* **In Progress** – Tasks currently being implemented.
* **Ready for Review** – PRs awaiting review.
* **Under Review** – Active review stage.
* **Done** – Completed items.

Each merged PR should auto‑move to **Done**.

---

## 🔐 Branch Protection Rules

Apply protections to the `main` branch:

* Require PR before merging
* Require at least 1 reviewer approval
* Require status checks to pass
* Require branches to be up to date before merging
* Block direct pushes to `main`

---

## 📄 Essential Setup Files

This milestone includes:

* `CONTRIBUTING.md`
* `README.md` (global project description)

---

## 🤝 Collaboration Notes

* All contributors should follow the project board workflow.
* Each task begins by opening an Issue, which moves through the board
  automatically.
* PR titles and descriptions must follow the project conventions.

---

## ✅ Completion Checklist

* [x] Repo initialized
* [x] Contribution guidelines created
* [x] Project board created and configured
* [x] Branch protections enabled
* [x] Base documentation completed
