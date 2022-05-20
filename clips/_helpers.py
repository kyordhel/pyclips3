# ## ################################################################
#
# Extra helper functions
#
# ## ################################################################

def escapeComment(comment):
    if comment is None:
        return ""
    if not isinstance(comment, str):
        try: comment = str(comment)
        except: return ""
    comment = comment.replace('"', '\\"')
    return f'"{comment}"'

def getStringRepr(s):
    if not isinstance(s, str):
        return None
    if type(s) == ClipsStringType:
        return _py2clsyntax(s)
    # Already escaped string:
    if len(s) > 1 and s[0] == s[-1] == '"':
        return s
    return f'"{(s)}"'
