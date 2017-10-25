package fi.cinia.techday.rss;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

public final class Formatter {

    private static final DateTimeFormatter DATEFORMAT = DateTimeFormatter.ofLocalizedDateTime(FormatStyle.SHORT)
            .withLocale(Locale.GERMAN).withZone(ZoneId.systemDefault());

    public static String format(Entry entry) {
        return "<li><strong>" + DATEFORMAT.format(entry.getTimestamp()) + " " + entry.getTitle() + "</strong><br>"
                + entry.getContent() + "</li>";
    }

    public static String format(Exception e) {
        StringWriter sw = new StringWriter();
        PrintWriter pw = new PrintWriter(sw);
        e.printStackTrace(pw);
        return sw.toString();
    }

    public static String format(List<Entry> entries) {
        return "<ul>" + entries.stream().map(Formatter::format).collect(Collectors.joining()) + "</ul>";
    }

    private Formatter() {
        throw new AssertionError("Static class");
    }
}
