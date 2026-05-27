import sys
from message_builder import build_topic_message


def main():
    if len(sys.argv) < 2:
        print("Please provide a topic.")
        print("Example: python topic_echo.py python")
        print("Example: python topic_echo.py machine learning")
    else:
        topic = " ".join(sys.argv[1:])
        message = build_topic_message(topic)
        print(message)


if __name__ == "__main__":
    main()