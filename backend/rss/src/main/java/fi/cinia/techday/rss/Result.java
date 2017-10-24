package fi.cinia.techday.rss;

public class Result {

	private final String content;
	private final String title;

	public Result(String title, String content) {
		this.title = title;
		this.content = content;
	}

	public String getContent() {
		return content;
	}

	public String getTitle() {
		return title;
	}
}
