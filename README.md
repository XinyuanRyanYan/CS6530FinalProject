# Adaptive Bε-tree

```
mkdir tmpdir
make test
```


## RUNNING THE TEST PROGRAM

Run the Be tree with fiexed ε value (baseline)

```bash
./test -m test -i 75upsertupdate.txt -d tmpdir -t 100000
```

NOTE: `-i 75upsertupdate.txt` represents we are testing the test dataset with 75% upserts.

Run the Be tree with adaptive ε value (baseline)

```bash
./test -m test -i 25upsertupdate.txt -d tmpdir -t 100000 -I 0.5 -e L
```

NOTE: `-I 0.5` represents the min_epsilon is `0.5`, we used `1.0` as the max_epsilon by default. `-e L` represents that we use the `LINEAR` function to adapt to the epsilon, we can also use `S` for `SIGMOID`, `T` for `TANH`.
