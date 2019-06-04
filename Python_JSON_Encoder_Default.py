# Python JSON
# json — JSON encoder and decoder.
# JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired
# by JavaScript object literal syntax (although it is not a strict subset of JavaScript).
# 
# json exposes an API familiar to users of the standard library marshal and pickle modules.
# 

#
# class json.JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
#

#
# Extensible JSON encoder for Python data structures.
#

#
# default(o) 
# Implement this method in a subclass such that it returns a serializable object for o, or calls the base implementation (to raise a TypeError).
#
 
#
# For example, to support arbitrary iterators, you could implement default like this:
# 

def default(self, o):

   try:
       iterable = iter(o)

   except TypeError:
       pass

   else:
       return list(iterable)

   # Let the base class default method raise the TypeError

   return json.JSONEncoder.default(self, o)
