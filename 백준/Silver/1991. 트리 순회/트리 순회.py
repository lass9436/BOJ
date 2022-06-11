import sys
N = int(sys.stdin.readline())
adj = {}
for _ in range(N):
    arr = sys.stdin.readline().split()
    adj[arr[0]] = [arr[1], arr[2]]

def preorder(node):
    global adj
    print(node, end="")
    if adj[node][0] != ".":
        preorder(adj[node][0])
    if adj[node][1] != ".":
        preorder(adj[node][1])        
    
def inorder(node):
    global adj
    if adj[node][0] != ".":
        inorder(adj[node][0])
    print(node, end="")        
    if adj[node][1] != ".":
        inorder(adj[node][1])        
        
def postorder(node):
    global adj
    if adj[node][0] != ".":
        postorder(adj[node][0])
    if adj[node][1] != ".":
        postorder(adj[node][1])        
    print(node, end="")
    
preorder("A")
print()
inorder("A")
print()
postorder("A")