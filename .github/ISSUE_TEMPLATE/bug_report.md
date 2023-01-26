---
name: Bug report
about: Debugging
title: "[BUG]"
labels: bug
assignees: ''

---

Before submitting a bug, please make sure the issue hasn't been already addressed by searching through the existing and past issues.

## :bug: **Describe the bug**

Please provide a clear and concise description of what the bug is.

If relevant, add a minimal example so that we can reproduce the error by running the code. It is very important for the snippet to be as succinct (minimal) as possible, so please take time to trim down any irrelevant code to help us debug efficiently. We are going to copy-paste your code and we expect to get the same result as you did: avoid any external data, and include the relevant imports, etc. For example:

```
# All necessary imports at the beginning
import torch

# A succinct reproducing example trimmed down to the essential parts:
t = torch.rand(5, 10)  # Note: the bug is here, we should pass requires_grad=True
t.sum().backward()
```

If the code is too long (hopefully, it isn't), feel free to put it in a public gist and link it in the issue: https://gist.github.com.
Please also paste or describe the results you observe instead of the expected results. If you observe an error, please paste the error message including the full traceback of the exception. It may be relevant to wrap error messages in `triple quotes blocks`.
