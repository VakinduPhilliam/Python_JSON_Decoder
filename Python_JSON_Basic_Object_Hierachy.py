# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
# 

#
# Encoding basic Python object hierarchies:
# 

import json

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

# OUTPUT: '["foo", {"bar": ["baz", null, 1.0, 2]}]'

print(json.dumps("\"foo\bar"))

# OUTPUT: '"\"foo\bar"'

print(json.dumps('\u1234'))

# OUTPUT: '"\u1234"'

print(json.dumps('\\'))

# OUTPUT: '"\\"'

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

# OUTPUT: '{"a": 0, "b": 0, "c": 0}'

from io import StringIO

io = StringIO()

json.dump(['streaming API'], io)

io.getvalue()

# OUTPUT: '["streaming API"]'
