```python
# vowels_count.py

def count_vowels(text: str) -> int:
    vowels = set('aeiou')
    return sum(1 for char in text.lower() if char in vowels)
```
