func numberOfSpecialChars(word string) int {
    s := make(map[rune]bool)

    for _, word := range word {
        s[word] = true
    }

    var ans int = 0

    for c := 'a'; c <= 'z'; c++ {
        if s[c] && s[c-'a' + 'A'] {
            ans++
        }
    }


    return ans
}