# `anki-time-to-recall`

Anki’s revision log, the table that records every review’s metadata, has a `time` field which [presently](https://forums.ankiweb.net/t/timer-is-still-counting-in-between-cards-is-it-normal/20552) measures the time between initially viewing a prompt and answering it (pressing “hard”, “good”, “easy”). This presents a problem when analysing a card’s efficacy as there’s often a non-deterministic difference between the time-to-recall (viewing a card then pressing “show answer”) and the time-to-answer (viewing a card, pressing “show answer”, _then_ choosing an interval).

This plugin makes the `revlog.time` field measure time to recall instead.

> **Warning:** This plugin will *irrevocably*—and discontinuously—affect the total study time and average answer time statistics, as they both derive from this field.

# Installation
## AnkiWeb

Install from [AnkiWeb](https://ankiweb.net/shared/info/1271147075).

## Manual

1. Download the latest release from [here](https://github.com/sameersismail/anki-time-to-recall/releases).
2. Open the `time-to-recall_v….ankiaddon` in Anki's “install plugin from file” dropdown.
3. Restart Anki.

## From source

1. Make a new directory for the plugin in Anki's `addons21` folder.

    ```sh
    mkdir $ANKI_DIRECTORY/addons21/time_to_recall
    ```

2. Copy over the `src/__init__.py` file.

    ```sh
    cp src/__init__.py $ANKI_DIRECTORY/addons21/time_to_recall
    ```

3. Restart Anki.