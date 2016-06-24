import unittest
from unittest.mock import patch

from ghhu import github


class AvatarTestesBasicos(unittest.TestCase):
    @patch('ghhu.github.requests')
    def test_avatar(self, req_mock):
        req_mock.get.return_value.text = resposta_json
        res = github.avatar('renzon')
        self.assertEquals('https://avatars.githubusercontent.com/u/3457115?v=2', res)


class AvatarTestsIntegracao(unittest.TestCase):
    def test_avatar(self):
        res = github.avatar('renzon')
        self.assertEquals('https://avatars.githubusercontent.com/u/3457115?v=3', res)


resposta_json = """{
  "login": "renzon",
  "id": 3457115,
  "avatar_url": "https://avatars.githubusercontent.com/u/3457115?v=2",
  "gravatar_id": "",
  "url": "https://api.github.com/users/renzon",
  "html_url": "https://github.com/renzon",
  "followers_url": "https://api.github.com/users/renzon/followers",
  "following_url": "https://api.github.com/users/renzon/following{/other_user}",
  "gists_url": "https://api.github.com/users/renzon/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/renzon/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/renzon/subscriptions",
  "organizations_url": "https://api.github.com/users/renzon/orgs",
  "repos_url": "https://api.github.com/users/renzon/repos",
  "events_url": "https://api.github.com/users/renzon/events{/privacy}",
  "received_events_url": "https://api.github.com/users/renzon/received_events",
  "type": "User",
  "site_admin": false,
  "name": "Renzo Nuccitelli",
  "company": "Python Pro",
  "blog": "https://adm.python.pro.br",
  "location": "Brazil",
  "email": "renzo@python.pro.br",
  "hireable": true,
  "bio": null,
  "public_repos": 87,
  "public_gists": 21,
  "followers": 287,
  "following": 3,
  "created_at": "2013-02-02T14:15:53Z",
  "updated_at": "2016-06-16T04:17:37Z"
}"""
