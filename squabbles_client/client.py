"""
afaik the entire api is entirely undocumented
"""
import requests
from .settings import Settings


class SquabblesClient:
    """
    a basic headless squabbles client that can log in and post topics/comments
    """

    session = None
    """ a requests.Session that is configured with the authentication headers to
    perform API requests """

    def __init__(self):
        self.session = requests.Session()

    def login(self, username: str = None, password: str = None):
        """the login sequence is straightforward:
        * obtain a CSRF token
        * use the CSRF token to get the cookie credentials from the login form
        * use the cookie credentials to get a bearer token
        * set the bearer token in the session headers
        """
        settings = Settings()
        if username is None:
            username = settings.SQUABBLES_USERNAME
        if password is None:
            password = settings.SQUABBLES_PASSWORD
        token = self.session.get("https://squabbles.io/csrf-token").content
        form = {
            "_token": token,
            "username": username,
            "password": password,
            "remember": "on",
        }
        self.session.post("https://squabbles.io/login", form)
        initialize_app_response = self.session.get(
            "https://squabbles.io/api/initialize-app"
        ).json()
        token = initialize_app_response["auth"]["token"]
        headers = {"authorization": "Bearer " + token}
        self.session.headers.update(headers)

    def profile(self, name: str) -> dict:
        """fetch a profile for a user
        :param name: eg. unkz
        """
        url = f"https://squabbles.io/api/user/{name}"
        return self.session.get(url).json()

    def posts(self, name: str, page: int = 1) -> dict:
        """fetch a list of posts
        :param name: eg. NeutralNews
        :param page: pagination parameter
        """
        url = f"https://squabbles.io/api/s/{name}/posts?page={page}"
        return self.session.get(url).json()

    def new_post(self, community_name: str, content: str) -> dict:
        """
        :param community_name: eg. NeutralNews
        :param content: the content of the post in markdown format
        :returns: some kind of dict
            {
            'hash_id': 'xxxxxxxx', # this can be used as a post_id to make a
                                   # top level reply
            ....
            }
        """
        response = self.session.post(
            "https://squabbles.io/api/new-post",
            files={
                "community_name": (None, community_name),
                "content": (None, content),
            },
        )
        return response.json()

    def reply(self, post_id, content):
        """
        :param post_id: a hash_id that identifies the post or comment
        :param content: the content of the comment in markdown format
        """
        url = f"https://squabbles.io/api/posts/{post_id}/reply"
        response = self.session.post(url, files={"content": (None, content)})
        return response.json()
