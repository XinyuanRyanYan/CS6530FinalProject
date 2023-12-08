# Adaptive Bε-tree



You can compile the tests using the provided Makefile: `make clean && make test_logging_restore`.


## RUNNING THE TEST PROGRAM

Run the Be tree with fiexed ε value (baseline)

```bash
./test_logging_restore -m test -d your_temp_dir -i test_inputs.txt -t 10400 -c 50 -p 200
```

NOTE: `-c 50` will set the checkpoint granularity to 50, and `-p 200` will set the persistence granularity to 200.

You can also add an optional -o flag to make sure the program has gone through all 10,400 operations and see the results of the various queries (e.g. `-o test_outputs.txt`).

## RUNNING THE TEST SCRIPT

We have also included a test script that will test crashing the program and resuming operation.

You can run the script by calling `bash ./TestScript.sh`. This will run through the test of running a crash and recovery. It will end the first test by making 400 queries at the end of the program based on the correct final state of the program.

When this test finishes, it will give you some results regarding the percentage of incorrect queries. Due to the potential of a crash losing a portion of your checkpoint data (as part of the checkpoint granularity), the final percentages may not be zero. We are looking for a value as close to zero as possible.
