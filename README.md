An API client for squabbles.io

Put your username and password in the SQUABBLES_USERNAME and SQUABBLES_PASSWORD environment variables.

Example usage:

	from squabbles_client import SquabblesClient

	client = SquabblesClient()
	client.login()

	title = "Big news from somewhere"
	url = "https://apnews.com/big-news-from-somewhere/"


	content = f"[{title}]({url})"

	response = client.new_post(community_name, content)
	post_id = response["hash_id"]
	client.post_toggle_like(post_id)
	response = client.reply(post_id, "What a great post!")
	comment_id = response['hash_id']
	client.comment_toggle_like(comment_id)

