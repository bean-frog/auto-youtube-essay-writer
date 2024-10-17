# Automated Essay from YouTube Video

Automate watching, transcribing, summarizing, and writing an essay on a topic from a YouTube video. Works best on fact-heavy, lecture-style YouTube videos.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gladly-hyphenated-21/auto-youtube-essay-writer.git
2. Navigate to the project directory:
   ```bash
   cd auto-youtube-essay-writer
3. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the script with the YouTube URL:
   ```bash
   python run.py [youtube url]

## Example
>(auto_astro_ls) user@computer ~/A/auto_astro_ls> python3 auto_astro_ls.py 'https://www.youtube.com/watch?v=r5Pcqkhmp_0'
>[youtube] Extracting URL: https://www.youtube.com/watch?v=r5Pcqkhmp_0
>[youtube] r5Pcqkhmp_0: Downloading webpage
>[youtube] r5Pcqkhmp_0: Downloading ios player API JSON
>[youtube] r5Pcqkhmp_0: Downloading mweb player API JSON
>[youtube] r5Pcqkhmp_0: Downloading m3u8 information
>[info] r5Pcqkhmp_0: Downloading subtitles: en-orig
>[info] r5Pcqkhmp_0: Downloading 1 format(s): 616+251
>Deleting existing file subs.en-orig.vtt
>[info] Writing video subtitles to: subs.en-orig.vtt
>[download] Destination: subs.en-orig.vtt
>[download] 100% of   40.91KiB in 00:00:00 at 706.61KiB/s
>[subtitles] ' scientists work on the boundaries of the unknown ...anity by watching one of these videos next [Music]'
>[ollama] loading Ollama
>[ollama] prompting Ollama...
>[ollama] prompting Ollama again...
>[ollama] Done!
>[essay] 
>The Enigmatic World of Paradoxes: Unraveling the Black Hole Information Paradox
>
>In the realm of physics, paradoxes have long been a thorn in the side of scientists, threatening to undermine our current understanding of the >universe. However, paradoxes have also consistently led to new discoveries and a deeper comprehension of the world. One such enigmatic conundrum is >the black hole information paradox, which has captivated physicists for decades.
>
>At its core, the paradox revolves around what happens to information contained in matter that falls into a black hole. According to the fundamental >principles of conservation of energy and momentum, this information should be preserved. Yet, the laws of physics suggest that it may be lost >forever, creating a seemingly insurmountable puzzle. The conundrum lies in understanding the concept of "information" itself – traditionally, we >associate it with visible characteristics such as color and texture. However, quantum mechanics reveals a different narrative, where information is >encoded in the unique properties of particles, including their position, velocity, spin, and other attributes.

>The conservation of quantum information is a cornerstone principle that underpins much of modern physics. This fundamental concept asserts that the >total amount of quantum information in the universe cannot be destroyed, even if an object is completely annihilated or appears to be "lost" >forever. While this idea may seem counterintuitive, it has profound implications for our understanding of space, time, and reality.

>The black hole information paradox arises when matter falls into a black hole, its quantum information seemingly dissolving into the void. This >conundrum is compounded by the event horizon, which marks the boundary beyond which information appears irretrievable. The apparent destruction of >information poses significant challenges to our fundamental theories of general relativity and quantum mechanics.

>Researchers have proposed various solutions to this paradox, ranging from theories suggesting that information still exists within the black hole to >others positing that it is encoded on the surface layer of the event horizon. The presence of Hawking radiation further complicates matters, as it >suggests that black holes gradually evaporate over incredibly long periods of time.

>The implications of resolving or reframing this paradox would be far-reaching and transformative. It could necessitate rewriting some of our most >fundamental scientific paradigms and challenging current models of reality. Fortunately, paradoxes in science have consistently yielded new >discoveries and a deeper understanding of the world.

>One promising area of research involves the holographic principle, which posits that the boundary of the observable universe is a two-dimensional >surface encoded with information about three-dimensional objects. If proven, this theory would revolutionize our comprehension of reality, >suggesting that reality as we know it might be a holographic projection of information.

>Ultimately, delving into paradoxes like the black hole information paradox has expanded humanity's knowledge, challenging assumptions and pushing >the boundaries of understanding. By embracing these intellectual conundrums, scientists can navigate the complexities of the universe and uncover >new truths about space, time, matter, and reality itself.

>[done] DONE!
>

## License
This project is licensed under the MIT License - see the LICENSE file for details.
