package fi.cinia.techday.rss;

public class Response {

	private final String content;
	private final String title;

	public Response(String title, String content) {
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
