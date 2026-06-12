# Mobile-Detection-YOLOv8
<img width="1536" height="1024" alt="ChatGPT Image Jun 12, 2026, 10_22_00 PM" src="https://github.com/user-attachments/assets/533bff5b-07bd-43d7-8571-97c771045067" />
# 📱 Mobile Detection YOLOv8

This project provides a complete setup for real-time mobile phone detection using the YOLOv8 model. Whether you want to use our pre-trained model or train your own, this repository has everything you need.

---

# 📱 Mobile Detection YOLOv8

This project enables real-time mobile phone detection using the YOLOv8 model. It provides a straightforward workflow to clone, install, test, and even train your own custom detection model.

---

## 🚀 Getting Started

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
Open your terminal and clone this project:
```bash
git clone [https://github.com/your-username/Mobile-Detection-YOLOv8.git](https://github.com/your-username/Mobile-Detection-YOLOv8.git)
cd Mobile-Detection-YOLOv8
2. Install Dependencies

Install all the necessary libraries required to run the project:
Bash

pip install -r requirements.txt

3. Running and Testing the Detection

Once the setup is complete, you can test the program using the following command:
Bash

python detect.py --weights best.pt

How to verify:

    After running the command, a camera window will automatically open.

    Point your camera at a mobile phone.

    The system should draw a bounding box around the phone and display the label "Mobile" in real-time.
