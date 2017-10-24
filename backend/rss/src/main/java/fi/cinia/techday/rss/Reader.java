package fi.cinia.techday.rss;

import java.io.IOException;
import java.net.URL;

import com.rometools.rome.feed.synd.SyndFeed;
import com.rometools.rome.io.FeedException;
import com.rometools.rome.io.SyndFeedInput;
import com.rometools.rome.io.XmlReader;

public final class Reader {

    public static SyndFeed read(String path) throws IOException, IllegalArgumentException, FeedException {
        URL feedUrl = new URL(path);
        XmlReader reader = new XmlReader(feedUrl);
        return new SyndFeedInput().build(reader);
    }

    private Reader() {
        throw new AssertionError("Static class");
    }
}
