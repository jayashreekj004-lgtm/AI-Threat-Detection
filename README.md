# AI Cyber Security Dashboard

A Python-based Cyber Security Dashboard designed to monitor, simulate, and manage different types of security threats through a graphical user interface.

## Project Overview

The AI Cyber Security Dashboard provides a desktop-based interface for monitoring security activities and managing detected threats.

The system allows an administrator to log in, perform manual and automatic scans, view detected threats, monitor activity logs, visualize attack distribution, send security alerts, isolate the system, and update firewall rules.

## Features

- Admin login authentication
- Manual threat scanning
- Automatic threat scanning
- Threat detection dashboard
- Threat counter
- Attack type identification
- Risk level classification
- Source IP generation
- Threat activity logging
- Attack distribution graph
- Email security alerts
- Threat details view
- System isolation
- Firewall rule update
- Cloud infrastructure activity monitoring
- Email threat analyzer simulation

## Supported Attack Types

The dashboard monitors the following attack types:

- Brute Force Attack
- DDoS Attack
- Port Scan
- Suspicious Login

## Risk Level Classification

| Attack Type | Risk Level |
|---|---|
| DDoS Attack | High |
| Brute Force Attack | High |
| Port Scan | Medium |
| Suspicious Login | Low |

## Dashboard Functions

### 1. Manual Scan

The Manual Scan button generates a threat event and displays the detected attack in the dashboard.

### 2. Auto Scan

The Auto Scan feature automatically performs threat scans at regular intervals.

### 3. Stop Auto Scan

The Stop Auto Scan option stops the automatic scanning process.

### 4. View Selected Threat

Users can select a threat from the table and view:

- Detection time
- Attack type
- Source IP
- Risk level
- Status

### 5. Attack Distribution

The system uses Matplotlib to display the distribution of different attack types using a bar chart.

### 6. Email Alert

When a threat is detected, the system can send an email notification containing:

- Attack type
- Source IP
- Risk level
- Security alert message

### 7. System Isolation

The system provides an option to isolate the system when a critical security situation is detected.

### 8. Firewall Update

The dashboard provides an option to add a firewall rule for blocking traffic from a detected source IP.

## Activity Monitoring

The dashboard includes simulated monitoring for:

### Cloud Infrastructure Activity

The system displays activities such as:

- User login attempt
- API request received
- Database access
- File upload request
- Unknown IP connection

### Email Threat Analyzer

The system simulates email security activities such as:

- Clean email received
- Phishing link detected
- Attachment scanning
- Malware attachment detection
- Suspicious login detection

## Technologies Used

- Python
- Tkinter
- Matplotlib
- CSV
- SMTP
- Threading

## Python Libraries

```text
tkinter
random
time
csv
threading
smtplib
matplotlib

Project Workflow
Admin Login
     ↓
Cyber Security Dashboard
     ↓
Manual Scan / Auto Scan
     ↓
Threat Detection
     ↓
Attack Type Identification
     ↓
Risk Level Classification
     ↓
Threat Logging
     ↓
Attack Distribution Graph
     ↓
Email Alert
     ↓
Security Response
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
View Threat   Isolate System   Update Firewall

Project Structure
AI-Threat-Detection/
│
├── app.py
├── model.py
├── send_alert.py
├── dataset.csv
├── attack_logs.csv
├── dataset.xlsx
├── attack_logs.xlsx
├── jpeg.jpg
├── output.jpg
├── output1.jpg
└── README.md

How to Run
Step 1: Install Python

Make sure Python is installed on your system.

Step 2: Install Required Libraries

pip install matplotlib

Tkinter is normally included with standard Python installations.

Step 3: Run the Application
python app.py
Step 4: Login

Use the administrator login configured in the application.

After successful login, the Cyber Security Dashboard will be displayed.

Data Logging

Detected threats are stored in a CSV file for maintaining attack records.

The stored information includes:

Time
Attack Type
Source IP
Risk Level
Status
Future Enhancements
Real-time network traffic monitoring
Real-time intrusion detection
Database integration
Advanced machine learning integration
Real-time firewall integration
Cloud security monitoring
Secure authentication system
Secure email credential management
Project Purpose

The main purpose of this project is to demonstrate the development of a Python-based cyber security monitoring dashboard with threat detection, visualization, logging, alert notification, and basic security response features.




