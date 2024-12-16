import os
from api_base import ApiBase
from dotenv import load_dotenv
load_dotenv()

class GetNewsApi(ApiBase):
    def __init__(self, session):
        self.base_url = os.getenv("BASE_URL")
        self.url = f"{self.base_url}"
        super().__init__(session, self.url)
        self.session = session
        self.session.headers["Authorization"] = os.getenv("NEWS_API_KEY")

    def get_top_headlines(  # noqa: C901
            self, q=None, qintitle=None, sources=None, language=None, country=None, category=None, page_size=None, page=None
        ):
            self.url = f"{self.url}/top-headlines"
            params = {}

            # Keyword/Phrase
            if q is not None:
                params["q"] = q

            # Keyword/Phrase in Title
            if qintitle is not None:
                params["qintitle"] = qintitle


            # Sources
            if (sources is not None) and ((country is not None) or (category is not None)):
                raise ValueError("cannot mix country/category param with sources param.")

            # Sources
            if sources is not None:
                params["sources"] = sources

            # Language
            if language is not None:
                params["language"] = language

            # Country
            if country is not None:
                params["country"] = country

            # Category
            if category is not None:
                params["category"] = category

            # Page Size
            if page_size is not None:
                params["pageSize"] = page_size

            # Page
            if page is not None:
                params["page"] = page

            # Send Request
            response = self.api_request("get", params=params)
            return response
