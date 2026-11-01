# Simulate Ghostly Screen Recorder Trigger

This example demonstrates how a screen recorder might exhibit "ghostly" behavior, starting or stopping without direct user interaction. It simulates a background process that monitors for both external triggers (like the creation of a specific file) and internal conditions (like a scheduled time or a duration limit) to control a simulated recording session. This illustrates how such unexpected actions can be intentionally programmed.

## Language

`python`

## How to Run

1. Save the code as `main.py`.
2. Run from your terminal: `python main.py`
3. To manually start recording, create an empty file named `start_recording_now.trigger` in the same directory (e.g., `touch start_recording_now.trigger` on Linux/macOS, or `New-Item start_recording_now.trigger` in PowerShell).
4. To manually stop recording, create an empty file named `stop_recording_now.trigger`.
5. Observe the console output for automatic starts/stops based on internal timing, and manual starts/stops via trigger files.

## Original Article

This example accompanies the Turkish article: [Ekran Kaydedicim Neden Kendiliğinden Çalışıyor Gibi? (Kasıtlı Olarak Booya!)](https://fatihsoysal.com/blog/ekran-kaydedicim-neden-kendiliginden-calisiyor-gibi-kasitli-olarak-booya/).

## License

MIT — see [LICENSE](LICENSE).
