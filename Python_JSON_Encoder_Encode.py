# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
#
 
#
# JSON Encoder
#

#
# encode(o) 
# Return a JSON string representation of a Python data structure, o.
#


#
# For example:
# 

json.JSONEncoder().encode({"foo": ["bar", "baz"]})


# OUTPUT: '{"foo": ["bar", "baz"]}'
