package fi.cinia.techday.rss;

import java.util.Date;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

import org.jsoup.Jsoup;
import org.springframework.stereotype.Component;

import com.rometools.rome.feed.synd.SyndContent;
import com.rometools.rome.feed.synd.SyndEntry;
import com.rometools.rome.feed.synd.SyndFeed;

@Component
public final class Converter {

    public List<Entry> convert(List<SyndEntry> entries) {
        return entries.stream().map(this::convert).collect(Collectors.toList());
    }

    public Entry convert(SyndEntry entry) {
        String title = stripHtml(entry.getTitle());
        String description = entry.getDescription() == null ? null : stripHtml(entry.getDescription().getValue());
        Date date = entry.getPublishedDate();
        List<String> contents = entry.getContents().stream().map(SyndContent::getValue).filter(Objects::nonNull)
                .map(this::stripHtml).collect(Collectors.toList());

        return new Entry.Builder().published(date).title(title).description(description).contents(contents).build();
    }

    public Feed convert(SyndFeed syndFeed) {
        Date date = syndFeed.getPublishedDate();
        String title = stripHtml(syndFeed.getTitle());
        String description = stripHtml(syndFeed.getDescription());
        List<Entry> entries = convert(syndFeed.getEntries());

        return new Feed.Builder().published(date).title(title).description(description).entries(entries).build();
    }

    private String stripHtml(String html) {
        return html == null ? null : Jsoup.parse(html).text();
    }
}
