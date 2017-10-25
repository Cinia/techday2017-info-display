package fi.cinia.techday.rss;

import java.io.IOException;
import java.net.URL;

import org.springframework.stereotype.Component;

import com.rometools.rome.feed.synd.SyndFeed;
import com.rometools.rome.io.FeedException;
import com.rometools.rome.io.SyndFeedInput;
import com.rometools.rome.io.XmlReader;

@Component
public final class Reader {

    public SyndFeed read(String path) throws IOException, IllegalArgumentException, FeedException {
        URL feedUrl = new URL(path);
        XmlReader reader = new XmlReader(feedUrl);
        return new SyndFeedInput().build(reader);
    }
}
