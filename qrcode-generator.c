#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <qrencode.h>

#define SAVE_DIR "Path_to_Your_Directory/"

// Function to save the QR code as a PNG file
void save_qr_image(QRcode *qrcode, const char *filename) {
    FILE *fp = fopen(filename, "wb");
    if (!fp) {
        perror("File opening failed");
        return;
    }

    int width = qrcode->width;
    int size = width * width;
    
    // Writing PGM format (simple grayscale image)
    fprintf(fp, "P5\n%d %d\n255\n", width, width);
    fwrite(qrcode->data, 1, size, fp);
    
    fclose(fp);
}

// Function to generate QR code
void generate_student_qr(const char *enrollment, const char *name, const char *course, const char *contact, const char *address) {
    char student_data[512];
    snprintf(student_data, sizeof(student_data), "Enrollment_Number: %s\nName: %s\nCourse: %s\nContactNo: %s\nAddress: %s",
             enrollment, name, course, contact, address);

    QRcode *qrcode = QRcode_encodeString(student_data, 0, QR_ECLEVEL_Q, QR_MODE_8, 1);
    
    if (!qrcode) {
        printf("Failed to generate QR code for %s\n", name);
        return;
    }

    char file_path[256];
    snprintf(file_path, sizeof(file_path), SAVE_DIR "student_%s.pgm", enrollment);
    save_qr_image(qrcode, file_path);

    printf("QR Code saved: %s\n", file_path);
    QRcode_free(qrcode);
}

int main() {
    generate_student_qr("123456", "John Doe", "Computer Science", "9876543210", "New York");
    return 0;
}
