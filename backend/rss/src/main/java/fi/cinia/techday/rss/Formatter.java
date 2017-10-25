package fi.cinia.techday.rss;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

import org.springframework.stereotype.Component;

@Component
public final class Formatter {

    private static final DateTimeFormatter DATEFORMAT = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.SHORT)
            .withLocale(Locale.GERMAN).withZone(ZoneId.systemDefault());

    public String format(Entry entry) {
        String date = entry.getPublished().isPresent() ? DATEFORMAT.format(entry.getPublished().get()) : "";
        String title = entry.getTitle().orElse("");
        String contents = formatContents(entry.getContents());

        return "<li><strong>" + date + " " + title + "</strong>" + contents + "</li>";
    }

    public String format(Exception e) {
        StringWriter sw = new StringWriter();
        PrintWriter pw = new PrintWriter(sw);
        e.printStackTrace(pw);
        return sw.toString();
    }

    public String format(List<Entry> entries) {
        return "<ul>" + entries.stream().map(this::format).collect(Collectors.joining()) + "</ul>";
    }

    private String formatContents(List<String> contents) {
        if (contents.isEmpty()) {
            return "";
        }
        return contents.size() == 1 ? "<br>" + contents.get(0)
                : "<ul><li>" + String.join("</li><li>", contents) + "</li></ul>";
    }
}
