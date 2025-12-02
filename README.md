# GitHub Activity Tracker

A simple command-line tool to fetch and display recent GitHub activity for any user. Built with Python and the GitHub API.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Features

- 🔍 Fetch recent activity for any GitHub user
- 📊 Display activity in a clean, human-readable format
- 🎯 Support for multiple event types (pushes, stars, PRs, issues, and more)
- ✅ Input validation for GitHub usernames
- 🖥️ Interactive command-line interface
- 🚀 No authentication required (uses public GitHub API)


## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/github-activity-tracker.git
cd github-activity-tracker
```

2. Install dependencies:
```
pip install -r requirements.txt
```

### Usage

Run the interactive CLI:

```
python main.py
```

Then enter any GitHub username to see their recent activity:

```
github-activity> torvalds

  • Pushed 3 commits to master in torvalds/linux
  • Commented on issue 'Fix memory leak' in torvalds/linux
  • Merged pull request 'Update documentation' in torvalds/linux
```

### Command Reference

| Command | Description |
|---------|-------------|
| `<username>` | Show activity for the specified GitHub user |
| `help` | Display available commands |
| `exit` or `quit` | Exit the program |

## 📖 Example Usage

```
$ python main.py
==================================================
GitHub User Activity - Interactive Mode
==================================================
Type 'help' for commands or 'exit' to quit

github-activity> octocat

  • Starred octocat/Hello-World
  • Pushed 2 commits to main in octocat/Spoon-Knife
  • Created branch 'feature-x' in octocat/Hello-World
  • Opened pull request 'Add new feature' in octocat/test-repo

github-activity> help

Available Commands:
  <username>    - Show activity for GitHub user
  help          - Show this help message
  exit / quit   - Exit the program

github-activity> exit
Goodbye!
```

## 🛠️ Project Structure

```
github-activity-tracker/
│
├── main.py              # Entry point and CLI interface
├── utils.py             # GitHub API client and utilities
└── requirements.txt     # Python dependencies       
```

## 📦 Dependencies

Install all dependencies with:
```
pip install -r requirements.txt
```

### Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- Inspired by the [GitHub User Activity Project](https://roadmap.sh/projects/github-user-activity)
---

⭐ Star this repo if you find it helpful!# github_user_activity