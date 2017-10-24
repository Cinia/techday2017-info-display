package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "{\"title\": \"%s\", \"content\": \"Hi there, I love %s!\"}", r.URL.Path[1:], r.URL.Path[1:])
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":80", nil)
}
