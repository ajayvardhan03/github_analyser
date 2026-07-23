import logging
from urllib.parse import urlparse

from LLM.scrap import scrap_repo

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AnalyzeRepo")


class AnalyzeRepo:
    """
    Main Class to perform all analyzing and summary operations
    """

    def __init__(self, token, url):
        self.llm_token = token

        # The extension sends whatever GitHub page the user currently has open,
        # which may be the repo root, a subpage (/issues, /tree/main, ...), or
        # have a trailing slash. Taking the last two "/"-separated segments
        # (the old approach) breaks on all of those. The owner/repo are always
        # the first two path segments, so parse the URL path and use those.
        path_parts = [part for part in urlparse(url).path.split("/") if part]
        if len(path_parts) < 2:
            raise ValueError(f"Could not parse a GitHub owner/repo from URL: {url}")
        self.github_owner, self.github_repo_name = path_parts[0], path_parts[1]
        logger.info("Necessary variables set")

    def run(self):
        result = scrap_repo(
            self.github_owner,
            self.github_repo_name,
            self.llm_token,
        )
        logger.info("Final summary ready!")

        return result
