package main

import "fmt"

func getGrade(score int) string {
    if score >= 90 {
        return "A"
    } else if score >= 80 {
        return "B"
    } else if score >= 70 {
        return "C"
    }
    return "F"
}

func main() {
    score := 85
    for i := 1; i <= 3; i++ {
        fmt.Printf("Attempt %d: Score=%d Grade=%s\n", i, score, getGrade(score))
    }
}