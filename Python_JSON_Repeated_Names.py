# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
# 

#
# Repeated Names Within an Object:
# The RFC specifies that the names within a JSON object should be unique, but does not mandate how repeated names in JSON objects should be handled.
# By default, this module does not raise an exception; instead, it ignores all but the last name-value pair for a given name:
# 

weird_json = '{"x": 1, "x": 2, "x": 3}'

json.loads(weird_json)

# OUTPUT: '{'x': 3}'
