# Automated Essay from YouTube Video

Automate watching, transcribing, summarizing, and writing an essay on a topic from a YouTube video. Works best on fact-heavy, lecture-style YouTube videos.

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/gladly-hyphenated-21/auto-youtube-essay-writer.git; cd auto-youtube-essay-writer

2. [Install Ollama](https://ollama.com/download):

      Linux:
      ```bash
      curl -fsSL https://ollama.com/install.sh | sh
      ```
      MacOS ([brew](https://brew.sh/)):
      ```bash
      brew install ollama
      ```
      MacOS (zip):
      ```bash
      curl -O 'https://ollama.com/download/Ollama-darwin.zip'
      ```
      Windows:
      [Follow instructions on Ollama.com](https://ollama.com/download/windows) 

4. OPTIONAL: create a venv:
   ```bash
   python3 -m venv venv; source venv/bin/activate

5. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the script with the YouTube URL:
   ```bash
   python run.py [youtube url]

## Example
![example usage](https://github.com/gladly-hyphenated-21/auto-youtube-essay-writer/blob/main/image.png)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/gladly-hyphenated-21/auto-youtube-essay-writer/blob/main/LICENSE) file for details.
