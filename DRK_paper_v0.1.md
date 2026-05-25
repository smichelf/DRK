# Emergent Dimensionality and Metastable Oriented Structures in Minimal Discrete Relational Networks

**Stanislav Michelfeit**  
*Independent researcher*

---

## Abstract

We introduce DRK (Discrete Relational Kernel), a stochastic relational
network model based on three local principles:

(1) persistent relational existence,
(2) time-asymmetric local reconfiguration,
(3) adaptive connectivity feedback.

The model generates dynamically evolving networks without predefined
geometry, coordinates, or dimensional background.

Numerical simulations show monotonic growth of effective shell dimension
with network size across all tested realizations. A local degree-adjustment
mechanism (Rule R) prevents connectivity freezing without global
information and stabilizes the network near a characteristic average degree.

The framework also produces metastable oriented subgraphs ("nexons")
formed by oriented 4-cycles with reinforced local flow structure.

The adaptive rule

    f = max(1, round(2·D_oriented))

frequently produces four-node structures near the transition between
one- and two-dimensional growth regimes.

The present work does not claim recovery of general relativity,
quantum mechanics, or Standard Model physics.
Instead, it proposes a minimal exploratory framework in which
dimensional growth and metastable oriented structures emerge jointly
from purely local stochastic rules.
## 1. Introduction

The question of whether spacetime is fundamentally continuous or discrete has 
motivated several research programs in quantum gravity. Causal Dynamical 
Triangulations (CDT) [1] recovers four-dimensional geometry from a path integral 
over simplicial complexes. Causal set theory [2] derives spacetime from partial 
orders of discrete events. Wolfram Physics [3] explores hypergraph rewriting 
systems as models of physical law. In all these approaches, the goal is to show 
that macroscopic spacetime geometry — including its dimensionality — emerges from 
simpler discrete structures.

A common feature of these frameworks is the introduction of explicit geometric 
input: simplices in CDT, a fixed partial-order axiom in causal sets, or specific 
rewriting rules chosen to match known physics. Here we ask a more minimal 
question: can spatial dimension emerge from a network that begins with a single 
node and a single loop, governed only by local rules with no geometric prejudice?

We introduce the Discrete Relational Kernel (DRK) framework, defined by three 
axioms and one local reconfiguration rule. The framework contains no coordinates, 
no metric, no pre-assigned dimension, and no global information accessible to 
individual nodes. We show numerically that:

1. Effective shell dimension D_nonoriented grows monotonically with network size N 
   in all tested realizations.
2. An adaptive connectivity rule based on D_oriented outperforms random connectivity,
   suggesting that dimensional feedback may play a nontrivial structural role.
3. A minimal four-node subgraph — the nexon — is topologically stable under 
   the reconfiguration dynamics.
4. A local degree-adjustment rule homogenizes node connectivity without any 
   global target, eliminating teleological assumptions.

The paper is structured as follows. Section 2 defines the model axioms, the 
nexon, and Rule R. Section 3 presents numerical results. Section 4 
discusses the fixed-point argument for D_nonoriented and D_oriented, comparison with related work, and 
open questions. Section 5 concludes.

---

## 2. The Model

### 2.1 Axiom 0: Existence

The primitive object is a node u carrying a permanent unoriented
loop (edge (u,u)). This loop is never destroyed and represents the
minimal internal state of a node: its identity. A node without a
loop has no relational content; it does not exist in the relational sense.

The permanent unoriented loop is distinct from oriented loops that
may emerge through reconfiguration (Section 2.2) and does not
contribute to the expansion threshold theta.

The model is a stochastic dynamical system: all edge creation and destruction events are governed by independent Bernoulli trials at each time step. No deterministic trajectory is assumed; results are reported as statistics over independent realizations.

### 2.2 Axiom 1: Orientational Dynamics

The network has two layers:

**Layer 1 — Non-oriented backbone (permanent):**
All non-oriented edges, including the permanent loop on each node
(Axiom 0), define topological neighborhood. They never decay.

**Layer 2 — Oriented dynamic edges:**
An oriented flow state may exist on top of an existing non-oriented edge.
It carries an orientational weight w_or ≥ 1 representing the
intensity of directional flow.

Two constants p_c, p_d0 in (0,1] with p_c > p_d0 govern Layer 2:

