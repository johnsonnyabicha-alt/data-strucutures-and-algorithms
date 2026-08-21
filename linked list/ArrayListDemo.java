import java.util.ArrayList; // Required import 

public class ArrayListDemo {
    public static void main(String[] args) {
        ArrayList<String> devices = new ArrayList<>();
        
        // Dynamically adding objects [cite: 401]
        devices.add("Phone");
        devices.add("Laptop");
        
        // Reading elements [cite: 406]
        System.out.println("First device: " + devices.get(0));
        System.out.println("Total items: " + devices.size()); 
    }
}