import time
from anki.cards import Card
from aqt.gui_hooks import reviewer_did_show_answer


def initialise_plugin() -> None:
    def on_reviewer_did_show_answer(card: Card) -> None:
        def time_taken(capped: bool = False):
            result = int((answer_shown_at - card.timer_started) * 1000)
            return result

        answer_shown_at = time.time()
        # Overwrite the card's `time_taken` method.
        card.time_taken = time_taken

    reviewer_did_show_answer.append(on_reviewer_did_show_answer)


initialise_plugin()
