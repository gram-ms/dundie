# Contributing to Dundie Project

Summary of project

## Guidelines

- Backwards compatibility
- Multiplatform
- Python 3 only

## Code of conduct

- Be gentle

## How to contribute

### Fork repository

- Click fork button on [github repo](https://github.com/...)

### Clone to local dev enviroment

```bash
git clone https://github.com/yourname/...
```

### Prepare virtual env

```bash
cd my_dundierw
make virtualenv
make install
```

### Coding style

- This project follows PEP8


### Run tests

```bash
make test
# or 
make watch
```

### Commit rules

- We follow convetional commit messages ex: `[bugfix] reason #issue`
- We require signed commits

### Pull requests rules

- We require all tests to be passing