**Creation (probability p_c per node per step):**
Node u attempts to create or strengthen an oriented edge:
- Neighbor w exists (non-oriented edge (u,w) exists):
  - No oriented edge yet: create with random orientation (50:50), w_or = 1.
  - Oriented edge exists: new attempt is random (50:50);
    if orientation matches existing → w_or(e) += 1;
    if opposite → rejected (antiparallel forbidden).
- No neighbor: oriented loop (u→u) above the permanent non-oriented
  loop (Axiom 0). Both directions of u→u are equivalent — no
  orientation conflict. w_or increments as above.

**Decay (probability p_d(e) per oriented edge per step):**

    p_d(e) = p_d0 / (1 + β · C(e))

where C(e) = number of oriented cycles of length ≤ 4 containing e
(computed only from the distance-2 neighborhood of e), β is a free parameter
(β = 0.1 in tests).

    w_or(e) → w_or(e) − 1.
    When w_or(e) = 0: oriented edge disappears; non-oriented backbone remains.

Edges in oriented cycles (C(e) ≥ 1) decay slower — local cycle-based stabilization.
The inequality p_c > p_d0 is the sole source of time asymmetry.
No other direction of time is imposed.


### 2.3 Axiom 2: Expansion

**Expansion trigger:**
A node u relaxes when its total oriented weight reaches theta:

    trigger(u) = w_or(loops of u) + Σ w_or(out-edges of u) ≥ theta

The number of 
new nodes added per relaxation event and their initial connectivity are 
both governed by a single formula:

    f = max(1, round(2 · D_oriented))

where D_oriented is the exponentially smoothed D_shell of the oriented subgraph
(edges with direction ≠ 0) over the last T_avg expansion events.

Two quantities govern the expansion event:

    f          = max(1, round(2 · D_oriented))  [inflation: nodes per event]
    k_initial  = 1                           [minimal coupling at birth]

f determines how many new nodes are added per relaxation — the inflation 
rate. It depends on current D_oriented and grows with dimension.

Each new node is born with exactly one edge (to its parent) and one
permanent unoriented loop 
(Axiom 0). Initial connectivity is minimal by design: the node has no 
information about the global network. The Rule R (Section 2.4) 
then builds connectivity dynamically from k=1 toward k_target = round(2·D_nonoriented).

    Axiom 2 governs inflation (f): how many nodes
    Rule R governs structure (k → k_target): how many edges

This separation is heuristically motivated: A newly created node does not begin
with maximal connectivity.

The adaptive rule for f is currently heuristic and motivated by the 
coordination number of regular lattices (2D neighbors in d dimensions). 
Its role is exploratory rather than derived.


### 2.4 Rule R: Spatial Reconfiguration

Rule R is not an axiom — it is a mechanistic rule ensuring that the
non-oriented spatial structure does not freeze at its initial state.
It operates independently of Axiom 1 and introduces no new parameters.

**Iteration:** Rule R iterates over pairs of nodes connected by a
non-oriented edge — not over individual nodes. A non-oriented edge
(u,v) is a symmetric bond; both nodes participate equally.

**Edge creation:** For each non-oriented edge (u,v), with probability p_c,
a new non-oriented edge is added to a neighbor of u or v:

    candidate w: reachable in 2 steps from u or v,
                 not already a direct neighbor of both u and v,
                 deg(w) < deg_local_avg(w)

Both endpoints must be below their local neighborhood average
(deg(u) < deg_local_avg(u) AND deg(w) < deg_local_avg(w)).
One candidate is selected uniformly at random.

**No edge removal:** All non-oriented edges are permanent
(Axiom 1 permanence rule). Rule R only adds edges, never removes them.

This rule is conceptually analogous to chemical valence: a bond forms
only when both endpoints have available binding capacity, determined
entirely by local neighborhood information.

### 2.5 The Nexon: Elementary Stable Subgraph

A nexon N is a connected subgraph G' of G satisfying:

