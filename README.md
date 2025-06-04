# Online Judge System (OJ-Project)

A full-featured Online Judge system built with **Django** that allows users to solve coding problems, run code with custom input, submit for evaluation against hidden test cases, and even receive AI-powered feedback on their solutions.

## 🔧 Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Code Execution:** Python & C/C++ using `subprocess` in Docker containers
- **AI Review:** Code feedback based on problem description
- **Containerization:** Docker


---

## 👥 User Types

1. **Normal User**
   - Register and log in
   - View all coding problems
   - Track progress: see how many problems are solved (e.g., "3/10 Solved")
   - Use the editor to:
     - `Run` code with custom input
     - `Submit` code for hidden test case validation
     - Get `AI Review` on solution quality
   - View submissions in **My Submissions**
   - View personal info in **My Profile**

2. **Problem Setter**
   - Normal User functionality
   - Add new coding problems
   - Add hidden test cases for problem evaluation
   - View all user submissions

3. **Admin**
   - Full control over the platform (extendable)

---

## 🚀 Features

- 🔐 **Authentication:** Role-based login system (normal user, problem setter, admin)
- 📚 **Problem List:** View all problems, solved status, and problem-specific details
- 👨‍💻 **Code Editor:** Supports C, C++, Python
- ⚙️ **Run Code:** Executes code with user-provided input
- ✅ **Submit Code:** Validates code with hidden test cases, returns verdict
- 🤖 **AI Review:** Provides code review based on problem description
- 📈 **Progress Tracking:** Shows solved tag and number of problems solved
- 👁️ **Submission History:** Users can view all their past submissions
- 🧪 **Docker Integration:** Isolates code execution for safety

---

## 🐳 Docker Usage

To run code securely in isolated environments, the platform uses Docker. Make sure Docker is installed and running.

![1](https://github.com/user-attachments/assets/0649871c-0093-47ff-9855-338da17f14d8)
![2](https://github.com/user-attachments/assets/d9ca8f01-12bc-4f9d-b480-72255f15ed6c)
![3](https://github.com/user-attachments/assets/dcce9387-7cba-4e37-81c4-000ca43a3e2f)
![6](https://github.com/user-attachments/assets/b09d8ec4-f7e6-4c5c-a01d-607cd5b02d4d)
![7](https://github.com/user-attachments/assets/7c8c3bd7-c856-4a30-8426-eb3f64503474)
![12](https://github.com/user-attachments/assets/ac5ec4ca-2f3a-4866-b967-391437412cdd)
![15](https://github.com/user-attachments/assets/a567dd2c-7589-457e-a24e-4d496030c219)
![4](https://github.com/user-attachments/assets/aaa755c2-f0c8-433b-820e-491551a336b2)
![5](https://github.com/user-attachments/assets/9cf2d1a4-60f3-4d56-94b2-e32833720d10)
![8](https://github.com/user-attachments/assets/0bd666ee-7dd4-431f-a84f-7450572cf7a6)
![9](https://github.com/user-attachments/assets/b86b0523-9dd2-418f-ae35-8124a223208e)
![16](https://github.com/user-attachments/assets/b5ddc013-16d2-4a20-b446-cc4affe16d3b)


