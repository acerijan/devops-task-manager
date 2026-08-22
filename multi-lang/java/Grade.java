public class Grade {
    public static void main(String[] args) {
        int score = 85;
        String grade;
        if (score >= 90) grade = "A";
        else if (score >= 80) grade = "B";
        else if (score >= 70) grade = "C";
        else grade = "F";

        for (int i = 1; i <= 3; i++) {
            System.out.println("Attempt " + i + ": Score=" + score + " Grade=" + grade);
        }
    }
}