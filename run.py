import yt_dlp
import webvtt
import requests
import sys
import ollama

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Window(Gtk.Window):
    response_type = "Essay"
    input_url = ""
    extra_prompt = ""
    model = "llama3.2:3b"
    prompts = {
        "essay": "The following transcript is a text summarization of an important lecture. From the lecture, draft an ESSAY that explains the concepts described. The essay should explain the concepts just learned from the transcription and be entirely in the third-person perspective. Use a conversational tone and simple but clear writing. ",
        "eli5": "The following transcript is a text summarization of an important lecture. Explain the main topics of this transcription using language and examples that would be familiar to a five-year-old. "
    }

    def __init__(self):
        Gtk.Window.__init__(self, title="Youtube Writer - floatme")
        self.set_default_size(1000, 600)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        title_label = Gtk.Label()
        title_label.set_use_markup(True)
        title_label.set_markup('<span font_desc="18" weight="bold">Youtube Writer</span>')
        vbox.pack_start(title_label, False, False, 0)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.pack_start(hbox, True, True, 0)

        left_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hbox.pack_start(left_vbox, False, False, 0)

        dropdown_label = Gtk.Label(label="Response type:")
        left_vbox.pack_start(dropdown_label, False, False, 0)

        combo_box = Gtk.ComboBoxText()
        combo_box.append_text("Essay")
        combo_box.append_text("Summary")
        combo_box.append_text("Explain Like I'm 5")
        combo_box.set_active(0)
        combo_box.connect("changed", self.on_selection_change)
        left_vbox.pack_start(combo_box, False, False, 0)

        textbox = Gtk.Entry()
        textbox.set_placeholder_text("Enter YouTube URL...")
        textbox.connect("changed", self.on_url_change)
        left_vbox.pack_start(textbox, False, False, 0)

        extra_prompt_entry = Gtk.Entry()
        extra_prompt_entry.set_placeholder_text("Enter extra prompting text...")
        extra_prompt_entry.connect("changed", self.on_extra_prompt_change)
        left_vbox.pack_start(extra_prompt_entry, False, False, 0)

        model_entry = Gtk.Entry()
        model_entry.set_placeholder_text('enter model name')
        model_entry.connect("changed", self.on_model_entry_changed)
        left_vbox.pack_start(model_entry, False, False, 0)

        submit_button = Gtk.Button(label="Submit")
        submit_button.connect("clicked", self.on_submit_click)
        left_vbox.pack_start(submit_button, False, False, 0)

        text_view = Gtk.TextView()
        text_view.set_editable(False)
        text_view.set_cursor_visible(False)
        text_view.set_wrap_mode(Gtk.WrapMode.WORD)

        self.text_view_buffer = text_view.get_buffer()
        self.text_view_buffer.set_text("Select a response type, then enter a URL")

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(text_view)
        hbox.pack_start(scrolled_window, True, True, 0)

    def on_selection_change(self, combo):
        self.response_type = combo.get_active_text()
        print(f"Response type set to: {self.response_type}")

    def on_url_change(self, textbox):
        self.input_url = textbox.get_text()
        print(f"Input URL set to: {self.input_url}")
    
    def on_extra_prompt_change(self, textbox):
        self.extra_prompt = textbox.get_text()
        print(f"Extra Prompt set to: {self.extra_prompt}")

    def on_model_entry_changed(self, textbox):
        self.model = textbox.get_text()
        print(f"model set to: {self.model}")
    def on_submit_click(self, button):
        if not self.input_url:
            self.text_view_buffer.set_text("Error: Please provide a URL.")
            return

        print(f"Submitting with URL: {self.input_url} and response type: {self.response_type}")
        self.run(self.input_url)

    def run(self, url):
        ydl_opts = {
            'extract_flat': 'discard_in_playlist',
            'fragment_retries': 10,
            'ignoreerrors': 'only_download',
            'postprocessors': [{'key': 'FFmpegConcat', 'only_multi_video': True, 'when': 'playlist'}],
            'retries': 10,
            'skip_download': True,
            'subtitleslangs': ['en-orig'],
            'writeautomaticsub': True,
            'outtmpl': 'subs.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(url)])

        vtt = webvtt.read('subs.en-orig.vtt')
        transcript = " ".join(line.text.strip() for line in vtt)

        print(f"[subtitles] '{transcript[:50]}...{transcript[-50:]}'")

        print("[ollama] loading Ollama")
        try:
            ollama.list()
        except:
            print("[ollama] Ollama not detected running, exiting")
            exit()

        print("[ollama] prompting Ollama...")

        def prompt_ollama(prompt):
            response = ollama.chat(model=self.model, messages=[{'role': 'user', 'content': prompt}])
            return str(response['message']['content'])

        prompt = "Create a long and DETAILED SUMMARY of the following lecture transcript. "
        response = prompt_ollama(prompt + self.extra_prompt + ". Here is the transcript: " + transcript)

        if self.response_type == "Summary":
            self.text_view_buffer.set_text(response)
        else:
            print("[ollama] prompting Ollama again...")

            prompt2 = self.prompts["eli5"] if self.response_type.lower() == "explain like i'm 5" else \
                      self.prompts["essay"] if self.response_type.lower() == "essay" else ""
            response2 = prompt_ollama(prompt2 + self.extra_prompt + response)
            print("[ollama] Done!")
            self.text_view_buffer.set_text(response2)

        print("[done] DONE!")

win = Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
