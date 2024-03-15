# Introduction


The pipeline has 3 nodes:
- A
- B
- Final

A->B->Final is no different from B->A->Final, dependings on the version of Kedro you are using. It may always resolve to one of them or just bouncing between two solutions randomly.

With the change implemented, there are possibility to provide custom ordering. The core idea is still using "dummy inputs" but this will be mostly hidden from the user. Because the toposort only cares about `node_dependencies` and it's okay if we inject something more there.

By default, the pipepline execute A before B. Go to `pipeline.py` and uncomment `custom_order = [node_b, node_a]` then you will see B->A->Final# kedro-partial-node-order
