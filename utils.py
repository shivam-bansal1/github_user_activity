from typing import Any, Dict, Tuple

import requests
from requests.exceptions import HTTPError, RequestException
import re


class GithubAPI:
    BASE_URL = "https://api.github.com"

    @staticmethod
    def get_user_events(username):
        try:
            response = requests.get(f"{GithubAPI.BASE_URL}/users/{username}/events")
            response.raise_for_status()
            return response.json()

        except HTTPError as http_err:
            if http_err.request.status_code == "403":
                raise ValueError("Api limit reached, try again later.")
            elif http_err.request.status_code == "404":
                raise ValueError(f"User {username} not found")
            else:
                raise ValueError(f"Http error: {http_err}")

        except RequestException as req_err:
            print(f"Network Error: {req_err}")


class EventFormatter:
    """Format GitHub events into human-readable strings."""

    @staticmethod
    def format_event(event: Dict[str, Any]) -> str:
        event_type = event["type"]
        repo_name = event.get("repo", {}).get("name", "Unknown")
        payload = event.get("payload", {})

        formatters = {
            "WatchEvent": lambda : f"Starred {repo_name}",
            "PushEvent": lambda : EventFormatter._format_push_event(payload, repo_name),
            "CreateEvent": lambda : EventFormatter._format_create_event(payload, repo_name),
            "DeleteEvent": lambda : EventFormatter._format_delete_event(payload, repo_name),
            "ForkEvent": lambda : f"Forked {repo_name}",
            "IssuesEvent": lambda : EventFormatter._format_issues_event(payload, repo_name),
            "IssueCommentEvent": lambda : EventFormatter._format_issue_comment_event(payload, repo_name),
            "PullRequestEvent": lambda: EventFormatter._format_pull_request_event(payload, repo_name),
            "PullRequestReviewEvent": lambda: f"Reviewed pull request in {repo_name}",
            "PullRequestReviewCommentEvent": lambda: f"Commented on pull request in {repo_name}",
            "CommitCommentEvent": lambda: f"Commented on commit in {repo_name}",
            "ReleaseEvent": lambda: EventFormatter._format_release_event(payload, repo_name),
            "PublicEvent": lambda: f"Made {repo_name} public",
            "MemberEvent": lambda: EventFormatter._format_member_event(payload, repo_name),
        }

        formatter = formatters.get(event_type)
        return formatter() if formatter else None

    @staticmethod
    def _format_push_event(payload: Dict[str, Any], repo_name: str) -> str:
        commit_count = payload.get("commits", {}).get("count", 1)
        ref = payload.get("ref", "").split("/")[-1]
        return f"Pushed {commit_count} commit(s) to {ref} in {repo_name}"

    @staticmethod
    def _format_create_event(payload: Dict[str, Any], repo_name: str) -> str:
        ref_type = payload.get("ref_type", "unknown")
        ref = payload.get("ref", "")
        if ref:
            return f"Created {ref_type} '{ref}' in {repo_name}"
        return f"Created {ref_type} in {repo_name}"

    @staticmethod
    def _format_delete_event(payload: Dict[str, Any], repo_name: str) -> str:
        ref_type = payload.get("ref_type", "unknown")
        ref = payload.get("ref", "")

        return f"Deleted {ref_type} '{ref}' in {repo_name}"

    @staticmethod
    def _format_issues_event(payload: Dict[str, Any], repo_name: str) -> str:
        action = payload.get("action", "modified")
        issue = payload.get("issue", {}).get("title", "")

        return f"{action.capitalize()} issue {issue} in {repo_name}"

    @staticmethod
    def _format_issue_comment_event(payload: Dict[str, Any], repo_name: str) -> str:
        issue = payload.get("issue", {}).get("title", "")
        comment = payload.get("comment", {}).get("body", "")

        return f"Commented '{comment}' on issue '{issue}' in {repo_name}"

    @staticmethod
    def _format_pull_request_event(payload: Dict[str, Any], repo_name: str) -> str:
        action = payload.get("action", "modified")
        pr_title = payload.get("pull_request", {}).get("title", "")
        return f"{action.capitalize()} pull request '{pr_title}' in {repo_name}"

    @staticmethod
    def _format_release_event(payload: Dict[str, Any], repo_name: str) -> str:
        tag = payload.get("release", {}).get("tag_name", "")
        return f"Released {tag} in {repo_name}"

    @staticmethod
    def _format_member_event(payload: Dict[str, Any], repo_name: str) -> str:
        action = payload.get("action", "modified")
        member = payload.get("member", {}).get("login", "someone")
        return f"{action.capitalize()} {member} as collaborator in {repo_name}"


class UsernameValidator:

    @staticmethod
    def validate(username: str) -> Tuple[bool, str | None]:

        if not username:
            return False, "GitHub username cannot be empty."

        if not (1 <= len(username) <= 39):
            return False, "Invalid username: length must be between 1 and 39 characters."

        if username[0] == "-" or username[-1] == "-":
            return False, "Invalid username: cannot start or end with a hyphen."

        if not re.fullmatch(r"[A-Za-z0-9-]+", username):
            return False, "Invalid username: only letters, digits, and hyphens are allowed."

        if "--" in username:
            return False, "Invalid username: cannot contain consecutive hyphens '--'."

        return True, None