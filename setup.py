import setuptools

setuptools.setup(
    name="workflowruns",
    version="0.0.0",
    py_modules=['workflowruns'],
    entry_points={"console_scripts": ["workflowruns=workflowruns:main"]},
    install_requires=["pygithub"],
)
