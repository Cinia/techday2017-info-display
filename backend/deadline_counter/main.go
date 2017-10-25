/*
This microservice needs environmental varianles EVENTNAME and DEADLINE to work.
Example:
     - EVENTNAME=Event name here
     - DEADLINE=2017-12-13 14:00 UTC
*/
package main

import (
	"fmt"
	"net/http"
	"os"
	"time"
)

const (
	// See http://golang.org/pkg/time/#Parse
	timeFormat = "2006-01-02 15:04 MST"
)

func jukkaTest(w http.ResponseWriter, r *http.Request) {
	eventname := os.Getenv("EVENTNAME")
	deadline := os.Getenv("DEADLINE")
	if eventname == "" || deadline == "" {
		fmt.Fprintf(w, "{\"title\": \"Deadline counter error\", \"content\":\"<h1>Error</h1><p>Environmental variables not configured.</p>\"}")
	} else {
		timeZone, _ := time.LoadLocation("UTC")
		// calculate time to deadline.
		startTime, _ := time.Parse(timeFormat, deadline)
		duration := startTime.Sub(time.Now().In(timeZone))
		// Convert time duration to human readable format.
		days := int(duration.Hours() / 24)
		hours := int(duration.Hours()) - int((days * 24))
		minutes := int(duration.Minutes()) - int(duration.Hours())*60
		if duration.Hours() > 0 {
			fmt.Fprintf(w, "{\"title\": \"Time to %s\", \"content\":\"<h1>Time to %s</h1><p>%d days, %d hours and %d minutes to event.</p>\"}", eventname, eventname, days, hours, minutes)
		} else {
			fmt.Fprintf(w, "{\"title\": \"Time to %s\", \"content\":\"<h1>Event %s passed already</h1><p>Deadline passed by %d days, %d hours and %d minutes.</p>\"}", eventname, eventname, days, hours, minutes)
		}
	}
}

func main() {
	http.HandleFunc("/", jukkaTest)
	http.ListenAndServe(":80", nil)
}
