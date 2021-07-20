# Example 4

## Requirements:

Make sure that you are in the current directory.
Install docker.

```sh
pip install -r requirements.txt
```

## Test:

Start the containers:

```sh
make up
```

Run the test:

```sh
make test-all
```
### End2end test:

Start the containers:

```sh
make up
```

Run the test:

```sh
make test-end2end
```
### Stop the containers:

```sh
make stop
```
