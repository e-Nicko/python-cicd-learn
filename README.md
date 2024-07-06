# 🌟 Simple Flask Web Application for CI/CD Learning


[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)](https://flask.palletsprojects.com/en/2.0.x/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/e-Nicko/python-cicd-learn)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-yellowgreen)](https://github.com/features/actions)
[![Git](https://img.shields.io/badge/Git-Version%20Control-lightgrey)](https://git-scm.com/)
[![Deployment](https://img.shields.io/badge/Deployment-VPS-orange)](https://en.wikipedia.org/wiki/Virtual_private_server)



This repository contains a comprehensive and straightforward web application built using Flask, designed specifically for educational purposes. It aims to provide hands-on experience with GitHub CI/CD processes and deploying applications on a VPS (Virtual Private Server). Whether you are a beginner looking to understand the basics of continuous integration and continuous deployment, or an intermediate developer seeking to refine your skills, this project offers practical insights into the workflow.

By following the steps outlined in this guide, you will learn how to set up a Flask web application, configure it for local development, and automate the deployment process using GitHub Actions. Each update pushed to the `main` branch triggers the deployment pipeline, ensuring that your application is always up-to-date with the latest changes. This project serves as an excellent resource for mastering the essential aspects of modern web development and deployment strategies.

## 🚀 Getting Started

Follow these instructions to run the application on your local computer.

### Prerequisites
Before you begin, ensure you have Python version 3.x and pip installed.

### 🛠️ Step 1: Clone the Repository

First, clone the repository to your local computer. Enter the following command in the terminal:

```
git clone https://github.com/e-Nicko/python-cicd-learn
```

### 🛠️ Step 2: Install Dependencies

Navigate to the project directory and install the dependencies by entering the following commands:

```
cd <directory_name>
```

```
pip install -r requirements.txt
```

### 🛠️ Step 3: Set Up Environment Variables

Create a `.env` file in the project's root directory and set the DEBUG environment variable to true if you want to enable debug mode. Example content of the `.env` file:

```
DEBUG=true
```

### 🛠️ Step 4: Run the Application

Now you can run the application by entering the following command:

```
python app.py
```

After this, your application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

### 🛠️ Step 5 (Optional): Modify Configuration

You can change the application's settings by editing the `app.py` file according to your needs.

---

## 🔒 Note

Remember, this is only for local deployment. When deploying to a server or cloud environment, additional steps and security measures should be considered.


