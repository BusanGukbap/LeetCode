func numberOfSpecialChars(word string) int {
    var ans int = 0
    
    upper := make(map[rune]int)
    lower := make(map[rune]int)

    for index, w := range word {
        if 'a' <= w && w <= 'z' {
            lower[w-'a'] = index
        } else if _, ok := upper[w-'A']; !ok {
            upper[w-'A'] = index
        }   
    }

    for i:=0; i<26; i++ {
        lv, lok := lower[rune(i)]
        uv, uok := upper[rune(i)]
        if lok && uok && lv < uv {
            ans++
        }
    }

    return ans
}