"""Arithmetic Coding Fractional Interval Subdivision Engine.
100% Python Standard Library.
"""

from collections import Counter

class ArithmeticCoder:
    """Arithmetic range coder mapping messages to real intervals [0.0, 1.0)."""

    @staticmethod
    def encode(text: str) -> tuple:
        if not text:
            return 0.0, {}
        counts = Counter(text)
        n = len(text)
        probs = {k: v / n for k, v in counts.items()}
        cum_probs = {}
        cum = 0.0
        for k, p in sorted(probs.items()):
            cum_probs[k] = (cum, cum + p)
            cum += p
        low = 0.0
        high = 1.0
        for ch in text:
            r = high - low
            c_low, c_high = cum_probs[ch]
            high = low + r * c_high
            low = low + r * c_low
        code = (low + high) / 2.0
        return code, {"cum_probs": cum_probs, "length": n}

    @staticmethod
    def decode(code: float, model: dict) -> str:
        cum_probs = model["cum_probs"]
        n = model["length"]
        out = []
        low = 0.0
        high = 1.0
        for _ in range(n):
            r = high - low
            val = (code - low) / r
            for ch, (c_low, c_high) in cum_probs.items():
                if c_low <= val < c_high:
                    out.append(ch)
                    high = low + r * c_high
                    low = low + r * c_low
                    break
        return "".join(out)
