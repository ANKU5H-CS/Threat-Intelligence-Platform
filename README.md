# Threat Intelligence Platform (TIP)

## Project Overview

The Threat Intelligence Platform (TIP) is a cybersecurity project developed to collect, process, store, analyze, and visualize threat intelligence data from multiple Open Source Intelligence (OSINT) sources. The project integrates MongoDB, Elasticsearch, Kibana, and Python automation to simulate a real-world Threat Intelligence and Security Operations Center (SOC) workflow.

---

# Objectives

* Collect threat intelligence from OSINT sources
* Store threat data securely
* Clean and normalize collected information
* Index threat data using Elasticsearch
* Visualize threat intelligence using Kibana
* Build a foundation for SOC monitoring and threat analysis
* Implement firewall automation and security controls

---

# Technology Stack

* Python
* MongoDB
* Elasticsearch
* Kibana
* Git & GitHub
* Linux (Kali Linux)
* OSINT Sources (AlienVault, VirusTotal)

---

# Project Structure

```text
TIP-Project/
│
├── data/
├── database/
├── docs/
├── elk/
├── logs/
├── reports/
├── screenshots/
├── scripts/
├── requirements.txt
└── README.md
```

---

# Week 1 – Environment Setup & Threat Collection

## Day 1 – Project Initialization

### Tasks Completed

* Kali Linux environment verification
* System update and package installation
* Project directory creation
* Python virtual environment setup
* Git repository initialization
* GitHub repository connection

### Deliverables

* Working project structure
* Virtual environment configured
* Initial Git commit

---

## Day 2 – MongoDB Setup

### Tasks Completed

* MongoDB installation
* MongoDB service configuration
* Database creation
* Collection creation
* Initial data verification

### Deliverables

* MongoDB operational
* Threat Intelligence database created

---

## Day 3 – AlienVault Threat Feed Integration

### Tasks Completed

* AlienVault API integration
* Threat feed collection script development
* API response validation
* Log generation

### Deliverables

* AlienVault feed automation script
* Threat logs generated

---

## Day 4 – VirusTotal Integration

### Tasks Completed

* Environment variable configuration
* VirusTotal API integration
* Threat intelligence retrieval
* Logging implementation

### Deliverables

* VirusTotal threat feed script
* API response validation

---

## Day 5 – MongoDB Storage

### Tasks Completed

* MongoDB connection setup
* Threat data insertion
* Data verification
* Storage automation

### Deliverables

* Threat data successfully stored in MongoDB

---

## Day 6 – Data Cleaning

### Tasks Completed

* Duplicate record identification
* Data cleaning script development
* Dataset normalization

### Deliverables

* Cleaned threat dataset

---

## Day 7 – Weekly Reporting

### Tasks Completed

* Week 1 report preparation
* Git commit verification
* Repository documentation review

### Deliverables

* Week 1 project report
* Updated repository

---

# Week 2 – ELK Stack Integration

## Day 8 – Elasticsearch Installation

### Tasks Completed

* Java verification
* Elasticsearch installation
* Service initialization
* Basic configuration

### Deliverables

* Elasticsearch installed successfully

---

## Day 9 – Elasticsearch Verification

### Tasks Completed

* Service validation
* Cluster verification
* API connectivity testing

### Deliverables

* Elasticsearch running successfully

---

## Day 10 – Elasticsearch Configuration

### Tasks Completed

* Index creation
* Configuration verification
* Cluster information validation

### Deliverables

* Operational Elasticsearch index

---

## Day 11 – Kibana Setup

### Tasks Completed

* Kibana installation
* Service configuration
* Browser connectivity verification

### Deliverables

* Kibana dashboard accessible

---

## Day 12 – Kibana Integration

### Tasks Completed

* Elasticsearch–Kibana connection
* Enrollment token configuration
* Verification code validation
* Kibana authentication setup

### Deliverables

* Successful ELK integration

---

## Day 13 – Data View Configuration

### Tasks Completed

* Data View creation
* Discover page validation
* Threat index integration

### Deliverables

* Threat Data View configured

---

## Day 14 – Dashboard Setup

### Tasks Completed

* Kibana dashboard creation
* Dashboard configuration
* Visualization workspace preparation

### Deliverables

* Threat Intelligence Dashboard created

---

# Week 3 – Threat Visualization & Firewall Automation

## Day 15 – Threat Visualization Dashboard

### Tasks Completed

* Threat records inserted into Elasticsearch
* Discover page verification
* Severity distribution visualization
* Dashboard integration

### Threat Samples Added

* Malware (High)
* Phishing (Medium)
* Ransomware (Critical)

### Deliverables

* Interactive Kibana dashboard
* Threat severity visualization

---

## Day 16 – Firewall Rule Verification

### Tasks Completed

- Created firewall automation script
- Verified iptables configuration
- Executed firewall checks using Python
- Validated INPUT, OUTPUT, and FORWARD chains

### Deliverables

- firewall_rules.py
- Firewall verification output

---
## Week 3

### Day 17 - Firewall Rule Management

- Verified current firewall rules using iptables.
- Developed a Python script to display firewall configuration.
- Checked INPUT, FORWARD, and OUTPUT chains.
- Verified default firewall policies.
- Confirmed firewall script placement in the project structure.

### Day 18 - Firewall Monitoring and Logging

- Created firewall_monitor.py script.
- Verified current firewall status using iptables.
- Implemented firewall monitoring module.
- Created firewall monitoring log file.
- Verified firewall scripts and project structure.

## Upcoming Tasks


### Day 19

* Automatic IP Blocking

### Day 20

* Threat-Based Automation

### Day 21

* Security Log Generation

---

# Key Features

* Threat Intelligence Collection
* MongoDB Storage
* Elasticsearch Indexing
* Kibana Dashboards
* Threat Severity Visualization
* Data Cleaning and Processing
* Security Monitoring
* Firewall Automation (In Progress)

---

# Current Project Status

## Completed

* Week 1 (Day 1–7)
* Week 2 (Day 8–14)
* Week 3 Day 15

## Current Progress

* Firewall Automation Phase Started

---

# Author

Ankush Dhanorkar

Cybersecurity Enthusiast | SOC Analyst Aspirant

GitHub: ANKU5H-CS

---

# Future Enhancements

* Real-Time Threat Intelligence Collection
* Automated IOC Processing
* Threat Correlation Engine
* Email Alerting System
* Advanced Kibana Dashboards
* Automated Firewall Response
* SOC Monitoring Workflow
* Incident Response Automation