1. |V(G')| = 4 (exactly)
2. G' contains exactly one oriented 4-cycle with O(e) > O_min
3. Each node carries exactly one loop
4. e(G') = 4 > |V(G')| − 1 = 3 (redundancy satisfied automatically)
5. G' is invariant under the reconfiguration dynamics for at least T_s steps

The type of loop on each node is determined by its role in the oriented cycle:

| Role                 | Degree  | Loop type           | Orientational role |
| -------------------- | ------- | ------------------- | ------------------ |
| Source (out=2, in=0) | active  | oriented loop (out) | source-like        |
| Sink (out=0, in=2)   | passive | oriented loop (in)  | sink-like          |
| Relay (out=1, in=1)  | neutral | permanent loop only | relay              |

Three distinct orientations of the 4-cycle yield three chiral classes (R, G, B), 
whose symmetry group contains Z_3 as a subgroup — a group-theoretic coincidence 
sharing some algebraic features with Z_3 structures resembling certain finite symmetry structures known from mathematical physics (see Section 4.3). A fourth orientation type (Type 4) 
has no natural annihilation partner under the chiral compatibility rules and 
is a candidate for a long-lived isolated chiral structure.

---

## 3. Results

### 3.1 Emergent Dimensionality

The model maintains two shell dimension estimates, each computed from the
shell growth profile S(k) ~ k^(D−1) around the topological center of the
respective subgraph:

    D_nonoriented = D_shell of the non-oriented subgraph (direction = 0)
                    Used by Rule R for spatial reconfiguration.
    D_oriented    = D_shell of the oriented subgraph (direction ≠ 0)
                    Used by Axiom 2 for inflation: f = round(2·D_oriented).

Both are smoothed over the last T_avg = 10 expansion events.
Results in this section report D_nonoriented as the primary measure
of emergent spatial dimensionality.

Figure 1 shows D_nonoriented and D_oriented as functions of N for a 
representative realization. Both grow monotonically from 0, with 
D_nonoriented leading in the early phase and D_oriented catching up 
as oriented connections accumulate.

**Table 1. D_shell growth with N (seed=42, with Rule R).**

| N | D_nonoriented | D_oriented |
|---|---------------|------------|
| 208 | 0.00 | 0.46 |
| 544 | 2.90 | 1.08 |
| 1108 | 4.01 | 2.30 |
| 2000 | 4.04 | 3.25 |

Both dimensions grow monotonically. D_oriented converges toward 3 at 
N ≈ 2000, consistent with the fixed-point argument (Section 4.1).

**Small-N note:** At N ≤ 500, Rule R appears to reduce D_nonoriented 
relative to the no-Rule-R baseline. This is an artifact of small network 
size: at small N, Rule R shortcuts reduce the effective diameter. At 
larger N (≥ 1000), Rule R is essential for dimensional growth — without 
it, the network freezes in a star topology with D_nonoriented ≈ 0.

### 3.2 Adaptive vs. Random Inflation (Null Model)

The physical model separates inflation (f, governed by Axiom 2) from 
connectivity (k = 1 at birth, built by Rule R). We test two null hypotheses 
against the adaptive model (10 seeds, 220 steps):

**H0a — No inflation (f = 1):** one node per relaxation, k = 1.
Tests whether adaptive inflation (growing f with D_oriented) contributes at all.

**H0b — Random inflation (f uniform in {1,...,6}):** random node count, k = 1.
Tests whether D_oriented-dependent f outperforms arbitrary inflation.

| Model | f rule | D_nonoriented | Better vs adaptive |
|-------|--------|-------|-------------------|
| Adaptive | round(2·D_oriented) | 2.25 | — |
| H0b: random f | uniform {1,...,6} | 2.22 | 4/10 |
| H0a: no inflation | f = 1 | 2.04 | 3/10 |

Key results:

- Adaptive f outperforms f=1 (Δ = +0.207, 7/10): inflation driven by 
  D_oriented contributes positively to dimensional growth.
- Adaptive f vs random f is weak (Δ = +0.026, 6/10): the specific 
  adaptive rule round(2·D_oriented) does not strongly dominate random inflation 
  at current simulation scales.

The second result is reported honestly: the adaptive rule for f has a 
directional advantage over no inflation, but its superiority over arbitrary 
inflation is not statistically robust in the present experiments. 
Larger N and more seeds are needed to resolve this question.

### 3.3 Nexon Stability

We embed a single nexon in a surrounding network of 20 nodes and run 
the reconfiguration dynamics for 200 steps (50 independent realizations).

The nexon has two components with distinct stability properties:

**Non-oriented backbone (4 permanent edges):** survives in 50/50 
realizations (100%). The permanence rule of Axiom 1 guarantees this: 
non-oriented edges are never removed. The four nodes of the nexon 
remain connected regardless of oriented dynamics.

**Oriented 4-cycle (dynamic flow):** survives in 35/50 realizations 
(70%) at T = 200 steps, with dynamic decay rate p_d(e) active 
(β = 0.1). Without dynamic p_d, survival drops to 23/50 (46%). 
The reinforcement rule applies the 50:50 filter — a new attempt 
succeeds only if its random orientation matches the existing one, 
giving an effective reinforcement rate of p_c/2. This reduces the 
average edge weight to 2.82 (previously 4.61 under deterministic 
reinforcement), but is physically more transparent. Topological 
protection (C(e) ≥ 1 → p_d(e) < p_d0) remains active.

This result is structurally meaningful: the nexon is not a permanently 
frozen structure but a metastable one. The non-oriented backbone remains stable
throughout all tested realizations; the oriented flow fluctuates. The 70% survival 
rate at T = 200 reflects the competition between p_d(e) (flow decay 
with local cycle-based stabilization) and p_c/2 (effective reinforcement rate). 
Longer-lived nexons are expected at higher p_c/p_d0 ratios.

The present framework does not yet contain a rigorous conservation law. 
Nexons should therefore currently be interpreted as metastable 
dynamical attractors rather than strictly conserved particles. 
Identifying possible topological or statistical invariants of the 
reconfiguration dynamics remains an important open problem.

### 3.4 Rule R: Preventing Frozen Topology

Every new node is born with k = 1 (one non-oriented edge to parent). 
Without Rule R, nodes remain frozen at degree 1 — the network forms a 
star topology and D_nonoriented cannot be measured.

Rule R is essential at large N. At small N (≤ 500), Rule R shortcuts 
reduce the effective diameter and appear to lower D_nonoriented. At large 
N (≥ 1000), this effect is negligible and Rule R enables dimensional growth 
by homogenizing local degree toward the neighborhood average.

| N | Without Rule R | With Rule R |
|---|----------------|-------------|
| 500 | D_no ≈ 3.6 (star artifact) | D_no ≈ 1.8 |
| 1000 | frozen (star) | D_no ≈ 3.0 |
| 2000 | frozen (star) | D_no ≈ 4.0 |

Without Rule R at large N: the network degenerates into a star graph 
(all nodes connected only to their expansion parent) and dimensional 
growth stalls. Rule R is structurally necessary to prevent this degenerate 
topology — nodes without additional connections are relational isolated 
and cannot participate in nexon formation.

The apparent high D_no at small N without Rule R is a transient artifact
caused by shell compression around the central hub.

### 3.5 Parameter Robustness

D_nonoriented grows with the ratio p_c / p_d (monotonically from 1.13 
at ratio 1.2 to 1.56 at ratio 2.0), confirming that the time-asymmetry 
of Axiom 1 directly governs dimensional growth. D_nonoriented decreases with 
increasing threshold theta (from 1.65 at theta=1.5 to 0.40 at theta=5.0): 
a higher threshold slows expansion, reducing the number of feedback cycles 
within a fixed simulation window.

---

## 4. Discussion

### 4.1 Fixed-Point Argument

The rule f = round(2·D_oriented) is self-consistent at any integer D*: 
a D*-dimensional cubic lattice has coordination number 2D*, so a network 
with D_nonoriented = D* generates nodes with k_new = 2D*, reinforcing the 
D*-dimensional structure.

Why does the system converge toward D* ≈ 2–3 rather than higher values?
A saturation argument: each new node connects to its parent plus neighbors 
of the parent. The number of available extra neighbors ≈ deg(parent) − 1 
≈ k_new − 1. At D* = 3 (k_new = 6), the requirement of 5 additional 
connections is marginally satisfiable from the parent's neighborhood. 
At D*=4 the required coordination becomes heuristically difficult
to sustain from local neighborhood information alone.

 
This argument is heuristic. A rigorous treatment would require showing
that (a) the stochastic process for D_nonoriented has a unique stationary
distribution, (b) that distribution is concentrated near D* = 3, and
(c) the feedback is stable — small deviations from D* are corrected
rather than amplified. None of these steps is currently established.
The numerical evidence (monotone growth in 20/20 realizations, low variance)
is consistent with convergence but does not constitute a proof.
A formal proof of convergence to a specific fixed point remains an open problem.

### 4.2 Nexon Threshold and Emergent Structure

The formula f = max(1, round(2·D_oriented)) produces f = 4 at D_oriented = 2. 
This is not imposed: it follows from the formula evaluated at the 
observed transition region between one- and two-dimensional growth regimes. 
The four-node nexon thus emerges as the characteristic expansion unit 
at the dimensional transition, without being postulated.

### 4.2b Network Laplacians

Two distinct Laplacian operators arise naturally in DRK:

**L_un** — symmetric Laplacian of the non-oriented backbone.
Describes effective connectivity geometry.

**L_or** — directed weighted operator of oriented flow states.
Describes propagation and orientational dynamics.

Working hypothesis: effective geometric behavior is primarily associated
with L_un; propagation and orientational dynamics with L_or.
Strong orientational organization may modify the effective network geometry
through long-term dynamical feedback.
### 4.3 Relation to Known Symmetries

The oriented 4-cycle admits several discrete chiral classes under
cyclic orientation patterns.

These classes exhibit nontrivial permutation structure and admit
a natural mapping to finite permutation groups related to S_4.

Certain algebraic features — such as Z_3-like periodicity and
three-dimensional irreducible representations — resemble structures
that also appear in other areas of mathematical physics.

No physical identification with SU(3), color charge,
quark structure, or Standard Model symmetries is claimed.

At present, this observation should be interpreted only as a
structural algebraic analogy.
### 4.4 Comparison with Related Frameworks

CDT recovers a four-dimensional de Sitter spacetime from path integrals 
over causal triangulations [1]. DRK differs in that dimension is not a 
target of the path integral but an emergent property of a feedback rule. 
No sum over histories is performed.

Causal set theory posits discrete events partially ordered by causality [2]. 
DRK shares the discrete relational ontology but does not pre-impose a 
causal partial order; the arrow of time emerges from p_c > p_d.

Wolfram Physics [3] generates spacetime from hypergraph rewriting. 
DRK is closer in spirit but uses a simpler primitive (node + loop) and 
derives its rewriting rule from an explicit local feedback principle 
(dimensional feedback) rather than by search.

### 4.5 Limitations and Open Questions

The present framework has several important limitations.

**1. No analytical proof of convergence**

The fixed-point argument for D_nonoriented → 3 remains heuristic.
A rigorous treatment would require analysis of the stochastic process
governing shell-dimension evolution and proof of stability of the
adaptive feedback rule.

**2. No continuum limit**

The relation between the discrete network and a smooth manifold
is not established. Preliminary experiments using graph Laplacian
operators suggest that large-scale effective geometric behavior may
emerge from the network dynamics, but no metric reconstruction or
continuum derivation currently exists.

**3. No Lorentz invariance**

The model does not possess explicit Lorentz symmetry. Whether
Lorentz-like behavior can emerge statistically in a continuum limit
remains unknown.

**4. No quantum dynamics**

The current framework is entirely classical and stochastic. No
Hilbert space, unitary evolution, or quantum field structure is included.

**5. No conservation law**

The framework currently lacks a rigorous invariant or conservation law.
Nexons should therefore be interpreted as metastable dynamical
structures rather than fully conserved particles.

These limitations are characteristic of exploratory discrete relational
models and do not undermine the primary numerical results regarding
dimensional growth and metastable oriented substructures.
## 5. Conclusion

We introduced DRK, a discrete relational framework based on persistent
existence, local stochastic reconfiguration, and adaptive dimensional
feedback.

The framework should currently be interpreted primarily
as a stochastic graph-dynamics model with emergent
connectivity structure.

Numerical simulations demonstrate that local graph dynamics can generate
nontrivial shell-dimensional growth without predefined geometry
or global coordination.

The numerical results reported here are exploratory
and intended primarily to identify qualitative dynamical behavior.

A local degree-adjustment mechanism (Rule R) prevents connectivity
freezing and stabilizes the network near a characteristic average degree
using only local information.

The framework also produces metastable oriented subgraphs ("nexons")
consisting of oriented 4-cycles with reinforced local flow structure.
The backbone of these structures survives in all tested realizations,
while the oriented flow itself remains metastable.

The adaptive rule

    f = max(1, round(2·D_oriented))

naturally produces four-node structures near D_oriented ≈ 2,
suggesting a possible structural transition associated with the emergence
of stable local organization.

The primary open question is whether D_nonoriented and D_oriented
converge toward stable fixed points for large network size and whether
such convergence can be established analytically.

Future work includes:

Future work will investigate spectral properties of the emergent network geometry, including graph Laplacian spectra and algebraic connectivity.

- rigorous convergence analysis,
- spectral analysis of network Laplacians,
- study of metastable flow structures,
- investigation of continuum limits,
- and analysis of possible emergent geometric behavior.

The present work should be interpreted as an exploratory study of
local stochastic relational dynamics rather than a complete physical
theory of spacetime or matter.
## Reproducibility

All simulations were implemented in Python 3 using standard library 
modules (`random`, `numpy`). No external simulation framework was used.

These values were chosen empirically as convenient stable operating points.
No fundamental significance is currently attributed to them.

Key reproducibility parameters:

- **Parameters**: P_C = 0.1618, P_D0 = 0.1, β = 0.1 (coherence parameter, see Section 2.2), THETA = 2.718
- **RNG seeds**: integer seeds in range 42–61 (20 seeds for reproducibility 
  tests, 42–51 for null model and parameter sweeps). Each seed fully 
  determines the stochastic trajectory.
- **Simulation steps**: 250–350 steps per realization (specified per experiment).
- **D_nonoriented/D_oriented computation**: exponential window of T_avg = 10 expansion events; 
  D_shell computed via log-log linear regression on shell profile S(k) 
  for k in [1, floor(0.8·diameter)], minimum 3 data points required.
- **Averaging procedure**: all reported means and standard deviations are 
  computed over independent realizations with distinct seeds; no within-run 
  averaging is performed.
- **Implementation language**: Python 3.11. BFS-based shell computation; 
  no compiled extensions.

Source code is available at [repository URL].

---

## Computational Complexity

The dominant cost per simulation step is D_shell computation, 
which requires BFS from the topological center of the network.

| Operation | Complexity | Notes |
|-----------|------------|-------|
| BFS from one node | O(N + E) | N nodes, E edges |
| Finding topological center | O(N · (N + E)) | BFS from all nodes |
| D_shell regression | O(diameter) | negligible |
| Rule R (per step) | O(k²) per sampled node | k = avg degree |
| Full step | O(N² + N·k²) | center BFS dominates |

For the network sizes used in this work (N ≤ 600, avg degree ≤ 8), 
wall-clock time per realization is under 60 seconds on a standard laptop. 
The O(N²) scaling of center-finding limits practical simulations to 
N ≲ 2000 without optimization. For larger N, approximate center 
estimation (random BFS sampling) would reduce this to O(N log N).

---

## References

[1] Ambjørn, J., Jurkiewicz, J., Loll, R. (2012). Causal dynamical 
    triangulations and the quest for quantum gravity. 
    *Foundations of Space and Time*, Cambridge UP, 321–337.

[2] Surya, S. (2019). The causal set approach to quantum gravity. 
    *Living Reviews in Relativity* 22, 5.

[3] Wolfram, S. (2020). *A Project to Find the Fundamental Theory of Physics*. 
    Wolfram Media.

[4] Penrose, R. (1971). Angular momentum: an approach to combinatorial 
    space-time. *Quantum Theory and Beyond* (ed. Bastin), Cambridge UP.

[5] Wheeler, J. A. (1990). Information, physics, quantum: the search for 
    links. *Complexity, Entropy, and the Physics of Information*, 
    Addison-Wesley, 3–28.

[6] Verlinde, E. (2011). On the origin of gravity and the laws of Newton. 
    *JHEP* 2011, 29.

[7] Smolin, L. (2006). The case for background independence. 
    *The Structural Foundations of Quantum Gravity* (eds. Rickles et al.), 
    Oxford UP, 196–239.

[8] Bombelli, L., Lee, J., Meyer, D., Sorkin, R. D. (1987). Space-time as 
    a causal set. *Physical Review Letters* 59, 521–524.

[9] Loll, R. (2019). Quantum gravity from causal dynamical triangulations: 
    a review. *Classical and Quantum Gravity* 37, 013002.

[10] Gorard, J. (2020). Some relativistic and gravitational properties of 
     the Wolfram model. *Complex Systems* 29(2).

---

*Manuscript prepared 25.5.2026. Code and data available at https://github.com/smichelf/DRK.*
