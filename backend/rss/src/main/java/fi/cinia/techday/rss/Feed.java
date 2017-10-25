package fi.cinia.techday.rss;

import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.Optional;

public final class Feed {

    public static class Builder {

        private String description;
        private List<Entry> entries;
        private Instant published;
        private String title;

        public Feed build() {
            return new Feed(published, title, description, entries);
        }

        public Builder description(String description) {
            this.description = description;
            return this;
        }

        public Builder entries(List<Entry> entries) {
            this.entries = entries;
            return this;
        }

        public Builder published(Date published) {
            published(published == null ? null : published.toInstant());
            return this;
        }

        public Builder published(Instant published) {
            this.published = published;
            return this;
        }

        public Builder title(String title) {
            this.title = title;
            return this;
        }
    }

    private final Optional<String> description;
    private final List<Entry> entries;
    private final Optional<Instant> published;
    private final Optional<String> title;

    private Feed(Instant published, String title, String description, List<Entry> entries) {
        this.description = Optional.ofNullable(description);
        this.entries = Collections.unmodifiableList(entries == null ? new ArrayList<>() : entries);
        this.published = Optional.ofNullable(published);
        this.title = Optional.ofNullable(title);
    }

    public Optional<String> getDescription() {
        return description;
    }

    public List<Entry> getEntries() {
        return entries;
    }

    public Optional<Instant> getPublished() {
        return published;
    }

    public Optional<String> getTitle() {
        return title;
    }
}
