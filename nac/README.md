## New Algorithm

### Setup

- Dependencies: [venv](https://docs.python.org/3.6/library/venv.html)
 
```bash
$ python3 -m venv venv

$ source venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
```

### Run

#### Parallel

```bash
 $ ./src/nac-distr.py [--workers=NUM(CPUS) | --graph=PATH(null)]
```

#### Secuencial

```bash
 $ ./src/nac-iter.py [GRAPH_PATH]
```

- Clean

```bash
 $ ./clean.sh
```

### Metrics

It runs the _parallel_ algorithm with the graphs generated using `make generate`

```bash
 $ ./metrics-getter.py
```

### Tests

- All tests

```bash
 $ pytest
```

- Single test

```bash
 $ pytest FILE
```

