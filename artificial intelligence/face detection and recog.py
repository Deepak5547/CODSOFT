import dlib
import cv2
import face_recognition

# Load the input image
image_path = 'path/to/image.jpg'
image = cv2.imread(image_path)

# Initialize the face detector from dlib
detector = dlib.get_frontal_face_detector()

# Find all face locations in the image using dlib
faces = detector(image, 1)

# Convert the image to RGB format (required by face_recognition library)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Compute face encodings using the face_recognition library
face_encodings = face_recognition.face_encodings(rgb_image, faces)

# Display the result with rectangles around the detected faces
for (top, right, bottom, left), face_encoding in zip(faces, face_encodings):
    # Draw a rectangle around the face
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # You can perform face recognition logic here using the computed face encoding
    # For simplicity, let's just print the face encoding
    print("Face Encoding:", face_encoding)

# Display the result
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
