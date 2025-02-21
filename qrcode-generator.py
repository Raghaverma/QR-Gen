import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Student data should be in the following format (list of dictionaries)
# students_Data =  

# Directory to save QR codes
SAVE_DIR = r"C:\NAS\QR\BCA 2ND SHIFT 2023"
# change the directory name according to departments

# Create the directory if it doesn't exist
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def generate_student_qr(student):
    """Generates a QR code for a student and saves it as a PNG file."""
    
    student_id = student.get("Enrollment_Number")
    if not student_id:
        print(f"Skipping {student['Name']} - No Enrollment Number")
        return
    
    student_data = f"Enrollment_Number: {student_id}\nName: {student['Name']}\nCourse: {student['Course']}\nContactNo: {student['ContactNo']}\nAddress: {student['Address']}"
    
    # Include optional ranks if available
    for rank_type in ["CUET_Rank", "CLAT_Rank", "CET_Rank"]:
        if rank_type in student:
            student_data += f"\n{rank_type}: {student[rank_type]}"
    
    # Generate QR code
    qr = qrcode.QRCode(version=2, box_size=10, border=5)
    qr.add_data(student_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white").convert("RGB")
    
    # Add Enrollment Number text on the QR image
    img_editable = ImageDraw.Draw(qr_image)
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()
    
    img_editable.text((120, 10), f"Enrollment: {student_id}", fill="black", font=font)
    
    # Save the QR code
    file_path = os.path.join(SAVE_DIR, f"student_{student_id}.png")
    qr_image.save(file_path)
    print(f"QR Code saved: {file_path}")

# Generate QR codes for all students
if __name__ == "__main__":
    for student in students_Data:
        generate_student_qr(student)