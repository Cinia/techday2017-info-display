package fi.cinia.techday.rss;

import java.util.List;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.rometools.rome.feed.synd.SyndFeed;

@SpringBootApplication
@RestController
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	@RequestMapping("/")
	public @ResponseBody Response home() {
		try {
			SyndFeed feed = Reader.read("https://bbs.io-tech.fi/forums/io-tech-fi-uutiset.67/index.rss");
			List<Entry> entries = Converter.convert(feed.getEntries());
			String content = Formatter.format(entries);
			return new Response("IO-TECH RSS", content);
		} catch (Exception e) {
			return new Response("IO-TECH RSS FAILURE", Formatter.format(e));
		}
	}
}
