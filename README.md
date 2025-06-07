# 🧑‍💻 Online Judge System (OJ-Project)

A full-featured Online Judge platform built with **Django**, designed to help users practice programming by solving coding problems, executing their code in isolated Docker containers, and receiving AI-powered feedback.

---

## 🔧 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Languages Supported:** Python, C, C++
- **Code Execution:** Isolated environments via Docker + `subprocess`
- **AI Review:** Solution feedback based on problem description
- **Containerization:** Docker
- **Deployment:** AWS EC2 + Amazon ECR (Elastic Container Registry)

---

## 👥 User Roles

### 🔹 Normal User
- Register and log in
- View coding problems
- Track progress: “x/y Solved”
- Interact with code editor:
  - `Run` code with custom input
  - `Submit` for evaluation via hidden test cases
  - Get `AI Review` of submitted code
- View submission history (`My Submissions`)
- View personal profile (`My Profile`)

### 🔸 Problem Setter
- All Normal User features
- Add new coding problems
- Add hidden test cases
- View all user submissions

### 🔺 Admin
- Full platform control (extendable for moderation, analytics, etc.)

---

## 🚀 Key Features

- 🔐 **Role-Based Authentication** (Normal, Setter, Admin)
- 📚 **Problem Dashboard** with Solved/Total view
- 🖊️ **In-browser Code Editor** with support for C, C++, Python
- ⚙️ **Run Code** with custom input
- ✅ **Submit Code** evaluated against hidden test cases
- 🤖 **AI Code Review** for quality feedback
- 📊 **User Progress Tracking**
- 👁️ **Submission History**
- 🐳 **Secure Code Execution via Docker Containers**

---

## 🐳 Docker Integration

Docker ensures secure and isolated code execution. Each code run or submission spins up a Docker container to:
- Avoid malicious code execution risks
- Provide language-specific environments
- Improve system scalability

> ✅ Docker must be installed and running for local development.

---

## ☁️ Deployment (AWS EC2 + ECR)

The system is containerized and deployed to the cloud via:
- **Amazon EC2**: Hosts the main Django app
- **Amazon ECR**: Stores and pulls Docker images used in code execution

### 🛠️ Deployment Summary
- Docker image of the project is pushed to **Amazon ECR**
- EC2 instance pulls and runs the image

---

## 📸 Screenshots

![1](https://github.com/user-attachments/assets/0649871c-0093-47ff-9855-338da17f14d8)
![18](https://github.com/user-attachments/assets/4ab01247-a1d2-40d5-ad55-4ca6e7d1663e)
![19](https://github.com/user-attachments/assets/4e944698-2b49-42c9-bda0-17a8fc9676fd)
![6](https://github.com/user-attachments/assets/b09d8ec4-f7e6-4c5c-a01d-607cd5b02d4d)
![7](https://github.com/user-attachments/assets/7c8c3bd7-c856-4a30-8426-eb3f64503474)
![17](https://github.com/user-attachments/assets/38b3d171-bd83-47e9-bd49-bec9504ef3e9)
![22](https://github.com/user-attachments/assets/0eafd279-67da-49af-9280-25a1be37f179)
![20](https://github.com/user-attachments/assets/ba62c31c-0bee-4176-9923-d347c30c7885)
![4](https://github.com/user-attachments/assets/aaa755c2-f0c8-433b-820e-491551a336b2)
![5](https://github.com/user-attachments/assets/9cf2d1a4-60f3-4d56-94b2-e32833720d10)
![21](https://github.com/user-attachments/assets/22e2fd66-11ee-4976-a7dd-aea4eea55c79)
![9](https://github.com/user-attachments/assets/b86b0523-9dd2-418f-ae35-8124a223208e)
![16](https://github.com/user-attachments/assets/b5ddc013-16d2-4a20-b446-cc4affe16d3b)


