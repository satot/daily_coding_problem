import sys

class Collatz:
    def __init__(self, n):
        self.n = n
        self.checked = set()
        self.probe(n)

    def next_val(self, n):
        if n <= 1:
            return 1
        elif n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1
    
    def validate(self, n):
        #print n
        k = n
        history = set()
        if k in self.checked:
            return True
        while k > 1:
            history.add(k)
            k = self.next_val(k)
            if k in history:
                break
            #print k
        if k == 1:
            self.checked = self.checked.union(history)
            return True
        else:
            return False

    def probe(self, n):
        failed = []
        for i in range(2, n):
            #print "checking " + str(i)
            if not self.validate(i):
                print "failed " + str(i)
                failed.append(i)
        #print len(self.checked)
        print "failed: " + (",").join([str(i) for i in failed])

try:
    n = int(sys.argv[1])
except ValueError:
    print "please specify a valid integer"
    exit(1)

Collatz(n)
