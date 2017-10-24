package main

import (
    "log"
	"net/http"
	"time"
	"fmt"
	"strings"
	"github.com/PuerkitoBio/goquery"
)

func main() {
	http.HandleFunc("/", AntellLunchToday)
    log.Fatal(http.ListenAndServe(":80", nil))
}

func AntellLunchToday(w http.ResponseWriter, r *http.Request) {
	var jsonResponse  = ""
	current := time.Now().UTC()
	doc, error := goquery.NewDocument("http://www.antell.fi/lounaslistat/lounaslista.html?owner=74")
    if error != nil {
        log.Fatal(error)
	}
	doc.Find("#lunch-content-table > tbody > tr:nth-child(1) > td > table > tbody").Each(func(index int, item *goquery.Selection) {
		trDay := item.Find("tr:nth-child(1)")
		dayText := strings.TrimSpace(trDay.Text())
		if (strings.Contains(dayText, GetWeekDayInFinnish(current.Weekday().String()))) {
			jsonResponse += "{'menuToday':["
			foodList := item.Find("tr:not(:first-child) > td:nth-child(2)")
			foodList.Each(func(index int, foodItem *goquery.Selection) {
				foodItem.Children().Remove()
				jsonResponse += "'" + strings.TrimSpace(foodItem.Text()) + "'"
				if (index < foodList.Size()-1) {
					jsonResponse += ","
				}
			})
			jsonResponse += "]}"
		}
	})
	fmt.Fprintln(w, jsonResponse)
}

func GetWeekDayInFinnish(weekDay string) string {
	weekdays := map[string]string{
		"Monday": "Maanantai",
		"Tuesday": "Tiistai",
		"Wednesday": "Keskiviikko",
		"Thursday": "Torstai",
		"Friday": "Perjantai",
	}
	return weekdays[weekDay]
}
