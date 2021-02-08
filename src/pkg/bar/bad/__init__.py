__all__ = ["eggs"]

spam = "I'm a spam variable, I shouldn't be in any namespace but I'm going in the `pkg.bar` namespace!"

eggs = "I belong in the `pkg.bar.bad` namespace but I'm going in the `pkg.bar` namespace!"
