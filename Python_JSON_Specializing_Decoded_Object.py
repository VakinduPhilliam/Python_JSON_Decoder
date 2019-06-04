# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
# 

#
# Specializing JSON object decoding:
# 

import json

def as_complex(dct):
        if '__complex__' in dct:

            return complex(dct['real'], dct['imag'])

        return dct

json.loads('{"__complex__": true, "real": 1, "imag": 2}',
        object_hook=as_complex)

# OUTPUT: '(1+2j)'

import decimal

json.loads('1.1', parse_float=decimal.Decimal)

# OUTPUT: 'Decimal('1.1')'
