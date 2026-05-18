# qedcbench-examples

Examples using the [QED-C Application-Oriented Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks) suite after `pip install qedcbench`.

## Installation

```bash
pip install qedcbench
```

This installs both **qedcbench** (the benchmarks) and **qedclib** (the execution engine).

## Examples

### basics/

Getting started — running benchmarks from Python scripts, customizing parameters, and working with results.

## Running the Standard Suite

The quickest way to run benchmarks is the built-in CLI runner:

```bash
python -m qedcbench.run_all                          # 5 defaults on simulator
python -m qedcbench.run_all -b ibm_sherbrooke -max 6  # IBM hardware
python -m qedcbench.run_all --list                    # show available benchmarks
```

## Documentation

- [Full Documentation](https://sri-international.github.io/QC-App-Oriented-Benchmarks/)
- [User Guide](https://sri-international.github.io/QC-App-Oriented-Benchmarks/user_guide/)
- [PyPI package](https://pypi.org/project/qedcbench/)

## License

Apache-2.0
