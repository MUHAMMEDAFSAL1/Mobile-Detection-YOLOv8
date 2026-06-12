from ultralytics import YOLO
import cv2
import os

# പാത്ത് കൃത്യമാക്കിയിരിക്കുന്നു
model_path = os.path.join(os.path.expanduser("~"), "mydectection", "best.pt")

# മോഡൽ ലോഡ് ചെയ്യുന്നു
model = YOLO(model_path) 

# വെബ്ക്യാം ഓൺ ചെയ്യുന്നു
cap = cv2.VideoCapture(0)

print("ഡിറ്റക്ഷൻ തുടങ്ങുന്നു... 'q' അമർത്തിയാൽ നിർത്താം.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model(frame)
    annotated_frame = results[0].plot()
    
    cv2.imshow("Phone Detection", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
