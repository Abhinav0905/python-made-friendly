"""Import equal module names through distinct package namespaces."""

import pkg_a.config
import pkg_b.config


print(pkg_a.config.SETTING)
print(pkg_b.config.SETTING)
