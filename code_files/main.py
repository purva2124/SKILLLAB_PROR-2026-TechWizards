import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam not detected")
    exit()

print("Yoga Mudra Recognizer Started")
print("Press q to exit")

def classify_mudra(area, defects_count):
    if area > 22000 and defects_count >= 4:
        return "Abhaya Mudra", "Open palm gesture"

    elif area > 20000 and defects_count <= 1:
        return "Namaste Mudra", "Prayer / greeting gesture"

    elif area < 9000 and defects_count <= 1:
        return "Fist Mudra", "Closed hand gesture"

    elif 9000 <= area <= 20000:
        return "Gyan Mudra", "Thumb and index finger mudra"

    else:
        return "Unknown", "Show mudra clearly"

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    x1, y1 = w // 4, h // 4
    x2, y2 = 3 * w // 4, 3 * h // 4

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    roi = frame[y1:y2, x1:x2]

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([25, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.GaussianBlur(mask, (5, 5), 100)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    mudra = "No Hand"
    meaning = "Place hand inside green box"
    defects_count = 0
    area = 0

    if contours:
        cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cnt)

        if area > 3000:
            hull_points = cv2.convexHull(cnt)
            hull_indices = cv2.convexHull(cnt, returnPoints=False)

            cv2.drawContours(roi, [cnt], -1, (255, 0, 0), 2)
            cv2.drawContours(roi, [hull_points], -1, (0, 255, 255), 2)

            if hull_indices is not None and len(hull_indices) > 3:
                defects = cv2.convexityDefects(cnt, hull_indices)

                if defects is not None:
                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        depth = d / 256.0

                        if depth > 15:
                            defects_count += 1

            mudra, meaning = classify_mudra(area, defects_count)

    cv2.rectangle(frame, (10, 10), (760, 120), (0, 0, 0), -1)

    cv2.putText(frame, "Mudra: " + mudra, (20, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(frame, "Meaning: " + meaning, (20, 85),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.putText(frame, "Area: " + str(int(area)) + "  Defects: " + str(defects_count),
                (20, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv2.imshow("Yoga Mudra Recognizer", frame)
    cv2.imshow("Skin Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
