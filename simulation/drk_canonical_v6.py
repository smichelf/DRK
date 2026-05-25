"""
DRK – Kanonický model v6
========================
Klíčová změna: dynamické p_d(e) = p_d0 / (1 + β·C(e))
C(e) = počet orientovaných cyklů délky 3-4 obsahujících e (lokální)
"""

import random, numpy as np
from collections import defaultdict, deque

P_C  = 0.1618
P_D0 = 0.1      # základní p_d
BETA = 0.1      # koherenční parametr
THETA= 2.718
T_AVG= 10
MAX_N= 2000

def mk(u,v): return (min(u,v),max(u,v))

def add_un(un,adj,u,v):
    e=mk(u,v)
    if e not in un: un[e]=0; adj[u].add(v); adj[v].add(u)
    un[e]+=1

def add_or(ori,un,u,v):
    """Orientovaná hrana: první vznik 50:50, reinforcement: 50:50 + filter."""
    e=mk(u,v)
    if e not in un: return
    if e not in ori:
        ori[e]={'w_or':1,'direction':+1 if random.random()<0.5 else -1}
    else:
        new_dir=+1 if random.random()<0.5 else -1
        if new_dir==ori[e]['direction']:
            ori[e]['w_or']+=1
        # else: odmítnut (antiparalelní zakázáno)

def src_tgt(ori,u,v):
    """Vrátí (src,tgt) podle direction hrany."""
    e=mk(u,v); d=ori[e]['direction']
    if (u<v and d==+1) or (u>v and d==-1): return u,v
    return v,u

def coherence(ori,u,v):
    """C(e): počet orient. cyklů délky 3-4 přes hranu (u,v). Čistě lokální."""
    e=mk(u,v)
    if e not in ori: return 0
    s,t=src_tgt(ori,u,v)
    count=0
    # Délka 3: s→t→w→s
    for (a,b),d1 in ori.items():
        w=None
        if a==t and d1['direction']==+1: w=b
        elif b==t and d1['direction']==-1: w=a
        if w is not None and w!=s:
            e3=mk(w,s)
            if e3 in ori:
                s2,t2=src_tgt(ori,w,s)
                if s2==w and t2==s: count+=1
    # Délka 4: s→t→w→x→s
    for (a,b),d1 in ori.items():
        w=None
        if a==t and d1['direction']==+1: w=b
        elif b==t and d1['direction']==-1: w=a
        if w is None or w==s: continue
        for (c,dd),d2 in ori.items():
            x=None
            if c==w and d2['direction']==+1: x=dd
            elif dd==w and d2['direction']==-1: x=c
            if x is None or x==t or x==s: continue
            e4=mk(x,s)
            if e4 in ori:
                s3,t3=src_tgt(ori,x,s)
                if s3==x and t3==s: count+=1
    return count

def pd_e(ori,u,v):
    """Dynamické p_d pro hranu (u,v)."""
    return P_D0/(1+BETA*coherence(ori,u,v))

def rm_or_dynamic(ori,u):
    """Odeber orientovanou hranu s dynamickým p_d(e)."""
    cands=[(a,b) for (a,b) in ori if a==u or b==u]
    if not cands: return
    for (a,b) in random.sample(cands,len(cands)):
        if random.random()<pd_e(ori,a,b):
            ori[(a,b)]['w_or']-=1
            if ori[(a,b)]['w_or']<=0: del ori[(a,b)]
            return

def out_d(ori,u):
    return sum(d['w_or'] for (a,b),d in ori.items()
               if (a==u and d['direction']==+1)or(b==u and d['direction']==-1))

def trig(ol,ori,u): return ol.get(u,0)+out_d(ori,u)

def bfs(src,sadj):
    d={src:0}; q=[src]
    while q:
        u=q.pop(0)
        for v in sadj.get(u,set()):
            if v not in d: d[v]=d[u]+1; q.append(v)
    return d

def Dsh(ed,n):
    if n<5: return 0.0
    sadj=defaultdict(set)
    for (u,v) in ed: sadj[u].add(v); sadj[v].add(u)
    nodes=[u for u in range(n) if sadj[u]]
    if len(nodes)<5: return 0.0
    if len(nodes)<=300:
        avg={u:sum(bfs(u,dict(sadj)).values())/max(1,len(bfs(u,dict(sadj)))) for u in nodes}
        ctr=min(nodes,key=lambda u:avg[u])
    else:
        d0=bfs(nodes[0],dict(sadj)); ctr=max(d0,key=d0.get)
    dist=bfs(ctr,dict(sadj)); by_k=defaultdict(int)
    for v in nodes:
        d=dist.get(v,-1)
        if d>=0: by_k[d]+=1
    max_d=max(by_k.keys()) if by_k else 0
    max_k=max(2,int(max_d*0.8))
    k_fit=[k for k in range(1,max_k+1) if by_k[k]>0]
    S_fit=[by_k[k] for k in k_fit]
    if len(k_fit)<3: return 0.0
    lk=np.log(np.array(k_fit,float)); lS=np.log(np.array(S_fit,float))
    A=np.column_stack([lk,np.ones_like(lk)]); c,_,_,_=np.linalg.lstsq(A,lS,rcond=None)
    return float(c[0]+1)

def kt(D): return max(1,round(2*D))
def local_avg(adj,u):
    nb=list(adj.get(u,set()))
    return sum(len(adj.get(w,set())) for w in nb)/max(1,len(nb))

