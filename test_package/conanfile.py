from conans import ConanFile


class TestPackageConan(ConanFile):
    build_requires = "java_installer/9.0.0@bincrafters/stable"
    def test(self):
        self.run("bazel version")
