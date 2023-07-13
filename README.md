# ctf_challenges
A repo containing a variety of home made ctf's and programming puzzles and the solutions.

Feel free to submit a pull request if you found a completely different or better solution.

Disclaimer: All challenges are self-made. Some challenges require using backdoors,
but rely on you playing "by the rules", as the solution is oftentimes included or 
easily accessible. All components are either in this repo, or on my website [dfsu.systems](http.//dfsu.systems) (or a subdomain thereof), if it explicitly says so there.
DO NOT attempt to hack or find abckdoors of anything outside the aforementioned scope of the challenge. 
Every challenege explicitly says what you may or may not touch.

# Challenges
| name                                              | type               | lang(s)             | tags                   |
|---------------------------------------------------|--------------------|---------------------|------------------------|
| [sql_injection](http://sqlinjection.dfsu.systems) | resource/challenge | `mysql`, `(python)` | `SQL`, `sql injection` |
| [calculator](./calculator)                        | ctf                | `python`            | `RCE`, `repl`, `eval`  |
- 

# Structure
(examples with python, might use other langs in the future)<br>
Take a look at the challenge's `README.md` for speical cases.
## Coding challenges
Typically such a challenge would contain
- `README.md` containing the task, tips, links, references, etc
- `solution.py` or `solution_[x].py` where multiple exist or `solution/*`: Look at only if stuck or you beat the challenge
- optionally `HINT.md` or `HINT_[x].md` where multiple exist: Look at those only if stuck
## CTF's/exploit finders
- `README.md` containing the task, tips, links, references, etc
- `[project].py` or `src/*` or `[project]/*` or similar -> Access: `Readonly` or sometimes `None`, see `README.md`
- `flag` or `flag.txt` or `flag.zip` or similar -> Access: `None`
- `solution.py` or `solution_x.py` where multiple exist or `solution/*`: Look at only if stuck or you beat the challenge
- optionally `HINT.md` or `HINT_[x].md` where multiple exist: Look at those only if stuck
### CTF File Access
- Solutions and hints may obviously only be checked after the challenge, or if completely stuck
- `None`: You may not open the file, look at it's metadata or in any way interact with it except through the exploit.<br>
(Imagine this file is on the server and contains a password or key, like a `.env` file)
- `Readonly`: You may open the file to read its contents, but not edit it. <br>
Exception: adding a shebang, fixing imports, etc, as long as it does not change behavior. To prettify or debug code, copy the file!<br>
(Imagine you found this project in a github repo and know a server deployed it)
 
