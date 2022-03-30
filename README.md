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

- Browser support

  |         | Chrome | Firefox          | Edge | Brave | Vivaldi | Opera |
  |---------|--------|------------------|------|-------|---------|-------|
  | PC      | ✅      | Show still image | ❎    |       |         |       |
  | Android | ✅      | ❎                |      |       |         | ✅     |
  | iOS     |        |                  |      |       |         |       |
