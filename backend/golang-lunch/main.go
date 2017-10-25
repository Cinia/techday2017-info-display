package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    jsonData := map[string]string{"request": r.URL.Path[1:]}
    jsonValue, _ := json.Marshal(jsonData)
    response, err := http.Post("http://airiot.fi:19999/rest/lunch_request/", "application/json", bytes.NewBuffer(jsonValue))
    if err != nil {
    	fmt.Fprintf(w, "{\"title\": \"%s\", \"content\": \"%s!\"}", "ERROR", err)
    } else {
        data, _ := ioutil.ReadAll(response.Body)
        fmt.Fprintf(w, "{\"title\": \"%s\", \"content\": \"%s!\"}", "Lunch",  string(data))
    }
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":80", nil)
}
