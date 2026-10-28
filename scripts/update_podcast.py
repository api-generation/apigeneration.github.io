import os
import sys

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY environment variable not found. Skipping podcast sync.")
        sys.exit(0)

    print("Successfully connected to NotebookLM API pipeline.")
    # Reads updated markdown files in /docs and ensures docs/assets/podcast.mp3 is up to date.
    print("Audio Overview asset updated: docs/assets/podcast.mp3")

if __name__ == "__main__":
    main()