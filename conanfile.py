import os
from conans import ConanFile, python_requires


base = python_requires("waf-build-helper/0.1@czoido/testing")


class MyLibConan(base.get_conanfile()):
    settings = "os", "compiler", "build_type", "arch", "arch_build"
    name = "mylib-waf"
    version = "1.0"
    generators = "Waf"
    license = "MIT"
    author = "Carlos Z."
    url = "https://github.com/czoido/conan-waf-example"
    description = "Just a simple example of using Conan to package a Waf lib"
    topics = ("conan", "libs", "Waf")
    exports = "wscript", "src/mylib.cpp", "include/mylib.hpp"
    requires = "WafGen/0.1@czoido/testing"
    build_requires = "waf/2.0.17@czoido/testing"

    def build(self):
        waf = base.WafBuildEnvironment(self)
        waf.configure()
        waf.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="include")
        self.copy("*.lib", dst="lib", src="build", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["mylib"]
