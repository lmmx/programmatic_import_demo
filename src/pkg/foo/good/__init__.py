__all__ = ["eggs"]

spam = "I'm a spam variable, I won't go in any namespace because I'm not in __all__"

eggs = "I belong in the `pkg.foo.good` namespace and I won't go in the `pkg.foo` namespace"