def run(seed,target_N=1000,use_r=True,adaptive=True):
    random.seed(seed); np.random.seed(seed)
    ol={0:0.0}; adj={0:set()}; un={}; ori={}; n=1
    Dh_no=deque([0.0]*T_AVG,maxlen=T_AVG)
    Dh_or=deque([0.0]*T_AVG,maxlen=T_AVG)
    snaps=[]
    step=0
    while n<target_N:
        step+=1
        nodes=list(range(n))
        Da_or=max(0.0,sum(Dh_or)/len(Dh_or))

        # Axiom 1
        for u in nodes:
            if random.random()<P_C:
                nb=list(adj.get(u,set()))
                if nb: add_or(ori,un,u,random.choice(nb))
                else: ol[u]=ol.get(u,0)+1.0
            # Zánik smyčky s P_D0
            if ol.get(u,0)>0 and random.random()<P_D0:
                ol[u]=max(0,ol[u]-1.0)
            # Zánik orientované hrany: gate P_D0, pak dynamický výběr
            if random.random()<P_D0:
                rm_or_dynamic(ori,u)

        # Pravidlo R
        if use_r and un:
            for (u,v) in random.sample(list(un.keys()),min(10,len(un))):
                if random.random()<P_C:
                    la_u=local_avg(adj,u); la_v=local_avg(adj,v)
                    cands=[]
                    for node,la in ((u,la_u),(v,la_v)):
                        if len(adj.get(node,set()))<la:
                            for w in adj.get(node,set()):
                                for x in adj.get(w,set()):
                                    if x!=u and x!=v and x not in adj.get(node,set()):
                                        if len(adj.get(x,set()))<local_avg(adj,x):
                                            cands.append((node,x))
                    if cands:
                        src,tgt=random.choice(cands)
                        add_un(un,adj,src,tgt)

        # Axiom 2
        expanded=False
        for u in list(nodes):
            if n>=target_N: break
            if trig(ol,ori,u)>=THETA:
                f=kt(Da_or) if adaptive else 1
                for _ in range(f):
                    if n>=target_N: break
                    x=n; n+=1; ol[x]=0.0; adj[x]=set()
                    add_un(un,adj,u,x)
                o=ol.get(u,0); od=out_d(ori,u); tot=o+od
                if tot>0:
                    frac=min(1.0,THETA/tot)
                    ol[u]=max(0,o-o*frac)
                expanded=True
        if expanded:
            Dh_no.append(max(0.0,Dsh(un,n)))
            Dh_or.append(max(0.0,Dsh(ori,n)))
            snaps.append((n,max(0.0,sum(Dh_no)/len(Dh_no)),
                            max(0.0,sum(Dh_or)/len(Dh_or))))
    return snaps

def nexon_stability(n_trials=50,n_steps=200):
    nc=[(0,1),(1,2),(2,3),(3,0)]
    surv_sp=0; surv_or=0; counts=[]
    for trial in range(n_trials):
        random.seed(200+trial); np.random.seed(200+trial)
        ol={i:0.0 for i in range(24)}
        adj={i:set() for i in range(4)}; un={}; ori={}
        for (u,v) in nc:
            add_un(un,adj,u,v); add_or(ori,un,u,v)
        n=4
        for u in range(4,24):
            adj[u]=set(); n+=1
            for v in random.sample(list(range(4,u)) if u>4 else [0],min(2,u-4)):
                add_un(un,adj,u,v)
            for v in random.sample(list(range(4)),2):
                add_un(un,adj,u,v)
        for _ in range(n_steps):
            for u in range(n):
                if random.random()<P_C:
                    nb=list(adj.get(u,set()))
                    if nb: add_or(ori,un,u,random.choice(nb))
                    else: ol[u]=ol.get(u,0)+1.0
                if ol.get(u,0)>0 and random.random()<P_D0:
                    ol[u]=max(0,ol[u]-1.0)
                if random.random()<P_D0:
                    rm_or_dynamic(ori,u)
        sp_ok=all(mk(u,v) in un for (u,v) in nc)
        or_ok=all(mk(u,v) in ori for (u,v) in nc)
        if sp_ok: surv_sp+=1
        if or_ok:
            surv_or+=1
            counts.append(np.mean([ori[mk(u,v)]['w_or'] for (u,v) in nc]))
    return surv_sp,surv_or,(np.mean(counts) if counts else 0.0)

if __name__=='__main__':
    print("DRK – Kanonický model v6")
    print(f"p_d(e) = {P_D0}/(1 + {BETA}·C(e))  [dynamické p_d]")
    print("="*55)

    print("\nTEST 1: D_shell růst s N (seed=42)")
    snaps=run(42,target_N=2000)
    print(f"{'N':>8}  {'D_no':>8}  {'D_or':>8}")
    print("─"*28)
    milestones=[200,500,1000,2000]
    last={}
    for (n,dno,dor) in snaps:
        for m in milestones:
            if n>=m and m not in last: last[m]=(n,dno,dor)
    for m in milestones:
        if m in last:
            n,dno,dor=last[m]
            print(f"{n:>8}  {dno:>8.3f}  {dor:>8.3f}")

    print("\nTEST 2: Nexon stabilita (50 realizací, 200 kroků)")
    surv_sp,surv_or,mc=nexon_stability()
    print(f"  Neorientovaný backbone: {surv_sp}/50")
    print(f"  Orientovaný 4-cyklus:   {surv_or}/50  (bez p_d(e): 23/50)")
    print(f"  Průměrný count:         {mc:.2f}")
    imp="✓ ZLEPŠENÍ" if surv_or>23 else "– beze změny"
    print(f"  {imp}")
