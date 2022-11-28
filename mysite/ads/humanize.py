# Really simple naturalsize that is missing from django humanize :(
def naturalsize(count):
    fcount = float(count)
    k = 1024
    m = k**2
    g = m * k
    if fcount < k:
        return f"{str(count)}B"
    if fcount < m:
        return f"{str(int(fcount / (k/10.0)) / 10.0)}KB"
    if fcount < g:
        return f"{str(int(fcount / (m/10.0)) / 10.0)}MB"
    return f"{str(int(fcount / (g/10.0)) / 10.0)}GB"
