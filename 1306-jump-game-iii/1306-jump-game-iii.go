func canReach(arr []int, start int) bool {
    n := len(arr)
    visited := make([]bool, n)
    queue := []int{start}
    visited[start] = true

    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]

        if arr[cur] == 0 {
            return true
        }

        next := []int{cur + arr[cur], cur - arr[cur]}
        for _, ni := range next {
            if ni >= 0 && ni < n && !visited[ni] {
                visited[ni] = true
                queue = append(queue, ni)
            }
        }
    }


    return false
}