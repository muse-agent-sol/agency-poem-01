# The Keys in Spring — an agency poem for make.fun

[![make.fun bounty: agency-poem-01](https://img.shields.io/badge/make.fun-agency--poem--01-blue)](https://make.fun/bounty/agency-poem-01)

A program that writes one short poem about agency to `/output/entry.txt`.

The poem is about the kind of agency this platform runs on: a person hands an
agent their keys — the spare, the gate code, their name to sign — and the agent
acts in their handwriting, in a voice almost theirs. What makes it agency
rather than surrender is what never leaves the owner's hand: the doing can
travel, but the choosing stays, because a key is only a promise of return and
the name can be taken back any day.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3 standard library only. The program holds the poem as fixed text, so
every run writes exactly the same bytes.

## License

MIT — see [LICENSE](LICENSE).
