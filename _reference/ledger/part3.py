# REFERENCE SOLUTION - do not read before you have submitted your own attempt.
import sys


def main():
    lines = [ln for ln in sys.stdin.read().split("\n")]
    i = 0
    while lines[i].strip() == "":
        i += 1
    n = int(lines[i].strip())
    events = lines[i + 1:i + 1 + n]

    balances = {}
    rejected = []
    applied = {}          # txnId -> parsed tuple, only if it took effect
    reversed_ids = set()

    def credit(user, amt):
        balances[user] = balances.get(user, 0) + amt

    for line in events:
        f = line.split()
        tid, kind = f[0], f[1]
        if kind == "DEPOSIT":
            user, amt = f[2], int(f[3])
            credit(user, amt)
            applied[tid] = ("DEPOSIT", user, amt)
        elif kind == "WITHDRAW":
            user, amt = f[2], int(f[3])
            if balances.get(user, 0) < amt:
                rejected.append(tid)
            else:
                credit(user, -amt)
                applied[tid] = ("WITHDRAW", user, amt)
        elif kind == "TRANSFER":
            src, dst, amt = f[2], f[3], int(f[4])
            if balances.get(src, 0) < amt:
                rejected.append(tid)
            else:
                credit(src, -amt)
                credit(dst, amt)
                applied[tid] = ("TRANSFER", src, dst, amt)
        elif kind == "REVERSE":
            target = f[2]
            if target not in applied or target in reversed_ids:
                rejected.append(tid)
            else:
                t = applied[target]
                if t[0] == "DEPOSIT":
                    credit(t[1], -t[2])
                elif t[0] == "WITHDRAW":
                    credit(t[1], t[2])
                else:
                    credit(t[2], -t[3])
                    credit(t[1], t[3])
                reversed_ids.add(target)

    out = ["%s %d" % (u, balances[u]) for u in sorted(balances) if balances[u] != 0]
    out.append("REJECTED" + ("".join(" " + r for r in rejected)))
    sys.stdout.write("\n".join(out) + "\n")


main()
