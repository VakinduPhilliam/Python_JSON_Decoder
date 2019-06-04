# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
# 

#
# Extending JSONEncoder:
# 

import json

class ComplexEncoder(json.JSONEncoder):

        def default(self, obj):

            if isinstance(obj, complex):
                return [obj.real, obj.imag]

            # Let the base class default method raise the TypeError

            return json.JSONEncoder.default(self, obj)

json.dumps(2 + 1j, cls=ComplexEncoder)

# OUTPUT: '[2.0, 1.0]'

ComplexEncoder().encode(2 + 1j)

# OUTPUT: '[2.0, 1.0]'

list(ComplexEncoder().iterencode(2 + 1j))

# OUTPUT: ['[2.0', ', 1.0', ']']
