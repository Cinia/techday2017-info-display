package fi.cinia.techday.rss;

import java.time.Instant;
import java.util.List;
import java.util.stream.Collectors;

import org.jsoup.Jsoup;

import com.rometools.rome.feed.synd.SyndEntry;

public final class Converter {

	public static List<Entry> convert(List<SyndEntry> entries) {
		return entries.stream().map(Converter::convert).collect(Collectors.toList());
	}

	public static Entry convert(SyndEntry entry) {
		String title = entry.getTitle();
		String html = entry.getContents().isEmpty() ? "" : entry.getContents().get(0).getValue();
		String content = Jsoup.parse(html).text();
		Instant timestamp = entry.getPublishedDate().toInstant();
		return new Entry(timestamp, title, content);
	}

	private Converter() {
		throw new AssertionError("Static class");
	}
}
