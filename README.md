# workflowruns

A simple script to get a log of the workflow runs in a GitHub
repository.

To install:

```bash
pip install git+https://github.com/pgdr/workflowruns
```

Then run:

```bash
workflowruns user/reponame  # [or workflowruns org/reponame]
```

```bash
workflowruns pgdr/ph
```

Depends on [PyGithub](https://pypi.org/project/PyGithub/), so that is
also installed.
