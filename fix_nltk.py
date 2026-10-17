"""
Fix NLTK data issues - run this script once
"""
import nltk
import sys

print("=" * 60)
print("NLTK Data Setup")
print("=" * 60)

# List of required data
required_data = [
    'punkt',
    'punkt_tab',
    'averaged_perceptron_tagger',
    'wordnet',
    'omw-1.4',
    'stopwords',
    'universal_tagset'
]

print(f"\nDownloading {len(required_data)} NLTK packages...\n")

failed = []
for package in required_data:
    try:
        print(f"  ⏳ Downloading {package}...", end=" ")
        nltk.download(package, quiet=True)
        print("✅")
    except Exception as e:
        print(f"❌ Failed")
        failed.append((package, str(e)))

print("\n" + "=" * 60)
print("Testing downloaded data...")
print("=" * 60)

# Test tokenization
try:
    from nltk.tokenize import sent_tokenize, word_tokenize
    result = sent_tokenize("This is a test. It works!")
    print("✅ Sentence tokenization works")
except Exception as e:
    print(f"❌ Sentence tokenization failed: {e}")
    failed.append(("sent_tokenize", str(e)))

# Test POS tagging
try:
    from nltk import pos_tag, word_tokenize
    tokens = word_tokenize("Hello world")
    tags = pos_tag(tokens)
    print("✅ POS tagging works")
    print(f"   Example: {tags}")
except Exception as e:
    print(f"❌ POS tagging failed: {e}")
    failed.append(("pos_tag", str(e)))

# Test lemmatization
try:
    from nltk.lemmatize import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    result = lemmatizer.lemmatize("going", pos='v')
    print("✅ Lemmatization works")
    print(f"   Example: going → {result}")
except Exception as e:
    print(f"❌ Lemmatization failed: {e}")
    failed.append(("lemmatize", str(e)))

# Test stopwords
try:
    from nltk.corpus import stopwords
    en_stops = stopwords.words('english')
    print(f"✅ Stopwords loaded ({len(en_stops)} words)")
except Exception as e:
    print(f"❌ Stopwords failed: {e}")
    failed.append(("stopwords", str(e)))

print("\n" + "=" * 60)
if failed:
    print(f"❌ {len(failed)} package(s) failed:")
    for package, error in failed:
        print(f"   - {package}: {error}")
    print("\nTry running again or switch to spaCy")
    sys.exit(1)
else:
    print("✅ All NLTK data ready!")
    print("\nYou can now use:")
    print("  - nltk.sent_tokenize()")
    print("  - nltk.word_tokenize()")
    print("  - nltk.pos_tag()")
    print("  - WordNetLemmatizer()")
    print("  - stopwords.words('english')")
    sys.exit(0)
