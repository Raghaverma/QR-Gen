import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.EncodeHintType;
import com.google.zxing.WriterException;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;

public class POSQRCodeGenerator {
    
    // Directory to save QR codes
    private static final String SAVE_DIR = "Path/To/Your/Directory";

    public static void main(String[] args) {
        // Sample product data
        List<Map<String, String>> products = new ArrayList<>();
        
        // Add sample product data
        products.add(Map.of(
            "Product_ID", "12345",
            "Name", "Sample Product",
            "Price", "$19.99",
            "MFG_Date", "2025-01-15",
            "EXP_Date", "2026-01-15",
            "Batch_No", "B123456"
        ));

        // Ensure the save directory exists
        File dir = new File(SAVE_DIR);
        if (!dir.exists()) {
            dir.mkdirs();
        }

        // Generate QR codes for all products
        for (Map<String, String> product : products) {
            generateProductQR(product);
        }
    }
    
    private static void generateProductQR(Map<String, String> product) {
        String productId = product.get("Product_ID");
        if (productId == null || productId.isEmpty()) {
            System.out.println("Skipping product - No Product ID");
            return;
        }

        StringBuilder productData = new StringBuilder();
        for (Map.Entry<String, String> entry : product.entrySet()) {
            productData.append(entry.getKey()).append(": ").append(entry.getValue()).append("\n");
        }
        
        try {
            QRCodeWriter qrCodeWriter = new QRCodeWriter();
            BitMatrix bitMatrix = qrCodeWriter.encode(
                productData.toString(),
                BarcodeFormat.QR_CODE,
                300,
                300
            );
            
            File qrFile = new File(SAVE_DIR + "/product_" + productId + ".png");
            MatrixToImageWriter.writeToPath(bitMatrix, "PNG", qrFile.toPath());
            System.out.println("QR Code saved: " + qrFile.getAbsolutePath());
        } catch (WriterException | IOException e) {
            System.err.println("Error generating QR code: " + e.getMessage());
        }
    }
}
