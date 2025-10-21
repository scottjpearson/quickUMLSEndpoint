from quickumls import get_quickumls_client
import sys

matcher = get_quickumls_client()
text = sys.argv[1]
json = matcher.match(text, best_match=True, ignore_syntax=False)
print(json)
