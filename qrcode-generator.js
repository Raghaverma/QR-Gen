const QRCode = require('qrcode');
const fs = require('fs');
const path = require('path');

const SAVE_DIR = "Path_to_Your_Directory/";

// Ensure the directory exists
if (!fs.existsSync(SAVE_DIR)) {
    fs.mkdirSync(SAVE_DIR, { recursive: true });
}

function generateStudentQR(student) {
    if (!student.Enrollment_Number) {
        console.log(`Skipping ${student.Name} - No Enrollment Number`);
        return;
    }

    const studentData = `Enrollment_Number: ${student.Enrollment_Number}
Name: ${student.Name}
Course: ${student.Course}
ContactNo: ${student.ContactNo}
Address: ${student.Address}`;

    const filePath = path.join(SAVE_DIR, `student_${student.Enrollment_Number}.png`);

    QRCode.toFile(filePath, studentData, {
        color: {
            dark: '#000000',
            light: '#ffffff'
        }
    }, (err) => {
        if (err) throw err;
        console.log(`QR Code saved: ${filePath}`);
    });
}

// Example student data
const studentsData = [
    { Enrollment_Number: "123456", Name: "John Doe", Course: "Computer Science", ContactNo: "9876543210", Address: "New York" }
];

// Generate QR codes for all students
studentsData.forEach(generateStudentQR);
