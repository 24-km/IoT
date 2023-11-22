import cv2

cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    # Define parameters for the sensors in the top row
    x1, y1, w1, h1 = 50, 50, 150, 200
    x2, y2, w2, h2 = 250, 50, 150, 200
    x3, y3, w3, h3 = 450, 50, 150, 200

    # Define parameters for the sensors in the bottom row
    x4, y4, w4, h4 = 50, 300, 150, 200
    x5, y5, w5, h5 = 250, 300, 150, 200

    # Increase horizontal spacing between boxes in the top row
    horizontal_spacing_top = 50
    x2 += horizontal_spacing_top
    x3 += horizontal_spacing_top * 2

    # Increase horizontal spacing between boxes in the bottom row
    horizontal_spacing_bottom = 50
    x4 += horizontal_spacing_bottom
    x5 += horizontal_spacing_bottom * 2

    # Draw rectangles and text for sensors in the top row
    cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
    cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
    cv2.rectangle(frame, (x3, y3), (x3 + w3, y3 + h3), (0, 0, 255), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Sensor 1 : 234 C", (x1, y1 - 10), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Sensor 2 : 234 C", (x2, y2 - 10), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Sensor 3 : 234 C", (x3, y3 - 10), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

    # Draw rectangles and text for sensors in the bottom row
    cv2.rectangle(frame, (x4, y4), (x4 + w4, y4 + h4), (255, 255, 0), 2)
    cv2.rectangle(frame, (x5, y5), (x5 + w5, y5 + h5), (255, 0, 255), 2)

    cv2.putText(frame, "Sensor 4 : 234 C", (x4, y4 - 10), font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Sensor 5 : 234 C", (x5, y5 - 10), font, 0.8, (255, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Webcam', frame)

    # Press 'q' to exit the loop and close the webcam window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
