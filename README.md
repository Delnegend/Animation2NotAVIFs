# Animation2NotAVIFs
- Requirements:
  - [Python >=3](https://www.python.org/downloads/)
  - [ffmpeg](https://www.ffmpeg.org/download.html) (already included)
  - [SvtAv1EncApp](https://github.com/AOMediaCodec/SVT-AV1/releases) (already included)
  - [Rav1e](https://github.com/xiph/rav1e/releases) (fallback transcoding) (already included)

- How to use
  - Create a folder name `input` and put your GIF(s) or whatever it is into, as long as it moves (and ffmpeg can decode)
  - Run `python run-me.py`
  - Output file(s) will be in `output` folder

- Notes:
  - Height is limited to 1080px because having a high resolution is possible, but not practice.

- Browser support

  |         | PC      | Android  |
  |---------|---------|----------|
  | Chrome  | 100 ✔️  | 100 ✔️   |
  | Firefox | ⚠️1     | 98 ❌     |
  | Edge    | 99 ❌    | 99 ❌     |
  | Brave   | 1.37 ✔️ | 1.36 ✔️  |
  | Vivaldi | 5.1 ✔️  | 5.1 ✔️   |
  | Opera   | 85 ✔️   | 68 ✔️    |
  | OperaGX | 84 ✔️   | 1.5.9 ✔️ |

  ⚠️1: only shows a still image
