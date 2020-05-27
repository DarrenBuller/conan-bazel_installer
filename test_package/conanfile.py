#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class TestPackageConan(ConanFile):
    def test(self):
        self.run("bazel version")

    def build_requirements(self):
        if not tools.which("javac"):
            self.build_requires("java_installer/8.0.144@bincrafters/stable")
