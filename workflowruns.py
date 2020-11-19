import os
import sys
from github import Github

from collections import namedtuple

WorkflowRun = namedtuple(
    "WorkflowRun",
    [
        "id",
        "conclusion",
        "head_repository",
        "head_branch",
        "head_sha",
        "head_commit",
        "event",
        "run_number",
        "status",
        "html_url",
    ],
)


def print_run(run):
    print(
        run.event,
        run.conclusion,
        run.head_branch,
        run.head_sha[:7],
        run.head_commit.author,
    )


def get_runs(repo):
    runs = repo.get_workflow_runs()
    for run in runs:
        yield WorkflowRun(
            id=run.id,
            conclusion=run.conclusion,
            head_repository=run.head_repository,
            head_branch=run.head_branch,
            head_sha=run.head_sha,
            head_commit=run.head_commit,
            event=run.event,
            run_number=run.run_number,
            status=run.status,
            html_url=run.html_url,
        )


def _main(reponame):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(reponame)
    runs = get_runs(repo)
    for run in runs:
        print_run(run)


def main():
    from sys import argv

    if len(argv) != 2:
        sys.exit("Usage: workflowruns repo")

    reponame = argv[1]
    if "/" not in reponame:
        sys.exit("repo needs to be full: org/repo")

    _main(reponame)


if __name__ == "__main__":
    main()
