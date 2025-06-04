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

![1](https://github.com/user-attachments/assets/2fdcabaf-c4c5-4644-a6e1-a90c8d03d42d)
![2](https://github.com/user-attachments/assets/5a6798e4-7f5e-48ab-aa88-9096a4fd9389) ![3](https://github.com/user-attachments/assets/516ee32e-ab7e-4726-8355-19ee8e8590df)
![6](https://github.com/user-attachments/assets/4829c457-c1ff-4780-96fe-35f911ac22b2)
![7](https://github.com/user-attachments/assets/dfc59bca-0fb3-48c2-9372-09f050e230b8)
![12](https://github.com/user-attachments/assets/6d5b9490-3aad-485d-8f38-6e82b1ad870a)
![15](https://github.com/user-attachments/assets/b692483f-03e1-4880-b90e-82edaef5cc8a)
![4](https://github.com/user-attachments/assets/6284754b-789e-414f-b34e-b55a0d7f447e)
![5](https://github.com/user-attachments/assets/e5ea6b05-dc70-47e5-906c-21c68f5f92a4)
![8](https://github.com/user-attachments/assets/b6bce87d-9b0c-44d0-a343-76821b92f85f)
![9](https://github.com/user-attachments/assets/1050826e-39da-4cf2-b343-1f779bf4af50)
![16](https://github.com/user-attachments/assets/c42caee1-2ef5-4fda-ae83-dd4ddd24a657)

