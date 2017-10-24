package fi.cinia.techday.rss;

import java.time.Instant;

public class Entry {

    private final String content;
    private final Instant timestamp;
    private final String title;

    public Entry(Instant timestamp, String title, String content) {
        this.timestamp = timestamp;
        this.title = title;
        this.content = content;
    }

    public String getContent() {
        return content;
    }

    public Instant getTimestamp() {
        return timestamp;
    }

    public String getTitle() {
        return title;
    }
}
