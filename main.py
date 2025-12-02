from utils import GithubAPI, EventFormatter, UsernameValidator
import sys

class GithubActionsCLI:

    def __init__(self):
        self.validator = UsernameValidator()
        self.formatter = EventFormatter()
        self.api = GithubAPI()

    def print_help(self) -> None:
        help_text = """
        Available Commands:
          <username>              - Github Username
          help                  - Show this help message
          exit / quit           - Exit the program
        """

        print(help_text)

    def display_user_activity(self, username: str) -> None:
        is_valid, error = self.validator.validate(username)
        if not is_valid:
            print(f"Error: {error}")
            return

        try:
            events = self.api.get_user_events(username)
            if not events:
                print(f"No recent activity found for user '{username}'")
                return
        except ValueError as e:
            print(f"Error: {e}")
            return

        formatted_events = []
        for event in events:
            formatted = self.formatter.format_event(event)
            if formatted:
                formatted_events.append(formatted)

        if not formatted_events:
            print(f"No events found for user '{username}'")
        else:
            for event in formatted_events:
                print(f" • {event}")

        print()



    def run(self) -> None:

        print("=" * 50)
        print("Github User Activity - Interactive Mode")
        print("=" * 50)
        print("Type 'help' for available commands or 'exit' to quit\n")

        while True:
            try:
                user_input = input("github-user-activity > ").strip("")
                if not user_input:
                    continue

                command = user_input.strip()

                if command.lower() in ["quit", "exit", "q"]:
                    print("Goodbye!")
                    return

                if command.lower() == "help":
                    self.print_help()
                    continue

                self.display_user_activity(user_input)

            except KeyboardInterrupt:
                print("\n\nUse 'exit' or 'quit' to leave the program")
            except EOFError:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    api = GithubActionsCLI()
    return api.run()


if __name__ == "__main__":
    sys.exit(main())