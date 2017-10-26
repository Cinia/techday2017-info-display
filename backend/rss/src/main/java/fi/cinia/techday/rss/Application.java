package fi.cinia.techday.rss;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.rometools.rome.feed.synd.SyndFeed;

@RestController
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    private final Converter converter;
    private final Formatter formatter;
    private final Reader reader;

    @Autowired
    public Application(Reader reader, Converter converter, Formatter formatter) {
        this.reader = reader;
        this.converter = converter;
        this.formatter = formatter;
    }

    @RequestMapping("/")
    public @ResponseBody Response home(@RequestParam(value = "count", defaultValue = "-1") int count) {
        try {
            String path = "https://www.io-tech.fi/feed/";
            SyndFeed syndFeed = count < 0 ? reader.read(path) : reader.read(path, count);
            Feed feed = converter.convert(syndFeed);
            String content = formatter.format(feed);
            return new Response(feed.getTitle().orElse("RSS FEED"), content);
        } catch (Exception e) {
            return new Response("RSS FEED FAILURE", formatter.format(e));
        }
    }
}
