# Lessr - watch and compile less codes.

[![Build Status](https://travis-ci.org/zhangxiao/lessr.png)](https://travis-ci.org/zhangxiao/lessr)

Lessr provides an API for watching and compiling less files to css files.

You can install it via `npm install lessr` and simply use it by `require('lessr').watch(src, opts)`.

`src` could be a string of:

* Path to a less file. The file will be watched and compiled.

* Path to a directory. All less files will be watched and compiled under this directory, recursively into sub directories.

`src` could also be an array of values like above.

Available options are:

* `output` Specify base path for saving the generated css files. If not given, css file will be sitting next to corresponding less file.

* `compress` Set to `true` if you want to compress the css codes. It doesn't mean to combine the css codes. If you want to combine them, use @import directive in Less.

* `watch` Specify paths you want to watch and when they change it automatically re-compiles sources.

A full example would be like:

    var lessr = require('lessr');

    lessr.watch("/path/to/less", {
        output: "/path/to/css",
        compress: true,
        watch: ["/path/to/less/a", "/path/to/less/b"]
    });

    console.log("start watching and compiling less files...");
