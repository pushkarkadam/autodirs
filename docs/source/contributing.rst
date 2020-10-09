.. highlight:: shell

============
Contributing
============

Contributions are highly appreciated. Credit will always be given.

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/pushkarkadam/autodirs/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/pushkarkadam/autodirs/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

Get started!
------------

Ready to contribute? Here's how to set up `autodirs` for local development.

1. Fork the `autodirs` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/autodirs.git

3. Install your local copy into a virtualenv.
    a. Install `virtualenv`::

        $ pip install virtualenv

    b. Go to the root of the project and create a virtual environment.
    c. For Mac/Linux::

        $ virtualenv venv

        # Activate venv
        $ source venv/bin/activate

    d. For Windows::

        $ python -m venv venv

        # Activate venv
        $ venv\Scripts\activate

    e. Install dependencies in the virtual environment::

        $ pip install -r requirements.txt

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5. When you are making changes, check that your changes pass the tests::

    $ python -m pytest

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python version 3.8 and above.
