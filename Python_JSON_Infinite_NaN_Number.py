# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
# 

#
# Infinite and NaN Number Values:
# The RFC does not permit the representation of infinite or NaN number values. Despite that, by default, this module accepts and outputs Infinity,
# -Infinity, and NaN as if they were valid JSON number literal values:
# 

# Neither of these calls raises an exception, but the results are not valid JSON

json.dumps(float('-inf'))

# OUTPUT: '-Infinity'

json.dumps(float('nan'))

# OUTPUT: 'NaN'

# Same when deserializing

json.loads('-Infinity')

# OUTPUT: '-inf'

json.loads('NaN')

# OUTPUT: 'nan'
