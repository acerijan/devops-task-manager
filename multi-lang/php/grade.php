<?php
$score = 85;
$grade = $score >= 90 ? "A" : ($score >= 80 ? "B" : ($score >= 70 ? "C" : "F"));

for ($i = 1; $i <= 3; $i++) {
    echo "Attempt $i: Score=$score Grade=$grade\n";
}
?>