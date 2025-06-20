# 🚨 Simple Network Sniffer

> A lightweight Python-based packet sniffer to peek into your network traffic — built for learning, testing, and messing around like a network ninja.

---

## 📌 What is this?

**Simple Network Sniffer** is a basic yet powerful Python tool to capture and inspect packets on a network interface in real-time. It’s designed for educational purposes, giving you hands-on exposure to low-level network data.

Think of it as Wireshark's baby cousin — written in Python, less bulky, more readable.

---

## ⚙️ Features

- 🔍 Real-time packet sniffing using raw sockets  
- 🧠 Parses IP headers to extract source and destination  
- 📦 Supports ICMP, TCP, UDP protocol inspection  
- 👨‍💻 Easy-to-read output in the console  
- 🐍 Fully written in Python — no shady dependencies

---

## 🚀 How to Run

### 🔧 Prerequisites

- Python 3.x  
- Root/admin privileges (required for raw sockets)

### 💻 Run it like a boss

```bash
git clone https://github.com/bagchiarindam2022/simple_network_sniffer.git
cd simple_network_sniffer
sudo python3 sniffer.py
