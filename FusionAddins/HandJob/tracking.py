from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # with draw

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType1 = hand1["type"]

        length1, info = detector.findDistance(lmList1[8][:2], lmList1[5][:2])
        length2, info = detector.findDistance(lmList1[12][:2], lmList1[9][:2])
        length3, info = detector.findDistance(lmList1[16][:2], lmList1[13][:2])
        length4, info = detector.findDistance(lmList1[20][:2], lmList1[17][:2])
        length5, info = detector.findDistance(lmList1[4][:2], lmList1[2][:2])
        length6, info = detector.findDistance(lmList1[3][:2], lmList1[1][:2])

        with open("coords.txt", "w") as text_file:
            text_file.write(
                str(int(round(length1 - 90)))
                + "."
                + str(int(round(length2 - 100)))
                + "."
                + str(int(round(length3 - 95)))
                + "."
                + str(int(round(length4 * 2  - 140)))
            )

        with open("coords.txt") as f:
            contents  = f.read()

        print(contents.split('.'))

    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
