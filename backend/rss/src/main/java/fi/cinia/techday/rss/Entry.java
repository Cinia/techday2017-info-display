package fi.cinia.techday.rss;

import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.Optional;

public final class Entry {

    public static class Builder {

        private List<String> contents;
        private String description;
        private Instant published;
        private String title;

        public Entry build() {
            return new Entry(published, title, description, contents);
        }

        public Builder contents(List<String> contents) {
            this.contents = contents;
            return this;
        }

        public Builder description(String description) {
            this.description = description;
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

    private final List<String> contents;
    private final Optional<String> description;
    private final Optional<Instant> published;
    private final Optional<String> title;

    private Entry(Instant published, String title, String description, List<String> contents) {
        this.published = Optional.ofNullable(published);
        this.title = Optional.ofNullable(title);
        this.description = Optional.ofNullable(description);
        this.contents = Collections.unmodifiableList(contents == null ? new ArrayList<>() : contents);
    }

    public List<String> getContents() {
        return contents;
    }

    public Optional<String> getDescription() {
        return description;
    }

    public Optional<Instant> getPublished() {
        return published;
    }

    public Optional<String> getTitle() {
        return title;
    }
}
