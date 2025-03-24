from textblob import TextBlob
from nltk.sentiment import vader
from nrclex import NRCLex


class AcceptanceIndexer:
    WEIGHTS = {}

    def __init__(self, baseline_text, comment_texts):
        self.baseline_text = baseline_text
        self.comment_texts = comment_texts

    def _scale(self, scores):
        return scores

    def _apply_weights(self, scores):
        weighted_scores = {
            label: score * self.WEIGHTS.get(label, 1) for label, score in scores.items()
        }
        return weighted_scores

    def _get_scores(self, text):
        return None

    def get_scores(self, text):
        return self._apply_weights(self._scale(self._get_scores(text)))

    def get_acceptance_scores(self):
        baseline_scores = self.get_scores(self.baseline_text)
        # print(f"Baseline Text: {self.baseline_text}")
        # print(f"Baseline Scores: {baseline_scores}")

        acceptance_scores = {}

        for comment_text in self.comment_texts:
            comment_scores = self.get_scores(comment_text)
            # print(f"Comment Text: {comment_text}")
            # print(f"Comment Scores: {comment_scores}")

            acceptance_score = 0

            for baseline_label, baseline_label_score in baseline_scores.items():
                comment_score = comment_scores.get(baseline_label, 0)
                # acceptance_score += abs(baseline_label_score - comment_score)
                acceptance_score += 1 - abs(baseline_label_score - comment_score)

            acceptance_scores[comment_text] = acceptance_score / len(baseline_scores)

        return acceptance_scores

    def calculate_acceptance_index(self):
        total_score = 0

        acceptance_scores = self.get_acceptance_scores()
        for score in acceptance_scores.values():
            total_score += score

        # return 1 - (total_score / len(acceptance_scores))
        return total_score / len(acceptance_scores)


class TextBlobAcceptanceIndexer(AcceptanceIndexer):
    WEIGHTS = {
        "polarity": 1.0,
        "subjectivity": 1.0,
    }

    def _scale(self, scores):
        scores["polarity"] = (scores["polarity"] + 1) / 2
        return scores

    def _get_scores(self, text):
        text_blob = TextBlob(text)
        polarity = text_blob.sentiment.polarity
        subjectivity = text_blob.sentiment.subjectivity

        return self._scale({"polarity": polarity, "subjectivity": subjectivity})


class VADERAcceptanceIndexer(AcceptanceIndexer):
    WEIGHTS = {
        "neg": 1.0,
        "neu": 1.0,
        "pos": 1.0,
        "compound": 1.0,
    }

    def _scale(self, scores):
        scores["compound"] = (scores["compound"] + 1) / 2
        return scores

    def _get_scores(self, text):
        scores = vader.SentimentIntensityAnalyzer().polarity_scores(text)
        scores = self._scale(scores)

        return scores


class NRCAcceptanceIndexer(AcceptanceIndexer):
    WEIGHTS = {
        "fear": 1.0,
        "anger": 1.0,
        "anticip": 1.0,
        "trust": 1.0,
        "surprise": 1.0,
        "positive": 1.0,
        "negative": 1.0,
        "sadness": 1.0,
        "disgust": 1.0,
        "joy": 1.0,
        "anticipation": 1.0,
    }

    def _get_scores(self, text):
        lexer = NRCLex(text)
        scores = lexer.affect_frequencies

        return scores


class CombinedAcceptanceIndexer(AcceptanceIndexer):
    def get_scores(self, text):
        combined_scores = {}
        for acceptance_indexer_cls in [
            TextBlobAcceptanceIndexer,
            NRCAcceptanceIndexer,
            VADERAcceptanceIndexer,
        ]:
            cls_name = acceptance_indexer_cls.__name__
            acceptance_indexer = acceptance_indexer_cls(
                self.baseline_text, self.comment_texts
            )

            combined_scores.update(
                {
                    f"{cls_name}.{key}": score
                    for key, score in acceptance_indexer.get_scores(text).items()
                }
            )

        return combined_scores
