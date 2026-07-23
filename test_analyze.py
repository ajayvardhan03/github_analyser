import unittest

from analyze import AnalyzeRepo


class TestAnalyzeRepoUrlParsing(unittest.TestCase):
    """AnalyzeRepo receives whatever GitHub page the user currently has open
    in the extension, not just clean repo root URLs."""

    def test_repo_root_url(self):
        repo = AnalyzeRepo("token", "https://github.com/octocat/Hello-World")
        self.assertEqual(repo.github_owner, "octocat")
        self.assertEqual(repo.github_repo_name, "Hello-World")

    def test_trailing_slash(self):
        repo = AnalyzeRepo("token", "https://github.com/octocat/Hello-World/")
        self.assertEqual(repo.github_owner, "octocat")
        self.assertEqual(repo.github_repo_name, "Hello-World")

    def test_subpage_url(self):
        repo = AnalyzeRepo("token", "https://github.com/octocat/Hello-World/issues")
        self.assertEqual(repo.github_owner, "octocat")
        self.assertEqual(repo.github_repo_name, "Hello-World")

    def test_deep_subpage_url(self):
        repo = AnalyzeRepo(
            "token", "https://github.com/octocat/Hello-World/blob/main/README.md"
        )
        self.assertEqual(repo.github_owner, "octocat")
        self.assertEqual(repo.github_repo_name, "Hello-World")

    def test_invalid_url_raises(self):
        with self.assertRaises(ValueError):
            AnalyzeRepo("token", "https://github.com/octocat")


if __name__ == "__main__":
    unittest.main()
