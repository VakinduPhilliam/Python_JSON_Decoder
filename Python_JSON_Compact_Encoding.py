# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
# 

#
# JSON Compact encoding:
# 

import json

json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))

# OUTPUT: '[1,2,3,{"4":5,"6":7}]'
