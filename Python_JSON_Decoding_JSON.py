# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
# 

#
# Decoding JSON:
# 

import json

json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

# OUTPUT: '['foo', {'bar': ['baz', None, 1.0, 2]}]'

json.loads('"\\"foo\\bar"')

# OUTPUT: '"foo\x08ar'

from io import StringIO

io = StringIO('["streaming API"]')

json.load(io)

# OUTPUT: '['streaming API']'
