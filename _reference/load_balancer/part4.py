# REFERENCE SOLUTION - do not read before you have submitted your own attempt.
import sys


def main():
    lines = sys.stdin.read().split("\n")
    n = int(lines[0].split()[0])
    caps = [int(x) for x in lines[1].split()]
    m = int(lines[2].split()[0])
    events = lines[3:3 + m]

    alive = [True] * n
    load = [0] * n
    conn_server = {}
    conn_obj = {}
    conn_seq = {}
    obj_conns = {}
    out = []
    seq = [0]

    def place(cid, oid, s):
        conn_server[cid] = s
        conn_obj[cid] = oid
        obj_conns.setdefault(oid, set()).add(cid)
        load[s] += 1
        out.append("ROUTED %s %d" % (cid, s))

    def detach(cid):
        s = conn_server.pop(cid)
        load[s] -= 1
        oid = conn_obj.pop(cid)
        obj_conns[oid].discard(cid)
        if not obj_conns[oid]:
            del obj_conns[oid]

    def route(cid, oid):
        live = obj_conns.get(oid)
        if live:
            target = conn_server[next(iter(live))]
            if alive[target] and load[target] < caps[target]:
                place(cid, oid, target)
            else:
                out.append("REJECTED %s" % cid)
            return
        best = -1
        for i in range(n):
            if alive[i] and load[i] < caps[i]:
                if best == -1 or load[i] < load[best]:
                    best = i
        if best == -1:
            out.append("REJECTED %s" % cid)
        else:
            place(cid, oid, best)

    for line in events:
        f = line.split()
        kind = f[0]
        if kind == "CONNECT":
            cid, oid = f[1], f[2]
            conn_seq[cid] = seq[0]
            seq[0] += 1
            route(cid, oid)
        elif kind == "DISCONNECT":
            cid = f[1]
            if cid in conn_server:
                detach(cid)
        elif kind == "SHUTDOWN":
            i = int(f[1])
            if not alive[i]:
                continue
            alive[i] = False
            victims = sorted((c for c in conn_server if conn_server[c] == i),
                             key=lambda c: conn_seq[c])
            pairs = [(c, conn_obj[c]) for c in victims]
            for c in victims:
                detach(c)
            for c, o in pairs:
                route(c, o)

    out.append("LOADS " + " ".join("-" if not alive[i] else str(load[i])
                                   for i in range(n)))
    sys.stdout.write("\n".join(out) + "\n")


main()
