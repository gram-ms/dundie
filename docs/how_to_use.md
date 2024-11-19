# How to use

## Load data

Having a file `people.csv` with the following format:

```csv
Jim Halpert, Sales, Salesman, jim@dundlermifflin.com
Dwight Schrute, C-Level, CEO, schrute@dundlermifflin.com
```

Run `dundie load` command

```py
dundie load people.csv
```

## Viewing data

### Viewing all information

```bash
$ dundie show

                            Dunder Mifflin Report
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┓
┃ Email        ┃ Balance ┃ Last_Moveme… ┃ Name         ┃ Dept    ┃ Role     ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━┩
│ jim@dundler… │ 450     │ 2024-11-18T… │ Jim Halpert  │ Sales   │ Salesman │
│ schrute@dun… │ 70      │ 2024-11-13T… │ Dwight       │ C-Level │ CEO      │
│              │         │              │ Schrute      │         │          │
└──────────────┴─────────┴──────────────┴──────────────┴─────────┴──────────┘
```

### Filtering

Available filters are `--dept` and `--email`

```bash
$ dundie show
                            Dunder Mifflin Report
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┓
┃ Email          ┃ Balance ┃ Last_Movement ┃ Name        ┃ Dept  ┃ Role     ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━┩
│ jim@dundlermi… │ 450     │ 2024-11-18T1… │ Jim Halpert │ Sales │ Salesman │
└────────────────┴─────────┴───────────────┴─────────────┴───────┴──────────┘
```

**NOTE** passing `--output=file.json` will save a json file with the results.

## Adding points

An admin user can easily add points to any user or dept.

```bash
dundie add 100 --email=jim@dundlermifflin.com
                                      Dunder Mifflin Report
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┓
┃ Email                  ┃ Balance ┃ Last_Movement              ┃ Name        ┃ Dept  ┃ Role     ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━┩
│ jim@dundlermifflin.com │ 450     │ 2024-11-18T16:32:12.186418 │ Jim Halpert │ Sales │ Salesman │
└────────────────────────┴─────────┴────────────────────────────┴─────────────┴───────┴──────────┘

```

Available selectors are `--email` and `--dept`
